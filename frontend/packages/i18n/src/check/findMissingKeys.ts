import type { Catalog, Catalogs, MissingKey } from '../types';

function flatten(catalog: Catalog, prefix: string, leaves: Map<string, string>): void {
  for (const [name, value] of Object.entries(catalog)) {
    const path = prefix === '' ? name : `${prefix}.${name}`;
    if (typeof value === 'string') {
      leaves.set(path, value);
    } else {
      flatten(value, path, leaves);
    }
  }
}

function compare(a: string, b: string): number {
  if (a < b) {
    return -1;
  }
  return a > b ? 1 : 0;
}

/**
 * Find the keys that a language lacks while another language has them.
 *
 * Each catalogue is flattened to dotted leaf paths, and the union of every language's paths is the expected key set.
 * A language misses a path when it is absent, is not a string leaf (an object where another language has a string),
 * or holds an empty or blank string. The result is sorted by language, then key. Pure: no I/O, no Vue.
 *
 * @param catalogs - Every catalogue, by language code.
 * @returns The missing keys, sorted by language then key; empty when every language is complete.
 */
export function findMissingKeys(catalogs: Catalogs): MissingKey[] {
  const flat = new Map<string, Map<string, string>>();
  const expected = new Set<string>();
  for (const [language, catalog] of Object.entries(catalogs)) {
    const leaves = new Map<string, string>();
    flatten(catalog, '', leaves);
    flat.set(language, leaves);
    for (const path of leaves.keys()) {
      expected.add(path);
    }
  }
  const missing: MissingKey[] = [];
  for (const [language, leaves] of flat) {
    for (const key of expected) {
      const value = leaves.get(key);
      if (value === undefined || value.trim() === '') {
        missing.push({ language, key });
      }
    }
  }
  return missing.sort((a, b) => compare(a.language, b.language) || compare(a.key, b.key));
}
