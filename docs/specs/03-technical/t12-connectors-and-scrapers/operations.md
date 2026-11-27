🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) › 🕸️ [Connectors and scrapers](README.md) ›
⚙️ Operations

# ⚙️ Operations

**Status:** ✅ specified

## Deployment

The connector runtime, fetch service and vault are separate images and services (one image per service).

## Monitoring

Health and drift per connector (REQ-T12-11); costs per run.

## Backups

The vault's own encrypted backups, kept apart from the database's.

## Runbooks

Revoke all credentials of a company; pause a connector; restore the vault.

---

⬅️ [Security](security.md) · ⬆️ [Up](README.md) · ➡️ [Errors](errors.md)
