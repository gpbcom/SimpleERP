import { defineStore } from 'pinia'
import { computed, ref, watch } from 'vue'

export type ThemePreference = 'system' | 'light' | 'dark'
export type ResolvedTheme = 'light' | 'dark'

const STORAGE_KEY = 'simpleerp.theme'
const DARK_QUERY = '(prefers-color-scheme: dark)'

function readStored(): ThemePreference {
  try {
    const value = window.localStorage.getItem(STORAGE_KEY)
    return value === 'light' || value === 'dark' ? value : 'system'
  } catch {
    return 'system'
  }
}

export const useThemeStore = defineStore('theme', () => {
  const preference = ref<ThemePreference>(readStored())
  const media =
    typeof window !== 'undefined' && typeof window.matchMedia === 'function'
      ? window.matchMedia(DARK_QUERY)
      : null
  const deviceDark = ref<boolean>(media?.matches ?? false)

  media?.addEventListener('change', (event: MediaQueryListEvent) => {
    deviceDark.value = event.matches
  })

  const resolved = computed<ResolvedTheme>(() =>
    preference.value === 'system' ? (deviceDark.value ? 'dark' : 'light') : preference.value,
  )

  function setPreference(next: ThemePreference): void {
    preference.value = next
    try {
      if (next === 'system') window.localStorage.removeItem(STORAGE_KEY)
      else window.localStorage.setItem(STORAGE_KEY, next)
    } catch {
      // Storage unavailable: the choice holds for this session only.
    }
  }

  function toggle(): void {
    setPreference(resolved.value === 'dark' ? 'light' : 'dark')
  }

  // The tokens select dark values with [data-theme="dark"], so the attribute is enough.
  watch(
    resolved,
    (theme) => {
      const root = document.documentElement
      root.setAttribute('data-theme', theme)
      root.style.colorScheme = theme
    },
    { immediate: true, flush: 'sync' },
  )

  return { preference, resolved, setPreference, toggle }
})
