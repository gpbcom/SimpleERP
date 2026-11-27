🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-14 Triage with severity, priority and target times

# 📏 BR-F25-14 Triage with severity, priority and target times

**Status:** ✅ specified

## Statement

Each USER ticket gets a severity (critical, high, normal, low) from its effect and a priority from its reach (companies
and users affected, votes); each severity has an acknowledgement and a resolution target, and the ticket shows the time
left.

## Why

Requests must be handled in order and on time (D482).

## Examples

| Case | Result |
|---|---|
| Invoices cannot be sent by 40 companies | passes: critical, acknowledged within 4 hours, fixed within 2 days |
| Wrong label on one screen | passes: low, next release |
| Ticket past its target | passes: flagged to the maintainers |

## Applies to

- [UC-F25-21 Triage requests by severity and priority](../use-cases/01-intake/uc-f25-21-triage-requests-by-severity-and-priority.md)
- [UC-F25-03 Open the USER feature with its ticket](../use-cases/01-intake/uc-f25-03-open-the-user-feature-with-its-ticket.md)
- [UC-F25-14 Follow my request's status](../use-cases/05-tell-the-customer/uc-f25-14-follow-my-request-s-status.md)

## Exceptions

Vulnerabilities follow BR-F25-15.

## Configurable

The targets per severity, critical 4 hours and 2 days, high 1 day and 10 days, normal 5 days and the next
release.

## Open questions

None.

---

⬅️ [BR-F25-13 Health data out of the agents' reach](br-f25-13-health-data-out-of-reach.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-15 Vulnerabilities handled under the CRA](br-f25-15-vulnerabilities-handled-under-the-cra.md)
