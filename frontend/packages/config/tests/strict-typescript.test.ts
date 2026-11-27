import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";
import ts from "typescript";

const fixture = fileURLToPath(new URL("./fixtures/strict-front-end/", import.meta.url));
const configPath = `${fixture}tsconfig.json`;

function load(): ts.ParsedCommandLine {
  const read = ts.readConfigFile(configPath, ts.sys.readFile);
  expect(read.error).toBeUndefined();
  return ts.parseJsonConfigFileContent(read.config, ts.sys, fixture);
}

describe("the shared strict TypeScript settings applied to a front end", () => {
  const parsed = load();
  const program = ts.createProgram(parsed.fileNames, parsed.options);
  const diagnostics = ts.getPreEmitDiagnostics(program);
  const codesOf = (file: string): number[] =>
    diagnostics.filter((d) => d.file?.fileName.endsWith(`/src/${file}`)).map((d) => d.code);

  it("turns strict on in the options the front end resolves", () => {
    expect(parsed.options.strict).toBe(true);
  });

  it("reports nothing for strict-clean code", () => {
    expect(codesOf("clean.ts")).toEqual([]);
  });

  it("reports the implicit any and the null assigned to a string", () => {
    const codes = codesOf("broken.ts");
    expect(codes).toContain(7006);
    expect(codes).toContain(2322);
  });
});
