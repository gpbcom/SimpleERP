🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-15 Vulnerabilities handled under the CRA

# 📏 BR-F25-15 Vulnerabilities handled under the CRA

**Status:** 🔄 waiting for the owner

## Statement

A confirmed vulnerability of SimpleERP is fixed by severity with a failing test first; an actively exploited one is
reported through the EU single reporting platform with an early warning within 24 hours, a notification within 72 hours
and a final report within 14 days after the fix; it is disclosed publicly in a coordinated way once fixed or after
(Proposed) 90 days.

## Why

[CR-FR-168 Cyber Resilience Act reporting](../../../10-country-packs/france/digital/cr-fr-168-cyber-resilience-reporting.md);
reports stay private until then (BR-F25-12).

## Examples

| Case | Result |
|---|---|
| Exploited flaw found 2026-11-12 09:00 | passes: early warning by 2026-11-13 09:00, notification by 2026-11-15 09:00 |
| Fix released 2026-11-14 | passes: final report by 2026-11-28 |
| Researcher's report not exploited | passes: fixed by severity, disclosed with credit once fixed |
| Advisory made public before the fix | fails: refused |

## Applies to

- [UC-F25-22 Handle a reported vulnerability under the CRA](../use-cases/06-vulnerability-handling/uc-f25-22-handle-a-reported-vulnerability-under-the-cra.md)
- [UC-F25-01 Report a bug from SimpleERP](../use-cases/01-intake/uc-f25-01-report-a-bug-from-simpleerp.md)

## Exceptions

None.

## Configurable

The disclosure delay (Proposed) 90 days.

## Open questions

None.

---

⬅️ [BR-F25-14](br-f25-14-triage-with-severity-priority-and-target-times.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-16 Agents' spec pull requests checked first](br-f25-16-agents-spec-pull-requests-checked-first.md)
