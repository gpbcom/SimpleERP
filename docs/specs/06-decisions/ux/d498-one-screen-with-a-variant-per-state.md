🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D498 One screen with a variant per state

# 📜 D498 One screen with a variant per state

**Status:** 🔄 draft (GH-2 step S7, from VD-15 / D498)

## Context

How a screen shows each state of the entities it shows.

## Options

- One screen with a variant per state.
- One page per state.
- Variants with images for the key states only.

## Choice

One screen with a variant per state: each screen page has a "States" table, one row per state of each entity it shows in
that flow, with its images per persona, device and theme.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 15).

## Consequences

- The [screen template](../../_templates/screen.md) gains the entity states in its "States" section; it extends the six
  screen states of GH-2's step 36a instead of adding a second section.
- About 51,500 state images by the estimate of 2026-11-12 (1,229 flow-entity pairs × 3.2 states × 3.1 personas × 4).
- A state the user never sees says so and gets no image.

## Related

- [Screen template](../../_templates/screen.md)
- [D497 Every entity draws its states](../foundations/d497-every-entity-draws-its-states.md)
- [D490 Example images for every persona that can open a
  view](d490-example-images-for-every-persona-that-can-open-a-view.md)
- [D500 Images live in the specs folders](d500-images-live-in-the-specs-folders.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D497 Every entity draws its states](../foundations/d497-every-entity-draws-its-states.md) · ⬆️ [Up](README.md) ·
➡️ [D499](../foundations/d499-the-work-is-carried-out-as-gh-2-steps-36c-to-36l.md)
