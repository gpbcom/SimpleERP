import { readdirSync, readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';

import { build } from 'vite';
import type { Rollup } from 'vite';
import { describe, expect, it } from 'vitest';

const ROOT = resolve(dirname(import.meta.filename), '../..');
const NAMESPACE = 'http://www.w3.org/';
const SCHEME_URL = /https?:\/\/[^\s'"`)]*/g;
const RELATIVE_URL = /(?<![:\w/*])\/\/[A-Za-z0-9-]+\.[A-Za-z]{2,}[^\s'"`)]*/g;
const FOREIGN_ICON_SOURCE = /^(@?lucide(?!-vue-next$)|@fortawesome|@heroicons|@mdi|@iconify|@tabler|feather|phosphor)/;

function sourceFiles(folder: string): string[] {
  return readdirSync(folder, { withFileTypes: true, recursive: true })
    .filter((entry) => entry.isFile())
    .map((entry) => join(entry.parentPath, entry.name));
}

function foreignUrls(text: string, pattern: RegExp): string[] {
  return (text.match(pattern) ?? []).filter((url) => !url.startsWith(NAMESPACE));
}

describe('third parties', () => {
  it('has no URL in any file under src except the SVG namespace', () => {
    const found: string[] = [];
    for (const file of sourceFiles(join(ROOT, 'src'))) {
      const text = readFileSync(file, 'utf-8');
      for (const url of foreignUrls(text, SCHEME_URL)) found.push(`${file}: ${url}`);
      for (const url of foreignUrls(text, RELATIVE_URL)) found.push(`${file}: ${url}`);
    }

    expect(found).toEqual([]);
  });

  it('imports every icon from lucide-vue-next', () => {
    const offenders: string[] = [];
    for (const file of sourceFiles(join(ROOT, 'src'))) {
      const text = readFileSync(file, 'utf-8');
      for (const match of text.matchAll(/from\s+['"]([^'"]+)['"]/g)) {
        const source = match[1] ?? '';
        if (FOREIGN_ICON_SOURCE.test(source)) offenders.push(`${file}: ${source}`);
      }
    }

    expect(offenders).toEqual([]);
  });

  it('lists lucide-vue-next under dependencies with an exact version', () => {
    const manifest = JSON.parse(readFileSync(join(ROOT, 'package.json'), 'utf-8')) as {
      dependencies?: Record<string, string>;
    };

    expect(manifest.dependencies?.['lucide-vue-next']).toMatch(/^\d+\.\d+\.\d+$/);
  });

  it('builds output with no http or https URL except the SVG namespace', async () => {
    const result = await build({
      root: ROOT,
      configFile: join(ROOT, 'vite.config.ts'),
      logLevel: 'silent',
      build: { write: false },
    });
    const outputs = (Array.isArray(result) ? result : [result]) as Rollup.RollupOutput[];
    const found: string[] = [];
    for (const output of outputs) {
      for (const item of output.output) {
        const text = item.type === 'chunk' ? item.code : String(item.source);
        for (const url of foreignUrls(text, SCHEME_URL)) found.push(`${item.fileName}: ${url}`);
      }
    }

    expect(found).toEqual([]);
  });
});
