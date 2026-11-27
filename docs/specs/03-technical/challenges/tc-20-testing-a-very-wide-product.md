🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🧪 TC-20 Testing a very wide product

# 🧪 TC-20 Testing a very wide product

**Status:** ✅ listed for the technical interviews

## Challenge

Prove that 21 capabilities, 16 sectors, 47 personas, 205 country rules, plugins and AI features work together, on the
real images, before each release.

## Raised by

- [F1 Administration](../../02-functional/f01-administration/README.md)
- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [T11 Legal corpora](../t11-legal-corpora/README.md)

## Why it is hard

- The combinations of modules, sectors and countries are too many to test by hand.
- Legal values must be tested per date in force.
- AI answers are not deterministic.

## Already decided

- [D120](../../06-decisions/ux/d120-png-mockups.md) PNG mockups of every flow step

## Options to weigh

- Tests generated from the specs (use cases, rules, flows).
- Playwright against the real images, with seeded companies per sector.
- Evaluation sets for each AI feature, and load tests per performance target.

## Settled in

- 19o Tests: unit, GUI, E2E and load ([chapter](../../../technical/delivery/tests-and-traceability.md))
- 19b Performance and capacity ([chapter](../../../technical/infrastructure/performance-and-capacity.md))
- Then the technical capabilities: [T9 Install, backups and updates](../t09-install-backups-and-updates/README.md).

## Questions for the interview

- Which sector companies are seeded on the stages?
- What AI quality blocks a release?

---

⬅️ [TC-19 Languages, currencies and countries](tc-19-languages-currencies-and-countries.md) · ⬆️ [Up](README.md) ·
➡️ [TC-21 Metering every paid call, and stopping on a budget](tc-21-metering-every-paid-call.md)
