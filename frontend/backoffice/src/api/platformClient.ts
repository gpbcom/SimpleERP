import { createApiClient, type PlatformClient } from '@simpleerp/api-client'

import { toRefusal } from '../errors/toRefusal'
import { useErrorStore } from '../stores/errors'

/**
 * The back office's one typed client. The generated paths already carry `/v1`, so the base is the page's own origin,
 * where the image proxies `/v1/` to the platform service.
 */
const platformClient: PlatformClient = createApiClient({ baseUrl: window.location.origin })

/** What `callPlatform` accepts besides the call. */
export interface CallPlatformOptions {
  /** How a refused call shows: a dialog by default. */
  presentation?: 'dialog' | 'banner'
  /** Run when the person uses the refusal's action. */
  onAction?: () => void
}

/**
 * Run one call on the platform client. A thrown error is put into the error store as a refusal (never its body) and
 * rethrown for the caller.
 */
export async function callPlatform<T>(
  call: (client: PlatformClient) => Promise<T>,
  { presentation = 'dialog', onAction }: CallPlatformOptions = {},
): Promise<T> {
  try {
    return await call(platformClient)
  } catch (error) {
    useErrorStore().show(toRefusal(error, presentation), onAction)
    throw error
  }
}
