import AxeBuilder from '@axe-core/playwright'
import type { Page } from '@playwright/test'

const WCAG_TAGS = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa']

export async function expectNoAccessibilityViolations(page: Page): Promise<void> {
  const results = await new AxeBuilder({ page }).withTags(WCAG_TAGS).analyze()
  if (results.violations.length === 0) return
  const lines = results.violations.map((violation) => {
    const targets = violation.nodes.map((node) => node.target.join(' ')).join(', ')
    return `${violation.id}: ${violation.help} (${targets})`
  })
  throw new Error(`Accessibility violations found:\n${lines.join('\n')}`)
}
