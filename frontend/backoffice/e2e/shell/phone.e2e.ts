import en from '../../src/locales/en.json' with { type: 'json' }
import fr from '../../src/locales/fr.json' with { type: 'json' }
import { expect, test } from '../fixtures/test'

function labels(): typeof en {
  const locale = test.info().project.use.locale ?? 'en'
  return locale.startsWith('fr') ? fr : en
}

test.describe('Back-office shell: phone tab bar', () => {
  test.use({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true })

  test('the bottom tab bar is a named navigation and the sidebar is hidden', { tag: '@smoke' }, async ({ page }) => {
    const text = labels()
    await page.goto('/')

    await expect(page.getByRole('navigation', { name: text.shell.navigation })).toBeVisible()
    await expect(page.locator('[data-shell="tabbar"]')).toBeVisible()
    await expect(page.locator('[data-shell="sidebar"]')).toBeHidden()
  })

  test('the tabs are Home, Tasks, Assistant and Me', { tag: '@smoke' }, async ({ page }) => {
    const text = labels()
    await page.goto('/')

    const tabs = page.getByRole('navigation', { name: text.shell.navigation })
    for (const label of [text.nav.home, text.nav.tasks, text.nav.assistant, text.nav.me]) {
      await expect(tabs.getByText(label, { exact: true })).toBeVisible()
    }
    await expect(tabs.getByRole('link', { name: text.nav.home })).toHaveAttribute('aria-current', 'page')
  })
})
