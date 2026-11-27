import '@simpleerp/tokens/tokens.css'
import '@simpleerp/ui/style.css'
import './styles/base.css'

import { createBackofficeApp } from './app/createBackofficeApp'

const { app, router } = createBackofficeApp()
void router.isReady().then(() => {
  app.mount('#app')
})
