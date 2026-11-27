<script setup lang="ts">
const items: number[] = [1, 2, 3];
</script>

<template>
  <ul>
    <li v-for="item in items" v-if="item > 1" :key="item">{{ item }}</li>
  </ul>
</template>
