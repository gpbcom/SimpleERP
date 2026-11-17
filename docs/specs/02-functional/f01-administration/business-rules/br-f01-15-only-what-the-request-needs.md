🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-15 Only what the request needs

# 📏 BR-F1-15 Only what the request needs

**Status:** ✅ specified

## Statement

A request to an external AI provider holds only the user's question and the passages retrieved for it, within the user's
permissions; every answer it produced shows the provider's name.

## Why

Data leaves the server only as far as a single answer needs. See
[D83](../../../06-decisions/f01-administration/d83-only-what-the-request-needs.md).

Legal values from the France country pack:
[CR-FR-049 Processors and transfers outside the EU](../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md).

## Examples

| Request | Sent |
|---|---|
| "What did Acme order last month?" | The question and Acme's orders of last month the user may see |
| A meeting summary | That meeting's transcript |
| "Summarise all our customers" | Refused as too broad for an external provider; answered locally |

## Applies to

- [UC-F1-08](../use-cases/06-choose-an-ai-provider/uc-f01-08-choose-the-ai-provider-of-a-feature.md); F3, F4, F5, F15.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-14 Confirming outside changes](br-f01-14-confirming-outside-changes.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-16 Fall back to the local model](br-f01-16-fall-back-to-the-local-model.md)
