import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

import UiSpinner from '../../src/components/UiSpinner.vue';
import { expectNoAxeViolations } from '../helpers/expect-no-axe-violations';
import { renderInTheme } from '../helpers/render-in-theme';
import { THEMES } from '../helpers/themes';

const SOURCE = readFileSync(resolve(dirname(import.meta.filename), '../../src/components/UiSpinner.vue'), 'utf-8');

describe('UiSpinner', () => {
  it('renders the Lucide LoaderCircle svg', async () => {
    const { container } = await renderInTheme(UiSpinner, { theme: THEMES[0], props: {} });
    const svg = container.querySelector('svg');

    expect(svg).not.toBeNull();
    expect(svg?.getAttribute('class')).toContain('lucide-loader-circle');
  });

  it('is hidden from screen readers without a label', async () => {
    const { container } = await renderInTheme(UiSpinner, { theme: THEMES[0], props: {} });

    expect(container.querySelector('svg')?.getAttribute('aria-hidden')).toBe('true');
  });

  it('is named by its label when it has one', async () => {
    const { container } = await renderInTheme(UiSpinner, { theme: THEMES[0], props: { label: 'Loading' } });
    const svg = container.querySelector('svg');

    expect(svg?.getAttribute('role')).toBe('img');
    expect(svg?.getAttribute('aria-label')).toBe('Loading');
  });

  it('turns with an animation', () => {
    expect(SOURCE).toMatch(/animation\s*:/);
    expect(SOURCE).toMatch(/@keyframes/);
  });

  it('removes its animation when the person prefers reduced motion', () => {
    const block = /@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{[^]*?animation\s*:\s*none/;

    expect(SOURCE).toMatch(block);
  });

  describe.each(THEMES)('in the %s theme', (theme) => {
    it('has no axe violation without a label', async () => {
      const { container } = await renderInTheme(UiSpinner, { theme, props: {} });

      await expectNoAxeViolations(container);
    });

    it('has no axe violation with a label', async () => {
      const { container } = await renderInTheme(UiSpinner, { theme, props: { label: 'Loading' } });

      await expectNoAxeViolations(container);
    });
  });
});
