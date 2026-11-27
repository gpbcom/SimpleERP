import { describe, expect, it } from 'vitest';

import { findMissingKeys } from '../../src/check/findMissingKeys';
import type { Catalogs } from '../../src/types';

describe('findMissingKeys', () => {
  it('reports a key added in English only as missing in French', () => {
    const catalogs: Catalogs = {
      en: { greeting: 'Hello', extra: 'Only English' },
      fr: { greeting: 'Bonjour' },
    };
    expect(findMissingKeys(catalogs)).toEqual([{ language: 'fr', key: 'extra' }]);
  });

  it('reports a key present in French only as missing in English', () => {
    const catalogs: Catalogs = {
      en: { greeting: 'Hello' },
      fr: { greeting: 'Bonjour', extra: 'Seulement en francais' },
    };
    expect(findMissingKeys(catalogs)).toEqual([{ language: 'en', key: 'extra' }]);
  });

  it('returns an empty list when every language has every key', () => {
    const catalogs: Catalogs = {
      en: { greeting: 'Hello', farewell: 'Bye' },
      fr: { greeting: 'Bonjour', farewell: 'Au revoir' },
    };
    expect(findMissingKeys(catalogs)).toEqual([]);
  });

  it('returns an empty list when there is a single language', () => {
    expect(findMissingKeys({ en: { greeting: 'Hello' } })).toEqual([]);
  });

  it('compares nested keys by their dotted path', () => {
    const catalogs: Catalogs = {
      en: { menu: { file: { open: 'Open', save: 'Save' } } },
      fr: { menu: { file: { open: 'Ouvrir' } } },
    };
    expect(findMissingKeys(catalogs)).toEqual([{ language: 'fr', key: 'menu.file.save' }]);
  });

  it('reports a key that is a string in one language and an object in another on both sides', () => {
    const catalogs: Catalogs = {
      en: { language: 'Language' },
      fr: { language: { en: 'Anglais' } },
    };
    expect(findMissingKeys(catalogs)).toEqual([
      { language: 'en', key: 'language.en' },
      { language: 'fr', key: 'language' },
    ]);
  });

  it.each([
    ['an empty string', ''],
    ['a blank string', '   '],
  ])('counts %s as missing', (_name, value) => {
    const catalogs: Catalogs = {
      en: { greeting: 'Hello' },
      fr: { greeting: value },
    };
    expect(findMissingKeys(catalogs)).toEqual([{ language: 'fr', key: 'greeting' }]);
  });

  it('reports each language that lacks a key when there are three languages', () => {
    const catalogs: Catalogs = {
      en: { greeting: 'Hello', farewell: 'Bye' },
      fr: { greeting: 'Bonjour' },
      de: { farewell: 'Tschuess' },
    };
    expect(findMissingKeys(catalogs)).toEqual([
      { language: 'de', key: 'greeting' },
      { language: 'fr', key: 'farewell' },
    ]);
  });

  it('sorts the result by language, then by key', () => {
    const catalogs: Catalogs = {
      fr: { a: 'a' },
      en: { b: 'b', a: 'a', c: 'c' },
      de: { c: 'c' },
    };
    expect(findMissingKeys(catalogs)).toEqual([
      { language: 'de', key: 'a' },
      { language: 'de', key: 'b' },
      { language: 'fr', key: 'b' },
      { language: 'fr', key: 'c' },
    ]);
  });
});
