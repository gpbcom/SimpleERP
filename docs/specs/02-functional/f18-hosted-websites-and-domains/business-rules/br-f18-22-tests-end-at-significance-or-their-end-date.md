🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-22 Tests end at significance or their end date

# 📏 BR-F18-22 Tests end at significance or their end date

**Status:** 🔄 waiting for the owner

## Statement

A page test ends when one version beats the other at the required level of certainty (95 % by default) with at least the
minimum visitors per version and the minimum days, or at its end date, whichever comes first; at the end date without
that certainty there is no winner, and a winner is published only after the approval of the site's publication gate.

## Why

Stopping a test as soon as a version looks ahead makes chance look like a result; and a page that changes by itself
breaks the rule that the customer approves what goes live. The owner asked for page tests
[D537](../../../06-decisions/f18-hosted-websites-and-domains/d537-benchmark-gaps-f18-hosted-websites-and-domains.md).

## Examples

| Case | Result |
|---|---|
| Version B ahead at 96 % after 1,187 visitors and 9 days | ends, B is the winner awaiting approval |
| Version B ahead at 80 % at the end date | ends with no winner, the original stays |
| Version B ahead at 97 % after 120 visitors | keeps running: below the minimum visitors |
| Version B ahead at 97 % on day 3 | keeps running: below the minimum days |
| A winner at significance | published only when the owner approves |

## Applies to

- [UC-F18-28](../use-cases/07-tests-visitors-and-accessibility/uc-f18-28-a-b-test-a-page.md)
- [E-F18-20 Page test](../data/e-f18-20-page-test.md)
- [E-F18-02 Page](../data/e-f18-02-page.md)
- [E-F18-10 Publication check report](../data/e-f18-10-publication-check-report.md)

## Exceptions

A marketing person may stop a test early when a version breaks the page; the test then has no winner.

## Configurable

The level of certainty, the minimum visitors and the minimum days, by the owner.

## Open questions

None.

---

⬅️ [BR-F18-21](br-f18-21-sites-backed-up-daily-restored-to-the-preview.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-23 Visits are tracked only with consent](br-f18-23-visits-are-tracked-only-with-consent.md)
