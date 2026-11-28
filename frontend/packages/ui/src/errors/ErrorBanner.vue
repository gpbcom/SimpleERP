<script setup lang="ts">
import { CircleAlert, X } from 'lucide-vue-next';

import UiButton from '../components/UiButton.vue';
import UiIcon from '../components/UiIcon.vue';

withDefaults(
  defineProps<{
    /** What went wrong, in one sentence. */
    title: string;
    /** Why it happened and what happens next. */
    why: string;
    /** The label of the optional action, such as Try again. */
    actionLabel?: string;
    /** The error reference, shown small in the code font. */
    reference?: string;
    /** The word placed before the reference, such as ref. */
    referenceLabel: string;
    /** The accessible name of the dismiss button. Without it the banner has no dismiss button. */
    dismissLabel?: string;
  }>(),
  { actionLabel: undefined, reference: undefined, dismissLabel: undefined },
);

const emit = defineEmits<{
  action: [];
  dismiss: [];
}>();
</script>

<template>
  <div class="error-banner" role="alert">
    <UiIcon class="error-banner__icon" :icon="CircleAlert" :size="20" />
    <div class="error-banner__body">
      <p class="error-banner__title">{{ title }}</p>
      <p class="error-banner__why">{{ why }}</p>
      <p v-if="reference !== undefined" class="error-banner__reference">{{ referenceLabel }} {{ reference }}</p>
    </div>
    <UiButton v-if="actionLabel !== undefined" variant="secondary" :label="actionLabel" @click="emit('action')" />
    <button
      v-if="dismissLabel !== undefined"
      type="button"
      class="error-banner__dismiss"
      :aria-label="dismissLabel"
      @click="emit('dismiss')"
    >
      <UiIcon :icon="X" :size="20" />
    </button>
  </div>
</template>

<style scoped>
.error-banner {
  display: flex;
  align-items: center;
  gap: var(--space-12);
  padding: var(--space-12) var(--space-16);
  background: var(--color-error-bg);
  color: var(--color-error);
  border-radius: var(--radius-card);
  font: var(--font-body);
}

.error-banner__icon {
  flex: none;
}

.error-banner__body {
  flex: 1;
}

.error-banner__title,
.error-banner__why,
.error-banner__reference {
  margin: 0;
}

.error-banner__title {
  font-weight: 600;
}

.error-banner__reference {
  font: var(--font-code);
  font-size: 12px;
}

.error-banner__dismiss {
  display: inline-flex;
  flex: none;
  padding: var(--space-4);
  background: transparent;
  color: inherit;
  border: 0;
  border-radius: var(--radius-field);
  cursor: pointer;
}

.error-banner__dismiss:focus-visible {
  outline: 2px solid color-mix(in srgb, var(--color-primary) 50%, var(--color-surface));
  outline-offset: 2px;
}
</style>
