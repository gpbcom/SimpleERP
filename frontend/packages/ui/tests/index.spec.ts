import { describe, expect, it } from 'vitest'

import * as ui from '../src/index'

describe('package exports', () => {
  const names = ['UiButton', 'UiFormField', 'UiNavItem', 'UiToast', 'UiModal', 'UiCard', 'UiIcon', 'UiSpinner']

  it.each(names)('exports %s', (name) => {
    expect(Object.keys(ui)).toContain(name)
  })

  it.each(names)('exports %s as a Vue component', (name) => {
    const value = (ui as Record<string, unknown>)[name]
    expect(['object', 'function']).toContain(typeof value)
  })
})
