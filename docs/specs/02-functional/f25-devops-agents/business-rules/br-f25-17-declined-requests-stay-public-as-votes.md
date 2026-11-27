🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-17 Declined requests stay public as votes

# 📏 BR-F25-17 Declined requests stay public as votes

**Status:** ✅ specified

## Statement

A request declined (not planned, or offered to the feature factory) stays in the public list of requests, without any
company or person name, where hosted customers can vote for it; a request passing 25 votes is studied again.

## Why

Customers see what others asked and weigh in (D482).

## Examples

| Case | Result |
|---|---|
| "Export payslips to Silae" declined, 3 votes | passes: public, anonymised |
| Request showing the requester's company | fails: never |
| 26 votes reached | passes: studied again by the agents |

## Applies to

- [UC-F25-24 Vote on declined requests](../use-cases/05-tell-the-customer/uc-f25-24-vote-on-declined-requests.md)
- [UC-F25-12 Approve or refuse agents' tickets](../use-cases/04-approve-and-govern/uc-f25-12-approve-or-refuse-agents-tickets.md)
- [UC-F25-20 Ask the AI assistant about my requests](../use-cases/05-tell-the-customer/uc-f25-20-ask-the-assistant-about-my-requests.md)

## Exceptions

Security reports and personal requests are never public (BR-F25-12).

## Configurable

The vote threshold.

## Open questions

None.

---

⬅️ [BR-F25-16 Agents' spec pull requests checked first](br-f25-16-agents-spec-pull-requests-checked-first.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F25-18 The roadmap shows accepted tickets only](br-f25-18-the-roadmap-shows-accepted-tickets-only.md)
