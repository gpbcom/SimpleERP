🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) › 👥 [Labour](README.md) ›
⚖️ CR-FR-210 Qualifications the law ties to tasks

# ⚖️ CR-FR-210 Qualifications the law ties to tasks

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A task the law reserves to holders of a qualification, an authorisation, a training or a professional card
is given only to an employee who holds it, verified and current; these requirements are legal, always required, and
cannot be relaxed by the planner.

## Values

The France qualification catalogue (YAML,
[E-F9-30](../../../02-functional/f09-hr-and-projects/data/e-f09-30-qualification-type.md)),
from the rules and standards the specs already list:

| Task | Qualification | Validity | Where the specs hold it |
|---|---|---|---|
| Kitchen work in a commercial restaurant | Food hygiene training, one trained person at least | At least 14 hours, no renewal | [CR-FR-110](../hospitality/cr-fr-110-food-hygiene-records.md) |
| Running a place that sells alcohol | Operating permit | 10 years, renewal training of at least 6 hours | [CR-FR-109](../hospitality/cr-fr-109-alcohol-licences.md) |
| Driving for hire | Initial qualification and continuous training | Continuous training every 5 years, the first within 5 years of the initial qualification ([Code des transports, art. R3314-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044326235), read 2026-11-27) | [CR-FR-119](../transport/cr-fr-119-driver-training.md) |
| Carrying dangerous goods | Dangerous-goods training | (⚖️ lawyer review before launch, D574) to read: the ADR training certificate and its period | [CR-FR-121](../transport/cr-fr-121-dangerous-goods.md) |
| Showing a property, managing for others | Estate agent's professional card (T, G, S) | Renewed every 3 years | [CR-FR-139](../real-estate/cr-fr-139-hoguet-card-and-guarantee.md) |
| Electrical work | Electrical authorisation (B0, B1V, B2V, BR and others) | Given by the employer for the tasks assigned, after training; issued, kept and renewed by the standards of R4544-3; near bare live parts, valid only with a current medical attestation since 2025-10-01 (Décret n° 2025-355), the fitness opinions issued before that date counting for 5 years ([Code du travail, art. R4544-9 to R4544-11](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000022848571), read 2026-11-27) | [Sector technical standards](../../../05-non-functional/sector-technical-standards.md) |
| Driving a lift truck | Employer's authorisation to drive (CACES R489 as practice) | Training renewed when needed; the authorisation needs a medical attestation, valid 5 years, since 2025-10-01 (Décret n° 2025-355); until 2025-09-30 a fitness opinion of the reinforced follow-up, such opinions counting as the attestation for 5 years from their date; equipment listed by ministerial order ([Code du travail, art. R4323-55 to R4323-57](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018489837), read 2026-11-27) | [Sector technical standards](../../../05-non-functional/sector-technical-standards.md) |

(⚖️ lawyer review before launch, D574) To add once read: driving licence categories for company vehicles, first-aid training, health professionals'
registration (RPPS), and the tasks an intern or an apprentice may not do alone.

## Legal references

- Food hygiene: Regulation (EC) 852/2004; Code rural L233-4, D233-11 to D233-13; arrêté du 12 février 2024, as
  [CR-FR-110](../hospitality/cr-fr-110-food-hygiene-records.md) cites them.
- Operating permit: Code de la santé publique L3332-1-1, as [CR-FR-109](../hospitality/cr-fr-109-alcohol-licences.md)
  cites it.
- Drivers: Code des transports R3314-1, R3314-10 ([Code des transports, art. R3314-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044326235), read 2026-11-27); Directive 2003/59/EC.
- Dangerous goods: ADR agreement; arrêté TMD (not read yet).
- Estate agents: Loi n° 70-9 (Hoguet); décret n° 72-678.
- Electrical work: Code du travail R4544-3 and following; NF C 18-510 by reference.
- Lifting equipment: Code du travail R4323-55 to R4323-57 ([Code du travail, art. R4323-55 to R4323-57](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018489837), read 2026-11-27).
- (⚖️ lawyer review before launch, D574) To read: Code de la route, the driving licence categories; Code de la santé publique, the registration of
  health professionals.

## Effective dates

Each line as its own rule; R3314-10 in force since 2022-02-01 ([Code des transports, art. R3314-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044326235), read 2026-11-27); (⚖️ lawyer review before launch, D574) to read for the
lines without one.

## Enforced by

- [E-F9-30 Qualification type](../../../02-functional/f09-hr-and-projects/data/e-f09-30-qualification-type.md)
- [E-F2-25 Request type](../../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md)
- [BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md)
- [BR-F9-26](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md)
- [BR-F9-27](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-27-unverified-attributes-do-not-count.md)
- [BR-F9-17](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-17-mandatory-trainings-must-be-current-for-the-work-that-needs-them.md)
- [REQ-T13-07](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-07-scheduling-engine.md)

## When the law changes

Watched in the law corpus: the references above, each as its own rule watches it. A change flags this rule, the
qualification types and the request types that use them, and warns the administrators; the corrected rule ships in a
pack update (D294).

## Penalty

As each rule above; not read yet for the lines marked "to read".

## Exceptions

None known; to read per line.

## Open questions

The lines marked "to read" and the unread references.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-209 Reinforced medical follow-up of posts](cr-fr-209-reinforced-medical-follow-up.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-211 Live geolocation of employees](../data-protection/cr-fr-211-live-geolocation-of-employees.md)
