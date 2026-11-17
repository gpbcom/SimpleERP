🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) ›
📜 D567 The agent team: roles, contract, worktrees, one-commit verification

# 📜 D567 The agent team: roles, contract, worktrees, one-commit verification

**Status:** 🔄 waiting for the owner

## Context

On 2026-11-16 the owner asked to enrich F25 with the ideas of a course on multi-agent development teams: six roles
(architect, backend engineer, frontend engineer, test engineer, code reviewer with read-only tools, release engineer),
an approved work contract per ticket, one worktree per role from one starting commit, a structured handoff, integration
in dependency order, verification of one candidate commit, at most two repair cycles, a draft pull request with its
evidence, and unattended runs that resume from checkpoints. The owner set one constraint: every requirement F25 already
specifies is kept. The team starts from a ticket approved through
[FL-F25-02](../../02-functional/f25-devops-agents/flows/fl-f25-02-feature-requests.md) or
[FL-F25-03 Bugs](../../02-functional/f25-devops-agents/flows/fl-f25-03-bugs.md) and ends in
[FL-F25-04](../../02-functional/f25-devops-agents/flows/fl-f25-04-approve-and-govern.md), where the maintainer still
reviews, approves and merges. The design below is a proposal written for the owner and waits for the owner's answer.

## Options

- Write the work contract of a ticket (UC-F25-29): (Proposed) a work contract per ticket that gives each role its own
  files, or workers that share every file.
- Approve the work contract (UC-F25-30): (Proposed) no worker before the maintainer approves the contract, or workers
  that start at once.
- Build in isolated worktrees (UC-F25-31): (Proposed) one worktree per role from one recorded starting commit, or one
  shared checkout.
- Hand over a worker's result (UC-F25-32): (Proposed) a structured handoff refused without its commits and checks, or a
  free-text message.
- Integrate the workers' commits (UC-F25-33): (Proposed) integration in dependency order with conflicts sent back to the
  architect, or conflicts resolved by the agent that meets them.
- Verify the candidate commit (UC-F25-34): (Proposed) checks and a read-only review bound to one commit, or a review of
  the branch as it moves.
- Repair a rejected candidate (UC-F25-35): (Proposed) two repair cycles at most then the maintainer, or repairs until
  the budget stops them.
- Open the draft pull request with its evidence (UC-F25-36): (Proposed) one draft pull request per branch with its
  evidence and the specification's screenshots, or a pull request with a short summary.
- Resume an interrupted run (UC-F25-37): (Proposed) one active run per repository resumed from a checkpoint, or parallel
  runs restarted from scratch.

## Choice

