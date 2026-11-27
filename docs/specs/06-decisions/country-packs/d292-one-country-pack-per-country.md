🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🌍 [Decisions: Country packs](README.md) ›
📜 D292 One country pack per country, law inside

# 📜 D292 One country pack per country, law inside

**Status:** ✅ decided

## Context

The law pack (D199) holds a country's legal texts for the legal assistant. The legal rules the capabilities enforce
(VAT, invoice mentions, closing, trial periods, till rules...) were written inside each capability.

## Options

- One country pack per country holding the law corpus and the rules to enforce (recommended).
- Two packs per country: the law pack and a separate country pack, installed together.

## Choice

One country pack per country, installed as a plugin from the store (F14). It holds the law corpus (what D199 called the
law pack, still pulled unattended from official APIs, D205), every legal rule SimpleERP enforces in that country, one
page per rule (`CR-<country>-nnn`), and the country set-up (chart of accounts, journals, taxes). France ships with
SimpleERP.

## Decided by

The owner, on 2026-11-11, in the specification interview.

## Consequences

D199's law pack becomes the law corpus of the country pack; T11 loads the whole pack; F14 lists country packs; the specs
gain the section `10-country-packs/`, with a country rule template.

## Related

- [🇫🇷 France country pack](../../10-country-packs/france/README.md)
- [D199 Law packs](../f15-legal-assistant/d199-law-packs.md)

---

⬅️ [D291 Contract editor](../f09-hr-and-projects/d291-contract-editor.md) · ⬆️ [Up](README.md) ·
➡️ [D293 Capabilities take legal rules from the country pack](d293-capabilities-take-legal-rules-from-the-pack.md)
