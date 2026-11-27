import { House } from 'lucide-vue-next';
import { describe, expect, it } from 'vitest';

import UiIcon from '../../src/components/UiIcon.vue';
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations';
import { renderInTheme } from '../helpers/render-in-theme';
import { THEMES } from '../helpers/themes';

describe('UiIcon', () => {
  describe.each(THEMES)('in the %s theme', (theme) => {
    it('renders an inline svg, never an img or a use href', async () => {
      const { container } = await renderInTheme(UiIcon, { theme, props: { icon: House } });

      expect(container.querySelector('svg')).not.toBeNull();
      expect(container.querySelector('img')).toBeNull();
      expect(container.querySelector('use')).toBeNull();
    });

    it('is 20 px wide and high by default, with a stroke width of 2', async () => {
      const { container } = await renderInTheme(UiIcon, { theme, props: { icon: House } });
      const svg = container.querySelector('svg');

      expect(svg?.getAttribute('width')).toBe('20');
      expect(svg?.getAttribute('height')).toBe('20');
      expect(svg?.getAttribute('stroke-width')).toBe('2');
    });

    it.each([16, 20, 24])('is %i px wide and high when asked', async (size) => {
      const { container } = await renderInTheme(UiIcon, { theme, props: { icon: House, size } });
      const svg = container.querySelector('svg');

      expect(svg?.getAttribute('width')).toBe(String(size));
      expect(svg?.getAttribute('height')).toBe(String(size));
      expect(svg?.getAttribute('stroke-width')).toBe('2');
    });

    it('is hidden from screen readers without a label', async () => {
      const { container } = await renderInTheme(UiIcon, { theme, props: { icon: House } });
      const svg = container.querySelector('svg');

      expect(svg?.getAttribute('aria-hidden')).toBe('true');
      expect(svg?.getAttribute('role')).toBeNull();
    });

    it('is an image named by its label when it has one', async () => {
      const { container } = await renderInTheme(UiIcon, { theme, props: { icon: House, label: 'Home' } });
      const svg = container.querySelector('svg');

      expect(svg?.getAttribute('role')).toBe('img');
      expect(svg?.getAttribute('aria-label')).toBe('Home');
      expect(svg?.getAttribute('aria-hidden')).not.toBe('true');
    });

    it('has no axe violation without a label', async () => {
      const { container } = await renderInTheme(UiIcon, { theme, props: { icon: House } });

      await expectNoAxeViolations(container);
    });

    it('has no axe violation with a label', async () => {
      const { container } = await renderInTheme(UiIcon, { theme, props: { icon: House, label: 'Home' } });

      await expectNoAxeViolations(container);
    });
  });
});
