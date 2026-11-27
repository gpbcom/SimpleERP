<script setup lang="ts">
import { computed } from 'vue';
import type { LucideIcon } from 'lucide-vue-next';

const props = withDefaults(
  defineProps<{
    /** The Lucide icon component to draw. */
    icon: LucideIcon;
    /** The width and height in px: 16, 20 or 24. */
    size?: 16 | 20 | 24;
    /** The accessible name. Without it the icon is decorative and hidden from screen readers. */
    label?: string;
  }>(),
  { size: 20, label: undefined },
);

const a11y = computed(() =>
  props.label ? { role: 'img', 'aria-label': props.label } : { 'aria-hidden': true as const, focusable: 'false' },
);
</script>

<template>
  <component :is="icon" :size="size" :stroke-width="2" color="currentColor" v-bind="a11y" />
</template>
