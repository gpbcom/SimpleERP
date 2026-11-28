import { useI18n } from '@simpleerp/i18n'

import { useErrorStore } from '../stores/errors'

export interface FieldErrors {
  errorFor(field: string): string | undefined
  focusFirstFaulty(root: HTMLElement): void
  clear(field: string): void
}

/**
 * Bind the field refusals of the error store to the form fields (Error messages pattern, D122).
 *
 * `errorFor` translates the why of a refusal with its params, reading the active language, so the
 * message follows it (D21). The form field's `error` prop does the highlight, the icon and the
 * `aria-invalid` and `aria-describedby` links (D46).
 */
export function useFieldErrors(): FieldErrors {
  const store = useErrorStore()
  const i18n = useI18n()

  function errorFor(field: string): string | undefined {
    const refusal = store.fieldErrors[field]
    if (refusal === undefined) return undefined
    return i18n.t(refusal.whyKey, refusal.params)
  }

  function focusFirstFaulty(root: HTMLElement): void {
    root.querySelector<HTMLElement>('[aria-invalid="true"]')?.focus()
  }

  function clear(field: string): void {
    store.clearField(field)
  }

  return { errorFor, focusFirstFaulty, clear }
}
