# 3. Rules

| File | IDs | About |
|---|---|---|
| `AGENT.md` | | How simple-erp code is written: layers, files, lifecycle, typing, messages, logging, tests |
| `.claude/rules/coding-style.md` | CS-1… | Code rules on top of `AGENT.md` |
| `.claude/rules/git-rules-and-deploy.md` | GIT-1…, DEP-1… | Branches (GitFlow), approvals, squash, pull requests, stages, dependencies |
| `.claude/rules/testing.md` | TEST-1… | Tests first, evidence, kept reports, Bruno, Playwright, paid AI |
| `.claude/rules/ticket-documentation.md` | DOC-1… | EXPLAIN.md, the project documentation, release notes |
| `.claude/rules/TESTS-NOTICE.md` | | How each test level runs |
| `.claude/rules/rule-proposals.md` | | Rules proposed from reviews, waiting for your decision |

- **One source of truth.** The four rule skills (`coding-style-rules`, `git-deploy-rules`, `testing-rules`,
  `ticket-documentation-rules`) hold no rule: they load the files live, so they can never disagree with them.
- **Applied with checks.** Each rule has a check (a command or a script) that must print nothing, run before each
  commit or at hand-over, and logged on the step's **Rules** line in PROGRESS.md.
- **Adding a rule:** say "From now on, …". Claude adds it to the right file with the next ID, a summary-table row,
  and its **Rule / Why / How to apply / Check**. A dropped rule is marked **Withdrawn**, its ID never reused.
- **From reviews:** a review remark that states a convention becomes a proposal in `rule-proposals.md`, and a rule
  once you accept it.
