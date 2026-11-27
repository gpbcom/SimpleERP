🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D500 Images live in the specs folders

# 📜 D500 Images live in the specs folders

**Status:** 🔄 draft (GH-2 step S8, from VD-17 / D500)

## Context

The images of [D490](d490-example-images-for-every-persona-that-can-open-a-view.md) and
[D498](d498-one-screen-with-a-variant-per-state.md) add about 58,700 images, about 2.5 GB, to 5,434 images (233 MB)
today; the repository's history already weighs 865 MB.

## Options

- A. Git LFS for the images of the specs: they stay next to their pages; LFS quotas apply.
- B. Sources versioned, images built by the CI and published.
- C. Images in the private tickets repository.
- D. Fewer images.

## Choice

The images go in the specs folders: every image sits next to its page in `docs/specs`, as today.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 17 (follow-up)).

## Consequences

- (Proposed) Whether Git LFS is used stays an implementation choice of GH-2, put to the owner in step S8 of the
  [plan](../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md).
- The free disk is checked before each rendering batch.

## Related

- [D120 PNG mockups](d120-png-mockups.md)
- [D490 Example images for every persona that can open a
  view](d490-example-images-for-every-persona-that-can-open-a-view.md)
- [D498 One screen with a variant per state](d498-one-screen-with-a-variant-per-state.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D499](../foundations/d499-the-work-is-carried-out-as-gh-2-steps-36c-to-36l.md) · ⬆️ [Up](README.md) ·
➡️ [D501](d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md)
