import { ApiProblemError } from './api-problem-error'
import { ApiUnexpectedResponseError } from './api-unexpected-response-error'

/** The member of the problem+json body that holds the D122 support code (ProblemDetails.code of the platform). */
export const PROBLEM_CODE_MEMBER = 'code'

const PROBLEM_MEDIA_TYPE = 'application/problem+json'

/**
 * Map an error answer to a typed error, copying only the code and the status (nothing else of the body is kept).
 */
export function toApiError(
  status: number,
  contentType: string | null,
  body: unknown,
): ApiProblemError | ApiUnexpectedResponseError {
  const mediaType = (contentType ?? '').split(';')[0]?.trim().toLowerCase()
  if (mediaType === PROBLEM_MEDIA_TYPE && typeof body === 'object' && body !== null && !Array.isArray(body)) {
    const code = (body as Record<string, unknown>)[PROBLEM_CODE_MEMBER]
    if (typeof code === 'string' && code.trim() !== '') {
      return new ApiProblemError(code.trim(), status)
    }
  }
  return new ApiUnexpectedResponseError(status)
}
