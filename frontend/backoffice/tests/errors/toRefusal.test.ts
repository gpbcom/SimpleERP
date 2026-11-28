import { describe, expect, it } from 'vitest';

import { ApiProblemError, ApiUnexpectedResponseError } from '@simpleerp/api-client';
import { resolveErrorCode } from '@simpleerp/i18n';

import { toRefusal } from '../../src/errors/toRefusal';

const KNOWN_CODE = 'INVALID-INPUT-01';
const UNKNOWN_CODE = 'NOT-IN-THE-CATALOGUE-99';

/** The T0.20 typed error carries the code and the status only, so the field and the values are set on a real instance. */
function problemWith(code: string, extra: Record<string, unknown>): ApiProblemError {
  return Object.assign(new ApiProblemError(code, 422), extra);
}

describe('toRefusal', () => {
  it('gives the three keys and the support reference of a known code', () => {
    const entry = resolveErrorCode(KNOWN_CODE);
    const refusal = toRefusal(new ApiProblemError(KNOWN_CODE, 400), 'dialog');

    expect(refusal.code).toBe(KNOWN_CODE);
    expect(refusal.titleKey).toBe(entry.titleKey);
    expect(refusal.whyKey).toBe(entry.whyKey);
    expect(refusal.actionKey).toBe(entry.actionKey);
    expect(refusal.reference).toBe(entry.reference);
    expect(refusal.reference).not.toBeNull();
    expect(refusal.field).toBeNull();
  });

  it.each(['dialog', 'banner'] as const)('keeps the %s presentation that was asked', (presentation) => {
    expect(toRefusal(new ApiProblemError(KNOWN_CODE, 400), presentation).presentation).toBe(presentation);
  });

  it('gives the fallback keys and the code as the reference for an unknown code', () => {
    const fallback = resolveErrorCode(UNKNOWN_CODE);
    const refusal = toRefusal(new ApiProblemError(UNKNOWN_CODE, 500), 'dialog');

    expect(refusal.titleKey).toBe(fallback.titleKey);
    expect(refusal.whyKey).toBe(fallback.whyKey);
    expect(refusal.actionKey).toBe(fallback.actionKey);
    expect(refusal.code).toBe(UNKNOWN_CODE);
    expect(refusal.reference).toBe(UNKNOWN_CODE);
  });

  it.each([
    ['a network failure', new TypeError('Failed to fetch')],
    ['an answer that is not a problem+json', new ApiUnexpectedResponseError(502)],
    ['a value that is not an error', 'boom'],
  ])('gives the fallback keys and no reference for %s', (_label, error) => {
    const fallback = resolveErrorCode(null);
    const refusal = toRefusal(error, 'banner');

    expect(refusal.titleKey).toBe(fallback.titleKey);
    expect(refusal.whyKey).toBe(fallback.whyKey);
    expect(refusal.actionKey).toBe(fallback.actionKey);
    expect(refusal.code).toBeNull();
    expect(refusal.reference).toBeNull();
    expect(refusal.field).toBeNull();
  });

  it.each(['dialog', 'banner'] as const)('shows an error naming a field next to it, whatever %s was asked', (asked) => {
    const refusal = toRefusal(problemWith(KNOWN_CODE, { field: 'email' }), asked);

    expect(refusal.presentation).toBe('field');
    expect(refusal.field).toBe('email');
  });

  it('turns the values of the body into string params', () => {
    const refusal = toRefusal(problemWith(KNOWN_CODE, { values: { max: 12, name: 'Acme', strict: true } }), 'dialog');

    expect(refusal.params).toEqual({ max: '12', name: 'Acme', strict: 'true' });
  });

  it('gives no params when the body carries no values', () => {
    expect(toRefusal(new ApiProblemError(KNOWN_CODE, 400), 'dialog').params).toEqual({});
  });

  it('gives each refusal its own id', () => {
    const first = toRefusal(new ApiProblemError(KNOWN_CODE, 400), 'dialog');
    const second = toRefusal(new ApiProblemError(KNOWN_CODE, 400), 'dialog');

    expect(first.id).not.toBe('');
    expect(first.id).not.toBe(second.id);
  });

  it('holds no raw body, detail text or stack trace', () => {
    const error = problemWith(KNOWN_CODE, {
      detail: 'secret detail for jane@example.com',
      body: { token: 'secret-token' },
      values: { max: 3 },
    });
    const refusal = toRefusal(error, 'dialog');
    const text = JSON.stringify(refusal);

    expect(text).not.toContain('secret detail');
    expect(text).not.toContain('secret-token');
    expect(text).not.toContain('jane@example.com');
    expect(text).not.toContain('stack');
    expect(text).not.toContain(' at ');
    expect(Object.keys(refusal).sort()).toEqual(
      ['actionKey', 'code', 'field', 'id', 'params', 'presentation', 'reference', 'titleKey', 'whyKey'].sort(),
    );
  });
});
