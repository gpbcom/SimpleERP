/** An error answer that is not a usable problem+json, reduced to its HTTP status. */
export class ApiUnexpectedResponseError extends Error {
  readonly status: number

  constructor(status: number) {
    super(`The API answered with an unexpected response (HTTP ${status}).`)
    Object.defineProperty(this, 'name', { value: 'ApiUnexpectedResponseError', enumerable: false })
    this.status = status
  }
}
