import '@simpleerp/tokens/tokens.css'
import '@simpleerp/ui/style.css'
import './styles/base.css'

import { checkPlatform } from './api/checkPlatform'
import { createBackofficeApp } from './app/createBackofficeApp'

const { app, router } = createBackofficeApp()
void router.isReady().then(() => {
  app.mount('#app')
  void checkPlatform()
})
