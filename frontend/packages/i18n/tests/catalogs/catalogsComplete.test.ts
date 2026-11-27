import { describe, expect, it } from 'vitest';

import { catalogs } from '../../src/catalogs/catalogs';
import { findMissingKeys } from '../../src/check/findMissingKeys';

describe('shipped catalogs', () => {
  it('has every key in every language', () => {
    const missing = findMissingKeys(catalogs);
    const message = missing.map(({ language, key }) => `${language}: ${key}`).join('\n');
    expect(missing, `Missing keys:\n${message}`).toEqual([]);
  });
});
