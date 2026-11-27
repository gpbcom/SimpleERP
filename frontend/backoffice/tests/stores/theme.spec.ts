import { createPinia, setActivePinia } from 'pinia'
import { afterEach, beforeEach, describe, expect, it } from 'vitest'

import { installMatchMedia, type MediaController } from '../helpers/media'
import { useThemeStore } from '../../src/stores/theme'

const STORAGE_KEY = 'simpleerp.theme'

describe('useThemeStore', () => {
  let media: MediaController

  function setUp(dark: boolean): void {
    media = installMatchMedia({ widthPx: 1280, dark })
    setActivePinia(createPinia())
  }

  beforeEach(() => {
    setUp(false)
  })

  afterEach(() => {
    media.uninstall()
  })

  it.each([
    { dark: false, expected: 'light' },
    { dark: true, expected: 'dark' },
  ])('with no stored choice it follows a device that is dark: $dark', ({ dark, expected }) => {
    media.uninstall()
    setUp(dark)
    const store = useThemeStore()
    expect(store.preference).toBe('system')
    expect(store.resolved).toBe(expected)
    expect(document.documentElement.getAttribute('data-theme')).toBe(expected)
    expect(document.documentElement.style.colorScheme).toBe(expected)
  })

  it('a device change while on system switches the theme live', () => {
    const store = useThemeStore()
    expect(store.resolved).toBe('light')
    media.setDark(true)
    expect(store.resolved).toBe('dark')
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark')
    media.setDark(false)
    expect(store.resolved).toBe('light')
    expect(document.documentElement.getAttribute('data-theme')).toBe('light')
  })

  it('toggle on a light device gives dark, stores dark and sets data-theme dark', () => {
    const store = useThemeStore()
    store.toggle()
    expect(store.preference).toBe('dark')
    expect(store.resolved).toBe('dark')
    expect(localStorage.getItem(STORAGE_KEY)).toBe('dark')
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark')
    expect(document.documentElement.style.colorScheme).toBe('dark')
  })

  it('toggle on a dark device gives light and stores light', () => {
    media.uninstall()
    setUp(true)
    const store = useThemeStore()
    store.toggle()
    expect(store.preference).toBe('light')
    expect(store.resolved).toBe('light')
    expect(localStorage.getItem(STORAGE_KEY)).toBe('light')
  })

  it('a stored dark wins over a light device at creation', () => {
    media.uninstall()
    localStorage.setItem(STORAGE_KEY, 'dark')
    setUp(false)
    const store = useThemeStore()
    expect(store.preference).toBe('dark')
    expect(store.resolved).toBe('dark')
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark')
  })

  it('a device change does not override a manual choice', () => {
    const store = useThemeStore()
    store.setPreference('light')
    media.setDark(true)
    expect(store.resolved).toBe('light')
    expect(document.documentElement.getAttribute('data-theme')).toBe('light')
    expect(localStorage.getItem(STORAGE_KEY)).toBe('light')
  })

  it('setting system removes the key and follows the device again', () => {
    const store = useThemeStore()
    store.setPreference('dark')
    expect(localStorage.getItem(STORAGE_KEY)).toBe('dark')
    store.setPreference('system')
    expect(localStorage.getItem(STORAGE_KEY)).toBeNull()
    expect(store.preference).toBe('system')
    expect(store.resolved).toBe('light')
    media.setDark(true)
    expect(store.resolved).toBe('dark')
  })

  it.each(['purple', '', 'DARK', 'system'])('an invalid stored value %j is treated as system', (stored) => {
    media.uninstall()
    localStorage.setItem(STORAGE_KEY, stored)
    setUp(true)
    const store = useThemeStore()
    expect(store.preference).toBe('system')
    expect(store.resolved).toBe('dark')
  })
})
