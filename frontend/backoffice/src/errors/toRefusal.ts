import { ApiProblemError } from '@simpleerp/api-client'
import { resolveErrorCode } from '@simpleerp/i18n'

import type { Refusal, RefusalPresentation } from './Refusal'

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null
}

function stringParams(values: unknown): Record<string, string> {
  const params: Record<string, string> = {}
  if (!isRecord(values)) {
    return params
  }
  for (const [name, value] of Object.entries(values)) {
    if (typeof value === 'string' || typeof value === 'number' || typeof value === 'boolean') {
      params[name] = String(value)
    }
  }
  return params
}

/**
 * Maps whatever a call threw to a refusal of message keys and params (D122, REQ-T05-03).
 * Never copies the raw body, the detail text or a stack trace.
 */
export function toRefusal(error: unknown, presentation: 'dialog' | 'banner'): Refusal {
  const id = crypto.randomUUID()
  if (!(error instanceof ApiProblemError)) {
    const fallback = resolveErrorCode(null)
    return {
      id,
      code: null,
      titleKey: fallback.titleKey,
      whyKey: fallback.whyKey,
      actionKey: fallback.actionKey,
      reference: null,
      params: {},
      field: null,
      presentation,
    }
  }
  const entry = resolveErrorCode(error.code)
  const extra: Record<string, unknown> = { ...(error as unknown as Record<string, unknown>) }
  const field = typeof extra.field === 'string' && extra.field !== '' ? extra.field : null
  const shown: RefusalPresentation = field === null ? presentation : 'field'
  return {
    id,
    code: error.code,
    titleKey: entry.titleKey,
    whyKey: entry.whyKey,
    actionKey: entry.actionKey,
    reference: entry.reference ?? error.code,
    params: stringParams(extra.values),
    field,
    presentation: shown,
  }
}
