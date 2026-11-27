<script setup lang="ts">
import { computed } from 'vue'
import { Moon, Sun } from 'lucide-vue-next'
import { useI18n } from '@simpleerp/i18n'

import { useThemeStore } from '../stores/theme'

const { t } = useI18n()
const theme = useThemeStore()
const label = computed(() => (theme.resolved === 'light' ? t('shell.switchToDark') : t('shell.switchToLight')))
</script>

<template>
  <button
    type="button"
    class="theme-switch"
    data-place="theme"
    :aria-label="label"
    @click="theme.toggle()"
  >
    <component
      :is="theme.resolved === 'light' ? Moon : Sun"
      :size="20"
      aria-hidden="true"
      focusable="false"
    />
  </button>
</template>

<style scoped>
.theme-switch {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--field-height);
  height: var(--field-height);
  padding: 0;
  border: 1px solid transparent;
  border-radius: var(--radius-field);
  background: transparent;
  color: var(--color-text);
  cursor: pointer;
}

.theme-switch:hover {
  background: var(--color-surface);
}

.theme-switch:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
</style>
