<script setup lang="ts">
import { LoaderCircle } from 'lucide-vue-next';

import UiIcon from './UiIcon.vue';

withDefaults(
  defineProps<{
    /** The width and height in px: 16, 20 or 24. */
    size?: 16 | 20 | 24;
    /** The accessible name. Without it the spinner is hidden from screen readers. */
    label?: string;
  }>(),
  { size: 20, label: undefined },
);
</script>

<template>
  <UiIcon class="ui-spinner" :icon="LoaderCircle" :size="size" :label="label" />
</template>

<style scoped>
.ui-spinner {
  animation: ui-spinner-turn 1s linear infinite;
}

@keyframes ui-spinner-turn {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ui-spinner {
    animation: none;
  }
}
</style>
