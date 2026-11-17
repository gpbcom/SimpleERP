🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🤖 [DevOps agents (hosted edition)](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Owner (U13) | Administrator (U07) | Maintainer (U47) | Hosting engineer (U48) | DevOps agents |
|---|---|---|---|---|---|
| Report, request, follow | ✅ | ✅ | read | read | - |
| File USER features and tickets | - | - | ✅ | ✅ | ✅ |
| Read the customer's masked copy | - | - | - | ✅ | read-only, masked |
| Branches, pull requests, issues | - | - | ✅ | - | ✅ |
| Merge, Ready, remove the approval label | - | - | ✅ | - | - |
| Deploy to the hosted edition | - | - | - | ✅ | - |
| Runners, rights, costs | read costs | - | quality | ✅ | - |

## Agent roles

(Proposed) Within the DevOps agents column, each role of the agent team
([FL-F25-08](flows/fl-f25-08-team-builds-a-ticket.md)) has only what it needs: the code reviewer reads only; the
implementation roles write only the files the approved work contract gives them, in their own worktree; the release
engineer integrates and opens draft pull requests; no role merges, deploys, sets Ready or removes the approval label
([BR-F25-05](business-rules/br-f25-05-agents-never-merge-or-deploy.md)).

## Record rules

- A customer sees only its own requests.
- Agents never reach another customer's namespace (BR-F25-04).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
