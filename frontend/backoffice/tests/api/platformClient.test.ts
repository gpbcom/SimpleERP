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

describe('callPlatform', () => {
  let server: StandInPlatform
  let closed: boolean

  async function load() {
    vi.resetModules()
    setActivePinia(createPinia())
    const { callPlatform } = await import('../../src/api/platformClient')
    const { useErrorStore } = await import('../../src/stores/errors')
    return { callPlatform, store: useErrorStore() }
  }

  beforeEach(async () => {
    server = await StandInPlatform.start()
    closed = false
    target.baseUrl = server.url
  })

  afterEach(async () => {
    if (!closed) {
      await server.close()
    }
  })

  it('adds nothing to the store when the call succeeds', async () => {
    const { callPlatform, store } = await load()

    const result = await callPlatform((client) => client.GET(StandInPlatform.HEALTH_PATH))

    expect(result.data?.status).toBe('ok')
    expect(store.dialog).toBeNull()
    expect(store.banner).toBeNull()
  })

  it('puts one dialog refusal with the code keys and reference into the store and rethrows the typed error', async () => {
    server.refuseWith(503, CODE)
    const { callPlatform, store } = await load()

    const error = await callPlatform((client) => client.GET(StandInPlatform.HEALTH_PATH)).catch(
      (caught: unknown) => caught,
    )

    expect(error).toMatchObject({ name: 'ApiProblemError', code: CODE, status: 503 })
    const expected = resolveErrorCode(CODE)
    expect(store.dialog).toMatchObject({
      code: CODE,
      titleKey: expected.titleKey,
      whyKey: expected.whyKey,
      actionKey: expected.actionKey,
      reference: expected.reference,
      presentation: 'dialog',
    })
    expect(store.banner).toBeNull()
  })

  it('gives a banner refusal when the presentation is banner', async () => {
    server.refuseWith(503, CODE)
    const { callPlatform, store } = await load()

    await callPlatform((client) => client.GET(StandInPlatform.HEALTH_PATH), { presentation: 'banner' }).catch(
      () => undefined,
    )

    expect(store.banner).toMatchObject({ code: CODE, presentation: 'banner' })
    expect(store.dialog).toBeNull()
  })

  it('runs the onAction when the refusal is acted on', async () => {
    server.refuseWith(503, CODE)
    const { callPlatform, store } = await load()
    const calls: string[] = []

    await callPlatform((client) => client.GET(StandInPlatform.HEALTH_PATH), {
      onAction: () => {
        calls.push('acted')
      },
    }).catch(() => undefined)
    store.act(store.dialog?.id ?? '')

    expect(calls).toEqual(['acted'])
    expect(store.dialog).toBeNull()
  })

  it('gives a fallback refusal without a reference when the server is down', async () => {
    await server.close()
    closed = true
    const { callPlatform, store } = await load()

    const outcome = await callPlatform((client) => client.GET(StandInPlatform.HEALTH_PATH)).then(
      () => 'resolved',
      () => 'rejected',
    )

    expect(outcome).toBe('rejected')
    expect(store.dialog).toMatchObject({ titleKey: resolveErrorCode('').titleKey, reference: null })
  })
})
