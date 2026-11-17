🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-19 Beta versions only where companies opt in

# 📏 BR-F14-19 Beta versions only where companies opt in

**Status:** ✅ specified

## Statement

A beta version is offered only to companies that opted into the plugin's beta channel; it passes the same checks and
signing as any release and is marked "beta" everywhere.

## Why

Publishers need early feedback without putting every company at risk (D471).

## Examples

| Case | Result |
|---|---|
| Company opted in, version 2.4.0-beta.1 signed | passes: offered |
| Company not opted in | passes: not offered |
| Unsigned beta | fails: refused (BR-F14-07) |

## Applies to

- [UC-F14-24 Publish to the beta channel](../use-cases/06-release-channels-and-rollback/uc-f14-24-publish-to-the-beta-channel.md)

## Exceptions

None.

## Configurable

The administrator opts in per plugin and may opt out at any time.

## Open questions

None.

---

⬅️ [BR-F14-18 Abandoned plugins can be taken over](br-f14-18-abandoned-plugins-can-be-taken-over.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F14-20 Staged rollout pauses on failures](br-f14-20-staged-rollout-pauses-on-failures.md)
