import { describe, expect, it } from "vitest";

import { contrastRatio, relativeLuminance } from "../../src/contrast/contrast-ratio";

describe("contrastRatio", () => {
  it("is 21 for black on white", () => {
    expect(contrastRatio("#000000", "#FFFFFF")).toBeCloseTo(21, 2);
  });

  it("is 1 for white on white", () => {
    expect(contrastRatio("#FFFFFF", "#FFFFFF")).toBeCloseTo(1, 2);
  });

  it("is symmetric", () => {
    expect(contrastRatio("#4B4FC9", "#FFFFFF")).toBeCloseTo(contrastRatio("#FFFFFF", "#4B4FC9"), 10);
  });

  it("gives a luminance of 1 for white and 0 for black", () => {
    expect(relativeLuminance("#FFFFFF")).toBeCloseTo(1, 5);
    expect(relativeLuminance("#000000")).toBeCloseTo(0, 5);
  });

  it("gives the 6.44:1 of the Colours page for the primary on white", () => {
    const ratio = contrastRatio("#4B4FC9", "#FFFFFF");
    expect(ratio).toBeGreaterThan(6.4);
    expect(ratio).toBeLessThan(6.5);
  });

  it("gives the same ratio for lower-case hex", () => {
    expect(contrastRatio("#4b4fc9", "#ffffff")).toBeCloseTo(contrastRatio("#4B4FC9", "#FFFFFF"), 10);
  });

  it.each([["#FFF"], ["4B4FC9"], ["#GGGGGG"], [""]])("throws on the invalid colour %j", (value) => {
    expect(() => contrastRatio(value, "#FFFFFF")).toThrow(Error);
    expect(() => relativeLuminance(value)).toThrow(Error);
  });
});
