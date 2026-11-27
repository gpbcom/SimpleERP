<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from '@simpleerp/i18n'

const route = useRoute()
const { t } = useI18n()
const title = computed(() => {
  const key = route.meta.titleKey
  return key ? t(key) : ''
})
</script>

<template>
  <section>
    <h1>{{ title }}</h1>
    <p>{{ t('page.empty') }}</p>
  </section>
</template>
