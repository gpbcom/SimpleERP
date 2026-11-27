import { render, type RenderResult } from '@testing-library/vue'
import type { Component } from 'vue'

import type { Theme } from './themes'

export interface RenderInThemeOptions {
  theme: Theme
  props?: Record<string, unknown>
  slots?: Record<string, unknown>
  attrs?: Record<string, unknown>
}

/**
 * Render a component after setting the theme the tokens package selects with the `data-theme` attribute of the
 * root element.
 */
export function renderInTheme(component: Component, options: RenderInThemeOptions): RenderResult {
  document.documentElement.setAttribute('data-theme', options.theme)
  return render(component, { props: options.props, slots: options.slots, attrs: options.attrs })
}

/**
 * Read the theme back from the `data-theme` attribute of the root element.
 */
export function currentTheme(): Theme {
  return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light'
}
