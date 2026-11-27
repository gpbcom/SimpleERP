import { isRef, nextTick, watch } from 'vue'
import { describe, expect, it } from 'vitest'

import { createI18n } from '../../src/translate/createI18n'

const catalogs = {
  en: { greeting: 'Hello {name}', menu: { open: 'Open' } },
  fr: { greeting: 'Bonjour {name}', menu: { open: 'Ouvrir' } },
}

describe('createI18n', () => {
  it('returns the text of the language of the starting locale', () => {
    const i18n = createI18n({ locale: 'en-GB', catalogs })
    expect(i18n.t('menu.open')).toBe('Open')
  })

  it('resolves nested keys by their dotted path', () => {
    const i18n = createI18n({ locale: 'fr', catalogs })
    expect(i18n.t('menu.open')).toBe('Ouvrir')
  })

  it('replaces a placeholder with its parameter', () => {
    const i18n = createI18n({ locale: 'en', catalogs })
    expect(i18n.t('greeting', { name: 'Ada' })).toBe('Hello Ada')
  })

  it('replaces a placeholder with a number', () => {
    const i18n = createI18n({ locale: 'en', catalogs: { en: { count: '{n} items' } } })
    expect(i18n.t('count', { n: 3 })).toBe('3 items')
  })

  it('leaves an unknown placeholder as it is', () => {
    const i18n = createI18n({ locale: 'en', catalogs })
    expect(i18n.t('greeting', { other: 'x' })).toBe('Hello {name}')
  })

  it('returns French and the new locale after setLocale to fr-FR', () => {
    const i18n = createI18n({ locale: 'en', catalogs })
    i18n.setLocale('fr-FR')
    expect(i18n.t('greeting', { name: 'Ada' })).toBe('Bonjour Ada')
    expect(i18n.locale.value).toBe('fr-FR')
  })

  it('exposes the locale as a ref that a watch sees change', async () => {
    const i18n = createI18n({ locale: 'en', catalogs })
    expect(isRef(i18n.locale)).toBe(true)
    const seen: string[] = []
    watch(i18n.locale, (value) => seen.push(value))
    i18n.setLocale('fr-FR')
    await nextTick()
    expect(seen).toEqual(['fr-FR'])
  })

  it('returns the key when it is not found', () => {
    const i18n = createI18n({ locale: 'en', catalogs })
    expect(i18n.t('menu.missing')).toBe('menu.missing')
  })

  it('refuses a starting locale without a catalogue', () => {
    expect(() => createI18n({ locale: 'de-DE', catalogs })).toThrow(RangeError)
  })

  it('refuses a locale without a catalogue and keeps the current one', () => {
    const i18n = createI18n({ locale: 'en', catalogs })
    expect(() => i18n.setLocale('de')).toThrow(RangeError)
    expect(i18n.locale.value).toBe('en')
    expect(i18n.t('menu.open')).toBe('Open')
  })

  it('matches the language subtag case-insensitively', () => {
    const i18n = createI18n({ locale: 'EN-gb', catalogs })
    expect(i18n.t('menu.open')).toBe('Open')
  })
})
