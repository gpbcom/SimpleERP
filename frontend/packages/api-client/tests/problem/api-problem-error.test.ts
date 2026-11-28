import { describe, expect, it } from 'vitest'

import { ApiProblemError } from '../../src/problem/api-problem-error'
import { ApiUnexpectedResponseError } from '../../src/problem/api-unexpected-response-error'

describe('ApiProblemError and ApiUnexpectedResponseError', () => {
  it('makes an ApiProblemError an Error and an ApiProblemError', () => {
    const error = new ApiProblemError('RIGHTS-DENIED-01', 403)
    expect(error).toBeInstanceOf(Error)
    expect(error).toBeInstanceOf(ApiProblemError)
    expect(error.name).toBe('ApiProblemError')
  })

  it('makes an ApiUnexpectedResponseError an Error and an ApiUnexpectedResponseError', () => {
    const error = new ApiUnexpectedResponseError(502)
    expect(error).toBeInstanceOf(Error)
    expect(error).toBeInstanceOf(ApiUnexpectedResponseError)
    expect(error.name).toBe('ApiUnexpectedResponseError')
  })

  it('names the code and the status in the message of a problem error', () => {
    const error = new ApiProblemError('RIGHTS-DENIED-01', 403)
    expect(error.message).toContain('RIGHTS-DENIED-01')
    expect(error.message).toContain('403')
  })

  it('names only the status in the message of an unexpected response error', () => {
    const error = new ApiUnexpectedResponseError(502)
    expect(error.message).toContain('502')
  })

  it('keeps the code and the status of a problem error', () => {
    const error = new ApiProblemError('RIGHTS-DENIED-01', 403)
    expect(error.code).toBe('RIGHTS-DENIED-01')
    expect(error.status).toBe(403)
  })

  it('makes the fields read-only at the type level', () => {
    const problem = new ApiProblemError('RIGHTS-DENIED-01', 403)
    const unexpected = new ApiUnexpectedResponseError(502)
    // @ts-expect-error code is read-only
    problem.code = 'OTHER-01'
    // @ts-expect-error status is read-only
    problem.status = 500
    // @ts-expect-error status is read-only
    unexpected.status = 500
    expect(problem).toBeDefined()
  })
})
