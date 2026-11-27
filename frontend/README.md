# Front ends

This folder holds the SimpleERP front ends: Vue 3 with TypeScript, Vite and Pinia, in one pnpm workspace, each app with
exactly one image.

- `backoffice/`: the back-office web app.
- `portals/<portal>/`: the customer and supplier portals, each added by a later ticket.
- `mobile/`: the offline-first mobile app, a progressive web app.
- `packages/`: the shared TypeScript packages (design tokens, components, API client).

Each app keeps its Playwright tests in its own `e2e/` folder. They run against the real images started by
`compose.e2e.yaml`, never a development server.

See [D438, the repository layout](../docs/specs/06-decisions/technical/d438-repository-layout.md) and
[the repository layout design page](../docs/technical/architecture/repository-layout.md).
