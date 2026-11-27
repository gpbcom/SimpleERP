# Front end

The front ends: framework, design system in code, offline and mobile, accessibility, Playwright tests. Nothing of the
target is built yet.

## Today

No front end is built yet; `AGENT.md` leaves the framework to be decided.

## Target design (specified in GH-2, not built yet)

**Framework (D407).** Vue 3 with TypeScript and Vite, Pinia for state, a component library built on the design system's
tokens ([UX](../../specs/04-ux/README.md)).

**Front ends.** One back-office web app whose menus follow the modules switched on (F21) and the user's roles; the
customer and supplier portals and the public website (F18) as separate front ends; one installable mobile app for tills,
waiters, field workers, carers and drivers, offline-first (TC-06). Each has its own image and Playwright tests against
the real images (`AGENT.md`, TKT-21).

**Mobile.** A progressive web app first, wrapped in a native shell (for example Capacitor) only where hardware needs it:
card terminals, receipt printers, scales, barcode scanners.

**Extensions.** Plugins and generated features declare their screens with the design system's components (forms, tables,
dashboards), rendered by the app; custom widgets run in a sandboxed iframe; the assistant panel is part of the shell on
every screen.

Decided in [D407](../../specs/06-decisions/technical/d407-front-end.md).

Last reviewed: 2026-11-12 (GH-2)
