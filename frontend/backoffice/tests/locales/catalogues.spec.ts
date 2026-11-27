import { describe, expect, it } from 'vitest';

import { findMissingKeys } from '@simpleerp/i18n';
import type { Catalog } from '@simpleerp/i18n';

import en from '../../src/locales/en.json';
import fr from '../../src/locales/fr.json';

function flatten(catalog: Catalog, prefix = ''): Record<string, string> {
  const leaves: Record<string, string> = {};
  for (const [name, value] of Object.entries(catalog)) {
    const path = prefix === '' ? name : `${prefix}.${name}`;
    if (typeof value === 'string') {
      leaves[path] = value;
    } else {
      Object.assign(leaves, flatten(value, path));
    }
  }
  return leaves;
}

const expected: ReadonlyArray<readonly [string, string, string]> = [
  ['app.name', 'SimpleERP', 'SimpleERP'],
  ['shell.skipToContent', 'Skip to content', 'Aller au contenu'],
  ['shell.navigation', 'Main navigation', 'Navigation principale'],
  ['shell.collapseSidebar', 'Collapse the menu', 'Réduire le menu'],
  ['shell.expandSidebar', 'Expand the menu', 'Déplier le menu'],
  ['shell.search', 'Search', 'Rechercher'],
  [
    'shell.searchPlaceholder',
    'Search customers, invoices, people...',
    'Rechercher des clients, des factures, des personnes...',
  ],
  ['shell.assistant', 'Assistant', 'Assistant'],
  ['shell.notifications', 'Notifications', 'Notifications'],
  ['shell.siteSwitcher', 'Switch site', 'Changer de site'],
  ['shell.userMenu', 'User menu', 'Menu utilisateur'],
  ['shell.switchToDark', 'Switch to dark mode', 'Passer en mode sombre'],
  ['shell.switchToLight', 'Switch to light mode', 'Passer en mode clair'],
  ['nav.home', 'Home', 'Accueil'],
  ['nav.tasks', 'Tasks', 'Tâches'],
  ['nav.assistant', 'Assistant', 'Assistant'],
  ['nav.me', 'Me', 'Moi'],
  ['page.empty', 'Nothing here yet.', 'Rien ici pour le moment.'],
];

describe('shell catalogues', () => {
  const english = flatten(en as Catalog);
  const french = flatten(fr as Catalog);

  it('hold exactly the same keys in both languages', () => {
    expect(Object.keys(french).sort()).toEqual(Object.keys(english).sort());
  });

  it.each([
    ['English', english],
    ['French', french],
  ])('hold no empty value in %s', (_name, leaves) => {
    for (const [key, value] of Object.entries(leaves)) {
      expect(value.trim(), key).not.toBe('');
    }
  });

  it.each(expected)('hold %s with its English and French text', (key, englishText, frenchText) => {
    expect(english[key]).toBe(englishText);
    expect(french[key]).toBe(frenchText);
  });

  it('pass the missing-key check of the i18n package', () => {
    expect(findMissingKeys({ en: en as Catalog, fr: fr as Catalog })).toEqual([]);
  });
});
