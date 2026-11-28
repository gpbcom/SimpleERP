import globals from "globals";
import base from "@simpleerp/config/eslint";

export default [
  { ignores: ["dist/**", "node_modules/**", "src/generated/**", "tests/fixtures/**"] },
  ...base,
  {
    files: ["**/*.js", "**/*.mjs", "**/*.ts"],
    languageOptions: { globals: { ...globals.node } },
  },
];
