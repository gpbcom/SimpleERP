import { createPinia } from 'pinia'
import type { Pinia } from 'pinia'
import type { Plugin } from 'vue'
import type { Router, RouterHistory } from 'vue-router'

import { createBackofficeI18n } from '../i18n/createBackofficeI18n'
import { resolveInitialLocale } from '../i18n/resolveInitialLocale'
import type { BackofficeLocale } from '../i18n/resolveInitialLocale'
import { createBackofficeRouter } from '../router/createBackofficeRouter'

export interface BackofficeOptions {
  history?: RouterHistory
  locale?: BackofficeLocale
}

/** Assemble the router, the Pinia store and the i18n plugin of the back office. */
export function createBackofficePlugins(options: BackofficeOptions = {}): {
  router: Router
  pinia: Pinia
  i18n: Plugin
} {
  const locale = options.locale ?? resolveInitialLocale(navigator.languages)
  return {
    router: createBackofficeRouter(options.history),
    pinia: createPinia(),
    i18n: createBackofficeI18n(locale),
  }
}
