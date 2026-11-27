<script setup lang="ts">
import { useI18n } from '@simpleerp/i18n'

import { navItems } from '../navigation/items'

const { t } = useI18n()
const tabs = navItems.filter((item) => item.placements.includes('tabs'))
</script>

<template>
  <nav class="bottom-tab-bar" data-shell="tabbar" :aria-label="t('shell.navigation')">
    <template v-for="item in tabs" :key="item.id">
      <RouterLink
        v-if="item.routeName"
        class="bottom-tab-bar__item"
        :to="{ name: item.routeName }"
        :data-nav-item="item.id"
      >
        <component :is="item.icon" class="bottom-tab-bar__icon" aria-hidden="true" :size="22" />
        <span class="bottom-tab-bar__label">{{ t(item.labelKey) }}</span>
      </RouterLink>
      <button v-else class="bottom-tab-bar__item" type="button" aria-disabled="true" :data-nav-item="item.id">
        <component :is="item.icon" class="bottom-tab-bar__icon" aria-hidden="true" :size="22" />
        <span class="bottom-tab-bar__label">{{ t(item.labelKey) }}</span>
      </button>
    </template>
  </nav>
</template>

<style scoped>
.bottom-tab-bar {
  position: fixed;
  inset-inline: 0;
  bottom: 0;
  display: flex;
  justify-content: space-around;
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  z-index: 10;
}

.bottom-tab-bar__item {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-4);
  min-height: 56px;
  min-width: 44px;
  padding: var(--space-8);
  background: transparent;
  border: 0;
  color: var(--color-text-muted);
  font: var(--font-caption);
  text-decoration: none;
  cursor: pointer;
}

.bottom-tab-bar__item[aria-current='page'] {
  color: var(--color-primary);
}

.bottom-tab-bar__item[aria-disabled='true'] {
  cursor: default;
}

.bottom-tab-bar__item:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: -2px;
}
</style>
