import globals from 'globals'
import base from '@simpleerp/config/eslint'

export default [
  { ignores: ['dist/**', 'node_modules/**'] },
  ...base,
  {
    files: ['**/*.js', '**/*.ts'],
    languageOptions: { globals: { ...globals.node } },
  },
]
