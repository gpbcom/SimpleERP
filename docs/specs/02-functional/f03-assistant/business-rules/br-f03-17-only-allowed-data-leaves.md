🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-17 Only allowed data leaves

# 📏 BR-F3-17 Only allowed data leaves

**Status:** ✅ specified

## Statement

A call to an outside tool carries only the data the request needs, and only of the categories its connection allows:
none, business data (companies, products, amounts), personal data (people's names, contacts, HR data). Each call appears
in the conversation as "Sent to <tool>", expandable to the exact data.

## Why

Data leaves the self-hosted ERP only knowingly. See
[D169](../../../06-decisions/f03-assistant/d169-outside-data-categories.md) and
[D83](../../../06-decisions/f01-administration/d83-only-what-the-request-needs.md).

Legal values from the France country pack:
[CR-FR-049 Processors and transfers outside the EU](../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md).

## Examples

| Case | Result |
|---|---|
| A shipping tool allowed business data; "track Durand's parcel" | The tracking number is sent, not Durand's contact |
| A translation tool allowed none; "translate this customer's notes" | Refused: "This tool may not receive your company's data" |
| A CRM allowed personal data | The contact's name and email are sent, shown in "Sent to" |

## Applies to

- [UC-F3-06](../use-cases/06-use-an-outside-tool/uc-f03-06-use-an-outside-tool-through-the-assistant.md)

## Exceptions

None.

## Configurable

Yes: per connection, by the administrator (UC-F1-07).

## Open questions

None.

---

⬅️ [BR-F3-16 Missing features become requests](br-f03-16-missing-features-become-requests.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-18 Outside results are marked](br-f03-18-outside-results-are-marked.md)
