🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🔒 [Data protection](README.md) › ⚖️ CR-FR-211 Live geolocation of employees

# ⚖️ CR-FR-211 Live geolocation of employees

**Status:** 🔄 draft (GH-2 step S4b, from VD-21, VD-22, VD-23 / D503, D504, D505)

## Statement

(Proposed) An employee's live position is recorded only for a stated purpose that nothing less intrusive serves, during
working hours only, never to control speed or measure performance; the employee is told beforehand, sees when it is on
and may pause it during breaks; the staff committee is consulted and an impact assessment is done before it is switched
on; positions are kept no longer than the purpose needs.

## Values

- Purposes allowed by the owner (VD-22): safety, planning of the next visit, proof of service when nothing else proves
  it.
- Off outside working hours; paused by the employee during breaks (VD-22, VD-23).
- Kept 2 months at most (D517); the CNIL guidance to read.
- Position at check-in and check-out stays the default, kept 1 year
  ([BR-F9-06](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-06-location-only-at-check-in.md), D290).

## Legal references

- [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) art. 5, 6, 7, as
  [CR-FR-054](cr-fr-054-location-with-consent.md) cites them; art. 35 (impact assessment), as
  [Privacy and GDPR](../../../05-non-functional/privacy-gdpr.md) cites it.
- Code du travail L2312-38 and L1222-4 (not read yet), as
  [CR-FR-206](../labour/cr-fr-206-cse-consulted-on-monitoring.md) cites them.
- (Proposed) To read: [CNIL guidance](https://www.cnil.fr/fr/professionnels) on the geolocation of employees and of
  their vehicles.

## Effective dates

GDPR since 2018-05-25; (Proposed) the CNIL guidance to read.

## Enforced by

- [BR-F9-30](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-30-live-position-team-option-working-hours.md)
- [BR-F9-31](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-31-live-positions-kept-two-months.md)
- [BR-F9-32](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-32-who-sees-a-position.md)
- [E-F9-32 Live position](../../../02-functional/f09-hr-and-projects/data/e-f09-32-live-position.md)
- [UC-F9-37](../../../02-functional/f09-hr-and-projects/use-cases/12-schedule-customer-requests/uc-f09-37-share-my-position-during-work.md)
- [REQ-T13-05](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-05-live-positions.md)

## When the law changes

Watched in the law corpus: GDPR art. 5 and 35; Code du travail L2312-38. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

Up to 20 000 000 EUR or 4 % of turnover (GDPR art. 83(5)), as
[CR-FR-207](cr-fr-207-call-recording-proportionate.md) cites it.

## Exceptions

(Proposed) A vehicle's telematics position is still personal data while an employee drives it; it follows this rule.

## Open questions

The CNIL guidance was not read; the retention and any further limits to read before launch; the 2 months are decided
(D517).
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-210 Qualifications the law ties to tasks](../labour/cr-fr-210-qualifications-tied-to-tasks.md) ·
⬆️ [Up](README.md) · ➡️ [CR-FR-212 LCR and cheque remittances](../payments/cr-fr-212-lcr-and-cheque-remittances.md)
