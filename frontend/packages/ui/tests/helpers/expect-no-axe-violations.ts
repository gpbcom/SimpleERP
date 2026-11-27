import axe from 'axe-core'

/**
 * Fail when axe finds a WCAG 2.2 AA violation in the container (D46).
 *
 * The `color-contrast` rule is disabled because jsdom cannot compute colours. Contrast is covered by the contrast
 * test of the tokens package and by the Playwright axe runs of the screens.
 */
export async function expectNoAxeViolations(container: Element): Promise<void> {
  const results = await axe.run(container, {
    runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] },
    rules: { 'color-contrast': { enabled: false } },
  })
  const lines = results.violations.map(
    (violation) =>
      `${violation.id} (${violation.impact ?? 'unknown'}): ${violation.nodes.map((node) => node.target.join(' ')).join(', ')}`,
  )
  if (lines.length > 0) {
    throw new Error(`Accessibility violations found:\n${lines.join('\n')}`)
  }
}
