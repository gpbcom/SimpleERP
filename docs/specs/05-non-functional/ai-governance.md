🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 🤖 AI governance

# 🤖 AI governance

**Status:** 🔄 waiting for the owner

## Requirement

- **Transparency (EU AI Act, article 50):** users and outside people know when an AI transcribes, summarises, drafts or
  answers (F3, F4, F15).
- **High-risk use: scoring candidates (Annex III, point 4).** The owner chose to score candidates and give match scores
  (D234). simple-ERP, as provider, needs for that feature: a risk management system, data governance and bias checks of
  the criteria, technical documentation, logging, instructions for use, human oversight built in (a recruiter validates
  every score), accuracy and robustness measures, a conformity assessment, CE marking and registration in the EU
  database. The company, as deployer, must turn the feature on knowingly, inform candidates, ensure human oversight and
  keep the logs (BR-F4-21). The dates these obligations apply from must be checked at build time.
- **High-risk use: ranking LinkedIn profiles (Annex III, point 4(a))**
  ([D518](../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)): the AI assistant scores the
  profiles of a sourcing search with a reason per score (UC-F9-40); HR approves the shortlist before anyone is contacted
  (BR-F9-36), which is the human oversight; the same provider and deployer duties as candidate scoring apply.
- **Not decided by AI alone:** no decision about a person is taken on a score alone (GDPR article 22).

- **Autonomy tiers** ([D439](../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md)): the AI assistant asks before
  every write; agents and automations act alone only within a procedure an administrator switched to automatic, within
  its limits, audited and sampled; never alone for payments, legal sendings, deletions or decisions about a person. This
  is simple-ERP's product policy; the AI Act's own oversight duties are in CR-FR-057.

- **High-risk use: evaluating workers (Annex III, point 4)**
  ([D449](../06-decisions/f04-meetings/d449-call-recording-off-by-default.md)): call scoring (UC-F4-12) and any score of
  an employee's work carry the same provider and deployer duties as candidate scoring; off by default, switched on
  knowingly, the staff committee consulted and workers told.

## Measures

- (Proposed) 5 % of each automatic procedure's acts, at least 10 a week, sampled for a person's check (D439).
- A risk file per high-risk feature (candidate scoring, call scoring and worker evaluation), with its evaluation set
  (REQ-T07-05) and its logs kept.
- Impact assessments as [Privacy and GDPR](privacy-gdpr.md) lists them.

## Country pack

The legal values this page relies on, from the France country pack (D293):

- [CR-FR-058 AI in recruitment and work is high-risk](../10-country-packs/france/ai-and-recording/cr-fr-058-high-risk-ai-in-employment.md)
- [CR-FR-057 Human oversight of high-risk AI](../10-country-packs/france/ai-and-recording/cr-fr-057-human-oversight.md)
- [CR-FR-206 Staff committee consulted before monitoring tools](../10-country-packs/france/labour/cr-fr-206-cse-consulted-on-monitoring.md)

## Open questions

⬜ To be specified.

---

⬅️ [Accessibility](accessibility.md) · ⬆️ [Up](README.md) · ➡️ [Meeting recording](meeting-recording.md)
