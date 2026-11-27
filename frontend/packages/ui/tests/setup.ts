import '@testing-library/jest-dom/vitest'
import '@simpleerp/tokens/tokens.css'
import { cleanup } from '@testing-library/vue'
import { afterEach } from 'vitest'

if (typeof window.matchMedia !== 'function') {
  window.matchMedia = (query: string): MediaQueryList => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: () => undefined,
    removeListener: () => undefined,
    addEventListener: () => undefined,
    removeEventListener: () => undefined,
    dispatchEvent: () => false,
  })
}

afterEach(() => {
  cleanup()
  document.documentElement.removeAttribute('data-theme')
})
