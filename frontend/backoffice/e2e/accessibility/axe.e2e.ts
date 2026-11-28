import { expectNoAccessibilityViolations } from '../fixtures/accessibility'
import { expect, test } from '../fixtures/test'

test.describe('Shell accessibility scan', () => {
  test('the shell with the sidebar expanded has no accessibility violation', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    await expect(page.locator('[data-shell="sidebar"]')).toHaveAttribute('data-collapsed', 'false')
    await expectNoAccessibilityViolations(page)
  })

  test('the shell with the sidebar collapsed has no accessibility violation', { tag: '@smoke' }, async ({ page }) => {
    await page.goto('/')
    await page.locator('[data-shell="sidebar-toggle"]').click()
    await expect(page.locator('[data-shell="sidebar"]')).toHaveAttribute('data-collapsed', 'true')
    await expectNoAccessibilityViolations(page)
  })

  // The user menu of T0.17 is a disabled placeholder button, not an opening menu, so there is no open state to scan.

  test.describe('on a phone', () => {
    test.use({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true })

    test('the shell with the bottom tab bar has no accessibility violation', { tag: '@smoke' }, async ({ page }) => {
      await page.goto('/')
      await expect(page.locator('[data-shell="tabbar"]')).toBeVisible()
      await expectNoAccessibilityViolations(page)
    })
  })
})
