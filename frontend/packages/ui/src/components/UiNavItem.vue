<script setup lang="ts">
import type { LucideIcon } from 'lucide-vue-next';

import UiIcon from './UiIcon.vue';

withDefaults(
  defineProps<{
    /** Where the item leads. */
    href: string;
    /** The text of the item, and its accessible name even when collapsed. */
    label: string;
    /** The Lucide icon drawn at 24 px before the label, hidden from screen readers. */
    icon?: LucideIcon;
    /** Whether the item is the current page: sets `aria-current="page"`. */
    current?: boolean;
    /** A count shown after the label, part of the accessible name. */
    badge?: number;
    /** Whether the sidebar is collapsed to icons: the label stays as visually hidden text. */
    collapsed?: boolean;
  }>(),
  { icon: undefined, current: false, badge: undefined, collapsed: false },
);
</script>

<template>
  <a
    class="ui-nav-item"
    :class="{ 'ui-nav-item--current': current, 'ui-nav-item--collapsed': collapsed }"
    :href="href"
    :aria-current="current ? 'page' : undefined"
  >
    <UiIcon
      v-if="icon"
      :icon="icon"
      :size="24"
    />
    <span :class="collapsed ? 'sr-only' : 'ui-nav-item__label'">{{ label }}</span>
    <span
      v-if="badge !== undefined"
      class="ui-nav-item__badge"
    >{{ badge }}</span>
  </a>
</template>

<style scoped>
.ui-nav-item {
  display: flex;
  align-items: center;
  gap: var(--space-12);
  padding: var(--space-8) var(--space-12);
  border-radius: var(--radius-field);
  color: var(--color-text);
  font: var(--font-label);
  text-decoration: none;
  transition: background-color 150ms ease;
}

.ui-nav-item--collapsed {
  justify-content: center;
}

.ui-nav-item:hover {
  background-color: var(--color-surface);
}

.ui-nav-item:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.ui-nav-item--current {
  background-color: var(--color-surface);
  color: var(--color-primary);
}

.ui-nav-item__label {
  flex: 1;
}

.ui-nav-item__badge {
  padding: 0 var(--space-8);
  border-radius: var(--radius-badge);
  background-color: var(--color-primary);
  color: var(--color-surface);
  font: var(--font-caption);
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .ui-nav-item {
    transition: none;
  }
}
</style>
