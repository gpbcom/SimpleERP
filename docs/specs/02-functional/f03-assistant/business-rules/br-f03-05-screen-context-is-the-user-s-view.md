🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-05 Screen context is the user's view

# 📏 BR-F3-05 Screen context is the user's view

**Status:** ✅ specified

## Statement

The AI assistant's screen context is the open record with its linked records, or the list with its filters and sort, or
the user's selection; it holds only what the user may see (BR-F3-02), and it is shown in the panel as a chip ("About:
Durand SA") that the user can remove.

## Why

Questions like "this customer" need the screen; the chip shows what is used. See
[D153](../../../06-decisions/f03-assistant/d153-screen-context.md) and
[D155](../../../06-decisions/f03-assistant/d155-ask-about-selection.md).

## Examples

| Case | Result |
|---|---|
| On customer Durand, "what do they owe?" | Durand's unpaid invoices |
| On the invoice list filtered "overdue", "total?" | The total of the filtered list |
| 3 rows selected, "total of these" | The total of the 3 rows |
| The user removes the chip | The question is answered without the screen |

## Applies to

- [UC-F3-02](../use-cases/02-ask-about-the-screen/uc-f03-02-ask-about-what-is-on-screen.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-04 Ask or say not found, never invent](br-f03-04-never-invent.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-06 Explanations never reveal hidden data](br-f03-06-explanations-never-reveal-hidden-data.md)
