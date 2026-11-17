🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-28 Scripts run sandboxed within time and memory limits

# 📏 BR-F2-28 Scripts run sandboxed within time and memory limits

**Status:** ✅ specified

## Statement

A script step runs in a sandbox with no network, file or cross-company access, within a time limit (2 seconds by
default) and a memory limit (64 MB by default) that the company may lower or raise up to a platform maximum; a run that
exceeds a limit is stopped, its changes are not saved and it is logged.

## Why

A script is code written by a configuration user: it must never slow, crash or read beyond what a rule may. The owner's
answer: "Low-code script step"
([D521](../../../06-decisions/f02-no-code-configuration/d521-benchmark-gaps-f02-no-code-configuration.md)).

## Examples

| Case | Result |
|---|---|
| A script that finishes in 12 ms | passes |
| A loop without end | stopped at 2 seconds, step failed, nothing saved |
| A script that asks for 200 MB | stopped at the memory limit |
| A call to the network | does not exist: refused when saved |
| A limit raised above the platform maximum | refused |

## Applies to

- [UC-F2-31 Add a low-code script step](../use-cases/13-low-code-bulk-and-cleaning/uc-f02-31-add-a-low-code-script-step.md)
- [E-F2-30 Script step](../data/e-f02-30-script-step.md)
- [UC-F2-24 Test rules and workflows with test cases](../use-cases/10-change-safely/uc-f02-24-test-rules-and-workflows-with-test-cases.md)

## Exceptions

None.

## Configurable

Yes: the limits per company, within the platform maximum.

## Open questions

None.

---

⬅️ [BR-F2-27](br-f02-27-every-approval-follows-its-chain-and-never-waits-forever.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-29 Bulk changes are previewed and can be undone](br-f02-29-bulk-changes-are-previewed-and-can-be-undone.md)
