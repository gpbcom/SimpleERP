🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D199 Law packs

# 📜 D199 Law packs

**Status:** ✅ decided

## Context

How other countries are added.

## Options

- Law pack plugins.
- All built in.
- France only in v1.

## Choice

Each country is a law pack plugin in the store (F14): its sources, ingestion rules, warnings, referral contacts and test
set; France ships with SimpleERP; packs are made by SimpleERP or partners and reviewed before publication.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

T11 loads law packs; F14 lists them. Law packs carry no test set ([D206](d206-unattended-pulls-without-test-gate.md)).

Revised by D448 on 2026-11-12: a law pack's raw texts are pulled unattended; its rule values ship as signed pack
updates.

## Related

- [UC-F15-01](../../02-functional/f15-legal-assistant/use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)

---

⬅️ [D198 One legal assistant use case](d198-legal-single-use-case.md) · ⬆️ [Up](README.md) ·
➡️ [D200 Legal answer quality](d200-legal-quality-test-set.md)
