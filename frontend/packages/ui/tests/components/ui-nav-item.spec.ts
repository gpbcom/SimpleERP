import userEvent from '@testing-library/user-event';
import { describe, expect, it } from 'vitest';
import { defineComponent, h, type Component } from 'vue';

import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations';
import { renderInTheme } from '../helpers/render-in-theme';
import { THEMES, type Theme } from '../helpers/themes';
import UiNavItem from '../../src/components/UiNavItem.vue';

const LABEL = 'Customers';

const TestIcon = defineComponent({
  name: 'TestIcon',
  setup(_props, { attrs }) {
    return () =>
      h('svg', { viewBox: '0 0 24 24', 'data-testid': 'nav-icon', ...attrs }, [h('path', { d: 'M0 0h24v24H0z' })]);
  },
});

const ITEM_PROPS: Record<string, Record<string, unknown>> = {
  default: { href: '/customers', label: LABEL, icon: TestIcon },
  current: { href: '/customers', label: LABEL, icon: TestIcon, current: true },
  'with a badge': { href: '/customers', label: LABEL, icon: TestIcon, badge: 5 },
  collapsed: { href: '/customers', label: LABEL, icon: TestIcon, collapsed: true },
};

function inNav(props: Record<string, unknown>): Component {
  return defineComponent({
    name: 'NavHost',
    setup() {
      return () => h('nav', { 'aria-label': 'Main' }, [h('ul', [h('li', [h(UiNavItem as Component, props)])])]);
    },
  });
}

function show(theme: Theme, props: Record<string, unknown>) {
  return renderInTheme(inNav(props), { theme });
}

describe('UiNavItem', () => {
  describe.each(THEMES)('in the %s theme', (theme) => {
    it.each(Object.keys(ITEM_PROPS))('the %s item has no accessibility violation', async (state) => {
      const { container } = show(theme, ITEM_PROPS[state]);

      await expectNoAxeViolations(container);
    });
  });

  it('renders one link to the href with the label', () => {
    const { getByRole } = show('light', ITEM_PROPS.default);

    const link = getByRole('link', { name: LABEL });

    expect(link.getAttribute('href')).toBe('/customers');
    expect(link.tagName).toBe('A');
  });

  it('marks the current page with aria-current page', () => {
    const { getByRole } = show('light', ITEM_PROPS.current);

    expect(getByRole('link', { name: LABEL }).getAttribute('aria-current')).toBe('page');
  });

  it.each([{ current: false }, {}])('has no aria-current when current is %j', (extra) => {
    const { getByRole } = show('light', { ...ITEM_PROPS.default, ...extra });

    expect(getByRole('link', { name: LABEL }).hasAttribute('aria-current')).toBe(false);
  });

  it('is focused by the keyboard with the tab key', async () => {
    const user = userEvent.setup();
    const { getByRole } = show('light', ITEM_PROPS.default);

    await user.tab();

    expect(document.activeElement).toBe(getByRole('link', { name: LABEL }));
  });

  it('hides the icon from assistive technology', () => {
    const { getByTestId } = show('light', ITEM_PROPS.default);

    expect(getByTestId('nav-icon').getAttribute('aria-hidden')).toBe('true');
  });

  it('keeps the accessible name equal to the label when collapsed', () => {
    const { getByRole } = show('light', ITEM_PROPS.collapsed);

    expect(getByRole('link', { name: LABEL })).toBeTruthy();
  });

  it('does not show the label as visible text when collapsed', () => {
    const { container } = show('light', ITEM_PROPS.collapsed);

    const link = container.querySelector('a') as HTMLAnchorElement;
    const labels = Array.from(link.querySelectorAll('*')).filter(
      (element) => element.children.length === 0 && element.textContent?.trim() === LABEL,
    );

    for (const element of labels) {
      expect(element.className).toMatch(/sr-only|visually-hidden/);
    }
  });

  it('renders the count of the badge', () => {
    const { getByText } = show('light', ITEM_PROPS['with a badge']);

    expect(getByText('5')).toBeTruthy();
  });

  it('includes the count of the badge in the accessible name', () => {
    const { getByRole } = show('light', ITEM_PROPS['with a badge']);

    expect(getByRole('link', { name: new RegExp(`${LABEL}.*5|5.*${LABEL}`) })).toBeTruthy();
  });
});
