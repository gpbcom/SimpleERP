import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

import type { Refusal, RefusalPresentation } from '../errors/Refusal'

export const useErrorStore = defineStore('errors', () => {
  const refusals = ref<Refusal[]>([])
  const actions = new Map<string, () => void>()

  function latest(presentation: RefusalPresentation): Refusal | null {
    for (let i = refusals.value.length - 1; i >= 0; i -= 1) {
      const refusal = refusals.value[i]
      if (refusal !== undefined && refusal.presentation === presentation) return refusal
    }
    return null
  }

  const dialog = computed<Refusal | null>(() => latest('dialog'))
  const banner = computed<Refusal | null>(() => latest('banner'))
  const fieldErrors = computed<Record<string, Refusal>>(() => {
    const byField: Record<string, Refusal> = {}
    for (const refusal of refusals.value) {
      if (refusal.presentation === 'field' && refusal.field !== null) byField[refusal.field] = refusal
    }
    return byField
  })

  function dismiss(id: string): void {
    refusals.value = refusals.value.filter((refusal) => refusal.id !== id)
    actions.delete(id)
  }

  function show(refusal: Refusal, onAction?: () => void): void {
    dismiss(refusal.id)
    refusals.value.push(refusal)
    if (onAction !== undefined) actions.set(refusal.id, onAction)
  }

  function clearField(name: string): void {
    const ids = refusals.value
      .filter((refusal) => refusal.presentation === 'field' && refusal.field === name)
      .map((refusal) => refusal.id)
    ids.forEach(dismiss)
  }

  function act(id: string): void {
    const onAction = actions.get(id)
    onAction?.()
    dismiss(id)
  }

  return { dialog, banner, fieldErrors, show, dismiss, clearField, act }
})
