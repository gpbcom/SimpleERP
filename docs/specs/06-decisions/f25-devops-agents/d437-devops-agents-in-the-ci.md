🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) › 📜 D437 DevOps agents live in the CI

# 📜 D437 DevOps agents live in the CI

**Status:** ✅ decided

## Context

How the DevOps agents of F25 are run; the owner: "The DevOps agents will live in the CI".

## Options

- Runners: self-hosted in the EU cluster, GitHub-hosted, or mixed.
- Agent: the Claude Code GitHub Action, or the Claude Agent SDK in workflow steps.

## Choice

Confirmed by the owner on 2026-11-12: GitHub Actions workflows run the Claude Code GitHub Action on self-hosted runners
(Actions Runner Controller) in the European hosting cluster; the intake service files sanitised USER tickets through its
own GitHub App, whose label events start the workflows.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The build study of F25; REQ-T06-07, REQ-T07-02 and REQ-T09-07 apply to the runners.

Revised by D442 on 2026-11-12: the runners run in a separate, isolated European cluster with no outbound access except
GitHub and the AI gateway, never in the hosting cluster; production is read only from a masked copy; no job from a fork
or an outside pull request runs on them.

## Related

- [F25 DevOps agents](../../02-functional/f25-devops-agents/README.md)
- [Build study](../../02-functional/f25-devops-agents/build-study.md)

---

⬅️ [D436 F25 use cases](d436-f25-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D438 Repository layout](../technical/d438-repository-layout.md)
