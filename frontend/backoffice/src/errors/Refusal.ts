export type RefusalPresentation = 'dialog' | 'banner' | 'field'

/**
 * A refusal as the screens show it: message keys and params only, never translated text (D21)
 * and never the raw problem+json body.
 */
export interface Refusal {
  id: string
  code: string | null
  titleKey: string
  whyKey: string
  actionKey: string
  reference: string | null
  params: Readonly<Record<string, string>>
  field: string | null
  presentation: RefusalPresentation
}
