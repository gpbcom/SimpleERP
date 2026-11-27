import { describe, expect, it, vi } from 'vitest'

import BottomTabBar from '../../src/shell/BottomTabBar.vue'
import { mountComponent } from '../helpers/mountComponent'

const TABS: Array<{ locale: 'en' | 'fr'; name: string; labels: string[] }> = [
  { locale: 'en', name: 'Main navigation', labels: ['Home', 'Tasks', 'Assistant', 'Me'] },
  { locale: 'fr', name: 'Navigation principale', labels: ['Accueil', 'Tâches', 'Assistant', 'Moi'] },
]
const KEYS = ['home', 'tasks', 'assistant', 'me']

describe('BottomTabBar', () => {
  it.each(TABS)('shows the four tabs in order with icon and label in $locale', async ({ locale, name, labels }) => {
    const { wrapper } = await mountComponent(BottomTabBar, { widthPx: 375, locale, path: '/' })
    const nav = wrapper.get('nav[data-shell="tabbar"]')
    expect(nav.attributes('aria-label')).toBe(name)
    const items = nav.findAll('[data-nav-item]')
    expect(items.map((item) => item.attributes('data-nav-item'))).toEqual(KEYS)
    items.forEach((item, index) => {
      expect(item.find('svg').exists()).toBe(true)
      expect(item.text()).toContain(labels[index])
    })
  })

  it('marks home as the current page at the root and tasks after navigating', async () => {
    const { wrapper, router } = await mountComponent(BottomTabBar, { widthPx: 375, locale: 'en', path: '/' })
    expect(wrapper.get('[data-nav-item="home"]').attributes('aria-current')).toBe('page')
    expect(wrapper.get('[data-nav-item="tasks"]').attributes('aria-current')).toBeUndefined()
    await router.push('/tasks')
    await wrapper.vm.$nextTick()
    expect(wrapper.get('[data-nav-item="tasks"]').attributes('aria-current')).toBe('page')
    expect(wrapper.get('[data-nav-item="home"]').attributes('aria-current')).toBeUndefined()
  })

  it('links home and tasks to their routes', async () => {
    const { wrapper } = await mountComponent(BottomTabBar, { widthPx: 375, locale: 'en', path: '/' })
    expect(wrapper.get('a[data-nav-item="home"]').attributes('href')).toBe('/')
    expect(wrapper.get('a[data-nav-item="tasks"]').attributes('href')).toBe('/tasks')
  })

  it('navigates to the tasks route when its link is clicked', async () => {
    const { wrapper, router } = await mountComponent(BottomTabBar, { widthPx: 375, locale: 'en', path: '/' })
    await wrapper.get('a[data-nav-item="tasks"]').trigger('click')
    await vi.waitFor(() => expect(router.currentRoute.value.name).toBe('tasks'))
  })

  it.each(['assistant', 'me'])('keeps the %s tab as a disabled button', async (key) => {
    const { wrapper } = await mountComponent(BottomTabBar, { widthPx: 375, locale: 'en', path: '/' })
    const tab = wrapper.get(`button[data-nav-item="${key}"]`)
    expect(tab.attributes('aria-disabled')).toBe('true')
  })
})
