🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-21 Candidate scoring is high-risk AI

# 📏 BR-F4-21 Candidate scoring is high-risk AI

**Status:** ✅ specified

## Statement

Candidate evaluation scores and match scores are a high-risk AI use (EU AI Act, Annex III, point 4). Therefore:
candidates are told an AI is used and how; a recruiter must validate every score and no decision is taken on a score
alone (human oversight); scores, inputs and validations are logged; the criteria are job-related and checked for bias;
candidates can ask for an explanation and a human review; the feature is off until the company turns it on and accepts
its deployer duties; SimpleERP, as provider, keeps the technical documentation, risk management and conformity
assessment it needs.

## Why

The owner chose to score candidates (D234); the law then sets these duties. Until 2027-12-01 the AI Act's high-risk
duties do not apply yet to Annex III uses; from 2027-12-02 they do (CR-FR-058, after the AI Omnibus); this rule holds
on both dates. See
[AI governance](../../../05-non-functional/ai-governance.md).

Legal values from the France country pack:
[CR-FR-058 AI in recruitment and work is high-risk](../../../10-country-packs/france/ai-and-recording/cr-fr-058-high-risk-ai-in-employment.md).

## Examples

| Case | Result |
|---|---|
| Grid pre-filled with scores | Shown "to validate"; not visible to the hiring manager until validated |
| A candidate asks why | The criteria, the quoted answers and the recruiter's validation |
| The company has not turned it on | Interviews are captured and reported, without scores |

## Applies to

- [UC-F4-13](../use-cases/09-score-calls-and-interviews/uc-f04-13-interview-a-candidate.md)

## Exceptions

None.

## Configurable

Turned on per company by an administrator, after accepting the deployer duties.

## Open questions

None.

---

⬅️ [BR-F4-20 Scores come with their evidence](br-f04-20-scores-come-with-their-evidence.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-22 Only chosen content leaves](br-f04-22-only-chosen-content-leaves.md)
