import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'

import { test, expect } from '../fixtures/test'

interface Catalogue {
  shell: Record<string, string>
  nav: Record<string, string>
}

function expectedLanguage(): 'fr' | 'en' {
  return test.info().project.use.locale?.startsWith('fr') ? 'fr' : 'en'
}

function loadCatalogue(language: 'fr' | 'en'): Catalogue {
  const path = resolve(process.cwd(), 'src', 'locales', `${language}.json`)
  return JSON.parse(readFileSync(path, 'utf-8')) as Catalogue
}

test.describe('language', () => {
  test('the page declares the language of the project', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    await expect(page.locator('html')).toHaveAttribute('lang', new RegExp(`^${expectedLanguage()}`))
  })

  test('the skip link and the first sidebar item use the catalogue', { tag: '@smoke' }, async ({ page }) => {
    const catalogue = loadCatalogue(expectedLanguage())
    await page.goto('/')
    await expect(page.locator('[data-shell="skip-link"]')).toHaveText(catalogue.shell.skipToContent)
    await expect(page.locator('[data-nav-item="home"]').first()).toContainText(catalogue.nav.home)
  })

  test('no visible text of the shell is a raw catalogue key', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    await expect(page.locator('[data-nav-item="home"]').first()).toBeVisible()
    const text = await page.locator('body').innerText()
    expect(text).not.toMatch(/\b(shell|nav|app|page)\.[A-Za-z]+\b/)
  })
})
