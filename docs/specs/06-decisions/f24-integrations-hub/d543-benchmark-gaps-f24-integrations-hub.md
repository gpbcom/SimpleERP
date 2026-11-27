🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔌 [Decisions: F24 Integrations hub](README.md) ›
📜 D543 Benchmark gaps of F24 Integrations hub

# 📜 D543 Benchmark gaps of F24 Integrations hub

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four
integration features that F24 did not cover: connectors built by the AI assistant, the two large commercial office
suites, a standing export to a data warehouse and a sync with the accountant's own software. F24 already has the
catalogue, the European open suites, two-way sync with an owner per record and the run-and-control screens; these extend
the reach of the hub.

## Options

- G119 AI-built connectors: AI-built connectors that run in the sandbox first, or connectors built only by the project.
- G120 Google and Microsoft suites: the two commercial suites connected with the fewest permissions, or the open suites
  only.
- G121 Data warehouse export: an export that applies field rights and masking, or the standard file export only.
- G122 Accounting firm tools: a sync where one side masters each period, or files handed over by hand.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F24 gets four use cases in one new flow, FL-F24-08, each with its screen and its rule, and three entities with their
lists; the suites connection has no entity of its own, since it creates connections and suite components that already
exist. All at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G119 | AI-built connectors | UC-F24-28: connectors drafted by the AI assistant and approved after sandbox tests | "AI-built connectors" |
| G120 | Google and Microsoft suites | UC-F24-29: the commercial suites connected with the fewest permissions needed | "Google and Microsoft suites" |
| G121 | Data warehouse export | UC-F24-30: a warehouse export that follows field rights and masking | "Data warehouse export" |
| G122 | Accounting firm tools | UC-F24-31: a sync where one side is the master of each period | "Accounting firm tools" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F24 Integrations hub").

## Consequences

- G119 AI-built connectors:
  [UC-F24-28](../../02-functional/f24-integrations-hub/use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-28-have-the-ai-build-a-connector.md),
  [S-F24-26](../../02-functional/f24-integrations-hub/screens/08-ai-connectors-suites-and-warehouse/s-f24-26-ai-connector-builder.md)
  and
  [BR-F24-17](../../02-functional/f24-integrations-hub/business-rules/br-f24-17-an-ai-built-connector-runs-in-the-sandbox-first.md),
  with [E-F24-17](../../02-functional/f24-integrations-hub/data/e-f24-17-connector-draft.md) Connector draft and its
  list [S-F24-L17](../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l17-connector-drafts.md).
- G120 Google and Microsoft suites:
  [UC-F24-29](../../02-functional/f24-integrations-hub/use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-29-connect-google-workspace-or-microsoft-365.md),
  [S-F24-27](../../02-functional/f24-integrations-hub/screens/08-ai-connectors-suites-and-warehouse/s-f24-27-office-suites.md)
  and
  [BR-F24-18](../../02-functional/f24-integrations-hub/business-rules/br-f24-18-suite-access-uses-the-fewest-scopes-needed.md).
- G121 Data warehouse export:
  [UC-F24-30](../../02-functional/f24-integrations-hub/use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-30-export-data-to-a-warehouse.md),
  [S-F24-28](../../02-functional/f24-integrations-hub/screens/08-ai-connectors-suites-and-warehouse/s-f24-28-warehouse-export.md)
  and
  [BR-F24-19](../../02-functional/f24-integrations-hub/business-rules/br-f24-19-exports-follow-field-rights-and-masking.md),
  with [E-F24-18](../../02-functional/f24-integrations-hub/data/e-f24-18-export-pipeline.md) Export pipeline and its
  list [S-F24-L18](../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l18-export-pipelines.md).
- G122 Accounting firm tools:
  [UC-F24-31](../../02-functional/f24-integrations-hub/use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-31-sync-with-the-accountants-software.md),
  [S-F24-29](../../02-functional/f24-integrations-hub/screens/08-ai-connectors-suites-and-warehouse/s-f24-29-accounting-firm-sync.md)
  and
  [BR-F24-20](../../02-functional/f24-integrations-hub/business-rules/br-f24-20-one-side-is-the-master-per-period.md),
  with [E-F24-19](../../02-functional/f24-integrations-hub/data/e-f24-19-firm-sync.md) Firm sync and its list
  [S-F24-L19](../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l19-firm-syncs.md).
- Drawn in [FL-F24-08](../../02-functional/f24-integrations-hub/flows/fl-f24-08-ai-connectors-suites-and-warehouse.md)
  AI connectors, office suites, warehouse and firms.

## Related

- [FL-F24-08](../../02-functional/f24-integrations-hub/flows/fl-f24-08-ai-connectors-suites-and-warehouse.md)
- [D427 Integrations hub](d427-integrations-hub-coverage.md)
- [D428 Office suites: full read and write API](d428-office-suites-full-api.md)
- [D481 F24 Integrations hub: gaps and improvements](d481-f24-gaps-and-improvements.md)
- [BR-F24-07](../../02-functional/f24-integrations-hub/business-rules/br-f24-07-two-way-sync-with-ownership.md)

---

⬅️ [D542](../f23-what-if-simulation/d542-benchmark-gaps-f23-what-if-simulation.md) · ⬆️ [Up](README.md) ·
➡️ [D544 Benchmark gaps of F25 DevOps agents](../f25-devops-agents/d544-benchmark-gaps-f25-devops-agents.md)
