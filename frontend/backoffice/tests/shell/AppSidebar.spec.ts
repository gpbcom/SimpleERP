import type { VueWrapper } from '@vue/test-utils';
import { describe, expect, it } from 'vitest';

import AppSidebar from '../../src/shell/AppSidebar.vue';
import { mountComponent } from '../helpers/mountComponent';

type Locale = 'en' | 'fr';

const ITEMS = ['home', 'tasks', 'assistant'] as const;

const LABELS: Record<Locale, Record<(typeof ITEMS)[number], string>> = {
  en: { home: 'Home', tasks: 'Tasks', assistant: 'Assistant' },
  fr: { home: 'Accueil', tasks: 'Tâches', assistant: 'Assistant' },
};

const NAV_LABELS: Record<Locale, string> = { en: 'Main navigation', fr: 'Navigation principale' };

const TOGGLE_LABELS: Record<Locale, { collapse: string; expand: string }> = {
  en: { collapse: 'Collapse the menu', expand: 'Expand the menu' },
  fr: { collapse: 'Réduire le menu', expand: 'Déplier le menu' },
};

const LOCALES: Locale[] = ['en', 'fr'];

function item(wrapper: VueWrapper, name: string) {
  return wrapper.get(`[data-nav-item="${name}"]`);
}

function toggle(wrapper: VueWrapper) {
  return wrapper.get('[data-shell="sidebar-toggle"]');
}

describe('AppSidebar', () => {
  it('is an aside that starts expanded on a desktop', async () => {
    const { wrapper } = await mountComponent(AppSidebar);
    const root = wrapper.get('aside[data-shell="sidebar"]');
    expect(root.attributes('data-collapsed')).toBe('false');
  });

  it.each(LOCALES)('holds a navigation landmark with a name in %s', async (locale) => {
    const { wrapper } = await mountComponent(AppSidebar, { locale });
    expect(wrapper.get('nav').attributes('aria-label')).toBe(NAV_LABELS[locale]);
  });

  it('shows the symbol as an image of symbol.svg', async () => {
    const { wrapper } = await mountComponent(AppSidebar);
    const symbol = wrapper.get('img[data-shell="symbol"]');
    expect(symbol.attributes('src')).toMatch(/symbol\.svg$/);
  });

  it('shows the wordmark when expanded', async () => {
    const { wrapper } = await mountComponent(AppSidebar);
    expect(wrapper.text()).toContain('SimpleERP');
  });

  it('makes home and tasks links and the assistant a disabled button', async () => {
    const { wrapper } = await mountComponent(AppSidebar);
    const home = item(wrapper, 'home');
    const tasks = item(wrapper, 'tasks');
    const assistant = item(wrapper, 'assistant');
    expect(home.element.tagName).toBe('A');
    expect(home.attributes('href')).toBe('/');
    expect(tasks.element.tagName).toBe('A');
    expect(tasks.attributes('href')).toBe('/tasks');
    expect(assistant.element.tagName).toBe('BUTTON');
    expect(assistant.attributes('aria-disabled')).toBe('true');
  });

  it.each(ITEMS)('gives the %s item an icon', async (name) => {
    const { wrapper } = await mountComponent(AppSidebar);
    expect(item(wrapper, name).find('svg').exists()).toBe(true);
  });

  it.each(LOCALES)('shows the label of each item in %s when expanded', async (locale) => {
    const { wrapper } = await mountComponent(AppSidebar, { locale });
    for (const name of ITEMS) {
      expect(item(wrapper, name).text()).toContain(LABELS[locale][name]);
    }
  });

  it.each(LOCALES)('names the toggle in %s and ties it to an existing id', async (locale) => {
    const { wrapper } = await mountComponent(AppSidebar, { locale });
    const button = toggle(wrapper);
    expect(button.element.tagName).toBe('BUTTON');
    expect(button.attributes('aria-label')).toBe(TOGGLE_LABELS[locale].collapse);
    expect(button.attributes('aria-expanded')).toBe('true');
    const controls = button.attributes('aria-controls');
    expect(controls).toBeTruthy();
    expect(document.getElementById(controls as string)).not.toBeNull();
  });

  it.each(LOCALES)('collapses to icons only when the toggle is pressed in %s', async (locale) => {
    const { wrapper } = await mountComponent(AppSidebar, { locale });
    await toggle(wrapper).trigger('click');
    expect(wrapper.get('aside[data-shell="sidebar"]').attributes('data-collapsed')).toBe('true');
    expect(toggle(wrapper).attributes('aria-expanded')).toBe('false');
    expect(toggle(wrapper).attributes('aria-label')).toBe(TOGGLE_LABELS[locale].expand);
    expect(wrapper.text()).not.toContain('SimpleERP');
    for (const name of ITEMS) {
      const entry = item(wrapper, name);
      expect(entry.text()).toBe('');
      expect(entry.attributes('aria-label')).toBe(LABELS[locale][name]);
      expect(entry.find('svg').exists()).toBe(true);
    }
  });

  it('restores the labels when the toggle is pressed again', async () => {
    const { wrapper } = await mountComponent(AppSidebar);
    await toggle(wrapper).trigger('click');
    await toggle(wrapper).trigger('click');
    expect(wrapper.get('aside[data-shell="sidebar"]').attributes('data-collapsed')).toBe('false');
    expect(toggle(wrapper).attributes('aria-expanded')).toBe('true');
    expect(item(wrapper, 'home').text()).toContain('Home');
    expect(wrapper.text()).toContain('SimpleERP');
  });

  it('starts collapsed on a tablet', async () => {
    const { wrapper } = await mountComponent(AppSidebar, { widthPx: 1000 });
    expect(wrapper.get('aside[data-shell="sidebar"]').attributes('data-collapsed')).toBe('true');
    expect(item(wrapper, 'home').text()).toBe('');
  });

  it('marks the home link as the current page at the root', async () => {
    const { wrapper } = await mountComponent(AppSidebar, { path: '/' });
    expect(item(wrapper, 'home').attributes('aria-current')).toBe('page');
    expect(item(wrapper, 'tasks').attributes('aria-current')).toBeUndefined();
  });

  it('moves the current page mark to tasks when the route changes', async () => {
    const { wrapper, router } = await mountComponent(AppSidebar, { path: '/' });
    await router.push('/tasks');
    await wrapper.vm.$nextTick();
    expect(item(wrapper, 'tasks').attributes('aria-current')).toBe('page');
    expect(item(wrapper, 'home').attributes('aria-current')).toBeUndefined();
  });

  it('keeps every item and the toggle reachable by keyboard', async () => {
    const { wrapper } = await mountComponent(AppSidebar);
    for (const name of ['home', 'tasks']) {
      const link = item(wrapper, name);
      expect(link.element.tagName).toBe('A');
      expect(link.attributes('href')).toBeTruthy();
      expect(link.attributes('tabindex')).not.toBe('-1');
    }
    for (const button of [item(wrapper, 'assistant'), toggle(wrapper)]) {
      expect(button.element.tagName).toBe('BUTTON');
      expect(button.attributes('tabindex')).not.toBe('-1');
    }
  });
});
