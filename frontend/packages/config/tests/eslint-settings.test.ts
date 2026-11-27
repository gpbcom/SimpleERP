import { fileURLToPath } from "node:url";
import { ESLint } from "eslint";
import { describe, expect, it } from "vitest";

const fixture = fileURLToPath(new URL("./fixtures/eslint-front-end", import.meta.url));

async function errorsOf(file: string): Promise<string[]> {
  const eslint = new ESLint({ cwd: fixture });
  const results = await eslint.lintFiles([file]);
  return results
    .flatMap((result) => result.messages)
    .filter((message) => message.severity === 2)
    .map((message) => message.ruleId ?? "parse-error");
}

describe("the shared ESLint settings applied to a front end", () => {
  it.each(["src/clean.ts", "src/Clean.vue"])("%s has no error", async (file) => {
    expect(await errorsOf(file)).toEqual([]);
  });

  it("flags an explicit any in a TypeScript file", async () => {
    expect(await errorsOf("src/broken.ts")).toEqual(["@typescript-eslint/no-explicit-any"]);
  });

  it("flags v-if with v-for on one element of a Vue file", async () => {
    expect(await errorsOf("src/Broken.vue")).toContain("vue/no-use-v-if-with-v-for");
  });
});
