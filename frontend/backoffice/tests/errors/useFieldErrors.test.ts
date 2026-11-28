import { mount } from '@vue/test-utils'
import type { VueWrapper } from '@vue/test-utils'
import { createPinia } from 'pinia'
import type { Pinia } from 'pinia'
import { afterEach, describe, expect, it } from 'vitest'
import { defineComponent, h, nextTick } from 'vue'

import { createI18n } from '@simpleerp/i18n'
import type { Catalog, I18n } from '@simpleerp/i18n'
import { UiFormField } from '@simpleerp/ui'

import type { Refusal } from '../../src/errors/Refusal'
import { useFieldErrors } from '../../src/errors/useFieldErrors'
import { useErrorStore } from '../../src/stores/errors'

const WHY_KEY = 'errors.codes.SE_TEST_INVALID.why'

const CATALOGS: Record<string, Catalog> = {
  en: { errors: { codes: { SE_TEST_INVALID: { why: 'The {name} is not valid.' } } } },
  fr: { errors: { codes: { SE_TEST_INVALID: { why: "Le champ {name} n'est pas valide." } } } },
}

type FieldErrors = ReturnType<typeof useFieldErrors>

interface Mounted {
  wrapper: VueWrapper
  pinia: Pinia
  i18n: I18n
  api: FieldErrors
}

function refusal(field: string): Refusal {
  return {
    id: `refusal-${field}`,
    code: 'SE_TEST_INVALID',
    titleKey: 'errors.codes.SE_TEST_INVALID.title',
    whyKey: WHY_KEY,
    actionKey: 'errors.codes.SE_TEST_INVALID.action',
    reference: null,
    params: { name: field },
    field,
    presentation: 'field',
  }
}

function mountForm(fields: string[]): Mounted {
  const pinia = createPinia()
  const i18n = createI18n({ locale: 'en', catalogs: CATALOGS })
  let captured: FieldErrors | undefined
  const Host = defineComponent({
    setup() {
      const api = useFieldErrors()
      captured = api
      return () =>
        h(
          'form',
          fields.map((name) => h(UiFormField, { id: name, label: name, error: api.errorFor(name) })),
        )
    },
  })
  const wrapper = mount(Host, { global: { plugins: [pinia, i18n] }, attachTo: document.body })
  if (!captured) throw new Error('The host component did not set up.')
  return { wrapper: wrapper as VueWrapper, pinia, i18n, api: captured }
}

describe('useFieldErrors', () => {
  let current: VueWrapper | undefined

  function setUp(fields: string[]): Mounted {
    const mounted = mountForm(fields)
    current = mounted.wrapper
    return mounted
  }

  afterEach(() => {
    current?.unmount()
    current = undefined
  })

  it('a field with no refusal shows no error', () => {
    const { wrapper, api } = setUp(['email'])
    expect(api.errorFor('email')).toBeUndefined()
    expect(wrapper.get('input#email').attributes('aria-invalid')).toBeUndefined()
    expect(wrapper.find('.ui-form-field__message').exists()).toBe(false)
  })

  it('a field refusal highlights the field with its message next to it', async () => {
    const { wrapper, pinia } = setUp(['email', 'phone'])
    useErrorStore(pinia).show(refusal('email'))
    await nextTick()

    const input = wrapper.get('input#email')
    expect(input.attributes('aria-invalid')).toBe('true')
    const message = wrapper.get('#email-message')
    expect(message.text()).toBe('The email is not valid.')
    expect(message.find('svg').exists()).toBe(true)
    expect(input.attributes('aria-describedby')).toBe('email-message')
    expect(input.element.closest('.ui-form-field__control')?.className).toContain(
      'ui-form-field__control--error',
    )
  })

  it('only the faulty field is highlighted', async () => {
    const { wrapper, pinia } = setUp(['email', 'phone'])
    useErrorStore(pinia).show(refusal('email'))
    await nextTick()
    expect(wrapper.get('input#phone').attributes('aria-invalid')).toBeUndefined()
    expect(wrapper.find('#phone-message').exists()).toBe(false)
  })

  it('the message is the why text of the code in the current language and follows the language', async () => {
    const { wrapper, pinia, i18n, api } = setUp(['email'])
    useErrorStore(pinia).show(refusal('email'))
    await nextTick()
    expect(api.errorFor('email')).toBe('The email is not valid.')

    i18n.setLocale('fr')
    await nextTick()
    expect(api.errorFor('email')).toBe("Le champ email n'est pas valide.")
    expect(wrapper.get('#email-message').text()).toBe("Le champ email n'est pas valide.")
  })

  it('focusFirstFaulty moves the focus to the first faulty field in document order', async () => {
    const { wrapper, pinia, api } = setUp(['name', 'email', 'phone'])
    const store = useErrorStore(pinia)
    store.show(refusal('phone'))
    store.show(refusal('email'))
    await nextTick()

    api.focusFirstFaulty(wrapper.element as HTMLElement)
    expect(document.activeElement).toBe(wrapper.get('input#email').element)
  })

  it('focusFirstFaulty leaves the focus alone when no field is faulty', () => {
    const { wrapper, api } = setUp(['name'])
    const before = document.activeElement
    api.focusFirstFaulty(wrapper.element as HTMLElement)
    expect(document.activeElement).toBe(before)
  })

  it('clear removes the highlight and the message of that field only', async () => {
    const { wrapper, pinia, api } = setUp(['email', 'phone'])
    const store = useErrorStore(pinia)
    store.show(refusal('email'))
    store.show(refusal('phone'))
    await nextTick()

    api.clear('email')
    await nextTick()

    expect(api.errorFor('email')).toBeUndefined()
    expect(wrapper.get('input#email').attributes('aria-invalid')).toBeUndefined()
    expect(wrapper.find('#email-message').exists()).toBe(false)
    expect(wrapper.get('input#phone').attributes('aria-invalid')).toBe('true')
    expect(store.fieldErrors.email).toBeUndefined()
  })

  it('the message is announced to screen readers as the form field error is', async () => {
    const { wrapper, pinia } = setUp(['email'])
    useErrorStore(pinia).show(refusal('email'))
    await nextTick()

    const input = wrapper.get('input#email')
    const message = document.getElementById(input.attributes('aria-describedby') ?? '')
    expect(message).not.toBeNull()
    expect(message?.textContent).toContain('The email is not valid.')
    expect(message?.closest('[aria-hidden="true"]')).toBeNull()
    expect(input.attributes('aria-invalid')).toBe('true')
  })
})
