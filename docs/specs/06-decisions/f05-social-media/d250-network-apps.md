🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📣 [Decisions: F5 Social media](README.md) ›
📜 D250 Network developer apps

# 📜 D250 Network developer apps

**Status:** ✅ decided

## Context

How each network's API rules and costs are handled.

## Options

- The company's own apps.
- One shared SimpleERP app.
- Both.

## Choice

Both: a shared SimpleERP app per network where the network allows it, and the company's (or its IT provider's) own app
as an option, its keys in the vault; SimpleERP shows each network's limits and costs, queues posts within rate limits,
and explains review steps.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F5-07; the shared apps are run by the SimpleERP project, with their quotas shared among installs.

Clarified on 2026-11-12 after the review (R22, the owner's yes): each install uses its own app per network, its keys in
the vault; the shared SimpleERP app exists only in the hosted edition, as a relay the publisher runs under its own
terms; no secret ships with the software (BR-F5-07).

## Related

- [F5 Social media](../../02-functional/f05-social-media/README.md)
- [D240](../security-and-compliance/d240-credential-vault.md)

---

⬅️ [D249 Social statistics](d249-social-statistics.md) · ⬆️ [Up](README.md) ·
➡️ [D251 The whole sales cycle](../f06-customers-and-sales/d251-sales-cycle.md)
