<script setup lang="ts">
import { Bell, Bot, ChevronDown, MapPin, User } from 'lucide-vue-next'
import { useI18n } from '@simpleerp/i18n'

import ThemeSwitch from './ThemeSwitch.vue'

const { t } = useI18n()
</script>

<template>
  <header
    class="topbar"
    data-shell="topbar"
  >
    <form
      class="topbar__search"
      role="search"
      data-place="search"
      :aria-label="t('shell.search')"
      @submit.prevent
    >
      <input
        class="topbar__input"
        type="search"
        name="q"
        :aria-label="t('shell.search')"
        :placeholder="t('shell.searchPlaceholder')"
      >
    </form>
    <button
      type="button"
      class="topbar__button"
      data-place="assistant"
      aria-disabled="true"
      :aria-label="t('shell.assistant')"
    >
      <Bot
        :size="20"
        aria-hidden="true"
        focusable="false"
      />
      <span class="topbar__text">{{ t('shell.assistant') }}</span>
    </button>
    <button
      type="button"
      class="topbar__button topbar__button--icon"
      data-place="notifications"
      aria-disabled="true"
      :aria-label="t('shell.notifications')"
    >
      <Bell
        :size="20"
        aria-hidden="true"
        focusable="false"
      />
    </button>
    <button
      type="button"
      class="topbar__button"
      data-place="site"
      aria-disabled="true"
      :aria-label="t('shell.siteSwitcher')"
    >
      <MapPin
        :size="20"
        aria-hidden="true"
        focusable="false"
      />
      <ChevronDown
        :size="16"
        aria-hidden="true"
        focusable="false"
      />
    </button>
    <ThemeSwitch />
    <button
      type="button"
      class="topbar__button topbar__button--icon"
      data-place="user"
      aria-disabled="true"
      :aria-label="t('shell.userMenu')"
    >
      <User
        :size="20"
        aria-hidden="true"
        focusable="false"
      />
    </button>
  </header>
</template>

<style scoped>
.topbar {
  display: flex;
  align-items: center;
  gap: var(--space-8);
  padding: var(--space-8) var(--space-16);
  border-bottom: 1px solid var(--color-border-strong);
  background: var(--color-surface);
  color: var(--color-text);
}

.topbar__search {
  flex: 1;
  min-width: 0;
}

.topbar__input {
  box-sizing: border-box;
  width: 100%;
  max-width: 32rem;
  height: var(--field-height);
  padding: 0 var(--space-8);
  border: 1px solid var(--color-border-strong);
  border-radius: var(--radius-field);
  background: var(--color-surface);
  color: var(--color-text);
  font: inherit;
}

.topbar__button {
  display: inline-flex;
  align-items: center;
  gap: var(--space-8);
  height: var(--field-height);
  padding: 0 var(--space-8);
  border: 1px solid transparent;
  border-radius: var(--radius-field);
  background: transparent;
  color: var(--color-text);
  font: var(--font-label);
  cursor: pointer;
}

.topbar__button--icon {
  justify-content: center;
  width: var(--field-height);
  padding: 0;
}

.topbar__button[aria-disabled='true'] {
  cursor: default;
}

.topbar__input:focus-visible,
.topbar__button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

@media (max-width: 767px) {
  .topbar {
    padding: var(--space-8);
  }

  .topbar__text {
    display: none;
  }
}
</style>
