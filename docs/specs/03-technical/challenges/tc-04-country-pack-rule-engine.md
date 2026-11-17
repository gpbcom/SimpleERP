🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🌍 TC-04 The country pack as a versioned rule engine

# 🌍 TC-04 The country pack as a versioned rule engine

**Status:** ✅ listed for the technical interviews

## Challenge

Take every legal value (rates, limits, durations, mentions, deadlines) from the company's country pack, by date in
force, flag a rule when its article changes, and ship the fix as a pack update.

## Raised by

- [F8 Accounting](../../02-functional/f08-accounting/README.md)
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md)
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md)
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md)
- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md)
- [T11 Legal corpora](../t11-legal-corpora/README.md)

## Why it is hard

- The France pack already holds 205 rules, read by every capability and sector.
- A value depends on the date of the fact, not today: an invoice of last year keeps last year's rate.
- A rule changed by law must reach every install without a software upgrade, and be tested before.

## Already decided

- [D199](../../06-decisions/f15-legal-assistant/d199-law-packs.md) Law packs
- [D293](../../06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md) Capabilities take legal
  rules from the country pack
- [D294](../../06-decisions/country-packs/d294-flag-then-pack-update.md) A law change flags the rule, a pack update
  fixes it

## Options to weigh

- Rules as data (a catalogue of values with validity dates) read by code, or as small versioned rule modules.
- One pack release cycle per country, apart from the software's.
- How a community-written pack is reviewed and signed.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19e Configuration ([chapter](../../../technical/architecture/configuration.md))
- 19l Release and versioning ([chapter](../../../technical/delivery/release-and-versioning.md))
- Then the technical capabilities: [T11 Legal corpora](../t11-legal-corpora/README.md).

## Questions for the interview

- Who may publish a country pack: the publisher only, or signed community maintainers?
- How long does an install keep running on an outdated pack before it warns?

---

⬅️ [TC-03 No-code configuration against schema and upgrades](tc-03-no-code-configuration-and-schema.md) ·
⬆️ [Up](README.md) ·
➡️ [TC-05 Records that must never change, and those that must be erased](tc-05-inalterable-and-certified-records.md)
