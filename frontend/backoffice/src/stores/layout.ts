import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export type Viewport = 'phone' | 'tablet' | 'desktop'

const PHONE_QUERY = '(max-width: 767px)'
const DESKTOP_QUERY = '(min-width: 1200px)'

export const useLayoutStore = defineStore('layout', () => {
  const viewport = ref<Viewport>('desktop')
  const userCollapsed = ref<boolean | null>(null)

  if (typeof window !== 'undefined' && typeof window.matchMedia === 'function') {
    const phone = window.matchMedia(PHONE_QUERY)
    const desktop = window.matchMedia(DESKTOP_QUERY)
    const update = (): void => {
      viewport.value = phone.matches ? 'phone' : desktop.matches ? 'desktop' : 'tablet'
    }
    update()
    phone.addEventListener('change', update)
    desktop.addEventListener('change', update)
  }

  const sidebarCollapsed = computed<boolean>(() => userCollapsed.value ?? viewport.value === 'tablet')

  function toggleSidebar(): void {
    userCollapsed.value = !sidebarCollapsed.value
  }

  return { viewport, sidebarCollapsed, toggleSidebar }
})
