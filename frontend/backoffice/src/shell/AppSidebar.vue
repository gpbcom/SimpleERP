<script setup lang="ts">
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import { useI18n } from '@simpleerp/i18n'

import symbolUrl from '../assets/symbol.svg?no-inline'
import { navItems } from '../navigation/items'
import { useLayoutStore } from '../stores/layout'

const LIST_ID = 'app-sidebar-list'
const symbol = symbolUrl.replace(/\?no-inline$/, '')

const layout = useLayoutStore()
const { t } = useI18n()
const collapsed = computed(() => layout.sidebarCollapsed)
const items = navItems.filter((item) => item.placements.includes('sidebar'))
</script>

<template>
  <aside
    class="app-sidebar"
    data-shell="sidebar"
    :data-collapsed="collapsed ? 'true' : 'false'"
  >
    <div class="app-sidebar__header">
      <img
        class="app-sidebar__symbol"
        data-shell="symbol"
        :src="symbol"
        alt=""
      >
      <span
        v-if="!collapsed"
        class="app-sidebar__wordmark"
      >{{ t('app.name') }}</span>
    </div>
    <nav :aria-label="t('shell.navigation')">
      <ul
        :id="LIST_ID"
        class="app-sidebar__list"
      >
        <li
          v-for="item in items"
          :key="item.id"
        >
          <RouterLink
            v-if="item.routeName"
            class="app-sidebar__item"
            :to="{ name: item.routeName }"
            :data-nav-item="item.id"
            :aria-label="collapsed ? t(item.labelKey) : undefined"
          >
            <component
              :is="item.icon"
              :size="24"
              aria-hidden="true"
            />
            <span v-if="!collapsed">{{ t(item.labelKey) }}</span>
          </RouterLink>
          <button
            v-else
            type="button"
            class="app-sidebar__item"
            aria-disabled="true"
            :data-nav-item="item.id"
            :aria-label="collapsed ? t(item.labelKey) : undefined"
          >
            <component
              :is="item.icon"
              :size="24"
              aria-hidden="true"
            />
            <span v-if="!collapsed">{{ t(item.labelKey) }}</span>
          </button>
        </li>
      </ul>
    </nav>
    <button
      type="button"
      class="app-sidebar__toggle"
      data-shell="sidebar-toggle"
      :aria-expanded="!collapsed"
      :aria-controls="LIST_ID"
      :aria-label="collapsed ? t('shell.expandSidebar') : t('shell.collapseSidebar')"
      @click="layout.toggleSidebar()"
    >
      <span aria-hidden="true">{{ collapsed ? '»' : '«' }}</span>
    </button>
  </aside>
</template>

<style scoped>
.app-sidebar {
  display: flex;
  flex-direction: column;
  gap: var(--space-16);
  inline-size: 240px;
  padding: var(--space-12);
  background-color: var(--color-surface-alt);
  color: var(--color-text);
}

.app-sidebar[data-collapsed='true'] {
  inline-size: 72px;
}

.app-sidebar__header {
  display: flex;
  align-items: center;
  gap: var(--space-12);
  padding: var(--space-8) var(--space-12);
}

.app-sidebar__symbol {
  inline-size: 32px;
  block-size: 32px;
}

.app-sidebar__wordmark {
  font: var(--font-label);
}

.app-sidebar__list {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  margin: 0;
  padding: 0;
  list-style: none;
}

.app-sidebar__item {
  display: flex;
  align-items: center;
  gap: var(--space-12);
  inline-size: 100%;
  padding: var(--space-8) var(--space-12);
  border: 0;
  border-radius: var(--radius-field);
  background: transparent;
  color: var(--color-text);
  font: var(--font-label);
  text-decoration: none;
  cursor: pointer;
}

.app-sidebar[data-collapsed='true'] .app-sidebar__item {
  justify-content: center;
}

.app-sidebar__item:hover {
  background-color: var(--color-surface);
}

.app-sidebar__item[aria-current='page'] {
  background-color: var(--color-surface);
  color: var(--color-primary);
}

.app-sidebar__item[aria-disabled='true'] {
  cursor: not-allowed;
}

.app-sidebar__toggle {
  align-self: flex-end;
  padding: var(--space-8) var(--space-12);
  border: 0;
  border-radius: var(--radius-field);
  background: transparent;
  color: var(--color-text);
  font: var(--font-label);
  cursor: pointer;
}

.app-sidebar__toggle:hover {
  background-color: var(--color-surface);
}

.app-sidebar__item:focus-visible,
.app-sidebar__toggle:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
</style>
