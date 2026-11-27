<script setup lang="ts">
import { computed } from 'vue';
import type { LucideIcon } from 'lucide-vue-next';

import UiIcon from './UiIcon.vue';
import UiSpinner from './UiSpinner.vue';

const props = withDefaults(
  defineProps<{
    /** The look of the button: the main action, another action, a destructive one or a minor one. */
    variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
    /** The text of the button, and the accessible name when only the icon shows. */
    label: string;
    /** The Lucide icon component drawn before the label. */
    icon?: LucideIcon;
    /** Shows only the icon, and gives the label as `aria-label`. */
    iconOnly?: boolean;
    /** The native type of the button. */
    type?: 'button' | 'submit' | 'reset';
    /** Renders a link to this address instead of a button. */
    href?: string;
    /** Replaces the icon with a spinner and swallows clicks, keeping the button in the tab order. */
    loading?: boolean;
    /** Disables the button. */
    disabled?: boolean;
    /** Says why the button is disabled, as its tooltip. */
    disabledReason?: string;
    /** Takes the full width on phones. */
    block?: boolean;
  }>(),
  {
    variant: 'primary',
    icon: undefined,
    iconOnly: false,
    type: 'button',
    href: undefined,
    loading: false,
    disabled: false,
    disabledReason: undefined,
    block: false,
  },
);

const emit = defineEmits<{ click: [event: MouseEvent] }>();

const isLink = computed(() => props.href !== undefined);
const inert = computed(() => props.loading || props.disabled);

const attributes = computed(() => ({
  ...(isLink.value ? { href: props.disabled ? undefined : props.href } : { type: props.type, disabled: props.disabled }),
  ...(props.iconOnly ? { 'aria-label': props.label } : {}),
  ...(props.disabled && props.disabledReason ? { title: props.disabledReason } : {}),
  ...(props.loading ? { 'aria-busy': 'true' } : {}),
  ...(props.loading || (isLink.value && props.disabled) ? { 'aria-disabled': 'true' } : {}),
}));

/**
 * Passes a click on, unless the button is loading or disabled.
 *
 * @param event - The native click.
 */
function onClick(event: MouseEvent): void {
  if (inert.value) {
    event.preventDefault();
    return;
  }
  emit('click', event);
}
</script>

<template>
  <component
    :is="isLink ? 'a' : 'button'"
    class="ui-button"
    :class="[`ui-button--${variant}`, { 'ui-button--block': block, 'ui-button--icon-only': iconOnly }]"
    v-bind="attributes"
    @click="onClick"
  >
    <UiSpinner
      v-if="loading"
      :size="20"
    />
    <UiIcon
      v-else-if="icon"
      :icon="icon"
      :size="20"
    />
    <span
      v-if="!iconOnly"
      class="ui-button__label"
    >{{ label }}</span>
  </component>
</template>

<style scoped>
.ui-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-8);
  box-sizing: border-box;
  height: var(--field-height);
  padding: 0 var(--space-16);
  border: 1px solid transparent;
  border-radius: var(--radius-field);
  font: var(--font-label);
  text-decoration: none;
  cursor: pointer;
  transition:
    background-color 150ms,
    border-color 150ms,
    color 150ms;
}

.ui-button--icon-only {
  width: var(--field-height);
  padding: 0;
}

.ui-button--primary {
  background: var(--color-primary);
  color: var(--color-surface);
}

.ui-button--secondary {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border-strong);
}

.ui-button--danger {
  background: var(--color-surface);
  color: var(--color-error);
  border: 1px solid var(--color-error);
}

.ui-button--ghost {
  background: transparent;
  color: var(--color-primary);
}

.ui-button--primary:hover,
.ui-button--primary:active {
  background: color-mix(in srgb, var(--color-primary), var(--color-text) 8%);
}

.ui-button--secondary:hover,
.ui-button--secondary:active {
  border-color: color-mix(in srgb, var(--color-border-strong), var(--color-text) 8%);
}

.ui-button--danger:hover,
.ui-button--danger:active {
  border-color: color-mix(in srgb, var(--color-error), var(--color-text) 8%);
  color: color-mix(in srgb, var(--color-error), var(--color-text) 8%);
}

.ui-button--ghost:hover,
.ui-button--ghost:active {
  color: color-mix(in srgb, var(--color-primary), var(--color-text) 8%);
}

.ui-button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.ui-button:disabled,
.ui-button[aria-disabled='true']:not([aria-busy='true']) {
  background: var(--color-surface-alt);
  border-color: transparent;
  color: var(--color-text-muted);
  cursor: not-allowed;
}

.ui-button[aria-busy='true'] {
  cursor: progress;
}

@media (max-width: 767px) {
  .ui-button--block {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ui-button {
    transition: none;
  }
}
</style>
