<script setup lang="ts">
import { computed, useId } from 'vue';
import { CircleAlert, Lock } from 'lucide-vue-next';
import type { LucideIcon } from 'lucide-vue-next';

import UiIcon from './UiIcon.vue';
import UiSpinner from './UiSpinner.vue';

const props = withDefaults(
  defineProps<{
    /** The visible label, always shown above the input. */
    label: string;
    /** The value of the input. */
    modelValue?: string | number;
    /** The kind of input. */
    type?: 'text' | 'number' | 'date' | 'email' | 'tel' | 'url';
    /** The id of the input. Generated when absent. */
    id?: string;
    required?: boolean;
    disabled?: boolean;
    readonly?: boolean;
    /** A value the user may see but not change, drawn with a lock icon. */
    locked?: boolean;
    /** A lookup is running: a spinner shows and the input is busy. */
    loading?: boolean;
    /** One short line under the input. */
    help?: string;
    /** The error text, from the caller. It replaces the help. */
    error?: string;
    /** A unit shown inside the field, after the value. */
    unit?: string;
    placeholder?: string;
    /** An icon shown inside the field, before the value. */
    icon?: LucideIcon;
  }>(),
  {
    modelValue: '',
    type: 'text',
    id: undefined,
    required: false,
    disabled: false,
    readonly: false,
    locked: false,
    loading: false,
    help: undefined,
    error: undefined,
    unit: undefined,
    placeholder: undefined,
    icon: undefined,
  },
);

const emit = defineEmits<{
  'update:modelValue': [value: string];
  blur: [event: FocusEvent];
}>();

const generatedId = useId();
const inputId = computed(() => props.id ?? generatedId);
const messageId = computed(() => `${inputId.value}-message`);
const message = computed(() => props.error ?? props.help);

function onInput(event: Event): void {
  emit('update:modelValue', (event.target as HTMLInputElement).value);
}
</script>

<template>
  <div class="ui-form-field">
    <label class="ui-form-field__label" :for="inputId">
      {{ label }}
      <span v-if="required" class="ui-form-field__mark" aria-hidden="true">*</span>
    </label>
    <div
      class="ui-form-field__control"
      :class="{
        'ui-form-field__control--error': error,
        'ui-form-field__control--locked': locked,
        'ui-form-field__control--muted': disabled || readonly || locked,
      }"
    >
      <UiIcon v-if="icon" :icon="icon" :size="20" />
      <input
        :id="inputId"
        class="ui-form-field__input"
        :type="type"
        :value="modelValue"
        :required="required"
        :disabled="disabled"
        :readonly="readonly || locked"
        :placeholder="placeholder"
        :aria-describedby="message ? messageId : undefined"
        :aria-invalid="error ? 'true' : undefined"
        :aria-busy="loading ? 'true' : undefined"
        @input="onInput"
        @blur="emit('blur', $event)"
      />
      <span v-if="unit" class="ui-form-field__unit">{{ unit }}</span>
      <UiSpinner v-if="loading" :size="20" />
      <UiIcon v-if="locked" :icon="Lock" :size="20" />
    </div>
    <p v-if="message" :id="messageId" class="ui-form-field__message" :class="{ 'ui-form-field__message--error': error }">
      <UiIcon v-if="error" :icon="CircleAlert" :size="16" />
      <span>{{ message }}</span>
    </p>
  </div>
</template>

<style scoped>
.ui-form-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.ui-form-field__label {
  font: var(--font-label);
  color: var(--color-text);
}

.ui-form-field__mark {
  color: var(--color-error);
}

.ui-form-field__control {
  box-sizing: border-box;
  display: flex;
  align-items: center;
  gap: var(--space-8);
  height: var(--field-height);
  padding: 0 var(--space-12);
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border-strong);
  border-radius: var(--radius-field);
}

.ui-form-field__control:hover {
  border-color: var(--color-text-muted);
}

.ui-form-field__control:focus-within {
  border: 2px solid var(--color-primary);
}

.ui-form-field__control--muted {
  background: var(--color-surface-alt);
  color: var(--color-text-muted);
}

.ui-form-field__control--locked {
  border-style: dashed;
}

.ui-form-field__control--error,
.ui-form-field__control--error:hover,
.ui-form-field__control--error:focus-within {
  border: 2px solid var(--color-error);
}

.ui-form-field__input {
  flex: 1;
  min-width: 0;
  height: 100%;
  padding: 0;
  border: none;
  outline: none;
  background: transparent;
  color: inherit;
  font: var(--font-body);
}

.ui-form-field__input::placeholder {
  color: var(--color-text-muted);
}

.ui-form-field__unit {
  font: var(--font-body);
  color: var(--color-text-muted);
}

.ui-form-field__message {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  margin: 0;
  font: var(--font-caption);
  color: var(--color-text-muted);
}

.ui-form-field__message--error {
  color: var(--color-error);
}
</style>
