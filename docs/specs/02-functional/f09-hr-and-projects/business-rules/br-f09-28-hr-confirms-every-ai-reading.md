🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-28 HR confirms every AI reading

# 📏 BR-F9-28 HR confirms every AI reading

**Status:** ✅ specified

## Statement

What the AI reads from a document (a CV, a diploma scan or photo, a licence, a certificate, a training record) is saved
"to verify"; it counts only once a person in HR confirms it with the source document beside it, and HR may instead
correct or reject it; each decision keeps who took it and when, and the employee is told what was read.

## Why

- The owner's decisions VD-25 and VD-26
  [D507](../../../06-decisions/f09-hr-and-projects/d507-attributes-entered-by-hand-or-read-by-the-ai-from-documents.md),
  [D508](../../../06-decisions/f09-hr-and-projects/d508-hr-confirms-every-ai-reading-before-it-counts.md): attributes
  are entered by hand or read by the AI from documents, and HR confirms each reading before it counts.
- An AI reading can be wrong; scheduling decides who may do a task, sometimes a task the law ties to a qualification
  (BR-F9-26).
- The readings and the documents are HR documents, with their retention:
  [CR-FR-047 HR records retention](../../../10-country-packs/france/labour/cr-fr-047-hr-records-retention.md).

## Examples

| Case | Result |
|---|---|
| A diploma photo read as "BTS Électrotechnique, EQF level 5, 2019" | To verify; HR confirms; the degree is verified and counts |
| A licence scan read as category C, the licence says C1 | HR corrects it to C1; verified |
| A blurred certificate | HR rejects the reading; the attribute does not count |
| A reading the AI is 99 % sure of | Still to verify: no reading counts without HR |
| The employee opens their profile | They see what was read from which document, and its status |

## Applies to

- [UC-F9-39](../use-cases/13-keep-qualifications/uc-f09-39-read-documents-and-verify.md)
- [UC-F9-38](../use-cases/13-keep-qualifications/uc-f09-38-record-degrees-and-qualifications.md)
- [E-F9-31 Attribute reading](../data/e-f09-31-attribute-reading.md)
- [E-F9-29 Degree](../data/e-f09-29-degree.md)
- [E-F9-12 Qualification](../data/e-f09-12-certification.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F9-27 Unverified or expired attributes do not count](br-f09-27-unverified-attributes-do-not-count.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F9-29 Planners see eligibility, never sensitive details](br-f09-29-planners-see-eligibility-only.md)
