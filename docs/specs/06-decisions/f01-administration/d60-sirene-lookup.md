🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D60 SIRENE lookup

# 📜 D60 SIRENE lookup

**Status:** ✅ decided

## Context

Whether the setup may look a French company up in the public SIRENE register from its SIREN.

## Options

- Yes, optional.
- No, manual only.

## Choice

Yes: typing the SIREN fills the name, legal form, address and establishments (SIRET) from the official open data, which
the administrator checks. It is an outside call, so an administrator can turn it off.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The only outside call of the setup; listed in the connections settings (F1).

## Related

- [UC-F1-01](../../02-functional/f01-administration/use-cases/01-guided-setup/uc-f01-01-set-up-a-new-company.md)

---

⬅️ [D59 Every setup step required](d59-every-setup-step-required.md) · ⬆️ [Up](README.md) ·
➡️ [D61 Setup imports](d61-setup-imports.md)
