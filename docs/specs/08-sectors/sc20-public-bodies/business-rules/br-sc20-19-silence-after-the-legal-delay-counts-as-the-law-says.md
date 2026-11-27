🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-19 Silence after the legal delay counts as the law says

# 📏 BR-SC20-19 Silence after the legal delay counts as the law says

**Status:** ✅ specified

## Statement

Each permit request has its legal delay from the day the file is complete, a missing document is asked for inside the
legal time that keeps the clock, and a request not decided in its delay is marked Delay passed with the law's effect for
its kind.

## Why

A delay that passes without a decision may give the citizen the permit by silence, so the body must see it coming
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). The France-pack rule is
[CR-FR-261 Planning permit instruction delays](../../../10-country-packs/france/real-estate/cr-fr-261-planning-permit-delays.md):
1 month for a prior declaration, 2 months for a house or demolition permit, 3 months for other permits, missing
documents asked within 1 month, and silence is a tacit permit except in the cases of R*424-2 to R*424-3; in communes of
more than 3 500 inhabitants every legal person files electronically, for requests from 2025-01-01.

## Examples

| Case | Result |
|---|---|
| Complete request | clock starts from the filing |
| Missing document asked in the first month | delay restarts when complete |
| Missing document asked later | the delay is not restarted |
| Consultation of the heritage architect | delay extended with the reason |
| No decision in the delay | Delay passed, effect by kind |

## Applies to

- [UC-SC20-19](../use-cases/05-council-registry-permits-and-assets/uc-sc20-19-instruct-planning-permits.md)
- [E-SC20-14 Permit request](../data/e-sc20-14-permit-request.md)
- [E-SC20-14 Permit request](../data/e-sc20-14-permit-request.md)
- [E-SC20-10 Council decision](../data/e-sc20-10-council-decision.md)
- France-pack rule:
  [CR-FR-261 Planning permit instruction delays](../../../10-country-packs/france/real-estate/cr-fr-261-planning-permit-delays.md)

## Exceptions

None.

## Configurable

The kinds of permit, their delays and the effect of silence, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC20-18](br-sc20-18-civil-records-are-corrected-only-by-a-margin-note.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC20-20 Assets follow the M57 depreciation rules](br-sc20-20-assets-follow-the-m57-depreciation-rules.md)
