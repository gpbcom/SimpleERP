🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-07 No deletes, no irreversible acts

# 📏 BR-F3-07 No deletes, no irreversible acts

**Status:** ✅ specified

## Statement

The AI assistant creates records, changes fields and moves statuses, within the user's rights, after confirmation
(D140). It never deletes, and never does an irreversible or outward act: validating an invoice or a payslip, sending to
a customer or supplier, paying, signing. It prepares them and opens the screen where the user finishes with their own
click.

This is the AI assistant tier of [D439](../../../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md): the AI assistant
always asks before writing; agents and automations follow their own tier (BR-F3-35).

## Why

Irreversible and legal acts stay a person's own act. See
[D157](../../../06-decisions/f03-assistant/d157-assistant-actions.md) and
[D439](../../../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md).

## Examples

| Case | Result |
|---|---|
| "Create a quote for Durand with 3 days of work" | Shown, confirmed, created as a draft |
| "Mark these 5 tasks done" | Shown, confirmed, done |
| "Delete these contacts" | "I can't delete records; here they are, selected, in the contact list" |
| "Send the quote to Durand" | The email is prepared and opened; the user clicks Send |

## Applies to

- [UC-F3-03](../use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)
- [UC-F3-15 Defend against instructions hidden in content](../use-cases/11-trust-the-answers/uc-f03-15-defend-against-instructions-hidden-in-content.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-06 Explanations never reveal hidden data](br-f03-06-explanations-never-reveal-hidden-data.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-08 A batch is undone as a whole](br-f03-08-a-batch-is-undone-as-a-whole.md)
