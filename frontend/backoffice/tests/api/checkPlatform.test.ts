import { createPinia, setActivePinia } from 'pinia'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import { resolveErrorCode } from '@simpleerp/i18n'

import { StandInPlatform } from './standInPlatform'

const target = vi.hoisted(() => ({ baseUrl: '' }))

vi.mock('@simpleerp/api-client', async (importOriginal) => {
  const original = await importOriginal<typeof import('@simpleerp/api-client')>()
  return {
    ...original,
    createApiClient: (options: Parameters<typeof original.createApiClient>[0]) =>
      original.createApiClient({ ...options, baseUrl: target.baseUrl }),
  }
})

const CODE = 'SERVICE-FAILURE-01'

describe('checkPlatform', () => {
  let server: StandInPlatform

  async function load() {
    vi.resetModules()
    setActivePinia(createPinia())
    const { checkPlatform } = await import('../../src/api/checkPlatform')
    const { useErrorStore } = await import('../../src/stores/errors')
    return { checkPlatform, store: useErrorStore() }
  }

  beforeEach(async () => {
    server = await StandInPlatform.start()
    target.baseUrl = server.url
  })

  afterEach(async () => {
    await server.close()
  })

  it('adds nothing to the store when the platform is healthy', async () => {
    const { checkPlatform, store } = await load()

    await checkPlatform()

    expect(server.paths).toEqual([StandInPlatform.HEALTH_PATH])
    expect(store.dialog).toBeNull()
    expect(store.banner).toBeNull()
  })

  it('adds one banner refusal and keeps running when the platform refuses', async () => {
    server.refuseWith(503, CODE)
    const { checkPlatform, store } = await load()

    await expect(checkPlatform()).resolves.toBeUndefined()

    expect(store.banner).toMatchObject({
      code: CODE,
      reference: resolveErrorCode(CODE).reference,
      presentation: 'banner',
    })
    expect(store.dialog).toBeNull()
  })

  it('calls the health path again when the banner action is used', async () => {
    server.refuseWith(503, CODE)
    const { checkPlatform, store } = await load()
    await checkPlatform()
    server.heal()

    store.act(store.banner?.id ?? '')

    await vi.waitFor(() => expect(server.paths).toHaveLength(2))
    expect(server.paths).toEqual([StandInPlatform.HEALTH_PATH, StandInPlatform.HEALTH_PATH])
  })
})
