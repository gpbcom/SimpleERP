🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-16 Every employee covered by the mandatory schemes

# 📏 BR-F13-16 Every employee covered by the mandatory schemes

**Status:** 🔄 waiting for the owner

## Statement

Every employee is enrolled in the company's mandatory health scheme and in the provident schemes their agreement or
category requires, unless an exemption the law allows is recorded with its proof; an employee neither enrolled nor
exempted blocks the pay run.

## Why

The employer must offer a collective health scheme and fund part of it, and agreements add provident cover (death,
disability); the law to cite is (Proposed) to read in the France pack (Code de la sécurité sociale L911-7 and the
national agreement on executives' provident cover).

## Examples

| Case | Result |
|---|---|
| New employee enrolled in health and provident on the first day | passes |
| Employee with a spouse's scheme, exemption form and proof kept | passes, no deduction |
| Employee with no enrolment and no exemption | fails: the pay run is blocked for that employee |
| Exemption proof older than its validity | fails: flagged (Proposed) one month before it lapses |

## Applies to

- [UC-F13-21 Enrol employees in health and provident schemes](../use-cases/07-schemes-and-special-contracts/uc-f13-21-enrol-employees-in-health-and-provident-schemes.md)

## Exceptions

Exemptions are only those the country pack lists; the payroll officer records them, never the employee alone.

## Configurable

The company sets its schemes, insurers and the employer's share; it cannot remove the mandatory scheme.

## Open questions

None.

---

⬅️ [BR-F13-15 Payroll assistant, own data only](br-f13-15-payroll-assistant-own-data-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F13-17 Special contracts paid by their own rules](br-f13-17-special-contracts-paid-by-their-own-rules.md)
