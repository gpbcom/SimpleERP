import { test, expect } from '../fixtures/test'

type Theme = 'light' | 'dark'

function expectedTheme(): Theme {
  return test.info().project.use.colorScheme === 'dark' ? 'dark' : 'light'
}

test.describe('theme', () => {
  test('the active theme follows the device setting', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    await expect(page.locator('html')).toHaveAttribute('data-theme', expectedTheme())
  })

  test('the two themes paint different backgrounds', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    const background = async (): Promise<string> =>
      page.evaluate(() => getComputedStyle(document.body).backgroundColor)
    const current = await background()
    await page.locator('[data-place="theme"]').click()
    await expect(page.locator('html')).not.toHaveAttribute('data-theme', expectedTheme())
    expect(await background()).not.toBe(current)
  })

  test('the manual switch overrides the device setting', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    const other: Theme = expectedTheme() === 'dark' ? 'light' : 'dark'
    await page.locator('[data-place="theme"]').click()
    await expect(page.locator('html')).toHaveAttribute('data-theme', other)
  })
})
