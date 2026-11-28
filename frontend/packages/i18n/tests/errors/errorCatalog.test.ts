import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

import { parse } from 'yaml';
import { describe, expect, it } from 'vitest';

import { ERROR_COMMON_KEYS, errorCatalog, resolveErrorCode } from '../../src/errors/errorCatalog';

interface BackendEntry {
  title: string;
  why: string;
  action: string;
  reference: string;
}

interface RefusalEntry {
  code: string;
  title_key: string;
  why_key: string;
  action_key: string;
  reference: string;
}

const ROOT = resolve(__dirname, '../../../../..');
const CODES_PATHS = [
  'backend/models/conf/catalogs/error_codes.yaml',
  'backend/services/platform/conf/catalogs/error_codes.yaml',
];
const REFUSALS_PATH = 'backend/shared/context/conf/catalogs/refusal_codes.yaml';

function read<T>(path: string): T {
  return parse(readFileSync(resolve(ROOT, path), 'utf-8')) as T;
}

function loadBackendCodes(): Record<string, BackendEntry> {
  const codes: Record<string, BackendEntry> = {};
  for (const path of CODES_PATHS) {
    Object.assign(codes, read<{ codes: Record<string, BackendEntry> }>(path).codes);
  }
  for (const entry of read<{ entries: RefusalEntry[] }>(REFUSALS_PATH).entries) {
    codes[entry.code] = {
      title: entry.title_key,
      why: entry.why_key,
      action: entry.action_key,
      reference: entry.reference,
    };
  }
  return codes;
}

describe('front-end error code catalogue', () => {
  const backend = loadBackendCodes();

  it('holds exactly the codes of the three backend catalogues', () => {
    expect(Object.keys(errorCatalog).sort()).toEqual(Object.keys(backend).sort());
  });

  it.each(Object.keys(backend))('gives %s the same keys and reference as the backend', (code) => {
    expect(errorCatalog[code]).toEqual({
      titleKey: backend[code].title,
      whyKey: backend[code].why,
      actionKey: backend[code].action,
      reference: backend[code].reference,
    });
  });

  it('resolves a known code to its entry', () => {
    const [code] = Object.keys(backend);
    expect(resolveErrorCode(code)).toEqual(errorCatalog[code]);
  });

  it.each(['NO-SUCH-CODE-99', '', 'invalid-input-01'])('resolves the unknown code %j to the fallback', (code) => {
    const entry = resolveErrorCode(code);
    expect(entry.titleKey).toBe('errors.fallback.title');
    expect(entry.whyKey).toBe('errors.fallback.why');
    expect(entry.actionKey).toBe('errors.fallback.action');
    expect(entry.reference).toBeUndefined();
  });

  it('shares no support reference between two codes', () => {
    const references = Object.values(errorCatalog).map((entry) => entry.reference);
    expect(new Set(references).size).toBe(references.length);
  });

  it('names the shared labels', () => {
    expect(Object.values(ERROR_COMMON_KEYS)).toEqual(
      expect.arrayContaining(['errors.common.cancel', 'errors.common.reference']),
    );
  });
});
