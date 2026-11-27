import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [vue()],
  build: {
    cssCodeSplit: false,
    lib: {
      entry: 'src/index.ts',
      formats: ['es'],
      fileName: () => 'ui.js',
      cssFileName: 'ui',
    },
    rollupOptions: {
      external: [/^vue$/, /^lucide-vue-next(\/.*)?$/, /^@simpleerp\/tokens(\/.*)?$/],
    },
  },
})
