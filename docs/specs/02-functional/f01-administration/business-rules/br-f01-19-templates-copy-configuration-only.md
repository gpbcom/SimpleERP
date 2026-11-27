🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-19 Templates copy configuration only

# 📏 BR-F1-19 Templates copy configuration only

**Status:** ✅ specified

## Statement

Creating a client company from a template copies the template's configuration (roles, forms, fields, workflows, sector
pack) and never its data.

## Why

Clients start configured, and no client's data reaches another. See
[D88](../../../06-decisions/f01-administration/d88-client-company-from-a-template.md).

## Examples

| In the template | In the new client company |
|---|---|
| Roles "Sales Lyon", custom fields on quotes | Copied |
| Sector pack construction | Copied |
| Customers, invoices, users | Not copied |
| Connections and AI keys | Not copied: secrets stay with their company |

## Applies to

- [UC-F1-10](../use-cases/08-provider-and-client-companies/uc-f01-10-create-a-client-company-on-the-platform.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-18 Allowed domains](br-f01-18-allowed-domains.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-20 Provider sessions are visible](br-f01-20-provider-sessions-are-visible.md)
