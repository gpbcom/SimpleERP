import { createPinia, setActivePinia } from 'pinia'
import { beforeEach, describe, expect, it, vi } from 'vitest'

import type { Refusal } from '../../src/errors/Refusal'
import { useErrorStore } from '../../src/stores/errors'

function aRefusal(overrides: Partial<Refusal> = {}): Refusal {
  return {
    id: 'r1',
    code: 'SITE-CLOSE-01',
    titleKey: 'errors.siteClose.title',
    whyKey: 'errors.siteClose.why',
    actionKey: 'errors.siteClose.action',
    reference: 'SITE-CLOSE-01',
    params: { site: 'Lyon' },
    field: null,
    presentation: 'dialog',
    ...overrides,
  }
}

describe('useErrorStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('starts with nothing to show', () => {
    const errors = useErrorStore()
    expect(errors.dialog).toBeNull()
    expect(errors.banner).toBeNull()
    expect(errors.fieldErrors).toEqual({})
  })

  it('shows a dialog refusal as the dialog', () => {
    const errors = useErrorStore()
    const refusal = aRefusal()
    errors.show(refusal)
    expect(errors.dialog).toEqual(refusal)
    expect(errors.banner).toBeNull()
  })

  it('shows a banner refusal as the banner', () => {
    const errors = useErrorStore()
    const refusal = aRefusal({ id: 'b1', presentation: 'banner' })
    errors.show(refusal)
    expect(errors.banner).toEqual(refusal)
    expect(errors.dialog).toBeNull()
  })

  it('keeps the latest dialog refusal as the dialog', () => {
    const errors = useErrorStore()
    errors.show(aRefusal({ id: 'first' }))
    errors.show(aRefusal({ id: 'second' }))
    expect(errors.dialog?.id).toBe('second')
  })

  it('keeps the latest banner refusal as the banner', () => {
    const errors = useErrorStore()
    errors.show(aRefusal({ id: 'first', presentation: 'banner' }))
    errors.show(aRefusal({ id: 'second', presentation: 'banner' }))
    expect(errors.banner?.id).toBe('second')
  })

  it('shows the earlier dialog again once the latest one is dismissed', () => {
    const errors = useErrorStore()
    errors.show(aRefusal({ id: 'first' }))
    errors.show(aRefusal({ id: 'second' }))
    errors.dismiss('second')
    expect(errors.dialog?.id).toBe('first')
  })

  it('removes a refusal when it is dismissed', () => {
    const errors = useErrorStore()
    errors.show(aRefusal())
    errors.dismiss('r1')
    expect(errors.dialog).toBeNull()
  })

  it('ignores the dismissal of an unknown id', () => {
    const errors = useErrorStore()
    errors.show(aRefusal())
    errors.dismiss('unknown')
    expect(errors.dialog?.id).toBe('r1')
  })

  it('maps each field name to its field refusal', () => {
    const errors = useErrorStore()
    const email = aRefusal({ id: 'f1', field: 'email', presentation: 'field' })
    const name = aRefusal({ id: 'f2', field: 'name', presentation: 'field' })
    errors.show(email)
    errors.show(name)
    expect(errors.fieldErrors).toEqual({ email, name })
  })

  it('keeps field refusals out of the dialog and the banner', () => {
    const errors = useErrorStore()
    errors.show(aRefusal({ id: 'f1', field: 'email', presentation: 'field' }))
    expect(errors.dialog).toBeNull()
    expect(errors.banner).toBeNull()
  })

  it('keeps dialog and banner refusals out of the field errors', () => {
    const errors = useErrorStore()
    errors.show(aRefusal())
    errors.show(aRefusal({ id: 'b1', presentation: 'banner' }))
    expect(errors.fieldErrors).toEqual({})
  })

  it('clears one field error and keeps the others', () => {
    const errors = useErrorStore()
    errors.show(aRefusal({ id: 'f1', field: 'email', presentation: 'field' }))
    errors.show(aRefusal({ id: 'f2', field: 'name', presentation: 'field' }))
    errors.clearField('email')
    expect(Object.keys(errors.fieldErrors)).toEqual(['name'])
  })

  it('does nothing when clearing a field that has no error', () => {
    const errors = useErrorStore()
    errors.show(aRefusal({ id: 'f2', field: 'name', presentation: 'field' }))
    errors.clearField('email')
    expect(Object.keys(errors.fieldErrors)).toEqual(['name'])
  })

  it('calls the action given at show, then dismisses the refusal', () => {
    const errors = useErrorStore()
    const seen: Array<string | undefined> = []
    const onAction = vi.fn(() => {
      seen.push(errors.dialog?.id)
    })
    errors.show(aRefusal(), onAction)
    errors.act('r1')
    expect(onAction).toHaveBeenCalledTimes(1)
    expect(seen).toEqual(['r1'])
    expect(errors.dialog).toBeNull()
  })

  it('dismisses a refusal acted on that has no action', () => {
    const errors = useErrorStore()
    errors.show(aRefusal())
    errors.act('r1')
    expect(errors.dialog).toBeNull()
  })

  it('calls only the action of the refusal acted on', () => {
    const errors = useErrorStore()
    const first = vi.fn()
    const second = vi.fn()
    errors.show(aRefusal({ id: 'first' }), first)
    errors.show(aRefusal({ id: 'second', presentation: 'banner' }), second)
    errors.act('second')
    expect(first).not.toHaveBeenCalled()
    expect(second).toHaveBeenCalledTimes(1)
    expect(errors.dialog?.id).toBe('first')
  })

  it('does not fail when acting on an unknown id', () => {
    const errors = useErrorStore()
    expect(() => errors.act('unknown')).not.toThrow()
  })

  it('keeps the keys and the params and never a translated text', () => {
    const errors = useErrorStore()
    errors.show(aRefusal())
    expect(errors.dialog).toMatchObject({
      titleKey: 'errors.siteClose.title',
      whyKey: 'errors.siteClose.why',
      actionKey: 'errors.siteClose.action',
      params: { site: 'Lyon' },
    })
    expect(Object.keys(errors.dialog ?? {}).sort()).toEqual(
      ['actionKey', 'code', 'field', 'id', 'params', 'presentation', 'reference', 'titleKey', 'whyKey'].sort(),
    )
  })
})
