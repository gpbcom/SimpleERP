🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-14 The accountant joins with the accountant role

# 📏 BR-F21-14 The accountant joins with the accountant role

**Status:** ✅ specified

## Statement

The external accountant invited during onboarding gets the accountant role for this company only; an accountant who
already has an account is linked, not duplicated, and sees each client company separately.

## Why

The accountant is needed early for balances and the FEC (D478); one account per email (BR-F1-07).

## Examples

| Case | Result |
|---|---|
| Accountant with no account | passes: invited with the accountant role |
| Accountant already serving 30 companies | passes: this company added to their list |
| Accountant invited as administrator | fails: refused, accountant role only |

## Applies to

- [UC-F21-23 Invite the external accountant](../use-cases/03-team-and-data/uc-f21-23-invite-the-external-accountant.md)

## Exceptions

The owner may grant more later (F1).

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F21-13 Opening balances match last year's FEC](br-f21-13-opening-balances-match-last-years-fec.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F21-15 Languages per company and per user](br-f21-15-languages-per-company-and-per-user.md)
