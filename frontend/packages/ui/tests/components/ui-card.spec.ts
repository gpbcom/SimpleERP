import userEvent from '@testing-library/user-event'
import { describe, expect, it } from 'vitest'

import UiCard from '../../src/components/UiCard.vue'
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations'
import { renderInTheme } from '../helpers/render-in-theme'
import { THEMES } from '../helpers/themes'

const SELECTABLES = ['radio', 'checkbox'] as const

describe('UiCard', () => {
  it('shows its title in a heading of the requested level', () => {
    const { getByRole } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Invoices', headingLevel: 4 },
    })
    expect(getByRole('heading', { level: 4, name: 'Invoices' })).toBeTruthy()
  })

  it('uses a level 3 heading by default', () => {
    const { getByRole } = renderInTheme(UiCard, { theme: 'light', props: { title: 'Invoices' } })
    expect(getByRole('heading', { level: 3, name: 'Invoices' })).toBeTruthy()
  })

  it('renders the default slot content', () => {
    const { getByText } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Invoices' },
      slots: { default: '<p>Twelve open</p>' },
    })
    expect(getByText('Twelve open')).toBeTruthy()
  })

  it('holds exactly one link, named by its title, when it has an href', () => {
    const { getAllByRole } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Invoices', href: '/invoices' },
    })
    const links = getAllByRole('link')
    expect(links).toHaveLength(1)
    expect(links[0]?.textContent?.trim()).toBe('Invoices')
    expect(links[0]?.getAttribute('href')).toBe('/invoices')
  })

  it('keeps the buttons of the actions slot outside the link', () => {
    const { getByRole } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Invoices', href: '/invoices' },
      slots: { actions: '<button type="button">Archive</button>' },
    })
    const button = getByRole('button', { name: 'Archive' })
    expect(getByRole('link').contains(button)).toBe(false)
  })

  it('has no link when it has no href', () => {
    const { queryByRole } = renderInTheme(UiCard, { theme: 'light', props: { title: 'Invoices' } })
    expect(queryByRole('link')).toBeNull()
  })

  it.each(SELECTABLES)('exposes a %s card with its own role, checked when selected', (selectable) => {
    const { getByRole } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Plan', selectable, selected: true, name: 'plan', value: 'pro' },
    })
    expect((getByRole(selectable) as HTMLInputElement).checked).toBe(true)
  })

  it.each(SELECTABLES)('leaves a %s card unchecked when it is not selected', (selectable) => {
    const { getByRole } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Plan', selectable, selected: false, name: 'plan', value: 'pro' },
    })
    expect((getByRole(selectable) as HTMLInputElement).checked).toBe(false)
  })

  it.each(SELECTABLES)('emits update:selected with true when space is pressed on a %s card', async (selectable) => {
    const user = userEvent.setup()
    const { getByRole, emitted } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Plan', selectable, selected: false, name: 'plan', value: 'pro' },
    })
    getByRole(selectable).focus()
    await user.keyboard(' ')
    expect(emitted()['update:selected']?.[0]).toEqual([true])
  })

  it.each(SELECTABLES)('shows an aria-hidden check icon on a selected %s card', (selectable) => {
    const { container } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Plan', selectable, selected: true, name: 'plan', value: 'pro' },
    })
    expect(container.querySelector('svg[aria-hidden="true"]')).not.toBeNull()
  })

  it.each(SELECTABLES)('shows no check icon on an unselected %s card', (selectable) => {
    const { container } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Plan', selectable, selected: false, name: 'plan', value: 'pro' },
    })
    expect(container.querySelector('svg[aria-hidden="true"]')).toBeNull()
  })

  it('is busy and shows skeleton lines while loading, without its slot content', () => {
    const { container, queryByText } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Invoices', loading: true },
      slots: { default: '<p>Twelve open</p>' },
    })
    expect(container.querySelector('[aria-busy="true"]')).not.toBeNull()
    expect(container.querySelectorAll('[class*="skeleton"]').length).toBeGreaterThan(0)
    expect(queryByText('Twelve open')).toBeNull()
  })

  it('is not busy when it is not loading', () => {
    const { container } = renderInTheme(UiCard, { theme: 'light', props: { title: 'Invoices' } })
    expect(container.querySelector('[aria-busy="true"]')).toBeNull()
  })

  it('renders its figure and its change', () => {
    const { getByText } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Revenue', figure: '12,400', change: '+4.2%' },
    })
    expect(getByText('12,400')).toBeTruthy()
    expect(getByText('+4.2%')).toBeTruthy()
  })

  it('reaches the link of a clickable card with the tab key', async () => {
    const user = userEvent.setup()
    const { getByRole } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Invoices', href: '/invoices' },
    })
    await user.tab()
    expect(document.activeElement).toBe(getByRole('link'))
  })

  it.each(SELECTABLES)('reaches the input of a selectable %s card with the tab key', async (selectable) => {
    const user = userEvent.setup()
    const { getByRole } = renderInTheme(UiCard, {
      theme: 'light',
      props: { title: 'Plan', selectable, selected: false, name: 'plan', value: 'pro' },
    })
    await user.tab()
    expect(document.activeElement).toBe(getByRole(selectable))
  })

  describe.each(THEMES)('in the %s theme', (theme) => {
    const cases: Array<[string, Record<string, unknown>, Record<string, unknown>]> = [
      ['a content card', { title: 'Invoices' }, { default: '<p>Twelve open</p>' }],
      ['a figure card', { title: 'Revenue', figure: '12,400', change: '+4.2%' }, {}],
      [
        'a clickable card',
        { title: 'Invoices', href: '/invoices' },
        { actions: '<button type="button">Archive</button>' },
      ],
      ['an unselected radio card', { title: 'Plan', selectable: 'radio', selected: false, name: 'plan', value: 'pro' }, {}],
      ['a selected radio card', { title: 'Plan', selectable: 'radio', selected: true, name: 'plan', value: 'pro' }, {}],
      [
        'an unselected checkbox card',
        { title: 'Plan', selectable: 'checkbox', selected: false, name: 'plan', value: 'pro' },
        {},
      ],
      [
        'a selected checkbox card',
        { title: 'Plan', selectable: 'checkbox', selected: true, name: 'plan', value: 'pro' },
        {},
      ],
      ['a loading card', { title: 'Invoices', loading: true }, {}],
    ]

    it.each(cases)('has no accessibility violation for %s', async (_name, props, slots) => {
      const { container } = renderInTheme(UiCard, { theme, props, slots })
      await expectNoAxeViolations(container)
    })
  })
})
