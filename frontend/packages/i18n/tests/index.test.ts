import { describe, expect, it } from 'vitest'

import * as i18n from '../src/index'
import type { Catalog, Catalogs, I18n, MissingKey, TranslateParams } from '../src/index'

describe('package entry point', () => {
  it.each([
    'createI18n',
    'useI18n',
    'availableLanguages',
    'findMissingKeys',
    'formatMoney',
    'formatNumber',
    'formatDate',
  ])('exports %s as a function', (name) => {
    expect(typeof (i18n as Record<string, unknown>)[name]).toBe('function')
  })

  it('exports the catalogues as a value', () => {
    expect(i18n.catalogs).toBeDefined()
  })

  it('exports the injection key as a symbol', () => {
    expect(typeof i18n.I18N_KEY).toBe('symbol')
  })

  it('lists English and French among the available languages', () => {
    expect(i18n.availableLanguages()).toEqual(expect.arrayContaining(['en', 'fr']))
  })

  it('translates a key in French through the entry point', () => {
    const instance: I18n = i18n.createI18n({ locale: 'fr-FR', catalogs: i18n.catalogs })
    expect(instance.t('language.fr').length).toBeGreaterThan(0)
  })

  it('exposes the public types', () => {
    const catalog: Catalog = {}
    const catalogs: Catalogs = { en: catalog }
    const missing: MissingKey[] = []
    const params: TranslateParams = {}
    expect([catalogs, missing, params]).toHaveLength(3)
  })
})
