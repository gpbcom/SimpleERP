🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-13 Automation tools through signed webhooks and the API

# 📏 BR-F24-13 Automation tools through signed webhooks and the API

**Status:** ✅ specified

## Statement

Automation tools (n8n, Make, Zapier) connect through webhooks signed with a secret and through the API (T5) with a token
of a service account whose rights the administrator chooses; a webhook failing after the retries is paused and the
administrator told.

## Why

Automation tools were absent (D481); every action keeps the rights model (BR-F24-04).

## Examples

| Case | Result |
|---|---|
| n8n receiving "invoice paid" with a valid signature | passes |
| Zapier token with "sales" rights writing a payslip | fails: refused by rights |
| Endpoint failing 10 times | passes: paused, administrator told |

## Applies to

- [UC-F24-22 Automate with n8n, Make or Zapier](../use-cases/06-business-tools/uc-f24-22-automate-with-n8n-make-or-zapier.md)
- [UC-F24-20 Control the rights and costs of connectors](../use-cases/04-run-and-control/uc-f24-20-control-the-rights-and-costs-of-connectors.md)

## Exceptions

None.

## Configurable

Events offered, retry count and the service account's rights.

## Open questions

None.

---

⬅️ [BR-F24-12 The catalogue covers every business category](br-f24-12-the-catalogue-covers-every-business-category.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F24-14](br-f24-14-hr-and-payroll-software-imports-with-their-history.md)
