🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🌍 [Decisions: Country packs](README.md) ›
📜 D293 Capabilities take legal rules from the country pack

# 📜 D293 Capabilities take legal rules from the country pack

**Status:** ✅ decided

## Context

Which capabilities read their legal rules from the country pack.

## Options

- Every capability, F1 to F16, and the sectors (recommended).
- From F10 onward only.

## Choice

Every capability, F1 to F16, and every sector take each legal value they enforce (rates, limits, durations, mandatory
mentions, records, retention, certifications) from the country pack of the company's country, and hard-code none. A
business rule that enforces law names its country rule; the rules already specified are moved into the France pack. A
feature added later that enforces law adds its rule to the pack first.

## Decided by

The owner, on 2026-11-11, in the specification interview.

## Consequences

Each business rule with a legal source links its `CR-FR-nnn` page; a company in another country gets that country's
values once its pack exists; without a pack, the legal checks are off and the administrator is told.

Revised by D446 on 2026-11-12: an entity whose kind has no rule in the pack follows its kind's default in the retention
schedule (Data retention).

## Related

- [🇫🇷 France country pack](../../10-country-packs/france/README.md)

---

⬅️ [D292 One country pack per country, law inside](d292-one-country-pack-per-country.md) · ⬆️ [Up](README.md) ·
➡️ [D294 A law change flags the rule, a pack update fixes it](d294-flag-then-pack-update.md)
