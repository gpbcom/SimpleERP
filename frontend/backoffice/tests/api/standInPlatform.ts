import { createServer, type Server } from 'node:http'
import type { AddressInfo } from 'node:net'

/** A real local HTTP server that answers like the platform service: its health path, and a D122 refusal on demand. */
export class StandInPlatform {
  static readonly HEALTH_PATH = '/v1/health'

  readonly paths: string[] = []
  readonly url: string
  private refusal: { status: number; code: string } | null = null
  private readonly server: Server

  private constructor(server: Server, url: string) {
    this.server = server
    this.url = url
  }

  static async start(): Promise<StandInPlatform> {
    const holder: { current?: StandInPlatform } = {}
    const server = createServer((request, response) => {
      const self = holder.current
      self?.paths.push(request.url ?? '')
      const refusal = self?.refusal ?? null
      if (refusal === null) {
        response.writeHead(200, { 'content-type': 'application/json' })
        response.end(JSON.stringify({ status: 'ok' }))
        return
      }
      response.writeHead(refusal.status, { 'content-type': 'application/problem+json' })
      response.end(
        JSON.stringify({
          title: 'errors.title',
          status: refusal.status,
          detail: 'errors.detail',
          code: refusal.code,
        }),
      )
    })
    await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve))
    const { port } = server.address() as AddressInfo
    const instance = new StandInPlatform(server, `http://127.0.0.1:${port}`)
    holder.current = instance
    return instance
  }

  refuseWith(status: number, code: string): void {
    this.refusal = { status, code }
  }

  heal(): void {
    this.refusal = null
  }

  async close(): Promise<void> {
    this.server.closeAllConnections()
    await new Promise<void>((resolve, reject) => {
      this.server.close((error) => (error ? reject(error) : resolve()))
    })
  }
}
