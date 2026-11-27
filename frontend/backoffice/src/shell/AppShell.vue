<script setup lang="ts">
import { computed } from 'vue'

import { useLayoutStore } from '../stores/layout'
import { useThemeStore } from '../stores/theme'
import AppSidebar from './AppSidebar.vue'
import BottomTabBar from './BottomTabBar.vue'
import SkipLink from './SkipLink.vue'
import TopBar from './TopBar.vue'

useThemeStore()
const layout = useLayoutStore()
const phone = computed(() => layout.viewport === 'phone')
</script>

<template>
  <div
    class="app-shell"
    :data-viewport="layout.viewport"
  >
    <SkipLink />
    <AppSidebar v-if="!phone" />
    <TopBar />
    <main
      id="main-content"
      class="app-shell__main"
      tabindex="-1"
    >
      <slot />
    </main>
    <BottomTabBar v-if="phone" />
  </div>
</template>

<style scoped>
.app-shell {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  grid-template-rows: auto minmax(0, 1fr);
  grid-template-areas:
    'sidebar topbar'
    'sidebar main';
  min-block-size: 100vh;
}

.app-shell[data-viewport='phone'] {
  grid-template-columns: minmax(0, 1fr);
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'topbar'
    'main'
    'tabbar';
}

.app-shell > :deep([data-shell='sidebar']) {
  grid-area: sidebar;
}

.app-shell > :deep([data-shell='topbar']) {
  grid-area: topbar;
}

.app-shell > :deep([data-shell='tabbar']) {
  grid-area: tabbar;
  position: sticky;
  inset-block-end: 0;
}

.app-shell__main {
  grid-area: main;
  padding: var(--space-24);
}

.app-shell__main:focus {
  outline: none;
}

.app-shell[data-viewport='phone'] .app-shell__main {
  padding: var(--space-16);
}
</style>
