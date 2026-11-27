<script setup lang="ts">
import { useI18n } from '@simpleerp/i18n'

const { t } = useI18n()

function focusMain(event: Event): void {
  event.preventDefault()
  document.getElementById('main-content')?.focus()
}
</script>

<template>
  <a
    class="skip-link"
    data-shell="skip-link"
    href="#main-content"
    @click="focusMain"
  >{{ t('shell.skipToContent') }}</a>
</template>

<style scoped>
.skip-link {
  position: absolute;
  inset-block-start: var(--space-8);
  inset-inline-start: var(--space-8);
  z-index: 100;
  padding: var(--space-8) var(--space-16);
  border-radius: var(--radius-field);
  background-color: var(--color-surface);
  color: var(--color-text);
  font: var(--font-label);
  transform: translateY(-200%);
}

.skip-link:focus {
  transform: none;
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
</style>
