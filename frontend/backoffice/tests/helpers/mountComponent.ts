import { mount } from '@vue/test-utils'
import type { VueWrapper } from '@vue/test-utils'
import type { Component } from 'vue'
import { createMemoryHistory } from 'vue-router'
import type { Router } from 'vue-router'

import { createBackofficePlugins } from '../../src/app/createBackofficePlugins'
import { installMatchMedia } from './media'
import type { MediaController } from './media'

export interface MountOptions {
  widthPx?: number
  dark?: boolean
  locale?: 'en' | 'fr'
  path?: string
  storedTheme?: 'light' | 'dark' | null
  props?: Record<string, unknown>
}

export async function mountComponent(
  component: Component,
  options: MountOptions = {},
): Promise<{ wrapper: VueWrapper; router: Router; media: MediaController }> {
  const media = installMatchMedia({ widthPx: options.widthPx ?? 1280, dark: options.dark ?? false })
  if (options.storedTheme) localStorage.setItem('simpleerp.theme', options.storedTheme)
  const { router, pinia, i18n } = createBackofficePlugins({
    history: createMemoryHistory(),
    locale: options.locale ?? 'en',
  })
  await router.push(options.path ?? '/')
  await router.isReady()
  const wrapper = mount(component, {
    props: options.props,
    global: { plugins: [pinia, router, i18n] },
    attachTo: document.body,
  })
  return { wrapper: wrapper as VueWrapper, router, media }
}
