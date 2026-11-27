🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-19 Betas run on a sandbox copy only

# 📏 BR-F25-19 Betas run on a sandbox copy only

**Status:** 🔄 waiting for the owner

## Statement

A beta feature runs only on a sandbox copy of the company's data, never on its live data or its live version; the copy
is separate, masked as set, limited to the chosen users, and deleted when the enrolment ends.

## Why

A beta may be wrong, and a live company must not pay for it. The owner asked for a beta programme
([D544](../../../06-decisions/f25-devops-agents/d544-benchmark-gaps-f25-devops-agents.md)); the agents likewise work
read-only on production ([BR-F25-04](br-f25-04-read-only-on-production.md)).

## Examples

| Case | Result |
|---|---|
| A beta feature enabled | it exists in the copy only |
| An administrator who tries to turn a beta feature on in the live company | refused: not released |
| A copy of 200 employees' data | personal data masked as set |
| The enrolment ends | the copy is deleted |
| Feedback sent from the copy | reaches the maintainers without the copy's personal data |

## Applies to

- [UC-F25-26](../use-cases/07-roadmap-beta-and-credits/uc-f25-26-join-the-beta-programme.md)
- [E-F25-17 Beta enrolment](../data/e-f25-17-beta-enrolment.md)
- [BR-F25-04 Read-only on production](br-f25-04-read-only-on-production.md)

## Exceptions

None.

## Configurable

The masking of the copy, by the administrator; the live data is never an option.

## Open questions

None.

---

⬅️ [BR-F25-18 The roadmap shows accepted tickets only](br-f25-18-the-roadmap-shows-accepted-tickets-only.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F25-20](br-f25-20-credits-go-to-confirmed-non-duplicate-reports-only.md)
