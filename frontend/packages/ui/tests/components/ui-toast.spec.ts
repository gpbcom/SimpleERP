import { screen } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import UiToast from '../../src/components/UiToast.vue'
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations'
import { renderInTheme } from '../helpers/render-in-theme'
import { THEMES } from '../helpers/themes'

const CLOSE_LABEL = 'Close notification'

function hover(target: Element, type: 'mouseenter' | 'mouseleave'): void {
  target.dispatchEvent(new MouseEvent(type, { bubbles: false }))
}

function focus(target: Element, type: 'focusin' | 'focusout'): void {
  target.dispatchEvent(new FocusEvent(type, { bubbles: true }))
}

describe('UiToast', () => {
  beforeEach(() => {
    vi.useFakeTimers()
  })

  afterEach(() => {
    vi.useRealTimers()
  })

  describe.each(THEMES)('in the %s theme', (theme) => {
    it.each([
      ['a success toast', { kind: 'success' }],
      ['an info toast', { kind: 'info' }],
      ['a toast with an action', { kind: 'success', actionLabel: 'Undo' }],
    ])('has no axe violation for %s', async (_name, extra) => {
      vi.useRealTimers()
      const { container } = renderInTheme(UiToast, {
        theme,
        props: { message: '12 tasks moved.', closeLabel: CLOSE_LABEL, ...extra },
      })
      await expectNoAxeViolations(container)
    })
  })

  it('is announced politely with role status and never as an alert', () => {
    const { container } = renderInTheme(UiToast, {
      theme: 'light',
      props: { message: 'Invoice out.', closeLabel: CLOSE_LABEL },
    })
    expect(screen.getByRole('status')).toBeTruthy()
    expect(container.querySelector('[role="alert"]')).toBeNull()
  })

  it.each([
    ['without an action', {}],
    ['with an action', { actionLabel: 'Undo' }],
  ])('never takes the focus when it mounts %s', (_name, extra) => {
    const before = document.createElement('button')
    document.body.appendChild(before)
    before.focus()
    renderInTheme(UiToast, {
      theme: 'light',
      props: { message: 'Invoice out.', closeLabel: CLOSE_LABEL, ...extra },
    })
    expect(document.activeElement).toBe(before)
    before.remove()
  })

  it('closes once after 6000 ms and not at 5999 ms when it has no action', () => {
    const view = renderInTheme(UiToast, {
      theme: 'light',
      props: { message: 'Invoice out.', closeLabel: CLOSE_LABEL },
    })
    vi.advanceTimersByTime(5999)
    expect(view.emitted('close')).toBeUndefined()
    vi.advanceTimersByTime(1)
    expect(view.emitted('close')).toHaveLength(1)
  })

  it.each([
    ['hovered', 'mouseenter', 'mouseleave'],
    ['focused', 'focusin', 'focusout'],
  ])('pauses while %s and closes after the time that was left', (_name, start, end) => {
    const view = renderInTheme(UiToast, {
      theme: 'light',
      props: { message: 'Invoice out.', closeLabel: CLOSE_LABEL },
    })
    const toast = screen.getByRole('status')
    vi.advanceTimersByTime(2000)
    if (start === 'mouseenter') hover(toast, 'mouseenter')
    else focus(toast, 'focusin')
    vi.advanceTimersByTime(60000)
    expect(view.emitted('close')).toBeUndefined()
    if (end === 'mouseleave') hover(toast, 'mouseleave')
    else focus(toast, 'focusout')
    vi.advanceTimersByTime(3999)
    expect(view.emitted('close')).toBeUndefined()
    vi.advanceTimersByTime(1)
    expect(view.emitted('close')).toHaveLength(1)
  })

  it('stays after 60 s when it has an action', () => {
    const view = renderInTheme(UiToast, {
      theme: 'light',
      props: { message: '12 tasks moved.', actionLabel: 'Undo', closeLabel: CLOSE_LABEL },
    })
    vi.advanceTimersByTime(60000)
    expect(view.emitted('close')).toBeUndefined()
  })

  it('reaches its action by keyboard and emits action on Enter', async () => {
    const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime })
    const view = renderInTheme(UiToast, {
      theme: 'light',
      props: { message: '12 tasks moved.', actionLabel: 'Undo', closeLabel: CLOSE_LABEL },
    })
    await user.tab()
    expect(document.activeElement).toBe(screen.getByRole('button', { name: 'Undo' }))
    await user.keyboard('{Enter}')
    expect(view.emitted('action')).toHaveLength(1)
  })

  it('names its close button by closeLabel and emits close when it is clicked', async () => {
    const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime })
    const view = renderInTheme(UiToast, {
      theme: 'light',
      props: { message: 'Invoice out.', closeLabel: CLOSE_LABEL },
    })
    await user.click(screen.getByRole('button', { name: CLOSE_LABEL }))
    expect(view.emitted('close')).toHaveLength(1)
  })

  it('renders different aria-hidden icons for the success and info kinds', () => {
    const icons = (['success', 'info'] as const).map((kind) => {
      const { container, unmount } = renderInTheme(UiToast, {
        theme: 'light',
        props: { kind, message: 'Export ready.', closeLabel: CLOSE_LABEL },
      })
      const icon = container.querySelector('[aria-hidden="true"]')
      expect(icon).not.toBeNull()
      const html = icon?.innerHTML ?? ''
      unmount()
      return html
    })
    expect(icons[0]).not.toBe('')
    expect(icons[0]).not.toBe(icons[1])
  })
})
