import globals from 'globals'
import base from '@simpleerp/config/eslint'

export default [
  { ignores: ['dist/**', 'node_modules/**', 'e2e/**'] },
  ...base,
  {
    files: ['**/*.js', '**/*.ts'],
    languageOptions: { globals: { ...globals.node } },
  },
]
