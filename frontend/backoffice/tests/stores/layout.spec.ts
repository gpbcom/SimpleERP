import { createPinia, setActivePinia } from 'pinia'
import { afterEach, beforeEach, describe, expect, it } from 'vitest'

import { useLayoutStore } from '../../src/stores/layout'
import { installMatchMedia, type MediaController } from '../helpers/media'

describe('useLayoutStore', () => {
  let media: MediaController

  beforeEach(() => {
    window.localStorage.clear()
    media = installMatchMedia({ widthPx: 1600, dark: false })
    setActivePinia(createPinia())
  })

  afterEach(() => {
    media.uninstall()
  })

  it.each([
    [375, 'phone'],
    [767, 'phone'],
    [768, 'tablet'],
    [1199, 'tablet'],
    [1200, 'desktop'],
    [1600, 'desktop'],
  ])('a width of %i px gives the %s viewport', (widthPx, expected) => {
    media.setWidth(widthPx)
    const layout = useLayoutStore()
    expect(layout.viewport).toBe(expected)
  })

  it('updates the viewport live when the width changes', () => {
    media.setWidth(1600)
    const layout = useLayoutStore()
    expect(layout.viewport).toBe('desktop')
    media.setWidth(900)
    expect(layout.viewport).toBe('tablet')
    media.setWidth(400)
    expect(layout.viewport).toBe('phone')
    media.setWidth(1300)
    expect(layout.viewport).toBe('desktop')
  })

  it('starts with the sidebar expanded on desktop', () => {
    media.setWidth(1400)
    const layout = useLayoutStore()
    expect(layout.sidebarCollapsed).toBe(false)
  })

  it('starts with the sidebar collapsed on tablet', () => {
    media.setWidth(900)
    const layout = useLayoutStore()
    expect(layout.sidebarCollapsed).toBe(true)
  })

  it('collapses then expands the sidebar when toggled', () => {
    media.setWidth(1400)
    const layout = useLayoutStore()
    layout.toggleSidebar()
    expect(layout.sidebarCollapsed).toBe(true)
    layout.toggleSidebar()
    expect(layout.sidebarCollapsed).toBe(false)
  })

  it('keeps a toggled choice across a change between tablet and desktop', () => {
    media.setWidth(1400)
    const layout = useLayoutStore()
    layout.toggleSidebar()
    expect(layout.sidebarCollapsed).toBe(true)
    media.setWidth(900)
    expect(layout.sidebarCollapsed).toBe(true)
    media.setWidth(1400)
    expect(layout.sidebarCollapsed).toBe(true)
  })

  it('follows the viewport default until the sidebar is toggled', () => {
    media.setWidth(1400)
    const layout = useLayoutStore()
    media.setWidth(900)
    expect(layout.sidebarCollapsed).toBe(true)
    media.setWidth(1400)
    expect(layout.sidebarCollapsed).toBe(false)
  })

  it('persists nothing in localStorage', () => {
    media.setWidth(1400)
    const layout = useLayoutStore()
    layout.toggleSidebar()
    media.setWidth(900)
    expect(window.localStorage.length).toBe(0)
  })
})
