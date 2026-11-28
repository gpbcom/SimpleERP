import { mount } from '@vue/test-utils'
import type { VueWrapper } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import type { Pinia } from 'pinia'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { nextTick } from 'vue'

import { createI18n } from '@simpleerp/i18n'
import type { Catalog, I18n } from '@simpleerp/i18n'

import ErrorOutlet from '../../src/errors/ErrorOutlet.vue'
import type { Refusal } from '../../src/errors/Refusal'
import { useErrorStore } from '../../src/stores/errors'

const en: Catalog = {
  errors: {
    common: { cancel: 'Cancel', reference: 'ref.' },
    siteClose: {
      title: 'The site cannot be closed',
      why: 'Site {site} still has open orders.',
      action: 'Review the orders',
    },
  },
}

const fr: Catalog = {
  errors: {
    common: { cancel: 'Annuler', reference: 'réf.' },
    siteClose: {
      title: 'Le site ne peut pas être fermé',
      why: 'Le site {site} a encore des commandes ouvertes.',
      action: 'Revoir les commandes',
    },
  },
}

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

function buttonLabelled(label: string): HTMLButtonElement | undefined {
  return Array.from(document.body.querySelectorAll('button')).find((button) => button.textContent?.trim() === label)
}

describe('ErrorOutlet', () => {
  let pinia: Pinia
  let i18n: I18n
  let wrapper: VueWrapper

  beforeEach(() => {
    pinia = createPinia()
    setActivePinia(pinia)
    i18n = createI18n({ locale: 'en', catalogs: { en, fr } })
    wrapper = mount(ErrorOutlet, { global: { plugins: [pinia, i18n] }, attachTo: document.body })
  })

  afterEach(() => {
    wrapper.unmount()
  })

  it('renders nothing while there is no refusal', () => {
    expect(document.body.querySelector('[role="alertdialog"]')).toBeNull()
    expect(document.body.querySelector('[role="alert"]')).toBeNull()
  })

  it('renders a dialog refusal with its translated title, why and action', async () => {
    useErrorStore().show(aRefusal())
    await nextTick()
    const dialog = document.body.querySelector('[role="alertdialog"]')
    expect(dialog).not.toBeNull()
    expect(dialog?.textContent).toContain('The site cannot be closed')
    expect(dialog?.textContent).toContain('Site Lyon still has open orders.')
    expect(buttonLabelled('Review the orders')).toBeDefined()
  })

  it('renders the Cancel button and the support reference of a dialog refusal', async () => {
    useErrorStore().show(aRefusal())
    await nextTick()
    expect(buttonLabelled('Cancel')).toBeDefined()
    expect(document.body.querySelector('[role="alertdialog"]')?.textContent).toContain('ref. SITE-CLOSE-01')
  })

  it('renders a banner refusal as an alert', async () => {
    useErrorStore().show(aRefusal({ id: 'b1', presentation: 'banner' }))
    await nextTick()
    const banner = document.body.querySelector('[role="alert"]')
    expect(banner).not.toBeNull()
    expect(banner?.textContent).toContain('The site cannot be closed')
    expect(banner?.textContent).toContain('Site Lyon still has open orders.')
    expect(document.body.querySelector('[role="alertdialog"]')).toBeNull()
  })

  it('renders the banner at the top of what the outlet renders', async () => {
    const errors = useErrorStore()
    errors.show(aRefusal())
    errors.show(aRefusal({ id: 'b1', presentation: 'banner' }))
    await nextTick()
    const banner = wrapper.element.querySelector('[role="alert"]')
    expect(banner).not.toBeNull()
    expect(wrapper.element.firstElementChild).toBe(banner)
  })

  it('shows the same message in French when the language switches, without a reload', async () => {
    useErrorStore().show(aRefusal())
    await nextTick()
    expect(document.body.textContent).toContain('The site cannot be closed')
    i18n.setLocale('fr')
    await nextTick()
    const dialog = document.body.querySelector('[role="alertdialog"]')
    expect(dialog?.textContent).toContain('Le site ne peut pas être fermé')
    expect(dialog?.textContent).toContain('Le site Lyon a encore des commandes ouvertes.')
    expect(dialog?.textContent).toContain('réf. SITE-CLOSE-01')
    expect(buttonLabelled('Revoir les commandes')).toBeDefined()
    expect(buttonLabelled('Annuler')).toBeDefined()
    expect(document.body.textContent).not.toContain('The site cannot be closed')
  })

  it('shows a banner in French when the language switches', async () => {
    useErrorStore().show(aRefusal({ id: 'b1', presentation: 'banner' }))
    i18n.setLocale('fr')
    await nextTick()
    expect(document.body.querySelector('[role="alert"]')?.textContent).toContain('Le site ne peut pas être fermé')
  })

  it('runs the action of the refusal and removes it when the action is clicked', async () => {
    const errors = useErrorStore()
    const onAction = vi.fn()
    errors.show(aRefusal(), onAction)
    await nextTick()
    buttonLabelled('Review the orders')?.click()
    await nextTick()
    expect(onAction).toHaveBeenCalledTimes(1)
    expect(errors.dialog).toBeNull()
    expect(document.body.querySelector('[role="alertdialog"]')).toBeNull()
  })

  it('dismisses the refusal without running its action when Cancel is clicked', async () => {
    const errors = useErrorStore()
    const onAction = vi.fn()
    errors.show(aRefusal(), onAction)
    await nextTick()
    buttonLabelled('Cancel')?.click()
    await nextTick()
    expect(onAction).not.toHaveBeenCalled()
    expect(errors.dialog).toBeNull()
    expect(document.body.querySelector('[role="alertdialog"]')).toBeNull()
  })

  it('shows no reference line for a refusal without a reference', async () => {
    useErrorStore().show(aRefusal({ reference: null }))
    await nextTick()
    const dialog = document.body.querySelector('[role="alertdialog"]')
    expect(dialog).not.toBeNull()
    expect(dialog?.textContent).not.toContain('ref.')
  })

  it('shows no reference line on a banner without a reference', async () => {
    useErrorStore().show(aRefusal({ id: 'b1', presentation: 'banner', reference: null }))
    await nextTick()
    expect(document.body.querySelector('[role="alert"]')?.textContent).not.toContain('ref.')
  })

  it('does not render a field refusal', async () => {
    useErrorStore().show(aRefusal({ id: 'f1', field: 'email', presentation: 'field' }))
    await nextTick()
    expect(document.body.querySelector('[role="alertdialog"]')).toBeNull()
    expect(document.body.querySelector('[role="alert"]')).toBeNull()
    expect(document.body.textContent).not.toContain('The site cannot be closed')
  })
})
