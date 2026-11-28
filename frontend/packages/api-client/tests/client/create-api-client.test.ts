import { afterEach, beforeEach, describe, expect, it } from 'vitest';

import { ApiProblemError, ApiUnexpectedResponseError, createApiClient } from '../../src/index';
import { ProblemServer } from '../helpers/problem-server';

const HEALTH_PATH = '/v1/health';
const PROBLEM = 'application/problem+json';

describe('createApiClient', () => {
  let server: ProblemServer;

  beforeEach(async () => {
    server = await ProblemServer.start();
  });

  afterEach(async () => {
    await server.close();
  });

  it('resolves a 200 on the health path with the typed data', async () => {
    server.answerWith(200, 'application/json', JSON.stringify({ status: 'ok' }));
    const client = createApiClient({ baseUrl: server.url });

    const { data } = await client.GET(HEALTH_PATH);

    expect(data?.status).toBe('ok');
    expect(server.requests[0]).toMatchObject({ method: 'GET', path: HEALTH_PATH });
  });

  it('rejects a problem+json refusal with its code and the HTTP status', async () => {
    const body = { title: 'errors.title', status: 409, detail: 'errors.detail', code: 'SITE-CLOSE-01' };
    server.answerWith(409, PROBLEM, JSON.stringify(body));
    const client = createApiClient({ baseUrl: server.url });

    const error = await client.GET(HEALTH_PATH).catch((caught: unknown) => caught);

    expect(error).toBeInstanceOf(ApiProblemError);
    expect(error).toMatchObject({ code: 'SITE-CLOSE-01', status: 409 });
  });

  it('rejects a 500 html page with an unexpected response error', async () => {
    server.answerWith(500, 'text/html', '<html>boom</html>');
    const client = createApiClient({ baseUrl: server.url });

    const error = await client.GET(HEALTH_PATH).catch((caught: unknown) => caught);

    expect(error).toBeInstanceOf(ApiUnexpectedResponseError);
    expect(error).toMatchObject({ status: 500 });
  });

  it('sends the given headers to the server', async () => {
    server.answerWith(200, 'application/json', JSON.stringify({ status: 'ok' }));
    const client = createApiClient({ baseUrl: server.url, headers: { 'X-Company-Id': 'c-42' } });

    await client.GET(HEALTH_PATH);

    expect(server.requests[0]?.headers['x-company-id']).toBe('c-42');
  });

  describe('when a call with a bearer token is refused', () => {
    const secrets = ['Bearer s3cr3t-token', 's3cr3t-token', 'password=hunter2', 'eyJ-secret', '/v1/x?api_key=k3y'];

    async function refusedError(): Promise<Error> {
      const body = {
        title: 'errors.title',
        status: 403,
        detail: 'password=hunter2',
        code: 'AUTH-DENIED-01',
        token: 'eyJ-secret',
        instance: '/v1/x?api_key=k3y',
      };
      server.answerWith(403, PROBLEM, JSON.stringify(body));
      const client = createApiClient({
        baseUrl: server.url,
        headers: { Authorization: 'Bearer s3cr3t-token' },
      });
      const error = await client.GET(HEALTH_PATH).catch((caught: unknown) => caught);
      expect(error).toBeInstanceOf(ApiProblemError);
      return error as Error;
    }

    it.each(secrets)('keeps %s out of the error in every form', async (secret) => {
      const error = await refusedError();

      expect(server.requests[0]?.headers.authorization).toBe('Bearer s3cr3t-token');
      expect(JSON.stringify(error)).not.toContain(secret);
      expect(String(error)).not.toContain(secret);
      expect(error.message).not.toContain(secret);
      expect(JSON.stringify(Object.values(error))).not.toContain(secret);
    });
  });
});
