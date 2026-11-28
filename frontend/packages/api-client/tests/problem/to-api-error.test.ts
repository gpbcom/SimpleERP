import { describe, expect, it } from 'vitest'

import { ApiProblemError } from '../../src/problem/api-problem-error'
import { ApiUnexpectedResponseError } from '../../src/problem/api-unexpected-response-error'
import { toApiError } from '../../src/problem/to-api-error'

const PROBLEM = 'application/problem+json'

const SECRET_BODY = {
  type: 'about:blank',
  title: 'errors.rights.title',
  status: 200,
  detail: 'password=hunter2',
  code: 'RIGHTS-DENIED-01',
  token: 'eyJ-secret',
  authorization: 'Bearer s3cr3t',
  stack: 'Error: boom at /srv/app/secret-path.py:12',
  instance: '/v1/x?api_key=k3y',
}

describe('toApiError', () => {
  it('maps a problem+json body with a code to an ApiProblemError carrying the code and the response status', () => {
    const error = toApiError(403, PROBLEM, { code: 'RIGHTS-DENIED-01', status: 200 })
    expect(error).toBeInstanceOf(ApiProblemError)
    expect(error).toMatchObject({ code: 'RIGHTS-DENIED-01', status: 403 })
  })

  it.each([
    'application/problem+json; charset=utf-8',
    'APPLICATION/PROBLEM+JSON',
    'Application/Problem+Json; Charset=UTF-8',
  ])('accepts the content type %s', (contentType) => {
    const error = toApiError(404, contentType, { code: 'NOT-FOUND-01' })
    expect(error).toBeInstanceOf(ApiProblemError)
    expect((error as ApiProblemError).code).toBe('NOT-FOUND-01')
  })

  it('trims the spaces around the code', () => {
    const error = toApiError(409, PROBLEM, { code: '  CONFLICT-01 \n' })
    expect((error as ApiProblemError).code).toBe('CONFLICT-01')
  })

  it.each([
    ['a missing code', {}],
    ['an empty code', { code: '' }],
    ['a blank code', { code: '   ' }],
    ['a numeric code', { code: 42 }],
    ['a null code', { code: null }],
    ['an object code', { code: { a: 1 } }],
    ['a string body', 'RIGHTS-DENIED-01'],
    ['an array body', [{ code: 'RIGHTS-DENIED-01' }]],
    ['a null body', null],
  ])('gives an ApiUnexpectedResponseError for %s', (_name, body) => {
    const error = toApiError(500, PROBLEM, body)
    expect(error).toBeInstanceOf(ApiUnexpectedResponseError)
    expect(error).toMatchObject({ status: 500 })
    expect(JSON.stringify(error)).toBe('{"status":500}')
  })

  it.each([['application/json'], ['text/html'], [null]])(
    'gives an ApiUnexpectedResponseError for the content type %s',
    (contentType) => {
      const error = toApiError(502, contentType, { code: 'RIGHTS-DENIED-01' })
      expect(error).toBeInstanceOf(ApiUnexpectedResponseError)
      expect(error.status).toBe(502)
      expect(error.message).not.toContain('RIGHTS-DENIED-01')
    },
  )

  describe('with a body that holds secrets', () => {
    const secrets = ['hunter2', 'eyJ-secret', 's3cr3t', 'k3y', 'secret-path', 'errors.rights.title']

    it.each(secrets)('keeps %s out of every view of a problem error', (secret) => {
      const error = toApiError(403, PROBLEM, SECRET_BODY)
      expect(JSON.stringify(error)).not.toContain(secret)
      expect(String(error)).not.toContain(secret)
      expect(error.message).not.toContain(secret)
      expect(Object.values(error).map(String).join(' ')).not.toContain(secret)
      expect(Object.keys(error).join(' ')).not.toContain(secret)
    })

    it.each(secrets)('keeps %s out of an unexpected response error', (secret) => {
      const error = toApiError(403, 'application/json', SECRET_BODY)
      expect(JSON.stringify(error)).not.toContain(secret)
      expect(String(error)).not.toContain(secret)
      expect(error.message).not.toContain(secret)
      expect(Object.values(error).map(String).join(' ')).not.toContain(secret)
      expect(Object.keys(error).join(' ')).not.toContain(secret)
    })

    it('holds only the code and the status as own fields', () => {
      const error = toApiError(403, PROBLEM, SECRET_BODY)
      expect(Object.keys(error).sort()).toEqual(['code', 'status'])
    })
  })
})
