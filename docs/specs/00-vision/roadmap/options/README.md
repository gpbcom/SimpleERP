🏠 [Specs](../../../README.md) › 🎯 [Vision](../../README.md) › 🛣️ [Roadmap and options](../README.md) ›
🔀 Roadmap options

# 🔀 Roadmap options

**Status:** ✅ specified

The ways to order V1 that respect its frame. The owner chose **option A** on 2026-11-27, cut into the twelve phases of
[Phases](../phases/README.md) ([Q20](../../../07-questions/q20-which-roadmap-option-orders-v1.md),
[D569](../../../06-decisions/vision/d569-roadmap-option-a-in-twelve-phases.md)); the other options are kept as the
record of what was compared.

## The frame every option keeps

- Everything the specifications hold is in V1, released once
  ([D3](../../../06-decisions/foundations/d03-every-area-in-the-first-version.md),
  [D380](../../../06-decisions/vision/d380-every-capability-first-confirmed.md)), built by the DevOps agents first
  ([D483](../../../06-decisions/vision/d483-roadmap-devops-agents-first.md)).
- The whole platform before the first business area ([D16](../../../06-decisions/foundations/d16-platform-first.md));
  the business areas in the order sales, purchasing and stock, accounting, HR and projects
  ([D4](../../../06-decisions/foundations/d04-business-build-order.md)); point of sale, shop, manufacturing and payroll
  last, as plugins ([D15](../../../06-decisions/foundations/d15-industry-areas-as-plugins.md)).
- A dated pilot of F1 to F9 with e-invoicing before 1 September 2027
  ([D451](../../../06-decisions/vision/d451-dated-pilot-before-the-release.md)), the date small companies must issue
  e-invoices; every company must already receive them since 1 September 2026.
- V1 succeeds when one real company runs on it for several months
  ([D10](../../../06-decisions/foundations/d10-first-version-success.md)); France first
  ([D8](../../../06-decisions/foundations/d08-france-first.md)).

An early release before V1 is not among the options: the owner was asked twice and kept one release
([D3](../../../06-decisions/foundations/d03-every-area-in-the-first-version.md), then
[D380](../../../06-decisions/vision/d380-every-capability-first-confirmed.md)).

## Options

| Option | Steps | Steps in a row before the pilot | Use cases the pilot waits for | Decisions bent |
|---|---|---|---|---|
| [Option A: ten steps in a row](option-a-ten-steps-in-a-row.md) | 10 | 6 | 426 (35 %), without F5 | D451 |
| [Option B: the platform, then parallel tracks](option-b-platform-then-parallel-tracks.md) | 9 | 3 (tracks) | 380 (31 %) | D4 |
| [Option C: the pilot first](option-c-the-pilot-first.md) | 8 | 3 | 380 (31 %) | none |
| [Option D: sector waves](option-d-sector-waves.md) | 7 | 3 | 380 (31 %) | D15, D483 |
| [Option E: the factory first](option-e-the-factory-first.md) | 7 | 4 | 442 (36 %) | D451 |
| [Option F: the pilot spine, with tracks and waves](option-f-pilot-spine-tracks-and-waves.md) | 7 | 3 (tracks) | 380 (31 %) | none |

| Criterion | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Pilot date protected | ⚠️ | ⚠️ shares the maintainer | ✅ | ✅ | ⚠️ | ✅ |
| Calendar to V1 | longest | short | long | long | short if the factory works | short |
| Early validation on real companies | end | pilot | pilot | every wave | pilot | pilot and waves |
| Parallel work for the maintainer | low | high | low | medium | high | high |
| Hosted services ready early | no | yes | no | no | the factory only | no |
| Owner decisions kept | all but D451 | all but D4 | all | all but D15, D483 | all but D451 | all |

## Recommendation

Claude's recommendation, written before the owner's choice: option F: it is the only one that both keeps every decision of the owner and protects the pilot's date. It
takes C's order, so nothing outside the pilot can delay it; B's tracks, so the DevOps agents build in parallel once the
contracts are frozen; and D's waves, so each group of sectors is accepted on its example companies. The five gaps of the
adopted roadmap ([What V1 holds](../inventory.md#gaps-of-the-adopted-roadmap)) are fixed by every option, F included.

If the owner prefers the fewest moving parts, option A with F5 moved before the pilot is the closest to the adopted
plan.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🧱 |  | [Option A: ten steps in a row](option-a-ten-steps-in-a-row.md) | ✅ |
| 🛤️ |  | [Option B: the platform, then parallel tracks](option-b-platform-then-parallel-tracks.md) | 🚫 |
| 🎯 |  | [Option C: the pilot first](option-c-the-pilot-first.md) | 🚫 |
| 🏘️ |  | [Option D: sector waves](option-d-sector-waves.md) | 🚫 |
| 🏭 |  | [Option E: the factory first](option-e-the-factory-first.md) | 🚫 |
| ⭐ |  | [Option F: the pilot spine, with tracks and waves](option-f-pilot-spine-tracks-and-waves.md) | 🚫 |

---

⬅️ [What V1 holds](../inventory.md) · ⬆️ [Up](../README.md)
