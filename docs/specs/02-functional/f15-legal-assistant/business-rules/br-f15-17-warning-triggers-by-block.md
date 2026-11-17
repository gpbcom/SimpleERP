🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-17 Warning triggers by block

# 📏 BR-F15-17 Warning triggers by block

**Status:** 🔄 waiting for the owner

## Statement

The warnings the French law pack ships with are the four families of D202 (working and rest times, leave and absences,
contracts and HR steps, thresholds and duties) raised from F9; the other blocks raise the triggers of the catalogue
below, each citing its country-pack rule.

## Why

UC-F15-02 needs the list of what the ERP sees as a legal risk (D472).

## Examples

| Case | Result |
|---|---|
| F9: a schedule breaking daily rest (CR-FR-042) | warning |
| F9: a fixed-term contract with a third renewal (CR-FR-041) | warning |
| F9: headcount crossing 11 or 50 (CR-FR-046) | warning to HR and the owner |
| F6: payment terms above 60 days (CR-FR-018) | (Proposed) warning |
| F6: an invoice missing a mandatory mention (CR-FR-015) | (Proposed) warning |
| F6 and F10: a cash payment above the limit (CR-FR-022) | (Proposed) warning |
| F5: a marketing message without consent (CR-FR-063) | (Proposed) warning |
| F13: a pay below the minimum wage (CR-FR-185) | blocked by F13 itself (BR-F13-04), not a warning |

## Applies to

- [UC-F15-07 Keep the compliance calendar](../use-cases/05-duties-and-records/uc-f15-07-keep-the-compliance-calendar.md)
- [UC-F15-02 Receive a legal warning](../use-cases/02-receive-a-legal-warning/uc-f15-02-receive-a-legal-warning.md)
- [UC-F15-04 Set up the legal assistant](../use-cases/04-set-up-the-legal-assistant/uc-f15-04-set-up-the-legal-assistant.md)

## Exceptions

Warnings turned off by the administrator (D193) show none.

## Configurable

Each trigger can be turned off per company; the families of D202 are on by default.

## Open questions

None.

---

⬅️ [BR-F15-16 Every answer shows its confidence](br-f15-16-every-answer-shows-its-confidence.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-18](br-f15-18-the-share-movement-register-is-written-before-a-transfer-is-final.md)
