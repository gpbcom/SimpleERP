import { readonly, ref, type App, type InjectionKey } from "vue";

import type { Catalog, Catalogs, I18n, TranslateParams } from "../types";

/** The injection key under which the Vue plugin provides the translator. */
export const I18N_KEY: InjectionKey<I18n> = Symbol("i18n");

/** Pick the catalogue of the language subtag of a BCP 47 tag, or throw when there is none. */
function pickCatalog(catalogs: Catalogs, locale: string): Catalog {
  const language = locale.split("-")[0]?.toLowerCase() ?? "";
  const found = Object.entries(catalogs).find(([code]) => code.toLowerCase() === language);
  if (!found) {
    throw new RangeError(`No catalogue matches the locale "${locale}".`);
  }
  return found[1];
}

/** Resolve a dotted key in a catalogue, or return undefined when it does not lead to a string. */
function resolveKey(catalog: Catalog, key: string): string | undefined {
  let node: string | Catalog | undefined = catalog;
  for (const part of key.split(".")) {
    if (node === undefined || typeof node === "string" || !Object.hasOwn(node, part)) {
      return undefined;
    }
    node = node[part];
  }
  return typeof node === "string" ? node : undefined;
}

/**
 * Create a translator whose active language is reactive.
 *
 * @param options - The starting locale (a BCP 47 tag) and the catalogues by language code.
 * @returns The translator, also usable as a Vue plugin.
 * @throws RangeError when no catalogue matches the starting locale.
 */
export function createI18n(options: { locale: string; catalogs: Catalogs }): I18n {
  const { catalogs } = options;
  pickCatalog(catalogs, options.locale);
  const locale = ref(options.locale);

  const instance: I18n = {
    locale: readonly(locale),
    t(key: string, params?: TranslateParams): string {
      const text = resolveKey(pickCatalog(catalogs, locale.value), key);
      if (text === undefined) {
        return key;
      }
      return text.replace(/\{(\w+)\}/g, (placeholder, name: string) =>
        params && Object.hasOwn(params, name) ? String(params[name]) : placeholder,
      );
    },
    setLocale(next: string): void {
      pickCatalog(catalogs, next);
      locale.value = next;
    },
    install(app: App): void {
      app.provide(I18N_KEY, instance);
    },
  };
  return instance;
}
