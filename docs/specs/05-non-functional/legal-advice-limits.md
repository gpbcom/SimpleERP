🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › ⚖️ Legal advice limits

# ⚖️ Legal advice limits

**Status:** ✅ specified

## Requirement

The legal assistant (F15) gives legal information, never legal advice: every answer ends with "This is legal
information, not legal advice."; it says what it does not know; for disputes, dismissals, discrimination or harassment,
health and safety emergencies and uncovered questions it refers to a lawyer, the labour inspectorate, the staff
representatives or the Défenseur des droits, and for an emergency gives the emergency numbers first
([D195](../06-decisions/f15-legal-assistant/d195-legal-referral.md),
[BR-F15-02](../02-functional/f15-legal-assistant/business-rules/br-f15-02-information-not-advice.md)). It never judges
facts, never predicts a court's decision, and never decides for the company (warnings inform, never block).

## Measures

- Automated tests of the legal assistant check that every answer carries the notice and that each referral
  topic gets its referral.
- A yearly review of the referral topics with the law pack's maintainers.

## Open questions

None.

---

⬅️ [Legal rules in France](legal-france.md) · ⬆️ [Up](README.md)
