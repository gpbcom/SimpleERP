// @vitest-environment node
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

const COPY = fileURLToPath(new URL('../../src/assets/symbol.svg', import.meta.url));
const ORIGINAL = fileURLToPath(new URL('../../../../docs/assets/symbol.svg', import.meta.url));

describe('symbol asset', () => {
  it('is a byte-identical copy of the symbol of the documentation', () => {
    const copy = readFileSync(COPY);
    const original = readFileSync(ORIGINAL);
    expect(copy.equals(original)).toBe(true);
  });

  it('is an svg document', () => {
    expect(readFileSync(COPY, 'utf-8')).toContain('<svg');
  });
});
