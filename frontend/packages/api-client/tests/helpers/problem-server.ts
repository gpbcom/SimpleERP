import { createServer, type IncomingHttpHeaders, type Server } from 'node:http';
import type { AddressInfo } from 'node:net';

export interface RecordedRequest {
  method: string;
  path: string;
  headers: IncomingHttpHeaders;
}

export interface Reply {
  status: number;
  contentType: string;
  body: string;
}

export class ProblemServer {
  readonly requests: RecordedRequest[] = [];
  readonly url: string;
  private reply: Reply = { status: 200, contentType: 'application/json', body: '{}' };
  private readonly server: Server;

  private constructor(server: Server, url: string) {
    this.server = server;
    this.url = url;
  }

  static async start(): Promise<ProblemServer> {
    const holder: { current?: ProblemServer } = {};
    const server = createServer((request, response) => {
      holder.current?.requests.push({
        method: request.method ?? '',
        path: request.url ?? '',
        headers: request.headers,
      });
      const reply = holder.current?.reply ?? { status: 500, contentType: 'text/plain', body: '' };
      response.writeHead(reply.status, { 'content-type': reply.contentType });
      response.end(reply.body);
    });
    await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve));
    const { port } = server.address() as AddressInfo;
    const instance = new ProblemServer(server, `http://127.0.0.1:${port}`);
    holder.current = instance;
    return instance;
  }

  answerWith(status: number, contentType: string, body: string): void {
    this.reply = { status, contentType, body };
  }

  async close(): Promise<void> {
    this.server.closeAllConnections();
    await new Promise<void>((resolve, reject) => {
      this.server.close((error) => (error ? reject(error) : resolve()));
    });
  }
}
