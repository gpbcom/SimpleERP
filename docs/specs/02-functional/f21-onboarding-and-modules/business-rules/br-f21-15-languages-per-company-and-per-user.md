🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-15 Languages per company and per user

# 📏 BR-F21-15 Languages per company and per user

**Status:** ✅ specified

## Statement

The company has a default language set in the guide; each user may choose their own interface language; legal documents
(invoices, payslips) follow the country pack's language, with a translation where the law allows.

## Why

Teams are mixed (D478); legal documents follow the country.

## Examples

| Case | Result |
|---|---|
| Company default French, user chooses English | passes: interface in English |
| French invoice for a French customer | passes: French |
| Payslip in English only | fails: French payslip, English copy offered |

## Applies to

- [UC-F21-24 Choose the company's and each user's language](../use-cases/01-first-run/uc-f21-24-choose-the-companys-and-each-users-language.md)

## Exceptions

None.

## Configurable

The languages offered come from T10.

## Open questions

None.

---

⬅️ [BR-F21-14](br-f21-14-the-accountant-joins-with-the-accountant-role.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F21-16 Employees onboard on the phone](br-f21-16-employees-onboard-on-the-phone.md)
