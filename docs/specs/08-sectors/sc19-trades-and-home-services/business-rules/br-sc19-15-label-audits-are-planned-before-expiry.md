🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-15 Label audits are planned before expiry

# 📏 BR-SC19-15 Label audits are planned before expiry

**Status:** 🔄 waiting for the owner

## Statement

A label's audit is planned before its expiry and a label past its validity covers nothing: quotes of its scopes are
refused and the grants of those quotes are dropped. A scope with no qualified person is flagged.

## Why

A lapsed label makes the customer lose a grant and the company liable
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Label valid for the scope | the quote may carry the grant |
| Label expired | quotes refused, grants dropped |
| Audit in 90 days | planned and shown |
| Qualified person leaves | scope flagged |
| Audit failed | grants of that scope stopped |

## Applies to

- [UC-SC19-15](../use-cases/04-installations-and-labels/uc-sc19-15-keep-the-rge-label-evidence.md)
- [E-SC19-09 Label](../data/e-sc19-09-label.md)
- [E-SC19-09 Label](../data/e-sc19-09-label.md)
- [E-F9-12](../../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md)

## Exceptions

None.

## Configurable

The days before expiry for the audit reminder, set by the owner.

## Open questions

None.

---

⬅️ [BR-SC19-14 Grants need the label at signature](br-sc19-14-grants-need-the-label-at-signature.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC19-16](br-sc19-16-refrigerant-handling-needs-a-certified-technician.md)
