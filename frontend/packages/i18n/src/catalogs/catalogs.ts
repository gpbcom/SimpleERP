import type { Catalog, Catalogs } from '../types';

const modules = import.meta.glob<Catalog>('./*.json', { eager: true, import: 'default' });

/**
 * Builds the catalogues by language code, taken from the file name (`fr.json` gives `fr`).
 * @param files The catalogue files, by path.
 * @returns The catalogues by language code.
 */
function build(files: Record<string, Catalog>): Catalogs {
  const result: Record<string, Catalog> = {};
  for (const [path, catalog] of Object.entries(files)) {
    const code = path.replace(/^.*\//, '').replace(/\.json$/, '');
    result[code] = catalog;
  }
  return result;
}

/** Every catalogue of the package, by language code. Adding a `<code>.json` file adds a language. */
export const catalogs: Catalogs = build(modules);

/**
 * Lists the languages the package holds a catalogue for.
 * @returns The language codes, sorted.
 */
export function availableLanguages(): string[] {
  return Object.keys(catalogs).sort();
}
