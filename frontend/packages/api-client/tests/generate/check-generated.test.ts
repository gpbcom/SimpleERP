import { spawnSync, type SpawnSyncReturns } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { afterEach, beforeEach, describe, expect, it } from 'vitest';

const packageDir = fileURLToPath(new URL('../..', import.meta.url));
const repoRoot = fileURLToPath(new URL('../../../../..', import.meta.url));
const script = join(packageDir, 'scripts', 'generate.mjs');
const v1 = join(packageDir, 'tests', 'fixtures', 'check', 'openapi-v1.json');
const v2 = join(packageDir, 'tests', 'fixtures', 'check', 'openapi-v2.json');
const regenerate = 'pnpm --filter ./frontend/packages/api-client run generate';

function run(args: string[]): SpawnSyncReturns<string> {
  return spawnSync(process.execPath, [script, ...args], { cwd: packageDir, encoding: 'utf8' });
}

describe('generate.mjs --check', () => {
  let work = '';
  let output = '';

  beforeEach(() => {
    work = mkdtempSync(join(tmpdir(), 'api-client-check-'));
    output = join(work, 'client.ts');
  });

  afterEach(() => {
    rmSync(work, { recursive: true, force: true });
  });

  it('passes when the client was generated from the same document', () => {
    expect(run(['--input', v1, '--output', output]).status).toBe(0);
    expect(run(['--input', v1, '--output', output, '--check']).status).toBe(0);
  });

  it('fails, names the stale file and the command, and leaves it unchanged when the document changed', () => {
    run(['--input', v1, '--output', output]);
    const before = readFileSync(output, 'utf8');
    const result = run(['--input', v2, '--output', output, '--check']);
    expect(result.status).toBe(1);
    expect(result.stderr).toContain(output);
    expect(result.stderr).toContain(regenerate);
    expect(readFileSync(output, 'utf8')).toBe(before);
  });

  it('fails without writing anything when the generated client is missing', () => {
    const result = run(['--input', v1, '--output', output, '--check']);
    expect(result.status).toBe(1);
    expect(result.stderr).toContain(output);
    expect(existsSync(output)).toBe(false);
  });

  it('generates the same bytes twice', () => {
    run(['--input', v1, '--output', output]);
    const first = readFileSync(output);
    run(['--input', v1, '--output', output]);
    expect(readFileSync(output).equals(first)).toBe(true);
  });

  it('exits 2 with a message when the input is missing', () => {
    const result = run(['--input', join(work, 'absent.json'), '--output', output]);
    expect(result.status).toBe(2);
    expect(result.stderr).not.toBe('');
  });

  it('keeps the committed platform client up to date with its OpenAPI document', () => {
    const input = join(repoRoot, 'backend', 'services', 'platform', 'openapi.json');
    const committed = join(packageDir, 'src', 'generated', 'platform.ts');
    const result = run(['--input', input, '--output', committed, '--check']);
    expect(result.stderr).toBe('');
    expect(result.status).toBe(0);
  });
});
