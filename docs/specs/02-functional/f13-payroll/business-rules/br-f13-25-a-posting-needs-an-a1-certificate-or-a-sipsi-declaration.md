🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-25 A posting needs an A1 certificate or a SIPSI declaration

# 📏 BR-F13-25 A posting needs an A1 certificate or a SIPSI declaration

**Status:** ✅ specified

## Statement

A posting becomes Documented, and so can be paid as a posting, only when it holds the paper its direction needs: an A1
certificate whose dates cover the whole posting for an employee posted abroad, or the receipt of the posting declaration
for a worker posted to France.

## Why

The paper is what makes the posting lawful and decides which social security scheme applies; paying posting allowances
without it exposes the company to back contributions and fines. The owner asked for posted workers
([D532](../../../06-decisions/f13-payroll/d532-benchmark-gaps-f13-payroll.md)). The France-pack rule is
[CR-FR-218 Posted workers and the SIPSI declaration](../../../10-country-packs/france/labour/cr-fr-218-posted-workers-sipsi.md): an A1
certificate for up to 24 months out, a SIPSI declaration before a posting to France starts.

## Examples

| Case | Result |
|---|---|
| Posted abroad, A1 covering all dates | Documented |
| Posted abroad, A1 ending a month early | refused with the uncovered days |
| Posted to France, declaration receipt recorded | Documented |
| Posted to France, no receipt | stays Draft |
| An A1 that expires during an Active posting | a warning 30 days before, and the pay run blocks that employee after the end date |

## Applies to

- [UC-F13-35](../use-cases/10-special-contracts-and-outsourcing/uc-f13-35-pay-posted-workers.md)
- [E-F13-28 Posting](../data/e-f13-28-posting.md)
- [E-F13-18 Special pay regime](../data/e-f13-18-special-pay-regime.md)
- France-pack rule:
  [CR-FR-218 Posted workers and the SIPSI declaration](../../../10-country-packs/france/labour/cr-fr-218-posted-workers-sipsi.md)

## Exceptions

None.

## Configurable

The warning delay (30 days by default), by the payroll officer.

## Open questions

None.

---

⬅️ [BR-F13-24 Agreement family rules dated and complete](br-f13-24-agreement-family-rules-dated-and-complete.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F13-26 Days worked never exceed the package](br-f13-26-days-worked-never-exceed-the-package.md)
