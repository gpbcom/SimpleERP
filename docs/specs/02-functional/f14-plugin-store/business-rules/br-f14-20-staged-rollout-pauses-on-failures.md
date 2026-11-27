🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-20 Staged rollout pauses on failures

# 📏 BR-F14-20 Staged rollout pauses on failures

**Status:** 🔄 waiting for the owner

## Statement

A release rolled out in stages moves to the next stage only when the failure rate of installs and updates at the current
stage stays under the limit; above it, the rollout pauses and the publisher is told.

## Why

A faulty release reaches few companies before it is stopped (D471).

## Examples

| Case | Result |
|---|---|
| Stage 5 % of 1 240 companies, 1 failure in 62 | passes: next stage (Proposed) limit 2 % |
| Stage 25 %, 9 failures in 310 | fails: paused at 2.9 % |
| Publisher forces the next stage while paused | fails: refused |

## Applies to

- [UC-F14-25 Roll out a release in stages](../use-cases/06-release-channels-and-rollback/uc-f14-25-roll-out-a-release-in-stages.md)
- [UC-F14-03 Update with compatibility checks](../use-cases/01-find-and-install/uc-f14-03-update-with-compatibility-checks.md)

## Exceptions

The store operator may stop any rollout.

## Configurable

The publisher sets the stages; the store sets the limit, (Proposed) 2 % of failed installs.

## Open questions

None.

---

⬅️ [BR-F14-19 Beta versions only where companies opt in](br-f14-19-beta-versions-only-where-companies-opt-in.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F14-21 Listings and plugins in the user's language](br-f14-21-listings-and-plugins-in-the-users-language.md)
