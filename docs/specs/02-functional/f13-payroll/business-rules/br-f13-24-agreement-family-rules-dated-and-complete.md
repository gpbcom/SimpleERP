🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-24 Agreement family rules dated and complete

# 📏 BR-F13-24 Agreement family rules dated and complete

**Status:** ✅ specified

## Statement

An establishment's agreement family supplies dated rules for every pay period; a run whose family has no rules for the
period stays a draft, and an employee whose classification is not in the family's grid is held out of the run.

## Why

Agreements change their minimums several times a year; paying with stale or missing values breaks BR-F13-05 (D470).

## Examples

| Case | Result |
|---|---|
| Hotels-and-restaurants grid dated 1 February used for March | passes |
| Syntec grid missing for the period | fails: run stays a draft, payroll and administrator warned |
| Classification "level 7" absent from the home-help grid | fails: employee held out, HR asked to fix it in F9 |

## Applies to

- [UC-F13-30 Apply the hotels-and-restaurants agreement](../use-cases/09-collective-agreements-by-family/uc-f13-30-apply-the-hotels-and-restaurants-agreement.md)
- [UC-F13-31 Apply the home-help agreement](../use-cases/09-collective-agreements-by-family/uc-f13-31-apply-the-home-help-agreement.md)
- [UC-F13-32 Apply the Syntec agreement](../use-cases/09-collective-agreements-by-family/uc-f13-32-apply-the-syntec-agreement.md)
- [UC-F13-33 Apply the construction agreements](../use-cases/09-collective-agreements-by-family/uc-f13-33-apply-the-construction-agreements.md)
- [UC-F13-01 Set up the company's payroll](../use-cases/01-set-up/uc-f13-01-set-up-the-company-s-payroll.md)
- [UC-F13-05 Apply collective-agreement rules](../use-cases/02-monthly-pay-run/uc-f13-05-apply-collective-agreement-rules.md)
- [UC-F13-19 Update rates and rules from the country pack](../use-cases/05-reports-and-rules/uc-f13-19-update-rates-and-rules-from-the-country-pack.md)

## Exceptions

None.

## Configurable

A company may add company-level supplements above the agreement, never below it.

## Open questions

None.

---

⬅️ [BR-F13-23 Payroll cost split by the analytic axes](br-f13-23-payroll-cost-split-by-the-analytic-axes.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F13-25](br-f13-25-a-posting-needs-an-a1-certificate-or-a-sipsi-declaration.md)
