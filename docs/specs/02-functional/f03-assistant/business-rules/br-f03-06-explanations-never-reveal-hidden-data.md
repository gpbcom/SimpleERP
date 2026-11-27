🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-06 Explanations never reveal hidden data

# 📏 BR-F3-06 Explanations never reveal hidden data

**Status:** ✅ specified

## Statement

When the AI assistant explains why a save was refused or an action is unavailable, it names the rule, the status or the
missing right, and who can help (the record's owner, the administrator); it never quotes a value, a record or a field
the user may not see.

## Why

An explanation must help without leaking. See [D156](../../../06-decisions/f03-assistant/d156-explain-the-screen.md).

## Examples

| Case | Result |
|---|---|
| "Why is Validate grey?" on an invoice | "Validating invoices needs the Accounting right, which your role does not have. Ask your administrator." |
| A save refused by the rule "amount over the credit limit" | The rule and the limit, if the user may see the limit; otherwise "over the customer's credit limit", no figure |
| "What does this field mean?" | The field's help text and how it is used |

## Applies to

- [UC-F3-02](../use-cases/02-ask-about-the-screen/uc-f03-02-ask-about-what-is-on-screen.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-05 Screen context is the user's view](br-f03-05-screen-context-is-the-user-s-view.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-07 No deletes, no irreversible acts](br-f03-07-no-deletes-no-irreversible-acts.md)
