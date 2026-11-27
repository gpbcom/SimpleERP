import { createRouter, createWebHistory } from 'vue-router'
import type { Router, RouterHistory } from 'vue-router'

import { routes } from './routes'

/** Create the router of the back office, with the browser history unless one is given. */
export function createBackofficeRouter(history?: RouterHistory): Router {
  return createRouter({
    history: history ?? createWebHistory(import.meta.env.BASE_URL),
    routes,
  })
}
