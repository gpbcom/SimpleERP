import type { App, Ref } from "vue";

/** A translation catalogue of one language: keys map to a string or to a nested catalogue. */
export type Catalog = { [key: string]: string | Catalog };

/** Every catalogue of the package, by language code. */
export type Catalogs = Readonly<Record<string, Catalog>>;

/** A key that a language lacks while another language has it. */
export type MissingKey = { language: string; key: string };

/** The values substituted into the placeholders of a translated string. */
export type TranslateParams = Readonly<Record<string, string | number>>;

/** The translator: the active language, the lookup, the language switch and its Vue plugin. */
export interface I18n {
  /** The active language code, reactive. */
  readonly locale: Readonly<Ref<string>>;
  /** Translate a dotted key, substituting the params into its placeholders. */
  t(key: string, params?: TranslateParams): string;
  /** Switch the active language. */
  setLocale(locale: string): void;
  /** Install the translator into a Vue application. */
  install(app: App): void;
}
