<script setup lang="ts">
import { computed, useId } from 'vue';
import { Check } from 'lucide-vue-next';

import UiIcon from './UiIcon.vue';

const props = withDefaults(
  defineProps<{
    /** The title, shown in a heading. */
    title: string;
    /** The level of the heading, 2 to 6. */
    headingLevel?: 2 | 3 | 4 | 5 | 6;
    /** Makes the title the card's only link. */
    href?: string;
    /** Makes the card a radio button or a checkbox. */
    selectable?: 'radio' | 'checkbox';
    /** Whether a selectable card is selected. */
    selected?: boolean;
    /** The input name of a selectable card. */
    name?: string;
    /** The input value of a selectable card. */
    value?: string;
    /** A dashboard figure, drawn in the display typeface. */
    figure?: string;
    /** The change shown under the figure. */
    change?: string;
    /** Shows skeleton lines in place of the content and marks the card busy. */
    loading?: boolean;
  }>(),
  {
    headingLevel: 3,
    href: undefined,
    selectable: undefined,
    selected: false,
    name: undefined,
    value: undefined,
    figure: undefined,
    change: undefined,
    loading: false,
  },
);

const emit = defineEmits<{
  'update:selected': [selected: boolean];
}>();

const titleId = useId();
const inputId = useId();
const heading = computed(() => `h${props.headingLevel}`);
const clickable = computed(() => props.href !== undefined || props.selectable !== undefined);

function onChange(event: Event): void {
  emit('update:selected', (event.target as HTMLInputElement).checked);
}
</script>

<template>
  <div
    class="ui-card"
    :class="{ 'ui-card--clickable': clickable, 'ui-card--selected': selectable && selected }"
    :aria-busy="loading ? 'true' : undefined"
  >
    <input
      v-if="selectable"
      :id="inputId"
      class="ui-card__input"
      :type="selectable"
      :name="name"
      :value="value"
      :checked="selected"
      :aria-labelledby="titleId"
      @change="onChange"
    />
    <component :is="heading" :id="titleId" class="ui-card__title">
      <a v-if="href" class="ui-card__link" :href="href">{{ title }}</a>
      <label v-else-if="selectable" class="ui-card__link" :for="inputId">{{ title }}</label>
      <template v-else>{{ title }}</template>
    </component>
    <UiIcon v-if="selectable && selected" class="ui-card__check" :icon="Check" :size="20" />
    <div v-if="loading" class="ui-card__body">
      <div class="ui-card__skeleton"></div>
      <div class="ui-card__skeleton ui-card__skeleton--short"></div>
    </div>
    <div v-else class="ui-card__body">
      <p v-if="figure" class="ui-card__figure">{{ figure }}</p>
      <p v-if="change" class="ui-card__change">{{ change }}</p>
      <slot />
    </div>
    <div v-if="$slots.actions" class="ui-card__actions">
      <slot name="actions" />
    </div>
  </div>
</template>

<style scoped>
.ui-card {
  --ui-card-padding: var(--space-24);

  position: relative;
  display: flex;
  flex-direction: column;
  gap: var(--space-12);
  padding: var(--ui-card-padding);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-card);
  background: var(--color-surface-raised-1);
  box-shadow: var(--elevation-1);
  color: var(--color-text);
  font: var(--font-body);
}

.ui-card--clickable:hover {
  border-color: var(--color-border-strong);
}

.ui-card--selected {
  border-color: var(--color-primary);
  outline: 2px solid var(--color-primary);
  outline-offset: -2px;
}

.ui-card:has(:focus-visible) {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.ui-card__input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  opacity: 0;
}

.ui-card__title {
  margin: 0;
  font: var(--font-h3);
}

.ui-card__link {
  color: inherit;
  text-decoration: none;
  cursor: pointer;
}

.ui-card__link::after {
  content: '';
  position: absolute;
  inset: 0;
}

.ui-card__link:focus-visible {
  outline: none;
}

.ui-card__check {
  position: absolute;
  top: var(--space-16);
  right: var(--space-16);
  color: var(--color-primary);
}

.ui-card__body {
  display: flex;
  flex-direction: column;
  gap: var(--space-8);
}

.ui-card__figure {
  margin: 0;
  font: var(--font-display);
}

.ui-card__change {
  margin: 0;
  color: var(--color-text-muted);
  font: var(--font-body-compact);
}

.ui-card__skeleton {
  height: var(--space-16);
  border-radius: var(--radius-field);
  background: var(--color-surface-alt);
}

.ui-card__skeleton--short {
  width: 60%;
}

.ui-card__actions {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: flex-end;
  gap: var(--space-8);
}

@media (max-width: 767px) {
  .ui-card {
    --ui-card-padding: var(--space-16);
  }
}
</style>
