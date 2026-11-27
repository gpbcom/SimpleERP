import { describe, expect, it } from 'vitest'

import { formatNumber } from '../../src/format/formatNumber'

function plain(text: string): string {
  return text.replace(/[\u202f\u00a0]/g, ' ')
}

describe('formatNumber', () => {
  it('groups thousands with a space and uses a decimal comma in French', () => {
    expect(plain(formatNumber(1234.5, 'fr-FR'))).toBe('1 234,5')
  })

  it('groups thousands with a comma and uses a decimal point in British English', () => {
    expect(plain(formatNumber(1234.5, 'en-GB'))).toBe('1,234.5')
  })

  it('keeps a long decimal string exact', () => {
    expect(
      plain(formatNumber('12345678901234567890.12', 'en-GB', { maximumFractionDigits: 2 })),
    ).toBe('12,345,678,901,234,567,890.12')
  })

  it('honours the percent style in British English', () => {
    expect(plain(formatNumber(0.25, 'en-GB', { style: 'percent' }))).toBe('25%')
  })

  it('honours the percent style in French', () => {
    expect(plain(formatNumber(0.25, 'fr-FR', { style: 'percent' }))).toBe('25 %')
  })

  it.each([
    ['a malformed string', 'abc'],
    ['not a number', Number.NaN],
    ['infinity', Number.POSITIVE_INFINITY],
  ])('refuses %s with a RangeError', (_name, value) => {
    expect(() => formatNumber(value, 'en-GB')).toThrow(RangeError)
  })
})
