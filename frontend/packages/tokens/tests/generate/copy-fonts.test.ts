import { mkdtempSync, readFileSync, readdirSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { copyFonts } from "../../src/generate/copy-fonts";
import { FontFileMissingError } from "../../src/generate/font-file-missing-error";
import type { TokenSource } from "../../src/source/token-source";

const source = JSON.parse(
  readFileSync(new URL("../../src/source/tokens.json", import.meta.url), "utf-8"),
) as TokenSource;

describe("copyFonts", () => {
  let outDir = "";

  beforeEach(() => {
    outDir = mkdtempSync(join(tmpdir(), "tokens-fonts-"));
  });

  afterEach(() => {
    rmSync(outDir, { recursive: true, force: true });
  });

  it("writes the seven font files and three licences", () => {
    copyFonts(source, outDir);
    const names = readdirSync(join(outDir, "fonts"));
    expect(names.filter((name) => name.endsWith(".woff2"))).toHaveLength(7);
    expect(names.filter((name) => name.startsWith("LICENSE-")).sort()).toEqual([
      "LICENSE-inter",
      "LICENSE-jetbrains-mono",
      "LICENSE-plus-jakarta-sans",
    ]);
  });

  it("copies real woff2 files", () => {
    copyFonts(source, outDir);
    for (const font of source.fonts) {
      const bytes = readFileSync(join(outDir, "fonts", font.file));
      expect(bytes.length).toBeGreaterThan(0);
      expect(bytes.subarray(0, 4).toString("latin1")).toBe("wOF2");
    }
  });

  it("copies the open font licence of every package", () => {
    const written = copyFonts(source, outDir);
    const licences = written.filter((path) => /LICENSE-/.test(path));
    expect(licences).toHaveLength(3);
    for (const path of licences) {
      expect(readFileSync(path, "utf-8").toLowerCase()).toContain("sil open font license");
    }
  });

  it("returns exactly the files it wrote", () => {
    const written = copyFonts(source, outDir);
    const onDisk = readdirSync(join(outDir, "fonts")).map((name) => join(outDir, "fonts", name));
    expect([...written].sort()).toEqual(onDisk.sort());
  });

  it("refuses a font file the package does not hold", () => {
    const broken: TokenSource = {
      ...source,
      fonts: [{ ...source.fonts[0], file: "inter-latin-999-normal.woff2" }],
    };
    let caught: unknown;
    try {
      copyFonts(broken, outDir);
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(FontFileMissingError);
    expect((caught as FontFileMissingError).file).toBe("inter-latin-999-normal.woff2");
  });

  it("can run twice into the same folder", () => {
    copyFonts(source, outDir);
    expect(() => copyFonts(source, outDir)).not.toThrow();
  });
});
