import { describe, expect, it } from 'vitest';

import { availableLanguages, catalogs } from '../../src/catalogs/catalogs';

type Node = { [key: string]: string | Node };

function leaves(node: Node, prefix = ''): { key: string; value: unknown }[] {
  return Object.entries(node).flatMap(([name, value]) =>
    typeof value === 'object' && value !== null
      ? leaves(value, `${prefix}${name}.`)
      : [{ key: `${prefix}${name}`, value }],
  );
}

function lookup(node: Node, path: string): unknown {
  return path.split('.').reduce<unknown>((current, part) => {
    if (typeof current === 'object' && current !== null) {
      return (current as Node)[part];
    }
    return undefined;
  }, node);
}

describe('catalogs', () => {
  it('lists English and French among the available languages', () => {
    const languages = availableLanguages();
    expect(languages).toContain('en');
    expect(languages).toContain('fr');
  });

  it('lists the available languages sorted', () => {
    const languages = availableLanguages();
    expect(languages).toEqual([...languages].sort());
  });

  it.each(['en', 'fr'])('holds a non-empty %s catalogue', (language) => {
    const catalog = catalogs[language];
    expect(catalog).toBeTypeOf('object');
    expect(Object.keys(catalog).length).toBeGreaterThan(0);
  });

  it.each(['en', 'fr'])('names both languages in the %s catalogue', (language) => {
    for (const key of ['language.en', 'language.fr']) {
      const value = lookup(catalogs[language], key);
      expect(typeof value, `${language}: ${key}`).toBe('string');
      expect((value as string).trim().length, `${language}: ${key}`).toBeGreaterThan(0);
    }
  });

  it.each(['en', 'fr'])('holds only non-empty strings as values in the %s catalogue', (language) => {
    for (const { key, value } of leaves(catalogs[language])) {
      expect(typeof value, `${language}: ${key}`).toBe('string');
      expect((value as string).trim().length, `${language}: ${key}`).toBeGreaterThan(0);
    }
  });
});
