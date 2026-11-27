import type { Component } from 'vue'
import { Bot, House, ListChecks, User } from 'lucide-vue-next'

export type NavItemId = 'home' | 'tasks' | 'assistant' | 'me'

export interface NavItem {
  id: NavItemId
  labelKey: string
  icon: Component
  routeName?: 'home' | 'tasks'
  placements: readonly ('sidebar' | 'tabs')[]
}

export const navItems: readonly NavItem[] = [
  { id: 'home', labelKey: 'nav.home', icon: House, routeName: 'home', placements: ['sidebar', 'tabs'] },
  { id: 'tasks', labelKey: 'nav.tasks', icon: ListChecks, routeName: 'tasks', placements: ['sidebar', 'tabs'] },
  { id: 'assistant', labelKey: 'nav.assistant', icon: Bot, placements: ['sidebar', 'tabs'] },
  { id: 'me', labelKey: 'nav.me', icon: User, placements: ['tabs'] },
]
