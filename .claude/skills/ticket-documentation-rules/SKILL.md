---
name: ticket-documentation-rules
description: The enforced documentation rules of simple-erp, DOC-1…DOC-n, read live from .claude/rules/ticket-documentation.md - DOC-1 every implemented ticket has an EXPLAIN.md for developers and testers, with its 7 sections, API changes first, and a check that must print nothing; DOC-2 every ticket keeps README.md, docs/functional/ and docs/technical/ current (project-docs skill); DOC-3 every ticket has a release note and a changelog fragment, assembled into CHANGELOG.md and the GitHub Release at a release (release-notes skill). Load when writing or updating a ticket's EXPLAIN.md, the project documentation, a release note or the changelog, before a hand-over, review or QA run, and together with the ticket-docs skill.
---

# Ticket documentation rules (DOC)

**Source of truth:** `.claude/rules/ticket-documentation.md`, loaded below as it is now. If the section below is empty or shows a command instead of the rules, Read that file before going on. The file wins over anything else; never copy its rules into another file.

## How to apply

1. The ticket folder itself (files, templates, icons, stages, times) is the **ticket-docs** skill; this skill holds the DOC rules it must meet.
2. DOC-2 is done with the **project-docs** skill, DOC-3 with the **release-notes** skill, both at hand-over, before the pull request.
3. Run each rule's check with the ticket key. It must print nothing. `ticket-docs check <KEY>` runs the DOC-1 check as well.
4. A new documentation rule the repository owner states goes into the rules file, in its format, not into this skill.

## Rules in force

!`cat "$(git rev-parse --show-toplevel)/.claude/rules/ticket-documentation.md"`
