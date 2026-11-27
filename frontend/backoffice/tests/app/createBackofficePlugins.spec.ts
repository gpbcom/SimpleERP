import { mount } from '@vue/test-utils';
import { describe, expect, it } from 'vitest';
import { defineComponent, h, nextTick } from 'vue';
import { createMemoryHistory } from 'vue-router';

import { useI18n } from '@simpleerp/i18n';

import { createBackofficePlugins } from '../../src/app/createBackofficePlugins';

const Probe = defineComponent({
  setup() {
    const { t, setLocale } = useI18n();
    return () => h('button', { onClick: () => setLocale('en') }, t('shell.skipToContent'));
  },
});

function mountWith(locale: 'fr' | 'en') {
  const { router, pinia, i18n } = createBackofficePlugins({ history: createMemoryHistory(), locale });
  const wrapper = mount(Probe, { global: { plugins: [router, pinia, i18n] } });
  return { wrapper, router };
}

describe('createBackofficePlugins', () => {
  it.each([
    ['fr', 'Aller au contenu'],
    ['en', 'Skip to content'],
  ] as const)('sets the page language and the texts for %s', (locale, text) => {
    const { wrapper } = mountWith(locale);
    expect(document.documentElement.lang).toBe(locale);
    expect(wrapper.text()).toBe(text);
  });

  it('switches the texts and the page language without a reload', async () => {
    const { wrapper } = mountWith('fr');
    await wrapper.trigger('click');
    await nextTick();
    expect(wrapper.text()).toBe('Skip to content');
    expect(document.documentElement.lang).toBe('en');
  });

  it.each([
    ['home', '/'],
    ['tasks', '/tasks'],
  ])('has the route named %s at %s', (name, path) => {
    const { router } = mountWith('en');
    expect(router.resolve({ name }).path).toBe(path);
  });
});
