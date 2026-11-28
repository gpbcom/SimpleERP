import createClient, { type Client, type Middleware } from 'openapi-fetch'

import type { paths } from '../generated/platform'
import { toApiError } from '../problem/to-api-error'

const PROBLEM_MEDIA_TYPE = 'application/problem+json'

/** The options of the typed client of the platform API. */
export interface ApiClientOptions {
  /** The root of the API, without the `/v1` prefix that the paths carry. */
  baseUrl: string
  /** Headers sent with every call, such as the company or the authorisation. */
  headers?: HeadersInit
  /** The fetch to use, the global one by default. */
  fetch?: typeof fetch
}

/** The typed client of the platform API. */
export type PlatformClient = Client<paths>

async function readProblemBody(response: Response, contentType: string | null): Promise<unknown> {
  const mediaType = (contentType ?? '').split(';')[0]?.trim().toLowerCase()
  if (mediaType !== PROBLEM_MEDIA_TYPE) {
    return undefined
  }
  try {
    return await response.json()
  } catch {
    return undefined
  }
}

const rejectNonSuccess: Middleware = {
  async onResponse({ response }) {
    if (response.ok) {
      return undefined
    }
    const contentType = response.headers.get('content-type')
    const body = await readProblemBody(response, contentType)
    throw toApiError(response.status, contentType, body)
  },
}

/**
 * Create the typed client of the platform API: every non-2xx answer rejects with an `ApiProblemError` or an
 * `ApiUnexpectedResponseError`, built from the status, the content type and the problem body only.
 */
export function createApiClient(options: ApiClientOptions): PlatformClient {
  const client = createClient<paths>({
    baseUrl: options.baseUrl,
    headers: options.headers,
    fetch: options.fetch,
  })
  client.use(rejectNonSuccess)
  return client
}
