import { createApp } from 'vue'
import type { App as VueApp, Plugin } from 'vue'
import type { Pinia } from 'pinia'
import type { Router } from 'vue-router'

import App from '../App.vue'
import { createBackofficePlugins } from './createBackofficePlugins'
import type { BackofficeOptions } from './createBackofficePlugins'

/** Create the back-office application with its router, store and i18n plugins installed. */
export function createBackofficeApp(options: BackofficeOptions = {}): {
  app: VueApp<Element>
  router: Router
  pinia: Pinia
  i18n: Plugin
} {
  const { router, pinia, i18n } = createBackofficePlugins(options)
  const app = createApp(App)
  app.use(pinia)
  app.use(router)
  app.use(i18n)
  return { app, router, pinia, i18n }
}
