🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T02-01 Keycloak for every user

# 📌 REQ-T02-01 Keycloak for every user

**Status:** ✅ specified

## Statement

Every user signs in through Keycloak: single sign-on with the company's providers, passkeys preferred, two factors for
every user (D450); a fresh sign-in is required before a link opens a payslip or personal data.

## Why

Confirmed by the owner on 2026-11-12; D85, D414.

Revised by D450 on 2026-11-12.

## Acceptance criteria

1. **Given** any user without a second factor, sign-in is refused until one is set.
2. **Given** a company's provider, single sign-on works.

## Measure

Sign-ins by method.

## Priority

Must

## Capabilities served

All: F1 to F25 and the sectors SC01 to SC16.

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [REQ-T02-02 Rights as policies in one library](req-t02-02-policies-one-library.md)
