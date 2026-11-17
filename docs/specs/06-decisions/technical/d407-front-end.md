🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) › 📜 D407 Front end

# 📜 D407 Front end

**Status:** ✅ decided

## Context

Step 19w of the technical interview (PLAN D35).

## Options

- Vue 3, React or Svelte.
- One app with portals and a mobile app, or micro-front ends.
- PWA first or native apps.
- Declared plugin screens or plugin bundles.

## Choice

Confirmed by the owner on 2026-11-12: Vue 3 with TypeScript; one back-office web app, separate portals and website, one
offline-first mobile app; PWA first with a native shell where hardware needs it; plugin screens declared and rendered by
the app, custom widgets sandboxed.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The front-end chapter's target design.

## Related

- [Front end](../../../technical/architecture/frontend.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D406 Back end](d406-back-end.md) · ⬆️ [Up](README.md) ·
➡️ [D408 Performance targets and resource profiles](d408-performance-and-profiles.md)
