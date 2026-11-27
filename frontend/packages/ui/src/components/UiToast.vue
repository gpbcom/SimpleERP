<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted } from 'vue';
import { CircleCheck, Info, X } from 'lucide-vue-next';

import UiIcon from './UiIcon.vue';

const props = withDefaults(
  defineProps<{
    /** The variant: a check for something done, an information icon for something done in the background. */
    kind?: 'success' | 'info';
    /** The one sentence the toast says. */
    message: string;
    /** The label of the optional action, such as Undo. With an action the toast never closes by itself. */
    actionLabel?: string;
    /** The accessible name of the close button. */
    closeLabel: string;
    /** How long a toast without an action stays, in ms. */
    durationMs?: number;
  }>(),
  { kind: 'success', actionLabel: undefined, durationMs: 6000 },
);

const emit = defineEmits<{
  action: [];
  close: [];
}>();

const icon = computed(() => (props.kind === 'info' ? Info : CircleCheck));

let timer: ReturnType<typeof setTimeout> | undefined;
let remainingMs = props.durationMs;
let startedAt = 0;

/** Starts the countdown with the time left, unless the toast has an action. */
function resume(): void {
  if (props.actionLabel !== undefined || timer !== undefined) return;
  startedAt = Date.now();
  timer = setTimeout(() => {
    timer = undefined;
    emit('close');
  }, remainingMs);
}

/** Stops the countdown and keeps the time left. */
function pause(): void {
  if (timer === undefined) return;
  clearTimeout(timer);
  timer = undefined;
  remainingMs = Math.max(0, remainingMs - (Date.now() - startedAt));
}

onMounted(resume);
onBeforeUnmount(pause);
</script>

<template>
  <div
    class="ui-toast"
    role="status"
    @mouseenter="pause"
    @mouseleave="resume"
    @focusin="pause"
    @focusout="resume"
  >
    <UiIcon class="ui-toast__icon" :icon="icon" :size="20" />
    <p class="ui-toast__message">{{ message }}</p>
    <button v-if="actionLabel !== undefined" type="button" class="ui-toast__button" @click="emit('action')">
      {{ actionLabel }}
    </button>
    <button type="button" class="ui-toast__button ui-toast__close" :aria-label="closeLabel" @click="emit('close')">
      <UiIcon :icon="X" :size="20" />
    </button>
  </div>
</template>

<style scoped>
.ui-toast {
  display: flex;
  align-items: center;
  gap: var(--space-12);
  padding: var(--space-12) var(--space-16);
  background: var(--color-text);
  color: var(--color-surface);
  border-radius: var(--radius-card);
  box-shadow: var(--elevation-2);
  font: var(--font-body);
  animation: ui-toast-enter 150ms ease-out;
}

.ui-toast__icon {
  flex: none;
}

.ui-toast__message {
  flex: 1;
  margin: 0;
}

.ui-toast__button {
  display: inline-flex;
  align-items: center;
  flex: none;
  padding: var(--space-4) var(--space-8);
  background: transparent;
  color: inherit;
  border: 0;
  border-radius: var(--radius-field);
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}

.ui-toast__close {
  padding: var(--space-4);
}

.ui-toast__button:focus-visible {
  outline: 2px solid color-mix(in srgb, var(--color-primary) 50%, var(--color-surface));
  outline-offset: 2px;
}

@keyframes ui-toast-enter {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ui-toast {
    animation: none;
  }
}
</style>
