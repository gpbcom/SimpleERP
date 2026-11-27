import { describe, expect, it } from 'vitest'
import userEvent from '@testing-library/user-event'
import { screen } from '@testing-library/vue'

import UiFormField from '../../src/components/UiFormField.vue'
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations'
import { renderInTheme } from '../helpers/render-in-theme'
import { THEMES } from '../helpers/themes'

describe('UiFormField', () => {
  describe.each(THEMES)('in the %s theme', (theme) => {
    const variants: Array<[string, Record<string, unknown>]> = [
      ['default', {}],
      ['help', { help: 'Use the legal name.' }],
      ['error', { error: 'The name is required.', help: 'Use the legal name.' }],
      ['required', { required: true }],
      ['disabled', { disabled: true }],
      ['locked', { locked: true }],
      ['loading', { loading: true }],
    ]

    it.each(variants)('the %s field has no axe violation', async (_name, props) => {
      const { container } = renderInTheme(UiFormField, {
        theme,
        props: { label: 'Company name', modelValue: 'Acme', ...props },
      })
      await expectNoAxeViolations(container)
    })
  })

  describe('label', () => {
    it('gives the input its label as its accessible name', () => {
      renderInTheme(UiFormField, { theme: 'light', props: { label: 'Company name', modelValue: '' } })
      expect(screen.getByLabelText('Company name').tagName).toBe('INPUT')
    })

    it('keeps the label visible when a placeholder is set', () => {
      renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '', placeholder: 'Acme' },
      })
      expect(screen.getByText('Company name')).toBeVisible()
      expect(screen.getByLabelText('Company name')).toHaveAttribute('placeholder', 'Acme')
    })
  })

  describe('help and error', () => {
    it('links the help to the input with aria-describedby', () => {
      renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '', help: 'Use the legal name.' },
      })
      const input = screen.getByLabelText('Company name')
      const describedBy = input.getAttribute('aria-describedby') ?? ''
      expect(describedBy).not.toBe('')
      expect(document.getElementById(describedBy)).toHaveTextContent('Use the legal name.')
      expect(input).not.toHaveAttribute('aria-invalid', 'true')
    })

    it('replaces the help with the error and marks the input invalid', () => {
      renderInTheme(UiFormField, {
        theme: 'light',
        props: {
          label: 'Company name',
          modelValue: '',
          help: 'Use the legal name.',
          error: 'The name is required.',
        },
      })
      const input = screen.getByLabelText('Company name')
      const describedBy = input.getAttribute('aria-describedby') ?? ''
      expect(input).toHaveAttribute('aria-invalid', 'true')
      expect(document.getElementById(describedBy)).toHaveTextContent('The name is required.')
      expect(screen.queryByText('Use the legal name.')).toBeNull()
    })

    it('shows the error with a hidden alert icon and its text', () => {
      renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '', error: 'The name is required.' },
      })
      const input = screen.getByLabelText('Company name')
      const message = document.getElementById(input.getAttribute('aria-describedby') ?? '')
      expect(message).toHaveTextContent('The name is required.')
      const icon = message?.querySelector('svg')
      expect(icon).not.toBeNull()
      expect(icon).toHaveAttribute('aria-hidden', 'true')
    })
  })

  describe('required', () => {
    it('sets required on the input and hides the visible mark from assistive technology', () => {
      const { container } = renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '', required: true },
      })
      expect(screen.getByLabelText(/Company name/)).toBeRequired()
      const mark = container.querySelector('[aria-hidden="true"]:not(svg)')
      expect(mark).not.toBeNull()
      expect(mark).toHaveTextContent('*')
    })
  })

  describe('events', () => {
    it('emits update:modelValue with the typed value', async () => {
      const user = userEvent.setup()
      const { emitted } = renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '' },
      })
      await user.type(screen.getByLabelText('Company name'), 'A')
      expect(emitted()['update:modelValue']).toEqual([['A']])
    })

    it('emits blur when the field is left', async () => {
      const user = userEvent.setup()
      const { emitted } = renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '' },
      })
      await user.click(screen.getByLabelText('Company name'))
      await user.tab()
      expect(emitted().blur).toHaveLength(1)
    })
  })

  describe('keyboard', () => {
    it('reaches the input with the tab key', async () => {
      const user = userEvent.setup()
      renderInTheme(UiFormField, { theme: 'light', props: { label: 'Company name', modelValue: '' } })
      await user.tab()
      expect(screen.getByLabelText('Company name')).toHaveFocus()
    })

    it('skips a disabled input', async () => {
      const user = userEvent.setup()
      renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '', disabled: true },
      })
      await user.tab()
      expect(screen.getByLabelText('Company name')).not.toHaveFocus()
    })

    it('reaches a locked input, which is read-only and shows a lock icon', async () => {
      const user = userEvent.setup()
      const { container, emitted } = renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: 'Acme', locked: true },
      })
      const input = screen.getByLabelText('Company name')
      await user.tab()
      expect(input).toHaveFocus()
      expect(input).toHaveAttribute('readonly')
      await user.keyboard('xyz')
      expect(input).toHaveValue('Acme')
      expect(emitted()['update:modelValue']).toBeUndefined()
      expect(container.querySelector('svg')).not.toBeNull()
    })
  })

  describe('loading', () => {
    it('shows a spinner inside the field and marks the input busy', () => {
      const { container } = renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Company name', modelValue: '', loading: true },
      })
      expect(screen.getByLabelText('Company name')).toHaveAttribute('aria-busy', 'true')
      expect(container.querySelector('svg')).not.toBeNull()
    })
  })

  describe('unit', () => {
    it('renders the unit inside the field', () => {
      const { container } = renderInTheme(UiFormField, {
        theme: 'light',
        props: { label: 'Weight', modelValue: 12, type: 'number', unit: 'kg' },
      })
      expect(container).toHaveTextContent('kg')
      expect(screen.getByText('kg')).toBeVisible()
    })
  })
})
