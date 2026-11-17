🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 📒 [Accounting](README.md) › 🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Accounting (U05) | External accountant (U08) | Owner (U13) | Manager (U02) | Employee (U01) | Administrator (U07) |
|---|---|---|---|---|---|---|
| Set up the books | ✅ | ✅ | - | - | - | ✅ company settings |
| Post entries | ✅ | ✅ | - | - | - | - |
| Review, annotate | ✅ | ✅ | ✅ read | - | - | - |
| Payments: prepare | ✅ | - | - | - | - | - |
| Payments: approve batches | - | - | ✅ | - | - | - |
| IBAN changes: second approval | ✅ | - | ✅ | - | - | - |
| VAT and filings: validate | - | ✅ | - | - | - | - |
| Lock periods | - | ✅ | - | - | - | - |
| Reports | ✅ | ✅ | ✅ | budgets of their plans | - | - |
| Expenses | approve above 500 EUR, reimburse | - | - | approve | submit | - |

## Record rules

- Posted entries never change (BR-F8-01); locked periods refuse entries (BR-F8-02).
- The external accountant sees only the client companies that granted access (D11).
- Employees see only their own expenses.

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
