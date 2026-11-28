import { defineConfig } from '@playwright/test'

const VIEWPORT = { width: 1440, height: 900 }

export default defineConfig({
  testDir: '.',
  testMatch: '**/*.e2e.ts',
  outputDir: '../test-results',
  forbidOnly: Boolean(process.env.CI),
  reporter: [['list'], ['html', { outputFolder: '../playwright-report', open: 'never' }]],
  use: {
    baseURL: process.env.ERP_E2E_BASE_URL ?? 'http://localhost:8080',
    trace: 'retain-on-failure',
    video: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'light-en', use: { browserName: 'chromium', viewport: VIEWPORT, colorScheme: 'light', locale: 'en-GB' } },
    { name: 'dark-en', use: { browserName: 'chromium', viewport: VIEWPORT, colorScheme: 'dark', locale: 'en-GB' } },
    { name: 'light-fr', use: { browserName: 'chromium', viewport: VIEWPORT, colorScheme: 'light', locale: 'fr-FR' } },
    { name: 'dark-fr', use: { browserName: 'chromium', viewport: VIEWPORT, colorScheme: 'dark', locale: 'fr-FR' } },
  ],
})
