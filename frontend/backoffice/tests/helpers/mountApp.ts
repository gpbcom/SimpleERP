import { createMemoryHistory } from 'vue-router'
import type { Router } from 'vue-router'

import { createBackofficeApp } from '../../src/app/createBackofficeApp'
import { installMatchMedia } from './media'
import type { MediaController } from './media'
import type { MountOptions } from './mountComponent'

export async function mountApp(
  options: Omit<MountOptions, 'props'> = {},
): Promise<{ container: HTMLElement; router: Router; media: MediaController; unmount(): void }> {
  const media = installMatchMedia({ widthPx: options.widthPx ?? 1280, dark: options.dark ?? false })
  if (options.storedTheme) localStorage.setItem('simpleerp.theme', options.storedTheme)
  const { app, router } = createBackofficeApp({
    history: createMemoryHistory(),
    locale: options.locale ?? 'en',
  })
  await router.push(options.path ?? '/')
  await router.isReady()
  const container = document.createElement('div')
  document.body.appendChild(container)
  app.mount(container)
  return { container, router, media, unmount: () => app.unmount() }
}
