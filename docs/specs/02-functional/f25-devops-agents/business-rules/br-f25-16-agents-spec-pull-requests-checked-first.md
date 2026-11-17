🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-16 Agents' spec pull requests checked first

# 📏 BR-F25-16 Agents' spec pull requests checked first

**Status:** ✅ specified

## Statement

A spec pull request written by the agents passes the spec checks before any maintainer is asked: every new statement
cites its source (an owner's answer, a decision, a country rule or a page) or carries the "Proposed" marker, nothing
contradicts a decided decision, and the project's spec checks (links, templates, prose, coverage) print nothing.

## Why

Agents may invent facts (D482); the specs mark what the owner has not decided with the "Proposed" marker.

## Examples

| Case | Result |
|---|---|
| New rule citing D454 | passes |
| New threshold "48 hours" with no source and no "Proposed" marker | fails: listed, back to the agent |
| Statement contradicting D443 (no seats) | fails: listed with D443 |
| Broken link | fails: the link check lists it |

## Applies to

- [UC-F25-23 Check an agent's spec pull request](../use-cases/02-feature-requests/uc-f25-23-check-an-agents-spec-pull-request.md)
- [UC-F25-06 Draft the spec changes as a pull request](../use-cases/02-feature-requests/uc-f25-06-draft-the-spec-changes-as-a-pull-request.md)
- [UC-F25-19 Measure the quality of the agents' work](../use-cases/04-approve-and-govern/uc-f25-19-measure-the-quality-of-the-agents-work.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-15 Vulnerabilities handled under the CRA](br-f25-15-vulnerabilities-handled-under-the-cra.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F25-17 Declined requests stay public as votes](br-f25-17-declined-requests-stay-public-as-votes.md)
