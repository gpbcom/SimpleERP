🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) › 📜 D432 DevOps agents

# 📜 D432 DevOps agents

**Status:** ✅ decided

## Context

The owner asked for DevOps agents: customers' feature requests and bug reports become GitHub features with one ticket
labelled USER-FEATURE-REQUEST or USER-REPORTED-BUG; the agents, with access to the fully managed simple-ERP, the GitHub
repository and the specs, study code and specs and create SPECS features with their tickets, which need maintainers'
approval (PLAN D38).

## Options

- The agents prepare everything, maintainers approve.
- Tickets only, no pull requests.

## Choice

The agents prepare everything, confirmed by the owner on 2026-11-12. A feature request gives a SPECS feature with as
many spec tickets as needed and the spec changes drafted as a pull request on docs/specs. A bug is reproduced on the
fully managed simple-ERP (read access as in F20), its cause found in the code, and the fix proposed as a pull request,
tests first (TEST-7), in a PRODUCT ticket. Nothing is merged, deployed or made Ready without a maintainer's approval. A
closed hosted service (D388).

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

Twenty use cases (D436); the harness gains the USER family (D433).

## Related

- [F25 DevOps agents](../../02-functional/f25-devops-agents/README.md)

---

⬅️ [D431 F24 use cases](../f24-integrations-hub/d431-f24-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D433 The USER family and its labels](d433-user-family-and-labels.md)
