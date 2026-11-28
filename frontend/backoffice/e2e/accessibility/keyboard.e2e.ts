import { readFileSync } from 'node:fs'
import { join } from 'node:path'

import type { Page } from '@playwright/test'

import { expect, test } from '../fixtures/test'

const MAX_TABS = 40

interface Catalogue {
  shell: { skipToContent: string }
}

function skipText(testDir: string, locale: string | undefined): string {
  const language = locale?.startsWith('fr') ? 'fr' : 'en'
  const raw: unknown = JSON.parse(readFileSync(join(testDir, '..', 'src', 'locales', `${language}.json`), 'utf-8'))
  return (raw as Catalogue).shell.skipToContent
}

async function focusedPlace(page: Page): Promise<string | null> {
  return page.evaluate(() => {
    const element = document.activeElement as HTMLElement | null
    if (element?.dataset.navItem) {
      return `nav:${element.dataset.navItem}`
    }
    const place = element?.closest<HTMLElement>('[data-place]')?.dataset.place
    return place ? `place:${place}` : null
  })
}

async function hasVisibleFocus(page: Page): Promise<boolean> {
  return page.evaluate(() => {
    const element = document.activeElement
    if (!element) {
      return false
    }
    const style = getComputedStyle(element)
    const outline = style.outlineStyle !== 'none' && parseFloat(style.outlineWidth) > 0
    return outline || (style.boxShadow !== 'none' && style.boxShadow !== '')
  })
}

test.describe('Shell keyboard navigation', () => {
  test('the first Tab focuses the skip link with the catalogue text', { tag: '@smoke' }, async ({ page }, testInfo) => {
    await page.goto('/')
    await page.keyboard.press('Tab')
    const link = page.locator('[data-shell="skip-link"]')
    await expect(link).toBeFocused()
    await expect(link).toHaveText(skipText(testInfo.project.testDir, testInfo.project.use.locale))
  })

  test('activating the skip link moves focus to the main landmark', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    await page.keyboard.press('Tab')
    await page.keyboard.press('Enter')
    await expect(page.getByRole('main')).toBeFocused()
  })

  test('the current page navigation item carries aria-current page', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    const current = page.locator('[data-shell="sidebar"] [aria-current="page"]')
    await expect(current).toHaveCount(1)
    await expect(current).toHaveAttribute('data-nav-item', 'home')
  })

  test(
    'every sidebar item and top bar place is reachable by Tab with a visible focus',
    { tag: '@smoke' },
    async ({ page }) => {
      await page.goto('/')
      const expected = new Set<string>()
      const items = await page
        .locator('[data-shell="sidebar"] [data-nav-item]')
        .evaluateAll((nodes) => nodes.map((node) => (node as HTMLElement).dataset.navItem ?? ''))
      for (const id of items) {
        expected.add(`nav:${id}`)
      }
      const places = await page
        .locator('[data-shell="topbar"] [data-place]')
        .evaluateAll((nodes) => nodes.map((node) => (node as HTMLElement).dataset.place ?? ''))
      for (const place of places) {
        expected.add(`place:${place}`)
      }
      expect(expected.size).toBeGreaterThan(0)

      const reached = new Set<string>()
      for (let press = 0; press < MAX_TABS && reached.size < expected.size; press += 1) {
        await page.keyboard.press('Tab')
        const place = await focusedPlace(page)
        if (place !== null && expected.has(place)) {
          reached.add(place)
          expect(await hasVisibleFocus(page), `focus is visible on ${place}`).toBe(true)
        }
      }
      expect([...reached].sort()).toEqual([...expected].sort())
    },
  )
})
