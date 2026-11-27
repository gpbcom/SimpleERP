import axe from 'axe-core'
import { describe, expect, it } from 'vitest'

import { mountApp } from '../helpers/mountApp'

const FOCUSABLE = 'a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])'

const AXE_OPTIONS = { rules: { 'color-contrast': { enabled: false } } }

describe('AppShell', () => {
  it('has the skip link as its first focusable element', async () => {
    const { container } = await mountApp()
    const first = container.querySelector(FOCUSABLE)
    expect(first).not.toBeNull()
    expect(first?.getAttribute('data-shell')).toBe('skip-link')
    expect(first?.getAttribute('href')).toBe('#main-content')
  })

  it('moves the focus to the main content when the skip link is clicked', async () => {
    const { container } = await mountApp()
    const link = container.querySelector<HTMLAnchorElement>('[data-shell="skip-link"]')
    const main = container.querySelector<HTMLElement>('main#main-content')
    expect(main?.getAttribute('tabindex')).toBe('-1')
    link?.click()
    expect(document.activeElement).toBe(main)
  })

  it.each([1280, 1000])('renders the sidebar and the top bar but no tab bar at %i px', async (widthPx) => {
    const { container } = await mountApp({ widthPx })
    expect(container.querySelector('[data-shell="sidebar"]')).not.toBeNull()
    expect(container.querySelector('[data-shell="topbar"]')).not.toBeNull()
    expect(container.querySelector('[data-shell="tabbar"]')).toBeNull()
  })

  it('renders the tab bar and the top bar but no sidebar at 375 px', async () => {
    const { container } = await mountApp({ widthPx: 375 })
    expect(container.querySelector('[data-shell="tabbar"]')).not.toBeNull()
    expect(container.querySelector('[data-shell="topbar"]')).not.toBeNull()
    expect(container.querySelector('[data-shell="sidebar"]')).toBeNull()
  })

  it('swaps the sidebar for the tab bar when the width drops to 375 px', async () => {
    const { container, media } = await mountApp({ widthPx: 1280 })
    expect(container.querySelector('[data-shell="sidebar"]')).not.toBeNull()
    media.setWidth(375)
    await new Promise((resolve) => setTimeout(resolve, 0))
    expect(container.querySelector('[data-shell="sidebar"]')).toBeNull()
    expect(container.querySelector('[data-shell="tabbar"]')).not.toBeNull()
  })

  it.each([1280, 1000, 375])('has exactly one labelled nav landmark at %i px', async (widthPx) => {
    const { container } = await mountApp({ widthPx })
    const navs = container.querySelectorAll('nav')
    expect(navs).toHaveLength(1)
    expect((navs[0]?.getAttribute('aria-label') ?? '').trim()).not.toBe('')
  })

  it.each([
    [1280, 'sidebar'],
    [375, 'tabbar'],
  ])('marks the current item with aria-current at %i px in the %s', async (widthPx, region) => {
    const { container } = await mountApp({ widthPx, path: '/' })
    const current = container.querySelectorAll(`[data-shell="${region}"] [data-nav-item][aria-current="page"]`)
    expect(current).toHaveLength(1)
  })

  it.each([
    ['light', false, 'en', 'Skip to content'],
    ['light', false, 'fr', 'Aller au contenu'],
    ['dark', true, 'en', 'Skip to content'],
    ['dark', true, 'fr', 'Aller au contenu'],
  ])('renders the %s theme in %s with no accessibility violation', async (theme, dark, locale, text) => {
    const { container } = await mountApp({ dark, locale: locale as 'en' | 'fr' })
    expect(document.documentElement.getAttribute('data-theme')).toBe(theme)
    expect(document.documentElement.lang).toBe(locale)
    expect(container.querySelector('[data-shell="skip-link"]')?.textContent?.trim()).toBe(text)
    const results = await axe.run(container, AXE_OPTIONS)
    expect(results.violations).toEqual([])
  })

  it('has no accessibility violation at 375 px', async () => {
    const { container } = await mountApp({ widthPx: 375 })
    const results = await axe.run(container, AXE_OPTIONS)
    expect(results.violations).toEqual([])
  })

  it('renders dark for a stored dark choice on a light device, and keeps it after a new mount', async () => {
    const first = await mountApp({ dark: false, storedTheme: 'dark' })
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark')
    first.unmount()
    document.documentElement.removeAttribute('data-theme')
    await mountApp({ dark: false })
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark')
  })
})
