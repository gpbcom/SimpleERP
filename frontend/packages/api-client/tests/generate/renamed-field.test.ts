import { spawnSync } from 'node:child_process'
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

import { afterAll, describe, expect, it } from 'vitest'

const here = dirname(fileURLToPath(import.meta.url))
const packageRoot = resolve(here, '../..')
const fixtures = join(packageRoot, 'tests', 'fixtures', 'renamed')
const tsc = join(packageRoot, 'node_modules', 'typescript', 'bin', 'tsc')

const folders: string[] = []

function compile(fixture: string, property: string): { status: number | null; output: string } {
  const folder = mkdtempSync(join(tmpdir(), 'api-client-renamed-'))
  folders.push(folder)
  const generated = spawnSync(
    'node',
    [
      join(packageRoot, 'scripts', 'generate.mjs'),
      '--input',
      join(fixtures, fixture),
      '--output',
      join(folder, 'schema.ts'),
    ],
    { cwd: packageRoot, encoding: 'utf8' },
  )
  expect(generated.status, generated.stdout + generated.stderr).toBe(0)
  writeFileSync(
    join(folder, 'caller.ts'),
    [
      "import type { paths } from './schema'",
      '',
      "type Item = paths['/v1/items/{id}']['get']['responses'][200]['content']['application/json']",
      '',
      'export function read(item: Item): string {',
      `  return item.${property}`,
      '}',
      '',
    ].join('\n'),
  )
  writeFileSync(
    join(folder, 'tsconfig.json'),
    JSON.stringify({
      compilerOptions: {
        strict: true,
        noEmit: true,
        module: 'NodeNext',
        moduleResolution: 'NodeNext',
        target: 'ES2022',
        skipLibCheck: true,
      },
      files: ['caller.ts'],
    }),
  )
  const result = spawnSync('node', [tsc, '-p', folder], { encoding: 'utf8' })
  return { status: result.status, output: result.stdout + result.stderr }
}

afterAll(() => {
  for (const folder of folders) rmSync(folder, { recursive: true, force: true })
})

describe('a renamed field in the OpenAPI document', () => {
  it.each([
    ['a caller using displayName compiles against the before schema', 'openapi-before.json', 'displayName'],
    ['a caller using label compiles against the after schema', 'openapi-after.json', 'label'],
  ])('%s', { timeout: 60_000 }, (_name, fixture, property) => {
    const result = compile(fixture, property)
    expect(result.status, result.output).toBe(0)
  })

  it('fails the type check of a caller still using the old name', { timeout: 60_000 }, () => {
    const result = compile('openapi-after.json', 'displayName')
    expect(result.status).not.toBe(0)
    expect(result.output).toContain('displayName')
  })
})
