<script setup lang="ts">
import { computed, onMounted, useId, watch } from 'vue';

import UiButton from '../components/UiButton.vue';
import UiModal from '../components/UiModal.vue';

const props = defineProps<{
  /** Whether the dialog is shown. */
  open: boolean;
  /** What is wrong, in a few words. It names the dialog. */
  title: string;
  /** Why it is wrong, and what to do. It describes the dialog. */
  why: string;
  /** The label of the primary action. */
  actionLabel: string;
  /** The label of the cancel button. */
  cancelLabel: string;
  /** The error reference, shown at the bottom in the code font. */
  reference?: string;
  /** The word before the reference, such as "ref.". */
  referenceLabel: string;
}>();

const emit = defineEmits<{ action: []; cancel: [] }>();

const whyId = useId();

/** The accessible name of the modal's close button: the cancel label and the title. */
const closeLabel = computed(() => `${props.cancelLabel}: ${props.title}`);

/** Points the dialog panel at the why, which the modal cannot do itself. */
function describeDialog(): void {
  const panel = document.getElementById(whyId)?.closest('[role="alertdialog"]');
  panel?.setAttribute('aria-describedby', whyId);
}

watch(
  () => props.open,
  (isOpen) => {
    if (isOpen) {
      describeDialog();
    }
  },
  { flush: 'post' },
);

onMounted(() => {
  if (props.open) {
    describeDialog();
  }
});
</script>

<template>
  <UiModal
    :open="open"
    :title="title"
    variant="error"
    :close-label="closeLabel"
    @close="emit('cancel')"
  >
    <p
      :id="whyId"
      class="error-dialog__why"
    >
      {{ why }}
    </p>
    <p
      v-if="reference"
      class="error-dialog__reference"
    >
      {{ referenceLabel }} {{ reference }}
    </p>
    <template #actions>
      <UiButton
        variant="secondary"
        :label="cancelLabel"
        @click="emit('cancel')"
      />
      <UiButton
        variant="primary"
        :label="actionLabel"
        @click="emit('action')"
      />
    </template>
  </UiModal>
</template>

<style scoped>
.error-dialog__why {
  margin: 0;
  color: var(--color-text);
}

:global(.ui-modal__icon--error) {
  color: var(--color-error);
}

.error-dialog__reference {
  margin: var(--space-16) 0 0;
  text-align: right;
  color: var(--color-text-muted);
  font: var(--font-caption);
  font-family: var(--font-family-code);
}
</style>
