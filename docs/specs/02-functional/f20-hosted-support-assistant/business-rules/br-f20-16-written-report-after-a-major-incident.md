🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-16 Written report after a major incident

# 📏 BR-F20-16 Written report after a major incident

**Status:** ✅ specified

## Statement

After an incident that interrupted or degraded customers' service, each affected customer receives a written report
within 5 business days: what happened, when, who was affected, the cause, what was done and what will prevent
it.

## Why

Customers need the facts in writing (D477), and some need them for their own duties (BR-F20-19).

## Examples

| Case | Result |
|---|---|
| Outage 09:00 to 09:40 on 2026-11-20, report on 2026-11-25 | passes |
| Report missing the cause | fails: not approved |
| Incident affecting no customer | passes: no report sent |

## Applies to

- [UC-F20-23 Send the written incident report](../use-cases/06-after-an-incident/uc-f20-23-send-the-written-incident-report.md)
- [UC-F20-10 Handle a wide incident with a status page](../use-cases/03-incidents/uc-f20-10-handle-a-wide-incident-with-a-status-page.md)

## Exceptions

Facts under a security investigation may follow in a second report.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F20-15 Release notes before each upgrade](br-f20-15-release-notes-before-each-upgrade.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-17 Service credits for missed targets](br-f20-17-service-credits-for-missed-targets.md)
