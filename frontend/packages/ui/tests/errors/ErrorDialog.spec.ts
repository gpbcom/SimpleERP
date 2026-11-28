import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { screen, waitFor } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import { describe, expect, it } from 'vitest'

import ErrorDialog from '../../src/errors/ErrorDialog.vue'
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations'
import { renderInTheme } from '../helpers/render-in-theme'
import { THEMES } from '../helpers/themes'

const props = {
  open: true,
  title: 'This site still has stock',
  why: 'The Lyon yard holds 40 items and 3 employees.',
  actionLabel: 'See what is left',
  cancelLabel: 'Cancel',
  reference: 'SITE-CLOSE-01',
  referenceLabel: 'ref.',
}

describe('ErrorDialog', () => {
  it('renders no dialog while it is closed', () => {
    renderInTheme(ErrorDialog, { theme: 'light', props: { ...props, open: false } })

    expect(screen.queryByRole('alertdialog')).toBeNull()
  })

  it('renders the title, the why, the action, the cancel button and the reference', () => {
    renderInTheme(ErrorDialog, { theme: 'light', props })

    expect(screen.getByText('This site still has stock')).toBeTruthy()
    expect(screen.getByText('The Lyon yard holds 40 items and 3 employees.')).toBeTruthy()
    expect(screen.getByRole('button', { name: 'See what is left' })).toBeTruthy()
    expect(screen.getByRole('button', { name: 'Cancel' })).toBeTruthy()
    expect(screen.getByText('ref. SITE-CLOSE-01')).toBeTruthy()
  })

  it('has the role alertdialog', () => {
    renderInTheme(ErrorDialog, { theme: 'light', props })

    expect(screen.getByRole('alertdialog')).toBeTruthy()
  })

  it('is labelled by its title', () => {
    renderInTheme(ErrorDialog, { theme: 'light', props })

    const dialog = screen.getByRole('alertdialog')
    const title = document.getElementById(dialog.getAttribute('aria-labelledby') ?? '')
    expect(title?.textContent).toContain('This site still has stock')
  })

  it('is described by its why', () => {
    renderInTheme(ErrorDialog, { theme: 'light', props })

    const dialog = screen.getByRole('alertdialog')
    const why = document.getElementById(dialog.getAttribute('aria-describedby') ?? '')
    expect(why?.textContent).toContain('The Lyon yard holds 40 items and 3 employees.')
  })

  it('moves the focus into the dialog when it opens', async () => {
    renderInTheme(ErrorDialog, { theme: 'light', props })

    const dialog = screen.getByRole('alertdialog')
    await waitFor(() => expect(dialog.contains(document.activeElement)).toBe(true))
  })

  it('emits action when the action button is clicked', async () => {
    const user = userEvent.setup()
    const view = renderInTheme(ErrorDialog, { theme: 'light', props })

    await user.click(screen.getByRole('button', { name: 'See what is left' }))

    expect(view.emitted().action).toHaveLength(1)
    expect(view.emitted().cancel).toBeUndefined()
  })

  it('emits cancel when the cancel button is clicked', async () => {
    const user = userEvent.setup()
    const view = renderInTheme(ErrorDialog, { theme: 'light', props })

    await user.click(screen.getByRole('button', { name: 'Cancel' }))

    expect(view.emitted().cancel).toHaveLength(1)
    expect(view.emitted().action).toBeUndefined()
  })

  it('emits cancel when Escape is pressed', async () => {
    const user = userEvent.setup()
    const view = renderInTheme(ErrorDialog, { theme: 'light', props })

    await user.keyboard('{Escape}')

    expect(view.emitted().cancel).toHaveLength(1)
  })

  it('shows the circle-alert icon beside the title, hidden from assistive technology', () => {
    renderInTheme(ErrorDialog, { theme: 'light', props })

    const icon = screen.getByRole('alertdialog').querySelector('svg.lucide-circle-alert')
    expect(icon).not.toBeNull()
    expect(icon?.getAttribute('aria-hidden')).toBe('true')
  })

  it('colours its icon with the error token', () => {
    const source = readFileSync(resolve(process.cwd(), 'src/errors/ErrorDialog.vue'), 'utf-8')

    expect(source).toContain('var(--color-error)')
  })

  it('never shows the error by colour alone, the words are always present', () => {
    renderInTheme(ErrorDialog, { theme: 'light', props })

    const dialog = screen.getByRole('alertdialog')
    expect(dialog.textContent).toContain('This site still has stock')
    expect(dialog.textContent).toContain('The Lyon yard holds 40 items and 3 employees.')
  })

  describe.each(THEMES)('in the %s theme', (theme) => {
    it('renders its content', () => {
      renderInTheme(ErrorDialog, { theme, props })

      expect(document.documentElement.getAttribute('data-theme')).toBe(theme)
      expect(screen.getByRole('alertdialog', { name: 'This site still has stock' })).toBeTruthy()
    })

    it('has no accessibility violation', async () => {
      renderInTheme(ErrorDialog, { theme, props })

      await expectNoAxeViolations(document.body)
    })
  })
})