(Proposed) F25 gets nine use cases in one new flow, FL-F25-08, each with its screen and its rule, and five entities with
their lists. The flow only adds: every existing rule and decision of F25 applies to the team. The maintainer approves
the ticket ([BR-F25-07](../../02-functional/f25-devops-agents/business-rules/br-f25-07-approval-before-ready.md)) and
the contract, a fix starts with a failing test
([BR-F25-08](../../02-functional/f25-devops-agents/business-rules/br-f25-08-fixes-test-first.md)), production is read
only from a masked copy in the isolated cluster ([D435 The agents' access and limits](d435-agents-access-and-limits.md),
[D442](d442-devops-runners-isolated-cluster.md)), every run is metered and audited and stops on its budget
([BR-F25-11](../../02-functional/f25-devops-agents/business-rules/br-f25-11-agents-metered-and-audited.md),
[D398 Budgets warn, then stop](../f22-unified-cost-management/d398-budgets-warn-then-stop.md)), and the code reviewer's
PASS is an extra gate before the maintainer, never a replacement
([BR-F25-05](../../02-functional/f25-devops-agents/business-rules/br-f25-05-agents-never-merge-or-deploy.md),
[D434 Maintainers approve agents' work](d434-maintainer-approval-label.md)). The runs stay in GitHub Actions with the
Claude Code GitHub Action ([D437 DevOps agents live in the CI](d437-devops-agents-in-the-ci.md)).

| Point | Use case | Proposal |
|---|---|---|
| Write the work contract of a ticket | [UC-F25-29](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-29-write-the-work-contract-of-a-ticket.md) | UC-F25-29: (Proposed) a work contract gives each role its own files |
| Approve the work contract | [UC-F25-30](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-30-approve-the-work-contract.md) | UC-F25-30: (Proposed) no worker starts before the contract is approved |
| Build in isolated worktrees | [UC-F25-31](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-31-build-in-isolated-worktrees.md) | UC-F25-31: (Proposed) one role, one worktree, one starting commit |
| Hand over a worker's result | [UC-F25-32](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-32-hand-over-a-workers-result.md) | UC-F25-32: (Proposed) a handoff without its commits and checks is refused |
| Integrate the workers' commits | [UC-F25-33](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-33-integrate-the-workers-commits.md) | UC-F25-33: (Proposed) a conflict goes back to the architect, never guessed |
| Verify the candidate commit | [UC-F25-34](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-34-verify-the-candidate-commit.md) | UC-F25-34: (Proposed) an approval belongs to one commit |
| Repair a rejected candidate | [UC-F25-35](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-35-repair-a-rejected-candidate.md) | UC-F25-35: (Proposed) two repair cycles at most, then a maintainer decides |
| Open the draft pull request with its evidence | [UC-F25-36](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-36-open-the-draft-pull-request-with-its-evidence.md) | UC-F25-36: (Proposed) a draft pull request carries its evidence and screenshots |
| Resume an interrupted run | [UC-F25-37](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-37-resume-an-interrupted-run.md) | UC-F25-37: (Proposed) one active run per repository, resumed from its checkpoint |

## Decided by

Not decided yet: a proposal of 2026-11-16 written for the owner, after the owner's request of the same day to take
inspiration from a course on multi-agent development teams. It waits for the owner.

## Consequences

-
  [UC-F25-29](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-29-write-the-work-contract-of-a-ticket.md),
  [S-F25-29](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-29-work-contract.md) and
  [BR-F25-22](../../02-functional/f25-devops-agents/business-rules/br-f25-22-a-contract-gives-each-role-its-own-files.md),
  with [E-F25-19](../../02-functional/f25-devops-agents/data/e-f25-19-work-contract.md) Work contract and its list
  [S-F25-L19](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l19-work-contracts.md).
-
  [UC-F25-30](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-30-approve-the-work-contract.md),
  [S-F25-30](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-30-contract-approval.md) and
  [BR-F25-23](../../02-functional/f25-devops-agents/business-rules/br-f25-23-no-worker-starts-before-the-contract-is-approved.md).
-
  [UC-F25-31](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-31-build-in-isolated-worktrees.md),
  [S-F25-31](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-31-agent-workers.md) and
  [BR-F25-24](../../02-functional/f25-devops-agents/business-rules/br-f25-24-one-role-one-worktree-one-starting-commit.md),
  with [E-F25-20](../../02-functional/f25-devops-agents/data/e-f25-20-agent-role.md) Agent role and its list
  [S-F25-L20](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l20-agent-roles.md).
-
  [UC-F25-32](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-32-hand-over-a-workers-result.md),
  [S-F25-32](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-32-worker-handoff.md) and
  [BR-F25-25](../../02-functional/f25-devops-agents/business-rules/br-f25-25-a-handoff-without-its-commits-and-checks-is-refused.md),
  with [E-F25-21](../../02-functional/f25-devops-agents/data/e-f25-21-worker-handoff.md) Worker handoff and its list
  [S-F25-L21](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l21-worker-handoffs.md).
-
  [UC-F25-33](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-33-integrate-the-workers-commits.md),
  [S-F25-33](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-33-integration.md) and
  [BR-F25-26](../../02-functional/f25-devops-agents/business-rules/br-f25-26-a-conflict-goes-back-to-the-architect-never-guessed.md).
-
  [UC-F25-34](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-34-verify-the-candidate-commit.md),
  [S-F25-34](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-34-candidate-verification.md)
  and [BR-F25-27](../../02-functional/f25-devops-agents/business-rules/br-f25-27-an-approval-belongs-to-one-commit.md),
  with [E-F25-22](../../02-functional/f25-devops-agents/data/e-f25-22-verification.md) Verification and its list
  [S-F25-L22](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l22-verifications.md).
-
  [UC-F25-35](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-35-repair-a-rejected-candidate.md),
  [S-F25-35](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-35-repair-cycles.md) and
  [BR-F25-28](../../02-functional/f25-devops-agents/business-rules/br-f25-28-two-repair-cycles-at-most-then-a-maintainer-decides.md).
-
  [UC-F25-36](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-36-open-the-draft-pull-request-with-its-evidence.md),
  [S-F25-36](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-36-draft-pull-request.md) and
  [BR-F25-29](../../02-functional/f25-devops-agents/business-rules/br-f25-29-a-draft-pull-request-carries-its-evidence-and-screenshots.md).
-
  [UC-F25-37](../../02-functional/f25-devops-agents/use-cases/08-team-builds-a-ticket/uc-f25-37-resume-an-interrupted-run.md),
  [S-F25-37](../../02-functional/f25-devops-agents/screens/08-team-builds-a-ticket/s-f25-37-run-resume.md) and
  [BR-F25-30](../../02-functional/f25-devops-agents/business-rules/br-f25-30-one-active-run-per-repository-resumed-from-its-checkpoint.md),
  with [E-F25-23](../../02-functional/f25-devops-agents/data/e-f25-23-run-checkpoint.md) Run checkpoint and its list
  [S-F25-L23](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l23-run-checkpoints.md).
- Drawn in [FL-F25-08](../../02-functional/f25-devops-agents/flows/fl-f25-08-team-builds-a-ticket.md) The agent team
  builds an approved ticket.
- (Proposed) The quality and cost dashboards of F25 gain the metrics per ticket: elapsed time, AI cost, repair cycles
  and maintainer interventions, shown on the costs and quality screens
  ([S-F25-18](../../02-functional/f25-devops-agents/screens/04-approve-and-govern/s-f25-18-agent-costs.md),
  [S-F25-19](../../02-functional/f25-devops-agents/screens/04-approve-and-govern/s-f25-19-agent-quality.md)).
- No existing requirement of F25 is changed or removed: the new pages link the rules and decisions they rely on.

## Related

- [FL-F25-08](../../02-functional/f25-devops-agents/flows/fl-f25-08-team-builds-a-ticket.md)
- [D432 DevOps agents](d432-devops-agents-coverage.md)
- [D434 Maintainers approve agents' work](d434-maintainer-approval-label.md)
- [D435 The agents' access and limits](d435-agents-access-and-limits.md)
- [D437 DevOps agents live in the CI](d437-devops-agents-in-the-ci.md)
- [D442](d442-devops-runners-isolated-cluster.md)
- [BR-F25-05](../../02-functional/f25-devops-agents/business-rules/br-f25-05-agents-never-merge-or-deploy.md)
- [BR-F25-07](../../02-functional/f25-devops-agents/business-rules/br-f25-07-approval-before-ready.md)
- [BR-F25-08](../../02-functional/f25-devops-agents/business-rules/br-f25-08-fixes-test-first.md)
- [BR-F25-11](../../02-functional/f25-devops-agents/business-rules/br-f25-11-agents-metered-and-audited.md)

---

⬅️ [D566](../foundations/d566-answers-of-2026-11-15-after-the-benchmark-gap-round.md) · ⬆️ [Up](README.md)
