🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📒 [Decisions: F8 Accounting](README.md) ›
📜 D454 E-invoicing platforms: Super PDP and B2Brouter first, then any AFNOR platform

# 📜 D454 E-invoicing platforms: Super PDP and B2Brouter first, then any AFNOR platform

**Status:** ✅ decided

## Context

[Q13](../../07-questions/q13-e-invoicing-platforms.md): a self-hosted ERP cannot be a registered platform itself, so
SimpleERP connects each company to one or more registered platforms; small companies must issue e-invoices from 1
September 2027, and the pilot of D451 includes e-invoicing.

## Options

- One platform only.
- Super PDP and B2Brouter first, then more.
- AFNOR XP Z12-013 only.
- Other platforms of the benchmark.

## Choice

Confirmed by the owner on 2026-11-12: "Super PDP + B2BRouter, then more + Any platform through the AFNOR standards.
Document all of that very well." Super PDP and B2Brouter adapters come first; more adapters are added on demand; one
generic adapter speaks AFNOR XP Z12-013, so that any platform offering the standard works without its own adapter;
Chorus Pro carries invoices to public buyers.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- [REQ-T12-19](../../03-technical/t12-connectors-and-scrapers/requirements/req-t12-19-e-invoicing-platforms.md) and
  [I-T12-06](../../03-technical/t12-connectors-and-scrapers/interfaces/i-t12-06-e-invoicing-platform-connector.md).
- The integration design on the [e-invoicing platforms](../../05-non-functional/e-invoicing-platforms.md) page.
- The pilot of D451 goes through one of the first two.

## Related

- [F8 Accounting](../../02-functional/f08-accounting/README.md)
- [E-invoicing platforms](../../05-non-functional/e-invoicing-platforms.md)
- [Q13](../../07-questions/q13-e-invoicing-platforms.md)

---

⬅️ [D453 An optional SIRET on a site](../f01-administration/d453-optional-siret-on-a-site.md) · ⬆️ [Up](README.md) ·
➡️ [D455 The owner's answers on the waiting list, by class](d455-waiting-list-answers-of-2026-11-12.md)
