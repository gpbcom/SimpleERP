🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) › 👥 [Labour](README.md) ›
⚖️ CR-FR-208 Young workers: forbidden and regulated work

# ⚖️ CR-FR-208 Young workers: forbidden and regulated work

**Status:** 🔄 draft (GH-2 step S4b, from VD-24, VD-27, VD-29 / D506, D509, D511)

## Statement

(Proposed) A worker under 18 is never given work the law forbids to young workers, and is given work the law only
regulates (such as work on hazardous machines or at height) only when the derogation it requires is on file and
current; night work and the serving of alcohol follow their own limits for young workers.

## Values

- (Proposed) The age limit: 18, computed from the birth date, which is used only for age checks (VD-24).
- (Proposed) The list of forbidden tasks and of regulated tasks with their derogation: to read, then shipped as task
  codes in the qualification and request-type catalogues
  ([E-F9-30](../../../02-functional/f09-hr-and-projects/data/e-f09-30-qualification-type.md)).
- (Proposed) A derogation on file: its date, its tasks, its validity, to read.
- (Proposed) Night work and working-time limits for young workers: to read, beside
  [CR-FR-042 Working time and rest](cr-fr-042-working-time-and-rest.md).

## Legal references

- (Proposed) To read: Code du travail, the provisions on work forbidden to young workers and on the work they may do
  under a derogation.
- (Proposed) To read: Code du travail, the provisions on young workers' night work and working time.
- (Proposed) To read: Code de la santé publique, the provisions on minors working where alcohol is served.

## Effective dates

(Proposed) To read.

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

Watched in the law corpus: (Proposed) the young-worker provisions of the Code du travail once their articles are read. A
change flags this rule and warns the administrators; the corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

(Proposed) Work done under a derogation on file and current; to read.

## Open questions

No official text was read for this draft; articles, values and dates to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-207 Call recording at work kept proportionate](../data-protection/cr-fr-207-call-recording-proportionate.md) ·
⬆️ [Up](README.md) · ➡️ [CR-FR-209 Reinforced medical follow-up of posts](cr-fr-209-reinforced-medical-follow-up.md)
