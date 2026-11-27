import { h } from 'vue'
import { screen, waitFor } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import { describe, expect, it } from 'vitest'

import UiModal from '../../src/components/UiModal.vue'
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations'
import { renderInTheme } from '../helpers/render-in-theme'
import { THEMES } from '../helpers/themes'

type Variant = 'confirmation' | 'error' | 'form'

const VARIANTS: Variant[] = ['confirmation', 'error', 'form']

const baseProps = { open: true, title: 'Delete the invoice', closeLabel: 'Close the dialog' }

function formContent() {
  return () => [
    h('label', { for: 'modal-name' }, 'Name'),
    h('input', { id: 'modal-name', type: 'text' }),
    h('label', { for: 'modal-email' }, 'Email'),
    h('input', { id: 'modal-email', type: 'text' }),
  ]
}

function textContent() {
  return () => h('p', 'This action cannot be undone.')
}

function actionButtons() {
  return () => [h('button', { type: 'button' }, 'Cancel'), h('button', { type: 'button' }, 'Delete')]
}

function focusableIn(dialog: HTMLElement): HTMLElement[] {
  return Array.from(
    dialog.querySelectorAll<HTMLElement>('button, input, select, textarea, a[href], [tabindex]:not([tabindex="-1"])'),
  ).filter((element) => !element.hasAttribute('disabled'))
}

describe('UiModal', () => {
  it('renders no dialog while it is closed', () => {
    renderInTheme(UiModal, { theme: 'light', props: { ...baseProps, open: false }, slots: { default: textContent() } })

    expect(screen.queryByRole('dialog')).toBeNull()
    expect(screen.queryByRole('alertdialog')).toBeNull()
  })

  it('renders a modal dialog named by its title when it is open', () => {
    renderInTheme(UiModal, { theme: 'light', props: baseProps, slots: { default: textContent() } })

    const dialog = screen.getByRole('dialog', { name: 'Delete the invoice' })
    expect(dialog.getAttribute('aria-modal')).toBe('true')
  })

  it('renders an alert dialog for the error variant', () => {
    renderInTheme(UiModal, {
      theme: 'light',
      props: { ...baseProps, variant: 'error', title: 'Payment failed' },
      slots: { default: textContent() },
    })

    const dialog = screen.getByRole('alertdialog', { name: 'Payment failed' })
    expect(dialog.getAttribute('aria-modal')).toBe('true')
    expect(screen.queryByRole('dialog')).toBeNull()
  })

  it('moves the focus to the first input of its content', async () => {
    renderInTheme(UiModal, {
      theme: 'light',
      props: { ...baseProps, variant: 'form' },
      slots: { default: formContent() },
    })

    await waitFor(() => expect(document.activeElement).toBe(document.getElementById('modal-name')))
  })

  it('moves the focus to the dialog when its content has no field', async () => {
    renderInTheme(UiModal, { theme: 'light', props: baseProps, slots: { default: textContent() } })

    const dialog = screen.getByRole('dialog')
    await waitFor(() => expect(document.activeElement).toBe(dialog))
  })

  it('sends the focus from the last focusable element to the first on Tab', async () => {
    const user = userEvent.setup()
    renderInTheme(UiModal, {
      theme: 'light',
      props: { ...baseProps, variant: 'form' },
      slots: { default: formContent(), actions: actionButtons() },
    })
    const focusable = focusableIn(screen.getByRole('dialog'))
    const first = focusable[0]
    focusable[focusable.length - 1].focus()

    await user.tab()

    expect(document.activeElement).toBe(first)
  })

  it('sends the focus from the first focusable element to the last on Shift+Tab', async () => {
    const user = userEvent.setup()
    renderInTheme(UiModal, {
      theme: 'light',
      props: { ...baseProps, variant: 'form' },
      slots: { default: formContent(), actions: actionButtons() },
    })
    const focusable = focusableIn(screen.getByRole('dialog'))
    const last = focusable[focusable.length - 1]
    focusable[0].focus()

    await user.tab({ shift: true })

    expect(document.activeElement).toBe(last)
  })

  it('emits close when Escape is pressed', async () => {
    const user = userEvent.setup()
    const view = renderInTheme(UiModal, { theme: 'light', props: baseProps, slots: { default: textContent() } })

    await user.keyboard('{Escape}')

    expect(view.emitted().close).toHaveLength(1)
  })

  it('emits close when the close button, named by closeLabel, is clicked', async () => {
    const user = userEvent.setup()
    const view = renderInTheme(UiModal, { theme: 'light', props: baseProps, slots: { default: textContent() } })

    await user.click(screen.getByRole('button', { name: 'Close the dialog' }))

    expect(view.emitted().close).toHaveLength(1)
  })

  it('gives the focus back to the opener when it closes', async () => {
    const opener = document.createElement('button')
    opener.textContent = 'Open'
    document.body.appendChild(opener)
    const view = renderInTheme(UiModal, {
      theme: 'light',
      props: { ...baseProps, open: false },
      slots: { default: textContent() },
    })
    opener.focus()

    await view.rerender({ open: true })
    await waitFor(() => expect(document.activeElement).not.toBe(opener))
    await view.rerender({ open: false })

    await waitFor(() => expect(document.activeElement).toBe(opener))
    opener.remove()
  })

  it('shows an error icon hidden from assistive technology in the error variant', () => {
    renderInTheme(UiModal, {
      theme: 'light',
      props: { ...baseProps, variant: 'error', title: 'Payment failed' },
      slots: { default: textContent() },
    })

    const dialog = screen.getByRole('alertdialog')
    expect(dialog.querySelector('[aria-hidden="true"]')).not.toBeNull()
  })

  describe.each(THEMES)('in the %s theme', (theme) => {
    it.each(VARIANTS)('has no accessibility violation in the %s variant', async (variant) => {
      renderInTheme(UiModal, {
        theme,
        props: { ...baseProps, variant },
        slots: {
          default: variant === 'form' ? formContent() : textContent(),
          actions: actionButtons(),
        },
      })

      await expectNoAxeViolations(document.body)
    })
  })
})
