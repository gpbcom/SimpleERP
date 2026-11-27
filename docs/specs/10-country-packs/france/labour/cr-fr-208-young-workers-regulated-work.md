🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) › 👥 [Labour](README.md) ›
⚖️ CR-FR-208 Young workers: forbidden and regulated work

# ⚖️ CR-FR-208 Young workers: forbidden and regulated work

**Status:** ✅ specified

## Statement

A worker under 18 is never given work the law forbids to young workers, and is given work the
law only regulates (such as work on hazardous machines or at height) only when the derogation it requires is on
file and current; night work and the serving of alcohol follow their own limits for young workers ([Code du travail, art. D4153-15 to D4153-37](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488483), [art. R4153-38 to R4153-52](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488561), [art. L3163-2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006902790), [Code de la santé publique, art. L3336-4](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048654800), read 2026-11-27).

## Values

- The age limit: 18 (D4153-15 covers young workers aged 15 to under 18) ([Code du travail, art. D4153-15 to D4153-37](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488483), read 2026-11-27).
  Computed from the birth date, which is used only for age checks (VD-24).
- Forbidden with no derogation in the article: pornographic or violent acts (D4153-16), biological agents of
  groups 3 and 4 (D4153-19), vibrations over the limits (D4153-20), electromagnetic fields over the limits
  (R4153-22-1), access to live bare parts and live work (D4153-24), demolition and trenches (D4153-25), quad
  bikes and tractors without roll-over protection (D4153-26), work in trees (D4153-32), extreme temperatures
  (D4153-36), slaughter and dangerous animals (D4153-37). Regulated, open to the derogation: dangerous chemical
  agents (D4153-17), asbestos at level 1 (D4153-18), ionising radiation from 16 (D4153-21), artificial optical
  radiation (D4153-22), hyperbaric interventions (D4153-23), driving mobile and lifting equipment (D4153-27),
  dangerous machines (D4153-28), maintenance not done when stopped (D4153-29), temporary work at height
  (D4153-30), scaffolding (D4153-31), pressure equipment (D4153-33), confined spaces (D4153-34), molten glass or
  metal (D4153-35) ([Code du travail, art. D4153-15 to D4153-37](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488483), read 2026-11-27).
  Shipped as task codes in the qualification and request-type catalogues
  ([E-F9-30](../../../02-functional/f09-hr-and-projects/data/e-f09-30-qualification-type.md)).
- A derogation on file: the employer's declaration to the labour inspector, sent before the assignment, valid 3
  years from its sending and renewed every 3 years; changes of sector, training or place sent within 8 days; for
  each young worker, identity, birth date, training, medical fitness opinion (yearly), safety training and the
  supervisors kept available (R4153-40 to R4153-45); holders of a matching diploma, an electrical authorisation
  or a driving authorisation may do that work without it (R4153-49 to R4153-52) ([art. R4153-38 to R4153-52](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488561), read 2026-11-27).
- Working time: at most 8 hours a day and 35 a week, no uninterrupted work over 4 hours 30, then a break of 30
  minutes (L3162-1, L3162-3); night work forbidden, save the derogations of the law (L3163-2); minors not
  employed at the bar of a drinks outlet (CSP L3336-4) ([art. L3162-1 to L3162-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037385958), [art. L3163-2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006902790), [Code de la santé publique, art. L3336-4](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048654800), read 2026-11-27). Beside
  [CR-FR-042 Working time and rest](cr-fr-042-working-time-and-rest.md).

## Legal references

- [Code du travail](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/)
  art. D4153-15 to D4153-37 (forbidden and regulated work), R4153-38 to R4153-52 (derogations), L3162-1 to
  L3162-3 (working time), L3163-2 (night work).
- Code de la santé publique art. L3336-4 (minors where alcohol is served).

## Effective dates

Since 2026-04-11, the latest change (D4153-21): D4153-15 in force since 2018-07-01, the
derogation articles R4153-41 to R4153-45 since 2021-02-13, L3162-1 since 2019-01-01, L3163-2 since 2008-05-01, CSP
L3336-4 since 2025-07-01 ([Code du travail, art. D4153-15 to D4153-37](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488483), [art. R4153-38 to R4153-52](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488561), [art. L3162-1 to L3162-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037385958), [art. L3163-2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006902790), [Code de la santé publique, art. L3336-4](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048654800), read 2026-11-27).

## Enforced by

- [BR-F9-26](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md)
- [BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md)
-
  [BR-F9-29](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-29-planners-see-eligibility-only.md);
  the planner sees "not eligible: under 18", never the birth date.
- [E-F2-25 Request type](../../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md)
- [E-F9-01 Employee record](../../../02-functional/f09-hr-and-projects/data/e-f09-01-employee-record.md) (birth date,
  change note of step S4b)
- [REQ-T13-07](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-07-scheduling-engine.md)

## When the law changes

Watched in the law corpus: CT D4153-15 to D4153-37, R4153-38 to R4153-52, L3162-1 to L3163-2; CSP L3336-4. A
change flags this rule and warns the administrators; the corrected rule ships in a pack update (D294).

## Penalty

The fine of a 5th-class contravention, up to 1 500 EUR, for forbidden work (R4743-3) or regulated
work without its conditions (R4743-4), repeat under Code pénal 132-11 and 132-15; under the admission age, once
per person employed (R4743-5, R4743-6); on repeat the court may post and publish the judgment (L4743-1) ([Code du travail, art. R4743-1 to R4743-7](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018494006), [art. L4743-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006903435), [Code pénal, art. 131-13](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006417259), read 2026-11-27).

## Exceptions

Work done under a derogation on file and current (R4153-40 to R4153-45), and the permanent derogations of R4153-49
to R4153-52 ([Code du travail, art. R4153-38 to R4153-52](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000018488561), read 2026-11-27).

## Open questions

No official text was read for this draft; articles, values and dates to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-207 Call recording at work kept proportionate](../data-protection/cr-fr-207-call-recording-proportionate.md) ·
⬆️ [Up](README.md) · ➡️ [CR-FR-209 Reinforced medical follow-up of posts](cr-fr-209-reinforced-medical-follow-up.md)
