import type { Catalogs } from '../types'

import en from '../catalogues/en/errors.json' with { type: 'json' }
import fr from '../catalogues/fr/errors.json' with { type: 'json' }

export interface ErrorCatalogEntry {
  readonly titleKey: string
  readonly whyKey: string
  readonly actionKey: string
  readonly reference?: string
}

export const ERROR_COMMON_KEYS = ['errors.common.cancel', 'errors.common.reference'] as const

export const errorCatalog: Readonly<Record<string, ErrorCatalogEntry>> = {
  'UNEXPECTED-ERROR-01': {
    titleKey: 'errors.unexpected_error_01.title',
    whyKey: 'errors.unexpected_error_01.why',
    actionKey: 'errors.unexpected_error_01.action',
    reference: 'UNEXPECTED-ERROR-01',
  },
  'SERVICE-FAILURE-01': {
    titleKey: 'errors.service_failure_01.title',
    whyKey: 'errors.service_failure_01.why',
    actionKey: 'errors.service_failure_01.action',
    reference: 'SERVICE-FAILURE-01',
  },
  'INVALID-INPUT-01': {
    titleKey: 'errors.invalid_input_01.title',
    whyKey: 'errors.invalid_input_01.why',
    actionKey: 'errors.invalid_input_01.action',
    reference: 'INVALID-INPUT-01',
  },
  'SITE-CLOSE-01': {
    titleKey: 'errors.site_close_01.title',
    whyKey: 'errors.site_close_01.why',
    actionKey: 'errors.site_close_01.action',
    reference: 'SITE-CLOSE-01',
  },
  'CONTEXT-COMPANY-01': {
    titleKey: 'errors.context.no_company.title',
    whyKey: 'errors.context.no_company.why',
    actionKey: 'errors.context.no_company.action',
    reference: 'CONTEXT-COMPANY-01',
  },
  'CONTEXT-USER-01': {
    titleKey: 'errors.context.no_user.title',
    whyKey: 'errors.context.no_user.why',
    actionKey: 'errors.context.no_user.action',
    reference: 'CONTEXT-USER-01',
  },
  'RIGHTS-DENIED-01': {
    titleKey: 'errors.rights.no_policy.title',
    whyKey: 'errors.rights.no_policy.why',
    actionKey: 'errors.rights.no_policy.action',
    reference: 'RIGHTS-DENIED-01',
  },
  'RIGHTS-DENIED-02': {
    titleKey: 'errors.rights.policy_denied.title',
    whyKey: 'errors.rights.policy_denied.why',
    actionKey: 'errors.rights.policy_denied.action',
    reference: 'RIGHTS-DENIED-02',
  },
  'RIGHTS-COMPANY-01': {
    titleKey: 'errors.rights.other_company.title',
    whyKey: 'errors.rights.other_company.why',
    actionKey: 'errors.rights.other_company.action',
    reference: 'RIGHTS-COMPANY-01',
  },
  'PLATFORM-ROUTE-01': {
    titleKey: 'errors.platform_route_01.title',
    whyKey: 'errors.platform_route_01.why',
    actionKey: 'errors.platform_route_01.action',
    reference: 'PLATFORM-ROUTE-01',
  },
  'PLATFORM-METHOD-01': {
    titleKey: 'errors.platform_method_01.title',
    whyKey: 'errors.platform_method_01.why',
    actionKey: 'errors.platform_method_01.action',
    reference: 'PLATFORM-METHOD-01',
  },
  'PLATFORM-REQUEST-01': {
    titleKey: 'errors.platform_request_01.title',
    whyKey: 'errors.platform_request_01.why',
    actionKey: 'errors.platform_request_01.action',
    reference: 'PLATFORM-REQUEST-01',
  },
  'PLATFORM-INTERNAL-01': {
    titleKey: 'errors.platform_internal_01.title',
    whyKey: 'errors.platform_internal_01.why',
    actionKey: 'errors.platform_internal_01.action',
    reference: 'PLATFORM-INTERNAL-01',
  },
}

const FALLBACK_ENTRY: ErrorCatalogEntry = {
  titleKey: 'errors.fallback.title',
  whyKey: 'errors.fallback.why',
  actionKey: 'errors.fallback.action',
}

export function resolveErrorCode(code: string | null | undefined): ErrorCatalogEntry {
  if (!code || !Object.prototype.hasOwnProperty.call(errorCatalog, code)) {
    return FALLBACK_ENTRY
  }
  return errorCatalog[code] as ErrorCatalogEntry
}

/** The texts of the error catalogue and of its shared labels, by language code. */
export const errorCatalogs: Catalogs = { en, fr }
