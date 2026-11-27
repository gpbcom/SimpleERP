import userEvent from '@testing-library/user-event'
import { screen } from '@testing-library/vue'
import { Send } from 'lucide-vue-next'
import { describe, expect, it } from 'vitest'

import UiButton from '../../src/components/UiButton.vue'
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations'
import { renderInTheme } from '../helpers/render-in-theme'
import { THEMES } from '../helpers/themes'

const VARIANTS = ['primary', 'secondary', 'danger', 'ghost'] as const

describe('UiButton', () => {
  describe.each(THEMES)('in the %s theme', (theme) => {
    it.each(VARIANTS)('the %s variant has its label as accessible name and no axe violation', async (variant) => {
      const { container } = renderInTheme(UiButton, { theme, props: { variant, label: 'Save' } })

      expect(screen.getByRole('button', { name: 'Save' })).toBeTruthy()
      await expectNoAxeViolations(container)
    })

    it('an icon-only button has its label as accessible name and no axe violation', async () => {
      const { container } = renderInTheme(UiButton, {
        theme,
        props: { label: 'Send', icon: Send, iconOnly: true },
      })

      expect(screen.getByRole('button', { name: 'Send' })).toBeTruthy()
      await expectNoAxeViolations(container)
    })
  })

  describe('element', () => {
    it('renders a native button of type button by default', () => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Save' } })

      const button = screen.getByRole('button', { name: 'Save' })
      expect(button.tagName).toBe('BUTTON')
      expect(button.getAttribute('type')).toBe('button')
    })

    it.each(['submit', 'reset'])('renders a button of type %s when asked', (type) => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Go', type } })

      expect(screen.getByRole('button', { name: 'Go' }).getAttribute('type')).toBe(type)
    })

    it('renders a link with its href when given one', () => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Open', href: '/orders' } })

      const link = screen.getByRole('link', { name: 'Open' })
      expect(link.tagName).toBe('A')
      expect(link.getAttribute('href')).toBe('/orders')
    })
  })

  describe('keyboard', () => {
    it('is focused by tab', async () => {
      const user = userEvent.setup()
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Save' } })

      await user.tab()

      expect(document.activeElement).toBe(screen.getByRole('button', { name: 'Save' }))
    })

    it.each(['{Enter}', ' '])('emits exactly one click on the key %j', async (key) => {
      const user = userEvent.setup()
      const { emitted } = renderInTheme(UiButton, { theme: 'light', props: { label: 'Save' } })

      await user.tab()
      await user.keyboard(key)

      expect(emitted('click')).toHaveLength(1)
    })

    it('emits one click when pressed with the pointer', async () => {
      const user = userEvent.setup()
      const { emitted } = renderInTheme(UiButton, { theme: 'light', props: { label: 'Save' } })

      await user.click(screen.getByRole('button', { name: 'Save' }))

      expect(emitted('click')).toHaveLength(1)
    })
  })

  describe('icon', () => {
    it('renders an aria-hidden svg before the label', () => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Send', icon: Send } })

      const button = screen.getByRole('button', { name: 'Send' })
      const svg = button.querySelector('svg')
      expect(svg).not.toBeNull()
      expect(svg?.getAttribute('aria-hidden')).toBe('true')
      expect(button.textContent).toContain('Send')
      expect(button.firstElementChild).toBe(svg)
    })

    it('an icon-only button has an aria-label equal to the label and shows no label text', () => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Send', icon: Send, iconOnly: true } })

      const button = screen.getByRole('button', { name: 'Send' })
      expect(button.getAttribute('aria-label')).toBe('Send')
      expect(button.querySelector('svg')).not.toBeNull()
      expect(button.textContent?.trim()).toBe('')
    })
  })

  describe('loading', () => {
    it('replaces the icon with a spinner and keeps the label', () => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Send', icon: Send, loading: true } })

      const button = screen.getByRole('button', { name: 'Send' })
      const svgs = button.querySelectorAll('svg')
      expect(svgs).toHaveLength(1)
      expect(svgs[0].getAttribute('aria-hidden')).toBe('true')
      expect(svgs[0].classList.contains('lucide-send')).toBe(false)
      expect(button.textContent).toContain('Send')
    })

    it('is marked busy and aria-disabled', () => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Send', loading: true } })

      const button = screen.getByRole('button', { name: 'Send' })
      expect(button.getAttribute('aria-busy')).toBe('true')
      expect(button.getAttribute('aria-disabled')).toBe('true')
    })

    it('stays in the tab order', async () => {
      const user = userEvent.setup()
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Send', loading: true } })

      await user.tab()

      expect(document.activeElement).toBe(screen.getByRole('button', { name: 'Send' }))
    })

    it('emits no click when pressed with the pointer', async () => {
      const user = userEvent.setup()
      const { emitted } = renderInTheme(UiButton, { theme: 'light', props: { label: 'Send', loading: true } })

      await user.click(screen.getByRole('button', { name: 'Send' }))

      expect(emitted('click')).toBeUndefined()
    })

    it.each(['{Enter}', ' '])('emits no click on the key %j', async (key) => {
      const user = userEvent.setup()
      const { emitted } = renderInTheme(UiButton, { theme: 'light', props: { label: 'Send', loading: true } })

      await user.tab()
      await user.keyboard(key)

      expect(emitted('click')).toBeUndefined()
    })
  })

  describe('disabled', () => {
    it('sets the native disabled attribute', () => {
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Save', disabled: true } })

      expect((screen.getByRole('button', { name: 'Save' }) as HTMLButtonElement).disabled).toBe(true)
    })

    it('is skipped by tab', async () => {
      const user = userEvent.setup()
      renderInTheme(UiButton, { theme: 'light', props: { label: 'Save', disabled: true } })

      await user.tab()

      expect(document.activeElement).not.toBe(screen.getByRole('button', { name: 'Save' }))
    })

    it('emits no click when pressed', async () => {
      const user = userEvent.setup()
      const { emitted } = renderInTheme(UiButton, { theme: 'light', props: { label: 'Save', disabled: true } })

      await user.click(screen.getByRole('button', { name: 'Save' }))

      expect(emitted('click')).toBeUndefined()
    })

    it('shows the reason as the title', () => {
      renderInTheme(UiButton, {
        theme: 'light',
        props: { label: 'Save', disabled: true, disabledReason: 'Nothing to save' },
      })

      expect(screen.getByRole('button', { name: 'Save' }).getAttribute('title')).toBe('Nothing to save')
    })
  })
})
