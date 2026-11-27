🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-13 Company-law deadlines kept

# 📏 BR-F15-13 Company-law deadlines kept

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

The company's general meetings, decisions and registers follow the deadlines and forms of its legal form in the law
pack: the accounts are approved within the legal delay after the year end, decisions are recorded in the register, and
changes of beneficial owners are declared.

## Why

Company law sets these duties. The approval of the accounts within six months of the year end, which the court can
extend, is read in [CR-FR-221 Shareholders' general meetings](../../../10-country-packs/france/company/cr-fr-221-general-meetings.md) (SARL);
(⚖️ lawyer review before launch, D574) the beneficial-owner declaration is still to read: Code monétaire et financier L561-45-1 and
L561-46.

## Examples

| Case | Result |
|---|---|
| Year end 2026-12-31, approval held on 2027-06-20 | passes |
| Approval not held by 2027-06-30 | fails: overdue, extension request suggested |
| Beneficial owner changed, no declaration | fails: duty created in the calendar |

## Applies to

- [UC-F15-09 Approve the accounts and keep the company registers](../use-cases/05-duties-and-records/uc-f15-09-approve-the-accounts-and-keep-the-company-registers.md)

## Exceptions

None.

## Configurable

The legal form chooses the rules; the company cannot remove them.

## Open questions

None.

---

⬅️ [BR-F15-12 Notice dates computed before renewals](br-f15-12-notice-dates-computed-before-renewals.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F15-14](br-f15-14-data-subject-requests-answered-within-one-month.md)
