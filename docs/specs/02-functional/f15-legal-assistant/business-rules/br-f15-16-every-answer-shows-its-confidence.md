🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-16 Every answer shows its confidence

# 📏 BR-F15-16 Every answer shows its confidence

**Status:** 🔄 waiting for the owner

## Statement

A legal answer shows its confidence: high when every statement cites an article in force that answers it directly,
medium when it relies on guidance or interpretation, low when the corpus covers it only in part; a low confidence always
offers the lawyer hand-off.

## Why

Users must know how far to rely on an answer (D472); answers inform, never advise (BR-F15-02).

## Examples

| Case | Result |
|---|---|
| Leave question answered by L3141-3 and the agreement | passes: high |
| Question on a recent reform with guidance only | passes: medium |
| Question partly covered | passes: low, hand-off offered |

## Applies to

- [UC-F15-12 Hand a question over to a lawyer](../use-cases/01-ask-a-legal-question/uc-f15-12-hand-a-question-over-to-a-lawyer.md)
- [UC-F15-13 Answer a client's tax question with their data](../use-cases/01-ask-a-legal-question/uc-f15-13-answer-a-clients-tax-question-with-their-data.md)
- [UC-F15-01 Use the legal assistant](../use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)
- [UC-F15-03 Check a document against the law](../use-cases/03-check-a-document-against-the-law/uc-f15-03-check-a-document-against-the-law.md)

## Exceptions

Referral topics (BR-F15-02) always offer the hand-off whatever the confidence.

## Configurable

No; (Proposed) the thresholds between levels are set by the quality test set (D200).

## Open questions

None.

---

⬅️ [BR-F15-15 Every AI use inventoried with its risk class](br-f15-15-every-ai-use-inventoried-with-its-risk-class.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F15-17 Warning triggers by block](br-f15-17-warning-triggers-by-block.md)
