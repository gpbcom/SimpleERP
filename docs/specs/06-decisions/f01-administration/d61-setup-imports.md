🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D61 Setup imports

# 📜 D61 Setup imports

**Status:** ✅ decided

## Context

What the setup can import (step 6).

## Options

- Spreadsheet templates.
- Opening balances from the FEC.
- Other ERPs.
- Nothing at setup.

## Choice

Spreadsheet templates (CSV or Excel) for customers, suppliers, products and employees; the chart of accounts and opening
balances from the previous software's FEC; and other ERPs (Odoo, Dolibarr, Sage, EBP) through import plugins.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Import plugins use the plugin API (T4), like any plugin.

## Related

- [UC-F1-01](../../02-functional/f01-administration/use-cases/01-guided-setup/uc-f01-01-set-up-a-new-company.md)

---

⬅️ [D60 SIRENE lookup](d60-sirene-lookup.md) · ⬆️ [Up](README.md) ·
➡️ [D62 The AI assistant in the setup](d62-assistant-in-setup.md)
