<script setup lang="ts">
import { RouterView } from 'vue-router'

import ErrorOutlet from './errors/ErrorOutlet.vue'
import AppShell from './shell/AppShell.vue'
</script>

<template>
  <AppShell>
    <ErrorOutlet />
    <RouterView />
  </AppShell>
</template>
