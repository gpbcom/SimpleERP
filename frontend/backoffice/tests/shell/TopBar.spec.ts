import { describe, expect, it } from 'vitest';

import TopBar from '../../src/shell/TopBar.vue';
import { mountComponent } from '../helpers/mountComponent';

const STORAGE_KEY = 'simpleerp.theme';

const PLACES = [
  { place: 'search', en: 'Search', fr: 'Rechercher' },
  { place: 'assistant', en: 'Assistant', fr: 'Assistant' },
  { place: 'notifications', en: 'Notifications', fr: 'Notifications' },
  { place: 'site', en: 'Switch site', fr: 'Changer de site' },
  { place: 'user', en: 'User menu', fr: 'Menu utilisateur' },
] as const;

const INACTIVE = PLACES.filter((entry) => entry.place !== 'search');

const PLACEHOLDERS = {
  en: 'Search customers, invoices, people...',
  fr: 'Rechercher des clients, des factures, des personnes...',
} as const;

const THEME_LABELS = {
  en: { dark: 'Switch to dark mode', light: 'Switch to light mode' },
  fr: { dark: 'Passer en mode sombre', light: 'Passer en mode clair' },
} as const;

function nameOf(element: Element): string {
  return element.getAttribute('aria-label') ?? element.textContent?.trim() ?? '';
}

describe('TopBar', () => {
  it('is a header marked as the top bar', async () => {
    const { wrapper } = await mountComponent(TopBar, { locale: 'en', dark: false, storedTheme: null });
    expect(wrapper.element.tagName).toBe('HEADER');
    expect(wrapper.attributes('data-shell')).toBe('topbar');
  });

  it.each(['en', 'fr'] as const)('holds the five places in order, named in %s', async (locale) => {
    const { wrapper } = await mountComponent(TopBar, { locale, dark: false, storedTheme: null });
    const found = wrapper.findAll('[data-place]').filter((node) => node.attributes('data-place') !== 'theme');
    expect(found.map((node) => node.attributes('data-place'))).toEqual(PLACES.map((entry) => entry.place));
    for (const entry of PLACES) {
      const node = wrapper.get(`[data-place="${entry.place}"]`);
      expect(nameOf(node.element)).toBe(entry[locale]);
    }
  });

  it.each(['en', 'fr'] as const)('has a search form with a search input in %s', async (locale) => {
    const { wrapper } = await mountComponent(TopBar, { locale, dark: false, storedTheme: null });
    const form = wrapper.get('[data-place="search"]');
    expect(form.element.tagName).toBe('FORM');
    expect(form.attributes('role')).toBe('search');
    const input = form.get('input[type="search"]');
    expect(input.attributes('placeholder')).toBe(PLACEHOLDERS[locale]);
  });

  it.each(INACTIVE.map((entry) => entry.place))('keeps the %s place inactive', async (place) => {
    const { wrapper } = await mountComponent(TopBar, { locale: 'en', dark: false, storedTheme: null });
    const node = wrapper.get(`[data-place="${place}"]`);
    expect(node.element.tagName).toBe('BUTTON');
    expect(node.attributes('aria-disabled')).toBe('true');
  });

  it.each(['en', 'fr'] as const)('offers dark mode on a light device in %s', async (locale) => {
    const { wrapper } = await mountComponent(TopBar, { locale, dark: false, storedTheme: null });
    const node = wrapper.get('[data-place="theme"]');
    expect(node.element.tagName).toBe('BUTTON');
    expect(node.attributes('disabled')).toBeUndefined();
    expect(node.attributes('aria-label')).toBe(THEME_LABELS[locale].dark);
  });

  it.each(['en', 'fr'] as const)('offers light mode on a dark device in %s', async (locale) => {
    const { wrapper } = await mountComponent(TopBar, { locale, dark: true, storedTheme: null });
    expect(wrapper.get('[data-place="theme"]').attributes('aria-label')).toBe(THEME_LABELS[locale].light);
  });

  it('switches to dark, stores the choice and offers light afterwards', async () => {
    const { wrapper } = await mountComponent(TopBar, { locale: 'en', dark: false, storedTheme: null });
    await wrapper.get('[data-place="theme"]').trigger('click');
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark');
    expect(localStorage.getItem(STORAGE_KEY)).toBe('dark');
    expect(wrapper.get('[data-place="theme"]').attributes('aria-label')).toBe(THEME_LABELS.en.light);
  });

  it('ignores the device once the person has chosen a theme', async () => {
    const { wrapper, media } = await mountComponent(TopBar, { locale: 'en', dark: false, storedTheme: null });
    await wrapper.get('[data-place="theme"]').trigger('click');
    media.setDark(false);
    media.setDark(true);
    media.setDark(false);
    await wrapper.vm.$nextTick();
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark');
  });
});
