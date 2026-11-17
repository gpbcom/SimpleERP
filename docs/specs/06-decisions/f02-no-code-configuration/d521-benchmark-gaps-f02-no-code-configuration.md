🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D521 Benchmark gaps of F2 No-code configuration

# 📜 D521 Benchmark gaps of F2 No-code configuration

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with the configuration tools of the benchmarked
suites and offered each gap as an option
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F2 No-code configuration").

## Options

- Take each gap as a use case of F2 in a new flow, or leave it out.
- For the data cleaning (G12), keep it in F2 with the other tools that act on many records.

## Choice

The owner selected all five gaps; each becomes a use case of F2, drawn in
[FL-F2-13 Low code, bulk work and data cleaning](../../02-functional/f02-no-code-configuration/flows/fl-f02-13-low-code-bulk-and-cleaning.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G31 | [UC-F2-31 Add a low-code script step](../../02-functional/f02-no-code-configuration/use-cases/13-low-code-bulk-and-cleaning/uc-f02-31-add-a-low-code-script-step.md) | "Low-code script step" |
| G32 | [UC-F2-32 Edit records in bulk](../../02-functional/f02-no-code-configuration/use-cases/13-low-code-bulk-and-cleaning/uc-f02-32-edit-records-in-bulk.md) | "Bulk edit and mass actions" |
| G33 | [UC-F2-33 Set a time-based rule](../../02-functional/f02-no-code-configuration/use-cases/13-low-code-bulk-and-cleaning/uc-f02-33-set-a-time-based-rule.md) | "Time-based rules" |
| G34 | [UC-F2-34 Translate the screens in place](../../02-functional/f02-no-code-configuration/use-cases/13-low-code-bulk-and-cleaning/uc-f02-34-translate-the-screens-in-place.md) | "In-place translation" |
| G12 | [UC-F2-35 Clean duplicates and stale records](../../02-functional/f02-no-code-configuration/use-cases/13-low-code-bulk-and-cleaning/uc-f02-35-clean-duplicates-and-stale-records.md) | "Data cleaning" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "Block by block").

## Consequences

- Use cases
  [UC-F2-31 Add a low-code script step](../../02-functional/f02-no-code-configuration/use-cases/13-low-code-bulk-and-cleaning/uc-f02-31-add-a-low-code-script-step.md)
  to
  [UC-F2-35 Clean duplicates and stale records](../../02-functional/f02-no-code-configuration/use-cases/13-low-code-bulk-and-cleaning/uc-f02-35-clean-duplicates-and-stale-records.md),
  screens
  [S-F2-31 Script step editor](../../02-functional/f02-no-code-configuration/screens/13-low-code-bulk-and-cleaning/s-f02-31-script-step-editor.md)
  to
  [S-F2-35 Data cleaning](../../02-functional/f02-no-code-configuration/screens/13-low-code-bulk-and-cleaning/s-f02-35-data-cleaning.md),
  rules
  [BR-F2-28 Scripts run sandboxed within time and memory limits](../../02-functional/f02-no-code-configuration/business-rules/br-f02-28-scripts-run-sandboxed-within-time-and-memory-limits.md)
  to
  [BR-F2-32 Merges keep every link and an undo window](../../02-functional/f02-no-code-configuration/business-rules/br-f02-32-merges-keep-every-link-and-an-undo-window.md),
  entities [E-F2-30 Script step](../../02-functional/f02-no-code-configuration/data/e-f02-30-script-step.md) to
  [E-F2-34 Cleaning rule](../../02-functional/f02-no-code-configuration/data/e-f02-34-cleaning-rule.md) and their lists
  [S-F2-L30 Script steps](../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l30-script-steps.md) to
  [S-F2-L34 Cleaning rules](../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l34-cleaning-rules.md).
- Scripts run in the sandbox of
  [BR-F2-16 A sandbox never touches live data](../../02-functional/f02-no-code-configuration/business-rules/br-f02-16-sandbox-never-touches-live-data.md)
  under the rule account of
  [BR-F2-12 Rule accounts never exceed their author](../../02-functional/f02-no-code-configuration/business-rules/br-f02-12-rule-accounts-never-exceed-their-author.md).
- Bulk changes extend the batch rules of the AI assistant:
  [BR-F3-08 A batch is undone as a whole](../../02-functional/f03-assistant/business-rules/br-f03-08-a-batch-is-undone-as-a-whole.md)
  and [BR-F3-09 Batch size limit](../../02-functional/f03-assistant/business-rules/br-f03-09-batch-size-limit.md).

## Related

- [FL-F2-13 Low code, bulk work and data cleaning](../../02-functional/f02-no-code-configuration/flows/fl-f02-13-low-code-bulk-and-cleaning.md)
- [D459 F2 No-code configuration: gaps and improvements](d459-f02-gaps-and-improvements.md)
- [Interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)

---

⬅️ [D520 Benchmark gaps of F1 Administration](../f01-administration/d520-benchmark-gaps-f01-administration.md) ·
⬆️ [Up](README.md) · ➡️ [D522 Benchmark gaps of F3 Assistant](../f03-assistant/d522-benchmark-gaps-f03-assistant.md)
