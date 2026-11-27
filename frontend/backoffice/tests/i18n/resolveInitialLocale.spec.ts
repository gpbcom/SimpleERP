import { describe, expect, it } from 'vitest';

import { availableLanguages } from '@simpleerp/i18n';

import { resolveInitialLocale } from '../../src/i18n/resolveInitialLocale';

describe('resolveInitialLocale', () => {
  const defaultLocale = availableLanguages()[0];

  it.each([
    [['fr-FR'], 'fr'],
    [['en-GB'], 'en'],
    [['de-DE', 'fr'], 'fr'],
    [['EN-us'], 'en'],
  ])('picks the first French or English browser language of %j', (languages, expected) => {
    expect(resolveInitialLocale(languages)).toBe(expected);
  });

  it.each([[['de']], [[]]])('falls back to the default locale of the i18n package for %j', (languages) => {
    expect(resolveInitialLocale(languages)).toBe(defaultLocale);
  });
});
