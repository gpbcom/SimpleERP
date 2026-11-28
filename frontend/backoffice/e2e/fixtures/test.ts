import { test as base, expect } from '@playwright/test'
import { expectNoAccessibilityViolations } from './accessibility'

export const test = base.extend<{ accessibility: void }>({
  accessibility: [
    async ({ page }, use) => {
      await use()
      if (page.url() !== 'about:blank') {
        await expectNoAccessibilityViolations(page)
      }
    },
    { auto: true },
  ],
})

export { expect }
