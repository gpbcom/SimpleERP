import en from '../../src/locales/en.json' with { type: 'json' }
import fr from '../../src/locales/fr.json' with { type: 'json' }
import { expect, test } from '../fixtures/test'

function labels(): typeof en {
  const locale = test.info().project.use.locale ?? 'en'
  return locale.startsWith('fr') ? fr : en
}

test.describe('Back-office shell: top bar', () => {
  test('the banner holds the places for search, assistant, notifications, site and user', { tag: '@smoke' }, async ({ page }) => {
    const text = labels()
    await page.goto('/')

    const banner = page.getByRole('banner')
    await expect(banner).toBeVisible()
    await expect(banner.getByRole('search', { name: text.shell.search })).toBeVisible()
    await expect(banner.getByRole('searchbox', { name: text.shell.search })).toBeVisible()
    for (const name of [
      text.shell.assistant,
      text.shell.notifications,
      text.shell.siteSwitcher,
      text.shell.userMenu,
    ]) {
      await expect(banner.getByRole('button', { name })).toBeVisible()
    }
  })
})
