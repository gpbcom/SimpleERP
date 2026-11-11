---
name: testing-rules
description: The enforced testing rules of simple-erp, TEST-1…TEST-n, read live from .claude/rules/testing.md - TEST-1 an API change updates the Bruno collection and runs it headless on the stage, TEST-2 a stand-in returns the real type's empty value, TEST-3 a new matching or lookup proved on real values (each branch fires), TEST-5 a test calling a paid AI runs through the $20-per-ticket cost guard, TEST-6 a front-end change has Playwright tests against the real images, TEST-7 tests written, committed and seen failing (red run recorded) BEFORE the code, no exemption, TEST-8 nothing passes without its evidence folder (command, commit, raw output, verdict), TEST-9 every unit, GUI and E2E report kept, failed runs included, indexed and archived to a GitHub pre-release. Load before writing any code (the tests come first), when writing or running tests, recording evidence, claiming that something passes, changing an API, a front end, a mapping or lookup, and before handing a ticket over.
---

# Testing rules (TEST)

**Source of truth:** `.claude/rules/testing.md`, loaded below as it is now, and `.claude/rules/TESTS-NOTICE.md` for how each level runs. If the section below is empty or shows a command instead of the rules, Read that file before going on. The file wins over anything else; never copy its rules into another file.

## How to apply

1. **Tests first, always (TEST-7).** For each code step: write the tests, commit them alone, record the red run with `ticket-docs record-run`, then write the code, commit it, record the green run. The `git-gate` hook refuses a production-code commit that skips this.
2. **No claim without evidence (TEST-8).** Never write ✅, PASS, "green" or "works" without the link to the evidence folder of a run on that commit. In a reply too.
3. **Keep every report (TEST-9).** Never delete an evidence folder; regenerate the index with `ticket-docs report-index`; archive at hand-over.
4. Decide early whether the ticket changes an API (TEST-1) or a front end (TEST-6): a behaviour change counts even when the schema does not change.
5. Log the results in the step's **Rules** line of PROGRESS.md.
6. A new testing rule the repository owner states goes into the rules file, in its format, not into this skill.

## Rules in force

!`cat "$(git rev-parse --show-toplevel)/.claude/rules/testing.md"`
