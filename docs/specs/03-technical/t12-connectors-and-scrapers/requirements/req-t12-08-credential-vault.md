🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-08 Credentials stored safely

# 📌 REQ-T12-08 Credentials stored safely

**Status:** ✅ specified

## Statement

Every customer credential (password, API key, OAuth refresh token, TOTP seed, client certificate) lives only
in a dedicated self-hosted secrets vault, never in the application database, logs, traces, prompts, exports, backups in
clear or Git. Envelope encryption: a data key per company (T1), wrapped by a master key in an HSM or KMS (on a
SecNumCloud host, the qualified provider's); AES-256-GCM. Entry is write-only: a secret is never shown again (only its
last 4 characters). It is decrypted only inside the sandboxed run that needs it, in memory, for that run; a model never
sees it: agents name a credential by handle and the runtime fills it in. Only the connector runtime identity can read;
administrators can replace or revoke, never read; every use is audited (which run, which action, when) and unusual use
alerts. OAuth with narrow scopes and service accounts are preferred; rotation reminders and automatic rotation where the
tool allows; removal destroys the key (crypto-shredding). Customer-managed keys (BYOK, HYOK) are supported. A customer
never sends a credential by email or chat: they enter it themselves, or through a one-time secure link into their own
vault, which the SimpleERP provider's staff cannot read.

A TOTP seed is wrapped by a key separate from its password's, so that one leak never gives both factors; where the owner
prefers, the owner is asked for each code instead.

## Why

Customers trust SimpleERP with keys to their systems
([D240](../../../06-decisions/security-and-compliance/d240-credential-vault.md)).

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A secret entered is unreadable in the database, logs and prompts; a run's audit shows its use; revocation stops the next
run.

## Measure

Secrets outside the vault: zero; audited uses: all.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-07 Fetch ladder](req-t12-07-fetch-ladder.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-09 Sandbox for connectors and generated code](req-t12-09-sandbox-isolation.md)
