/** A problem+json answer of the API, reduced to its D122 support code and its HTTP status. */
export class ApiProblemError extends Error {
  readonly code: string
  readonly status: number

  constructor(code: string, status: number) {
    super(`The API answered with the problem ${code} (HTTP ${status}).`)
    Object.defineProperty(this, 'name', { value: 'ApiProblemError', enumerable: false })
    this.code = code
    this.status = status
  }
}
