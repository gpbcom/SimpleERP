import type { RouteRecordRaw } from 'vue-router'

declare module 'vue-router' {
  interface RouteMeta {
    /** The translation key of the page title. */
    titleKey?: string
  }
}

export const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/PlaceholderView.vue'),
    meta: { titleKey: 'nav.home' },
  },
  {
    path: '/tasks',
    name: 'tasks',
    component: () => import('../views/PlaceholderView.vue'),
    meta: { titleKey: 'nav.tasks' },
  },
  { path: '/:pathMatch(.*)*', redirect: { name: 'home' } },
]
