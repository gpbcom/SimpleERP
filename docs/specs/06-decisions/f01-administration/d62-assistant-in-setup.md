🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D62 The AI assistant in the setup

# 📜 D62 The AI assistant in the setup

**Status:** ✅ decided

## Context

What the AI assistant may do during the setup.

## Options

- Explain and suggest.
- Fill steps on the administrator's approval.
- No AI in the setup.

## Choice

Both: the AI assistant explains fields and suggests the sector pack from the company's activity code (NAF), and it can
prefill whole steps (for example the sites from the SIRENE establishments, or users from a pasted list), which the
administrator approves before they are saved.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Nothing the AI assistant prepares is saved without the administrator's approval. No API, MCP or A2A access to the setup.

## Related

- [UC-F1-01](../../02-functional/f01-administration/use-cases/01-guided-setup/uc-f01-01-set-up-a-new-company.md)

---

⬅️ [D61 Setup imports](d61-setup-imports.md) · ⬆️ [Up](README.md) ·
➡️ [D63 Who changes sites](d63-who-changes-sites.md)
