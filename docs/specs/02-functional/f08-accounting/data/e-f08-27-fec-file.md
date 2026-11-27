🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F8-27 FEC file

# 🗃️ E-F8-27 FEC file

**Status:** 🔄 waiting for the owner

## Purpose

(Proposed) The FEC file the flow charts name with the words "FEC"
([FL-F1-14](../../f01-administration/flows/fl-f01-14-close-a-company.md),
[FL-F21-05](../../f21-onboarding-and-modules/flows/fl-f21-05-migration-from-another-tool.md),
[FL-F8-01](../flows/fl-f08-01-set-up-and-post.md), [FL-F8-05](../flows/fl-f08-05-close-report-and-consolidate.md)). The
owner decided to create it
([D516](../../../06-decisions/foundations/d516-naming-rules-and-the-seven-classes-of-names.md)); what it holds waits for
the owner's confirmation.

## Fields

(Proposed) To define with the owner: the flow charts name the record, not its fields.

## Relations

(Proposed) To define with the owner, from the use cases below.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F1-23
```

## Indexes and search

(Proposed) To define with the owner.

## Retention

(Proposed) As the other records of its capability, to confirm with the owner.

## Audit

(Proposed) Every change, as the other records of its capability.

## Import and export

(Proposed) To define with the owner.

## Used by

- [UC-F1-23 Close a company and export all its data](../../f01-administration/use-cases/14-close-a-company/uc-f01-23-close-a-company-and-export-all-its-data.md)
- [UC-F21-22 Check opening balances against last year's FEC](../../f21-onboarding-and-modules/use-cases/05-migration-from-another-tool/uc-f21-22-check-opening-balances-against-last-years-fec.md)
- [UC-F8-01 Set up the books](../use-cases/01-set-up-and-post/uc-f08-01-set-up-the-books.md)
- [UC-F8-10 Close the period and the year](../use-cases/05-close-report-and-consolidate/uc-f08-10-close-the-period-and-the-year.md)

## Open questions

(Proposed) Its fields, relations and states wait for the owner (waiting list, step 36e).

---

⬅️ [E-F8-26 Accountant request](e-f08-26-accountant-request.md) · ⬆️ [Up](README.md) ·
➡️ [E-F8-28 Payment run](e-f08-28-payment-run.md)
