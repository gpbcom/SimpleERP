import { availableLanguages } from '@simpleerp/i18n'

export type BackofficeLocale = 'fr' | 'en'

/** Pick the first browser language whose primary subtag is French or English, else the i18n package's default. */
export function resolveInitialLocale(languages: readonly string[]): BackofficeLocale {
  for (const language of languages) {
    const primary = language.split('-')[0]?.toLowerCase()
    if (primary === 'fr' || primary === 'en') {
      return primary
    }
  }
  return availableLanguages()[0] as BackofficeLocale
}
