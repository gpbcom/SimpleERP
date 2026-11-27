export interface MediaState {
  widthPx: number
  dark: boolean
}

export interface MediaController {
  setWidth(px: number): void
  setDark(dark: boolean): void
  uninstall(): void
}

type Listener = (event: MediaQueryListEvent) => void

interface Entry {
  query: string
  list: MediaQueryList
  listeners: Set<Listener>
  last: boolean
}

function evaluate(query: string, state: MediaState): boolean {
  return query
    .split(/\band\b/)
    .map((part) => part.trim())
    .every((part) => {
      const match = /^\(\s*([a-z-]+)\s*:\s*([a-z0-9.]+?)(px)?\s*\)$/.exec(part)
      if (!match) return false
      const feature = match[1]
      const value = match[2] ?? ''
      if (feature === 'max-width') return state.widthPx <= Number(value)
      if (feature === 'min-width') return state.widthPx >= Number(value)
      if (feature === 'prefers-color-scheme') return value === (state.dark ? 'dark' : 'light')
      return false
    })
}

export function installMatchMedia(state: MediaState): MediaController {
  const previous = window.matchMedia
  const previousWidth = window.innerWidth
  const current: MediaState = { ...state }
  const entries: Entry[] = []
  window.innerWidth = current.widthPx

  window.matchMedia = ((query: string): MediaQueryList => {
    const listeners = new Set<Listener>()
    const entry = { query, listeners, last: evaluate(query, current) } as Entry
    const add = (_type: string, listener: Listener): void => {
      listeners.add(listener)
    }
    const remove = (_type: string, listener: Listener): void => {
      listeners.delete(listener)
    }
    entry.list = {
      media: query,
      onchange: null,
      get matches(): boolean {
        return evaluate(query, current)
      },
      addEventListener: add,
      removeEventListener: remove,
      addListener: add,
      removeListener: remove,
      dispatchEvent: (): boolean => true,
    } as unknown as MediaQueryList
    entries.push(entry)
    return entry.list
  }) as typeof window.matchMedia

  function refresh(): void {
    window.innerWidth = current.widthPx
    for (const entry of entries) {
      const matches = evaluate(entry.query, current)
      if (matches === entry.last) continue
      entry.last = matches
      const event = { matches, media: entry.query, type: 'change' } as MediaQueryListEvent
      for (const listener of [...entry.listeners]) listener(event)
    }
  }

  return {
    setWidth(px: number): void {
      current.widthPx = px
      refresh()
    },
    setDark(dark: boolean): void {
      current.dark = dark
      refresh()
    },
    uninstall(): void {
      window.matchMedia = previous
      window.innerWidth = previousWidth
    },
  }
}
