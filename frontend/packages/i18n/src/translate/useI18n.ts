import { inject } from "vue";

import type { I18n } from "../types";
import { I18N_KEY } from "./createI18n";

/**
 * Return the translator provided by the i18n plugin.
 *
 * @returns The translator of the application.
 * @throws Error when the plugin is not installed.
 */
export function useI18n(): I18n {
  const instance = inject(I18N_KEY);
  if (!instance) {
    throw new Error("The i18n plugin is not installed. Install it with app.use(createI18n(...)).");
  }
  return instance;
}
