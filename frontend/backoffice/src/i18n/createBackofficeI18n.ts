import { watch } from 'vue'
import type { App, Plugin } from 'vue'

import { createI18n } from '@simpleerp/i18n'
import type { Catalog } from '@simpleerp/i18n'

import en from '../locales/en.json'
import fr from '../locales/fr.json'
import type { BackofficeLocale } from './resolveInitialLocale'

/** Create the i18n plugin of the back office, which keeps `<html lang>` equal to the active locale. */
export function createBackofficeI18n(locale: BackofficeLocale): Plugin {
  const i18n = createI18n({ locale, catalogs: { en: en as Catalog, fr: fr as Catalog } })
  return {
    install(app: App): void {
      i18n.install(app)
      document.documentElement.lang = i18n.locale.value
      watch(
        i18n.locale,
        (next) => {
          document.documentElement.lang = next
        },
        { flush: 'sync' },
      )
    },
  }
}
