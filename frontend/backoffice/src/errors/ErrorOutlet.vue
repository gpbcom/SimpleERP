<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { watch } from 'vue'

import { createI18n, errorCatalogs, useI18n } from '@simpleerp/i18n'
import type { TranslateParams } from '@simpleerp/i18n'
import { ErrorBanner, ErrorDialog } from '@simpleerp/ui'

import { useErrorStore } from '../stores/errors'

const app = useI18n()
const own = createI18n({ locale: app.locale.value, catalogs: errorCatalogs })
watch(app.locale, (next) => own.setLocale(next), { flush: 'sync' })

/** Translate with the texts of the error catalogue first, then with the application's own. */
function t(key: string, params?: TranslateParams): string {
  const text = own.t(key, params)
  return text === key ? app.t(key, params) : text
}
const errors = useErrorStore()
const { banner, dialog } = storeToRefs(errors)
</script>

<template>
  <div class="error-outlet">
    <ErrorBanner
      v-if="banner !== null"
      class="error-outlet__banner"
      :title="t(banner.titleKey, banner.params)"
      :why="t(banner.whyKey, banner.params)"
      :action-label="t(banner.actionKey, banner.params)"
      :reference="banner.reference ?? undefined"
      :reference-label="t('errors.common.reference')"
      :dismiss-label="t('errors.common.cancel')"
      @action="errors.act(banner.id)"
      @dismiss="errors.dismiss(banner.id)"
    />
    <ErrorDialog
      v-if="dialog !== null"
      :open="true"
      :title="t(dialog.titleKey, dialog.params)"
      :why="t(dialog.whyKey, dialog.params)"
      :action-label="t(dialog.actionKey, dialog.params)"
      :cancel-label="t('errors.common.cancel')"
      :reference="dialog.reference ?? undefined"
      :reference-label="t('errors.common.reference')"
      @action="errors.act(dialog.id)"
      @cancel="errors.dismiss(dialog.id)"
    />
  </div>
</template>

<style scoped>
.error-outlet__banner {
  margin-block-end: var(--space-16);
}
</style>
