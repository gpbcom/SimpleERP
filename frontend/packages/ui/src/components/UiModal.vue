<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, useId, watch } from 'vue';
import { CircleAlert, Info, X } from 'lucide-vue-next';

import UiIcon from './UiIcon.vue';

const props = withDefaults(
  defineProps<{
    /** Whether the modal is shown. */
    open: boolean;
    /** The title, which names the dialog. */
    title: string;
    /** The kind of modal: a question, a short form or a refusal. */
    variant?: 'confirmation' | 'form' | 'error';
    /** The accessible name of the close button. */
    closeLabel: string;
  }>(),
  { variant: 'confirmation' },
);

const emit = defineEmits<{ close: [] }>();

const FOCUSABLE =
  'button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), a[href], [tabindex]:not([tabindex="-1"])';
const FIELDS = 'input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled])';

const titleId = useId();
const panel = ref<HTMLElement | null>(null);
const content = ref<HTMLElement | null>(null);
const opener = ref<HTMLElement | null>(null);

const isError = computed(() => props.variant === 'error');

/** Moves the focus into the modal: the first field of the content, otherwise the panel. */
async function focusInside(): Promise<void> {
  await nextTick();
  if (panel.value?.contains(document.activeElement)) {
    return;
  }
  const field = content.value?.querySelector<HTMLElement>(FIELDS);
  (field ?? panel.value)?.focus();
}

/** Gives the focus back to the element that had it before the modal opened. */
function restoreFocus(): void {
  opener.value?.focus();
  opener.value = null;
}

watch(
  () => props.open,
  (isOpen) => {
    if (isOpen) {
      opener.value = document.activeElement instanceof HTMLElement ? document.activeElement : null;
      void focusInside();
    } else {
      restoreFocus();
    }
  },
);

onMounted(() => {
  if (props.open) {
    opener.value = document.activeElement instanceof HTMLElement ? document.activeElement : null;
    void focusInside();
  }
});

onBeforeUnmount(() => {
  if (props.open) {
    restoreFocus();
  }
});

/** Closes on Escape and keeps Tab and Shift+Tab inside the panel. */
function onKeydown(event: KeyboardEvent): void {
  if (event.key === 'Escape') {
    event.preventDefault();
    emit('close');
    return;
  }
  if (event.key !== 'Tab' || !panel.value) {
    return;
  }
  const focusable = Array.from(panel.value.querySelectorAll<HTMLElement>(FOCUSABLE));
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  if (!first || !last) {
    event.preventDefault();
    panel.value.focus();
  } else if (event.shiftKey && (document.activeElement === first || document.activeElement === panel.value)) {
    event.preventDefault();
    last.focus();
  } else if (!event.shiftKey && document.activeElement === last) {
    event.preventDefault();
    first.focus();
  }
}
</script>

<template>
  <Teleport to="body">
    <div
      v-if="open"
      class="ui-modal__veil"
      @keydown="onKeydown"
    >
      <div
        ref="panel"
        class="ui-modal__panel"
        :role="isError ? 'alertdialog' : 'dialog'"
        aria-modal="true"
        :aria-labelledby="titleId"
        tabindex="-1"
      >
        <header class="ui-modal__header">
          <UiIcon
            class="ui-modal__icon"
            :class="{ 'ui-modal__icon--error': isError }"
            :icon="isError ? CircleAlert : Info"
            :size="24"
          />
          <h2
            :id="titleId"
            class="ui-modal__title"
          >
            {{ title }}
          </h2>
          <button
            type="button"
            class="ui-modal__close"
            :aria-label="closeLabel"
            @click="emit('close')"
          >
            <UiIcon
              :icon="X"
              :size="20"
            />
          </button>
        </header>
        <div
          ref="content"
          class="ui-modal__content"
        >
          <slot />
        </div>
        <footer
          v-if="$slots.actions"
          class="ui-modal__actions"
        >
          <slot name="actions" />
        </footer>
      </div>
    </div>
  </Teleport>
</template>

<style scoped>
.ui-modal__veil {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  background: color-mix(in srgb, var(--color-text) 45%, transparent);
}

.ui-modal__panel {
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: var(--space-16);
  width: 520px;
  max-width: 100%;
  max-height: 100%;
  overflow: auto;
  padding: var(--space-24);
  background: var(--color-surface);
  color: var(--color-text);
  border-radius: var(--radius-panel);
  box-shadow: var(--elevation-2);
  font: var(--font-body);
  animation: ui-modal-in 250ms ease-out;
}

.ui-modal__panel:focus-visible,
.ui-modal__close:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.ui-modal__header {
  display: flex;
  align-items: center;
  gap: var(--space-12);
}

.ui-modal__icon {
  flex: none;
  color: var(--color-primary);
}

.ui-modal__icon--error {
  color: var(--color-error);
}

.ui-modal__title {
  flex: 1;
  margin: 0;
  font: var(--font-h3);
}

.ui-modal__close {
  display: inline-flex;
  flex: none;
  align-items: center;
  justify-content: center;
  padding: var(--space-8);
  background: transparent;
  color: var(--color-text);
  border: none;
  border-radius: var(--radius-field);
  cursor: pointer;
}

.ui-modal__actions {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-8);
}

@keyframes ui-modal-in {
  from {
    opacity: 0;
    transform: translateY(var(--space-16));
  }
}

@media (max-width: 639px) {
  .ui-modal__veil {
    align-items: flex-end;
  }

  .ui-modal__panel {
    width: 100%;
    border-radius: var(--radius-panel) var(--radius-panel) 0 0;
  }

  .ui-modal__actions {
    flex-direction: column-reverse;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ui-modal__panel {
    animation: none;
  }
}
</style>
