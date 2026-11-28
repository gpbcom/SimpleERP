import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'

import type { Page } from '@playwright/test'

import { resolveErrorCode } from '../../../packages/i18n/src/errors/errorCatalog'
import { expectNoAccessibilityViolations } from '../fixtures/accessibility'
import { test, expect } from '../fixtures/test'

const REFUSED_CODE = 'CONTEXT-COMPANY-01'
const HEALTH_PATTERN = '**/v1/health'
const REFUSED_PATH = '/v1/anything'

type Language = 'fr' | 'en'
type Texts = Record<string, unknown>

function projectLanguage(): Language {
  return test.info().project.use.locale?.startsWith('fr') ? 'fr' : 'en'
}

function loadTexts(language: Language): Texts {
  const path = resolve(process.cwd(), '..', 'packages', 'i18n', 'src', 'catalogues', language, 'errors.json')
  return JSON.parse(readFileSync(path, 'utf-8')) as Texts
}

function walk(texts: Texts, path: string): unknown {
  return path.split('.').reduce<unknown>((node, part) => {
    return node && typeof node === 'object' ? (node as Texts)[part] : undefined
  }, texts)
}

function textOf(texts: Texts, key: string): string {
  const candidates = [texts[key], walk(texts, key), walk(texts, key.replace(/^errors\./, ''))]
  const value = candidates.find((candidate) => typeof candidate === 'string')
  if (typeof value !== 'string') throw new Error(`Missing error text: ${key}`)
  return value
}

async function refuseHealthCall(page: Page): Promise<void> {
  await page.route(HEALTH_PATTERN, async (route) => {
    const origin = new URL(route.request().url()).origin
    await route.continue({ url: `${origin}${REFUSED_PATH}` })
  })
}

test.describe('a refused call of platform', () => {
  test('the banner shows the title, the why, the action and the reference', async ({ page }) => {
    const texts = loadTexts(projectLanguage())
    const entry = resolveErrorCode(REFUSED_CODE)
    expect(entry.reference).toBeDefined()
    await refuseHealthCall(page)
    await page.goto('/')
    const banner = page.getByRole('alert').first()
    await expect(banner).toBeVisible()
    await expect(banner).toContainText(textOf(texts, entry.titleKey))
    await expect(banner).toContainText(textOf(texts, entry.whyKey))
    await expect(banner.getByRole('button', { name: textOf(texts, entry.actionKey) })).toBeVisible()
    await expect(banner).toContainText(`${textOf(texts, 'errors.common.reference')} ${entry.reference}`)
  })

  test('the banner is announced and drawn with the error colour and an icon', async ({ page }) => {
    await refuseHealthCall(page)
    await page.goto('/')
    const banner = page.getByRole('alert').first()
    await expect(banner).toBeVisible()
    await expect(banner.locator('svg').first()).toBeVisible()
    const colour = await banner.evaluate((element) => getComputedStyle(element).color)
    const expected = await page.evaluate(() => {
      const token = getComputedStyle(document.documentElement).getPropertyValue('--color-error').trim()
      const element = document.createElement('span')
      element.style.color = token
      document.body.appendChild(element)
      const value = getComputedStyle(element).color
      element.remove()
      return value
    })
    expect(colour).toBe(expected)
  })

  test('the page with the banner has no accessibility violation', async ({ page }) => {
    await refuseHealthCall(page)
    await page.goto('/')
    await expect(page.getByRole('alert').first()).toBeVisible()
    await expectNoAccessibilityViolations(page)
  })

  test('the action retries the health call without the reroute and the banner goes away', async ({ page }) => {
    const texts = loadTexts(projectLanguage())
    const entry = resolveErrorCode(REFUSED_CODE)
    await refuseHealthCall(page)
    await page.goto('/')
    const banner = page.getByRole('alert').first()
    await expect(banner).toBeVisible()
    await page.unroute(HEALTH_PATTERN)
    const retry = page.waitForResponse((response) => response.url().endsWith('/v1/health'))
    await banner.getByRole('button', { name: textOf(texts, entry.actionKey) }).click()
    expect((await retry).status()).toBe(200)
    await expect(page.getByRole('alert')).toHaveCount(0)
  })
})
