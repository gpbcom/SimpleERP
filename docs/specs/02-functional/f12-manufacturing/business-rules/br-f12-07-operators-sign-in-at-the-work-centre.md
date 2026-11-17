🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-07 Operators sign in at the work centre

# 📏 BR-F12-07 Operators sign in at the work centre

**Status:** ✅ specified

## Statement

On a shared tablet each operator signs in with a badge or PIN, so work is recorded under their name; time recorded feeds
F9 within the working-time rules:
[CR-FR-042 Working time and rest](../../../10-country-packs/france/labour/cr-fr-042-working-time-and-rest.md).

## Why

See [D313](../../../06-decisions/f12-manufacturing/d313-manufacturing-personas.md).

## Examples

| Case | Result |
|---|---|
| Shift change | The next operator signs in, the open operation continues under their name |

## Applies to

Every F12 use case concerned.

- [UC-F12-22 Require operator qualifications per work centre](../use-cases/10-people-and-tools/uc-f12-22-require-operator-qualifications-per-work-centre.md)

## Exceptions

None.

## Configurable

Badge, PIN or both.

## Open questions

None.

---

⬅️ [BR-F12-06 A failed check blocks the step](br-f12-06-a-failed-check-blocks-the-step.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-08 Machine data through connectors](br-f12-08-machine-data-through-connectors.md)
