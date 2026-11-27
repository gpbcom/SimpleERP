import globals from "globals";
import base from "./eslint.base.js";

export default [
  { ignores: ["tests/fixtures/**", "node_modules/**"] },
  ...base,
  {
    files: ["**/*.js", "**/*.ts"],
    languageOptions: { globals: { ...globals.node } },
  },
];
