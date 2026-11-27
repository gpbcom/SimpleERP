🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D573 Which page wins when two specification pages disagree

# 📜 D573 Which page wins when two specification pages disagree

**Status:** ✅ decided

## Context

The review of the specifications before their confirmation found 10 contradictions between pages: a use case and its
entity, a business rule and a screen, a feature page and a technical capability, a product page and the France
country pack. Each one needed a winner, and the same question will come back whenever two pages drift apart.

## Options

- Ask the owner about each contradiction, one by one.
- Let the most recent page win.
- A fixed precedence between kinds of pages, applied to every contradiction.

## Choice

A fixed precedence, in this order:

1. **The law wins over a business rule:** a rule of the country pack
   ([France](../../10-country-packs/france/README.md)) beats any business rule, use case, entity or screen that says
   otherwise.
2. **A business rule or a use case wins over a screen or a mock-up:** the screen is redrawn to match.
3. **A technical capability wins over a feature page:** what a T capability provides is not redefined by an F page.

The losing page is corrected to say what the winning page says, and cites it when it helps a reader.

## Decided by

The owner, on 2026-11-27.

## Consequences

The 10 contradictions are settled as follows. Screens and mock-ups are corrected by the screens work; every other
losing page is corrected now.

| # | Contradiction | Winner | Pages corrected |
|---|---|---|---|
| 1 | Immediate advance of the home-services tax credit: what happens when the client does not validate | Law: validated automatically after 48 hours, URSSAF pays the whole service and debits the client's share ([CR-FR-104](../../10-country-packs/france/tax-and-vat/cr-fr-104-immediate-advance-of-tax-credit.md)) | [UC-SC04-10](../../08-sectors/sc04-home-care/use-cases/04-bill-and-fund/uc-sc04-10-use-the-immediate-advance.md) (alternative 3e), [E-SC04-13](../../08-sectors/sc04-home-care/data/e-sc04-13-immediate-advance-claim.md) (no Expired state, "validated by"), [BR-SC04-13](../../08-sectors/sc04-home-care/business-rules/br-sc04-13-immediate-advance-on-request.md), [UC-SC19-12](../../08-sectors/sc19-trades-and-home-services/use-cases/03-home-services-tax-credit/uc-sc19-12-use-the-immediate-advance.md), [BR-SC19-12](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-12-the-advance-needs-the-customers-consent.md) |
| 2 | The meeting preparation brief: read-only or editable | Use case: the organiser edits it ([UC-F4-09](../../02-functional/f04-meetings/use-cases/README.md)) | [E-F4-24](../../02-functional/f04-meetings/data/e-f04-24-meeting-prep-brief.md); screen S-F4-08 to redraw |
| 3 | The meeting bot's name: fixed or editable | Business rule [BR-F4-01](../../02-functional/f04-meetings/business-rules/README.md) | [E-F4-25](../../02-functional/f04-meetings/data/e-f04-25-meeting-recording-setting.md), [E-F4-18](../../02-functional/f04-meetings/data/e-f04-18-recording-notice.md); screen S-F4-07 to redraw |
| 4 | Lunch orders: one per employee or one per team | Use case: one per employee ([UC-F9-13](../../02-functional/f09-hr-and-projects/use-cases/README.md)) | [E-F9-39](../../02-functional/f09-hr-and-projects/data/e-f09-39-lunch-order.md); list view S-F9-L39 to redraw |
| 5 | The personnel register: one per company and year, or one per establishment | Law: one per establishment ([CR-FR-038](../../10-country-packs/france/labour/cr-fr-038-personnel-register.md)) | [E-F9-40](../../02-functional/f09-hr-and-projects/data/e-f09-40-personnel-register.md), [BR-F9-03](../../02-functional/f09-hr-and-projects/business-rules/README.md), [UC-F9-03](../../02-functional/f09-hr-and-projects/use-cases/README.md), [D287](../f09-hr-and-projects/d287-french-hr-duties.md); list view S-F9-L40 to redraw |
| 6 | The occupational risk assessment: one document per work unit, or one document listing every work unit | Law: one document listing every work unit (Code du travail R4121-1, [CR-FR-076](../../10-country-packs/france/labour/cr-fr-076-occupational-risk-assessment.md)) | [BR-F9-19](../../02-functional/f09-hr-and-projects/business-rules/br-f09-19-the-risk-assessment-is-versioned-and-kept.md), [UC-F9-27](../../02-functional/f09-hr-and-projects/use-cases/README.md), [E-F9-24](../../02-functional/f09-hr-and-projects/data/README.md), [BR-F12-15](../../02-functional/f12-manufacturing/business-rules/br-f12-15-risk-assessment-versions-kept.md), [UC-F12-17](../../02-functional/f12-manufacturing/use-cases/07-compliance-and-safety/uc-f12-17-keep-the-risk-assessment-and-safety-registers.md), [E-F12-26](../../02-functional/f12-manufacturing/data/e-f12-26-risk-assessment.md); screen S-F9-24 to redraw |
| 7 | Unbuilding a product: a separate entity or a kind of manufacturing order | Use case and business rules: a kind of [E-F12-04 Manufacturing order](../../02-functional/f12-manufacturing/data/e-f12-04-manufacturing-order.md) (make, unbuild, rework, repair, subcontract) | [E-F12-29](../../02-functional/f12-manufacturing/data/e-f12-29-unbuild-order.md) now points to E-F12-04, [UC-F12-11](../../02-functional/f12-manufacturing/use-cases/03-make-the-products/uc-f12-11-unbuild-rework-and-repair.md), [FL-F12-03](../../02-functional/f12-manufacturing/flows/fl-f12-03-make-the-products.md), the [P8 roadmap phase](../../00-vision/roadmap/phases/09-p8-plugins-and-the-plugin-store.md); screens S-F12-11 and S-F12-L29 to redraw |
| 8 | Where the law pack takes its sources | Technical capability: the [T11 legal corpora](../../03-technical/t11-legal-corpora/README.md) own the sources, their licences and their schedule | [E-F15-01](../../02-functional/f15-legal-assistant/data/README.md) (corpora instead of its own sources list), BR-F15-09, E-F15-12; screens S-F15-05 and S-F15-L12 to redraw |
| 9 | The channels of a consent record | Use cases: postal mail and push are channels too ([UC-F5-26](../../02-functional/f05-social-media/use-cases/10-referrals-push-and-listening/uc-f05-26-send-push-notifications.md), [UC-F5-28](../../02-functional/f05-social-media/use-cases/10-referrals-push-and-listening/uc-f05-28-send-postal-mail-campaigns.md)) | [E-F5-10](../../02-functional/f05-social-media/data/e-f05-10-consent-and-suppression-record.md) |
| 10 | How often an integration is reviewed | Business rule: yearly ([BR-F24-06](../../02-functional/f24-integrations-hub/business-rules/README.md)) | [E-F24-15](../../02-functional/f24-integrations-hub/data/README.md) and the other non-screen pages already said yearly; screen S-F24-18 to redraw with every state |

- A contradiction found later is settled with the same precedence, without a new decision.
- Two pages of the same kind that disagree (two business rules, two use cases) are not covered: they become a question
  for the owner.

## Related

- [D572 The owner's proposals confirmed in bulk](d572-proposals-confirmed-in-bulk.md)
- [D516 Naming rules and the seven classes of names](d516-naming-rules-and-the-seven-classes-of-names.md)
- [Legal rules in France](../../05-non-functional/legal-france.md)

---

⬅️ [D572](d572-proposals-confirmed-in-bulk.md) · ⬆️ [Up](README.md) ·
➡️ [D574](d574-lawyer-review-before-launch.md)
