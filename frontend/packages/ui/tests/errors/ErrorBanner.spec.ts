import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { screen } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import { describe, expect, it } from 'vitest'

import ErrorBanner from '../../src/errors/ErrorBanner.vue'
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations'
import { renderInTheme } from '../helpers/render-in-theme'
import { THEMES } from '../helpers/themes'

const props = {
  title: 'You are offline',
  why: 'Your time is saved and will sync.',
  actionLabel: 'Try again',
  reference: 'NET-OFFLINE-01',
  referenceLabel: 'ref.',
}

describe('ErrorBanner', () => {
  it('renders the title, the why, the action and the reference', () => {
    renderInTheme(ErrorBanner, { theme: 'light', props })

    expect(screen.getByText('You are offline')).toBeTruthy()
    expect(screen.getByText('Your time is saved and will sync.')).toBeTruthy()
    expect(screen.getByRole('button', { name: 'Try again' })).toBeTruthy()
    expect(screen.getByText('ref. NET-OFFLINE-01')).toBeTruthy()
  })

  it('renders no action button without an action label', () => {
    renderInTheme(ErrorBanner, { theme: 'light', props: { ...props, actionLabel: undefined } })

    expect(screen.queryByRole('button', { name: 'Try again' })).toBeNull()
  })

  it('has the role alert so that it is announced', () => {
    renderInTheme(ErrorBanner, { theme: 'light', props })

    expect(screen.getByRole('alert')).toBeTruthy()
  })

  it('shows the circle-alert icon, hidden from assistive technology, with the words', () => {
    renderInTheme(ErrorBanner, { theme: 'light', props })

    const banner = screen.getByRole('alert')
    const icon = banner.querySelector('svg.lucide-circle-alert')
    expect(icon).not.toBeNull()
    expect(icon?.getAttribute('aria-hidden')).toBe('true')
    expect(banner.textContent).toContain('You are offline')
  })

  it('colours itself with the error token', () => {
    const source = readFileSync(resolve(import.meta.dirname, '../../src/errors/ErrorBanner.vue'), 'utf-8')

    expect(source).toContain('var(--color-error)')
  })

  it('emits action when the action button is clicked', async () => {
    const user = userEvent.setup()
    const view = renderInTheme(ErrorBanner, { theme: 'light', props })

    await user.click(screen.getByRole('button', { name: 'Try again' }))

    expect(view.emitted().action).toHaveLength(1)
  })

  describe.each(THEMES)('in the %s theme', (theme) => {
    it('renders its content', () => {
      renderInTheme(ErrorBanner, { theme, props })

      expect(document.documentElement.getAttribute('data-theme')).toBe(theme)
      expect(screen.getByRole('alert').textContent).toContain('Your time is saved and will sync.')
    })

    it('has no accessibility violation', async () => {
      renderInTheme(ErrorBanner, { theme, props })

      await expectNoAxeViolations(document.body)
    })
  })
})
