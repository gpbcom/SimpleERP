🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-15 The e-invoicing platform connected step by step

# 📏 BR-F24-15 The e-invoicing platform connected step by step

**Status:** ✅ specified

## Statement

The e-invoicing platform is connected in these steps: choose the platform (Super PDP or B2Brouter first, any platform
through the AFNOR XP Z12-013 adapter), register the company and its addresses, send a test invoice, receive the
acknowledgement, then go live; public buyers go through Chorus Pro (D454).

## Why

[D454](../../../06-decisions/f08-accounting/d454-e-invoicing-platforms.md);
[CR-FR-016 Electronic invoicing](../../../10-country-packs/france/invoicing/cr-fr-016-electronic-invoicing.md),
[CR-FR-017 E-reporting](../../../10-country-packs/france/invoicing/cr-fr-017-e-reporting.md).

## Examples

| Case | Result |
|---|---|
| Super PDP, test invoice accepted | passes: live |
| Platform offering AFNOR XP Z12-013 | passes: generic adapter |
| Test invoice rejected for a missing SIREN | fails: reason shown, not live |

## Applies to

- [UC-F24-24 Connect the e-invoicing platform](../use-cases/06-business-tools/uc-f24-24-connect-the-e-invoicing-platform.md)

## Exceptions

None.

## Configurable

The platform chosen.

## Open questions

None.

---

⬅️ [BR-F24-14](br-f24-14-hr-and-payroll-software-imports-with-their-history.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-16 Every integration shows its icon](br-f24-16-every-integration-shows-its-icon.md)
