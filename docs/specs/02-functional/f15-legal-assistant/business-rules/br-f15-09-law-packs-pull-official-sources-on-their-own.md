🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-09 Law packs pull official sources on their own

# 📏 BR-F15-09 Law packs pull official sources on their own

**Status:** ✅ specified

## Statement

A law pack lists its official sources and how to read them (APIs, official downloads); simple-ERP pulls them on a
schedule, with no human validation, so that the corpus stays current: national law (for France, Légifrance through
PISTE), EU regulation (EUR-Lex), official guidance, case law, and the sector technical rules published as law;
copyrighted standards are not pulled, only their register entries from open sources (BR-F15-10,
[D448](../../../06-decisions/f15-legal-assistant/d448-law-texts-and-signed-rule-packs.md)).
Daily for codes and EU texts, weekly for the rest; each pull is logged with what changed.

The pulls feed the law corpus with raw official texts only; the country pack's rule values change only through signed
pack updates after a flagged change (D294, REQ-T11-01).

## Why

The law changes; only an unattended pull keeps up. See
[D205](../../../06-decisions/f15-legal-assistant/d205-law-packs-fed-from-official-apis.md).

## Examples

| Case | Result |
|---|---|
| An article amended on Légifrance | Its new version is in the corpus after the next pull, the old one kept with its dates (BR-F15-01) |
| A new EU regulation in the company's sector | Added at the next EUR-Lex pull, listed in the monthly digest |
| An official source down | Retried (BR-F3-32); the last copy is used and the administrators told after a day |

## Applies to

- [UC-F15-01](../use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)
- [UC-F15-04](../use-cases/04-set-up-the-legal-assistant/uc-f15-04-set-up-the-legal-assistant.md)
- [UC-F15-05](../use-cases/04-set-up-the-legal-assistant/uc-f15-05-follow-the-law-packs-refresh.md)

## Exceptions

Sources with no official API or download: see
[Sector technical standards](../../../05-non-functional/sector-technical-standards.md).

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-08 Document checks list, never rewrite](br-f15-08-document-checks-list-never-rewrite.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F15-10 Standards as a register, own copies opt-in](br-f15-10-standards-as-a-register-own-copies-opt-in.md)
