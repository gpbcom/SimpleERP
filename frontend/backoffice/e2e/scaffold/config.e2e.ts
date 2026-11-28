import { dirname, resolve } from 'node:path'

import { test, expect } from '../fixtures/test'

const EXPECTED_VIEWPORT = { width: 1440, height: 900 }
const EXPECTED_PROJECTS = ['light-en', 'dark-en', 'light-fr', 'dark-fr']

test.describe('the scaffold configuration contract', () => {
  test('a failure keeps its trace, its video and its screenshot', { tag: '@smoke' }, () => {
    const use = test.info().project.use
    expect(use.trace).toBe('retain-on-failure')
    expect(use.video).toBe('retain-on-failure')
    expect(use.screenshot).toBe('only-on-failure')
  })

  test('no development server is started', { tag: '@smoke' }, () => {
    expect(test.info().config.webServer).toBeNull()
  })

  test('the html report goes to the playwright-report folder and never opens', { tag: '@smoke' }, () => {
    const html = test.info().config.reporter.find(([name]) => name === 'html')
    expect(html).toBeDefined()
    const options = html?.[1] as { outputFolder?: string; open?: string } | undefined
    expect(options?.outputFolder).toBeDefined()
    const configFolder = dirname(test.info().config.configFile ?? '')
    const folder = resolve(configFolder, options?.outputFolder ?? '')
    expect(folder.replace(/\\/g, '/')).toMatch(/frontend\/backoffice\/playwright-report$/)
    expect(options?.open).toBe('never')
  })

  test('the results go to the test-results folder', { tag: '@smoke' }, () => {
    expect(test.info().project.outputDir.replace(/\\/g, '/')).toMatch(/frontend\/backoffice\/test-results$/)
  })

  test('the projects are the four themes and languages', { tag: '@smoke' }, () => {
    const names = test.info().config.projects.map((project) => project.name)
    expect(names).toEqual(EXPECTED_PROJECTS)
  })

  test('the current project matches its colour scheme, locale and viewport', { tag: '@smoke' }, () => {
    const { name, use } = test.info().project
    const [scheme, language] = name.split('-')
    expect(use.colorScheme).toBe(scheme)
    expect(use.locale).toBe(language === 'fr' ? 'fr-FR' : 'en-GB')
    expect(use.viewport).toEqual(EXPECTED_VIEWPORT)
  })

  test('the base URL is the one of the running images', { tag: '@smoke' }, () => {
    const baseUrl = process.env.ERP_E2E_BASE_URL
    test.skip(baseUrl === undefined || baseUrl === '', 'ERP_E2E_BASE_URL is not set.')
    expect(test.info().project.use.baseURL).toBe(baseUrl)
  })
})
