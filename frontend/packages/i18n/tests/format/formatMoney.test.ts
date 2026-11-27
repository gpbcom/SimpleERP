import { describe, expect, it } from "vitest";
import { formatMoney } from "../../src/format/formatMoney";

function plain(text: string): string {
  return text.replace(/[\u00a0\u202f]/g, " ");
}

describe("formatMoney", () => {
  it("keeps every digit of a large amount in French", () => {
    expect(plain(formatMoney("1234567890123456.78", "EUR", "fr-FR"))).toBe("1 234 567 890 123 456,78 €");
  });

  it("keeps every digit of a large amount in British English", () => {
    expect(formatMoney("1234567890123456.78", "EUR", "en-GB")).toBe("€1,234,567,890,123,456.78");
  });

  it("keeps a trailing zero of the amount", () => {
    expect(formatMoney("0.30", "EUR", "en-GB")).toBe("€0.30");
  });

  it("pads the amount up to the minor digits of the currency", () => {
    expect(formatMoney("0.1", "EUR", "en-GB")).toBe("€0.10");
  });

  it("keeps decimals beyond the minor digits without rounding", () => {
    expect(formatMoney("12.345", "EUR", "en-GB")).toBe("€12.345");
  });

  it("shows a negative amount with its minus sign and its decimals", () => {
    const text = plain(formatMoney("-5.50", "EUR", "fr-FR"));
    expect(text).toContain("5,50");
    expect(text).toMatch(/[-−]/);
  });

  it("uses the decimal separator of each locale", () => {
    const french = formatMoney("1.5", "EUR", "fr-FR");
    const british = formatMoney("1.5", "EUR", "en-GB");
    expect(french).not.toBe(british);
    expect(french).toContain("1,50");
    expect(british).toContain("1.50");
  });

  it.each(["1,5", "abc", "", "1e3"])("refuses the malformed amount %j", (amount) => {
    expect(() => formatMoney(amount, "EUR", "en-GB")).toThrow(RangeError);
  });

  it.each(["eur", "EURO"])("refuses the malformed currency %j", (currency) => {
    expect(() => formatMoney("1.00", currency, "en-GB")).toThrow(RangeError);
  });
});
