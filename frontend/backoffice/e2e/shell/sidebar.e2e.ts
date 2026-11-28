import en from '../../src/locales/en.json' with { type: 'json' }
import fr from '../../src/locales/fr.json' with { type: 'json' }
import { expect, test } from '../fixtures/test'

function labels(): typeof en {
  const locale = test.info().project.use.locale ?? 'en'
  return locale.startsWith('fr') ? fr : en
}

test.describe('Back-office shell: sidebar', () => {
  test('the expanded sidebar shows the symbol and the items with their labels', { tag: '@smoke' }, async ({ page }) => {
    const text = labels()
    await page.goto('/')

    const nav = page.getByRole('navigation', { name: text.shell.navigation })
    await expect(nav).toBeVisible()
    await expect(page.locator('[data-shell="symbol"]')).toBeVisible()
    for (const label of [text.nav.home, text.nav.tasks, text.nav.assistant]) {
      await expect(nav.getByText(label, { exact: true })).toBeVisible()
    }
  })

  test('the item of the current page carries aria-current page', { tag: '@smoke' }, async ({ page }) => {
    const text = labels()
    await page.goto('/')

    const nav = page.getByRole('navigation', { name: text.shell.navigation })
    await expect(nav.getByRole('link', { name: text.nav.home })).toHaveAttribute('aria-current', 'page')
    await expect(nav.getByRole('link', { name: text.nav.tasks })).not.toHaveAttribute('aria-current', 'page')
  })

  test('collapsing the sidebar leaves icons only, and expanding it restores the labels', { tag: '@smoke' }, async ({ page }) => {
    const text = labels()
    await page.goto('/')
    const nav = page.getByRole('navigation', { name: text.shell.navigation })

    await page.getByRole('button', { name: text.shell.collapseSidebar }).click()

    const expand = page.getByRole('button', { name: text.shell.expandSidebar })
    await expect(expand).toHaveAttribute('aria-expanded', 'false')
    for (const label of [text.nav.home, text.nav.tasks, text.nav.assistant]) {
      await expect(nav.getByText(label, { exact: true })).toHaveCount(0)
    }
    await expect(nav.getByRole('link', { name: text.nav.home })).toBeVisible()
    await expect(nav.getByRole('link', { name: text.nav.tasks })).toBeVisible()
    await expect(nav.getByRole('button', { name: text.nav.assistant })).toBeVisible()

    await expand.click()

    await expect(page.getByRole('button', { name: text.shell.collapseSidebar })).toHaveAttribute('aria-expanded', 'true')
    for (const label of [text.nav.home, text.nav.tasks, text.nav.assistant]) {
      await expect(nav.getByText(label, { exact: true })).toBeVisible()
    }
  })
})
