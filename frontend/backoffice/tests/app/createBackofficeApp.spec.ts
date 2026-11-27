import { describe, expect, it } from 'vitest'

import { mountApp } from '../helpers/mountApp'

describe('createBackofficeApp', () => {
  it.each([
    ['en', '/', 'Home'],
    ['fr', '/', 'Accueil'],
    ['en', '/tasks', 'Tasks'],
    ['fr', '/tasks', 'Tâches'],
  ] as const)('in %s the page heading at %s reads %s', async (locale, path, heading) => {
    const { container } = await mountApp({ locale, path })
    expect(container.querySelector('h1')?.textContent?.trim()).toBe(heading)
  })

  it('an unknown path ends on the home route', async () => {
    const { router } = await mountApp({ path: '/no/such/page' })
    expect(router.currentRoute.value.name).toBe('home')
  })

  it.each(['en', 'fr'] as const)('the html lang equals the locale %s', async (locale) => {
    await mountApp({ locale })
    expect(document.documentElement.lang).toBe(locale)
  })

  it('a main#main-content element holds the page', async () => {
    const { container } = await mountApp()
    const main = container.querySelector('main#main-content')
    expect(main).not.toBeNull()
    expect(main?.querySelector('h1')).not.toBeNull()
  })

  it('the theme store is usable with a light device', async () => {
    await mountApp({ dark: false })
    expect(document.documentElement.getAttribute('data-theme')).toBe('light')
  })
})
