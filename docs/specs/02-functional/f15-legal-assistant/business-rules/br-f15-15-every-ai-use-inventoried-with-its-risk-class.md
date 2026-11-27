🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-15 Every AI use inventoried with its risk class

# 📏 BR-F15-15 Every AI use inventoried with its risk class

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

Each AI feature the company turns on is listed in the AI uses inventory with its purpose, provider, data used and risk
class; a high-risk use stays off until the company accepts its deployer duties and an impact assessment is approved.

## Why

[CR-FR-056](../../../10-country-packs/france/ai-and-recording/cr-fr-056-people-know-they-deal-with-an-ai.md),
[CR-FR-057](../../../10-country-packs/france/ai-and-recording/cr-fr-057-human-oversight.md),
[CR-FR-058](../../../10-country-packs/france/ai-and-recording/cr-fr-058-high-risk-ai-in-employment.md); the impact
assessment under the GDPR: (⚖️ lawyer review before launch, D574) to read: GDPR article 35 and the CNIL's list.

## Examples

| Case | Result |
|---|---|
| Assistant on the local model, limited risk | passes: listed, no assessment |
| Candidate scoring turned on | fails until the deployer duties are accepted and the assessment approved |
| AI feature turned on with no inventory line | passes: the line is created at once from the feature's settings |

## Applies to

- [UC-F15-11 Keep the AI uses inventory and impact assessments](../use-cases/06-privacy-and-ai-duties/uc-f15-11-keep-the-ai-uses-inventory-and-impact-assessments.md)
- [UC-F15-04 Set up the legal assistant](../use-cases/04-set-up-the-legal-assistant/uc-f15-04-set-up-the-legal-assistant.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-14](br-f15-14-data-subject-requests-answered-within-one-month.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-16 Every answer shows its confidence](br-f15-16-every-answer-shows-its-confidence.md)
