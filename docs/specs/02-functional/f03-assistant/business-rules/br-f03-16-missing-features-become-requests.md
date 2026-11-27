🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-16 Missing features become requests

# 📏 BR-F3-16 Missing features become requests

**Status:** ✅ specified

## Statement

When the user asks for something the ERP cannot do yet (a missing field, screen, status or rule), the AI assistant says
so plainly and offers to send a configuration request, pre-filled with what the user wanted and where; the user can edit
it before sending; configurators see it in their list.

## Why

What users miss should reach those who can add it. See
[D168](../../../06-decisions/f03-assistant/d168-configuration-requests.md).

## Examples

| Case | Result |
|---|---|
| "Record the vehicle on this visit" with no such field | "Visits have no vehicle field yet. Send a request to your configurators?" Pre-filled: "Add a Vehicle field to visits" |
| The same request already open | "Already requested by Paul on 3 November; add your vote?" |

## Applies to

- [UC-F3-05](../use-cases/05-find-and-get-guided/uc-f03-05-find-a-record-or-a-screen-get-guided.md)

## Exceptions

None.

## Configurable

Requests can be turned off by an administrator.

## Open questions

None.

---

⬅️ [BR-F3-15 Guidance matches the company's setup](br-f03-15-guidance-matches-the-company-s-setup.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-17 Only allowed data leaves](br-f03-17-only-allowed-data-leaves.md)
