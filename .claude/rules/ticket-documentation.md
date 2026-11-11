# Ticket documentation rules

These rules apply to the documentation of every simple-erp ticket, and to the project documentation the tickets keep current.

## How this file works

- Each rule has an ID (`DOC-<n>`) that never changes. Reviews and discussions can cite it ("breaks DOC-2").
- New rules are added at the end with the next free ID and a row in the summary table. A rule that is dropped stays in the file, marked **Withdrawn** with the date, so that its ID is never reused.
- Each rule uses the same parts: **Rule**, **Why**, **Check before handing over**.
- The ticket folder itself (files, templates, icons, stages, times) is the **ticket-docs** skill. This file holds the rules it must meet.
- `docs/tickets/` is local and not versioned (`.gitignore`): `ticket-docs archive` keeps each ticket folder on GitHub (TEST-9). In `docs/`, only `specs/`, `functional/` and `technical/` are versioned.
- DOC-1 comes from the harness this one was adapted from (2026-11-10).

| ID | Rule | Enforced since |
|---|---|---|
| [DOC-1](#doc-1--every-implemented-ticket-has-an-explainmd) | Every implemented ticket has an `EXPLAIN.md`: what was done and how to test it, for developers and testers | 2026-11-10 |
| [DOC-2](#doc-2--every-ticket-keeps-the-project-documentation-current) | Every ticket keeps the project documentation current: `README.md`, `docs/functional/` and `docs/technical/` | 2026-11-10 |
| [DOC-3](#doc-3--every-ticket-has-a-release-note-and-a-changelog-entry) | Every ticket has a release note and a changelog fragment; a release assembles them into `CHANGELOG.md` and its GitHub Release | 2026-11-10 |

## DOC-1 — Every implemented ticket has an EXPLAIN.md

**Rule:** once a ticket is implemented, its folder holds `docs/tickets/GH-<n>/EXPLAIN.md`, which explains what was done and how to test it. One file serves two readers:
- **a tester**, who must be able to test the change from this file alone, without reading code or the other ticket documents;
- **a developer**, who must understand what changed in the code, why, and how to run its tests.

The file is written before the work is handed over for review or QA. It is updated whenever a later change alters what it says: a review fix, a rebase that changes behaviour, a new limitation, a new test run.

The file has these sections, in this order:

| # | Section | Reader | Content |
|---|---|---|---|
| — | Header | both | Issue link and title; status (implemented, in review, merged, deployed on…); repositories, branches, PR and final commit; date of the last update |
| 1 | In short | both | 3 to 6 sentences in plain words: the problem, what changes, where it can be seen |
| 2 | What changed for users | QA first | The behaviour before and after, from the outside (screens, API, files, jobs): what is new, what changed, what did not change, who is affected |
| 3 | What changed in the code | developers | **3.1 API changes** first (see below). Then: the flow and the components involved; the other contracts (storage schema, configuration, dependencies); the files modified, grouped by service, front end or package; the main decisions and the options left aside |
| 4 | How to test | both | **4.1 Prerequisites**: stage (`dev` or `qa` run of `stage.yml`, or local `compose.e2e.yaml`), accounts (the user names, never passwords: say where to get them), test data, access and tools. **4.2 Test cases**: numbered and runnable by a tester, each with exact steps (URL, screen, request and payload), the expected result and the acceptance criterion it covers, including negative and edge cases. **4.3 Automated tests**: the command of each level (unit, Playwright, Bruno, stage), what it covers and the expected result. **4.4 Last results**: the date, commit, stage and outcome of the last run of each level, each linked to its evidence. |
| 5 | Acceptance criteria | both | One row per criterion of the ticket: how it is verified (test cases of 4.2, automated tests), status (PASS, FAIL, not verified yet) and evidence link |
| 6 | Limitations, risks and out of scope | both | Known limitations, open points, what the ticket deliberately does not do, side effects of testing (data overwritten, costs), rollback when it matters |
| 7 | References | both | Links to the other ticket documents (TICKET, PLAN, IMPLEMENTATION, PROGRESS, TESTS-NOTICE, RELEASE-NOTE, tests-evidences and its archive) and to the pull request |

**3.1 API changes** lists every change to an API, in both directions:
- **APIs this project exposes:** REST endpoints, events and messages published, files produced for other systems;
- **APIs this project calls:** other services, queues, third-party APIs.

One row per change:

| Column | Content |
|---|---|
| API | Exposed or called, and its name: e.g. `customers API`, `GitHub REST API` |
| Operation | Method and path (`GET /customers/{id}`), event or message name, or function name |
| Change | New endpoint, new / changed / removed field, status code, header, error message or behaviour |
| Before → after | The concrete difference, with the field names and an example value |
| Compatibility | Additive (existing callers unaffected) or breaking (say who must adapt) |
| Defined in | Where the contract lives: OpenAPI file and schema or operation name, and the route or client file that implements it |
| See it | Where a reader sees it running: published API docs, an example request and response in `tests-evidences/…`, the test case of 4.2 that exercises it |

When nothing changed, write **"No API change"**, for both directions, with the reason (e.g. "dependency upgrade only: no endpoint, field or call changed"). Behaviour changes count as API changes even when the schema is unchanged, e.g. a request that is now refused, or data that is now filtered out.

Writing rules:
- **Self-contained.** Never write "see the chat" or "as discussed". Explain technical terms the first time they appear in sections 1, 2 and 4.
- **Exact.** Give the real values: URLs, user names, references, payloads, expected figures, commands. A tester must not have to guess.
- **Proven.** Every "passes" links to its evidence (`tests-evidences/…`, PROGRESS.md, an Actions run). A check not run yet says "not verified yet".
- **Safe.** No password, token, API key, presigned URL or personal data. Say where a credential is obtained, not what it is.
- **Consistent.** When EXPLAIN.md and another ticket document disagree, fix the one that is wrong.

**Why:**
- Testers and reviewers need one entry point. The other ticket documents are written for the implementation (plan, progress log, evidence) and are too long to test from.
- A developer who picks up the code later needs the reasons, not only the diff.
- Writing the test cases down before the hand-over exposes the untestable parts while they can still be fixed.

**Check before handing over:** this script must print nothing. `ticket-docs check <KEY>` runs it. By hand, from `docs/tickets/`, with the ticket key as argument:

```bash
python3 -I - GH-12 <<'PY'
import pathlib, re, sys
path = pathlib.Path(sys.argv[1]) / "EXPLAIN.md"
if not path.is_file():
    sys.exit(f"{path}: missing")
text = path.read_text(encoding="utf-8")
headings = [h.strip().lower() for h in re.findall(r"^## (.+)$", text, re.M)]
for number, name in enumerate(["in short", "what changed for users", "what changed in the code", "how to test",
                               "acceptance criteria", "limitations, risks and out of scope", "references"], 1):
    if not any(h.startswith(f"{number}. {name}") for h in headings):
        print(f"{path}: section '{number}. {name}' missing or out of order")
for sub in ("3.1", "4.1", "4.2", "4.3", "4.4"):
    if not re.search(rf"^### {re.escape(sub)}\b", text, re.M):
        print(f"{path}: sub-section {sub} missing")
api = re.search(r"^### 3\.1 API changes\b", text, re.M)
code, test = re.search(r"^## 3\.", text, re.M), re.search(r"^## 4\.", text, re.M)
if not (api and code and test and code.start() < api.start() < test.start()):
    print(f"{path}: '### 3.1 API changes' must be the first sub-section of section 3")
for link in re.findall(r"\]\(([^)#\s]+)", text):
    if not link.startswith(("http", "mailto:")) and not (path.parent / link).exists():
        print(f"{path}: broken link {link}")
if re.search(r"eyJ[A-Za-z0-9_-]{20,}|(?i:password)\s*[:=]\s*\S+", text):
    print(f"{path}: looks like a secret")
PY
```

## DOC-2 — Every ticket keeps the project documentation current

**Rule:** before a ticket is handed over, the project documentation describes the code as the ticket leaves it:
- **`README.md`**: what simple-erp is, the quick start, the commands, the layout, the services and front ends, the links to the documentation. It changes when one of those changes.
- **`docs/functional/`**: what users can do and see, one chapter per business capability (from `docs/specs/`). It takes what EXPLAIN §2 says changed for users.
- **`docs/technical/`**: how it is built: architecture, services, data model, API, configuration, CI/CD and stages, tests and traceability, operations. It takes what EXPLAIN §3 says changed in the code.

The **project-docs** skill does it (mode `update`): it maps the branch's changed files to the chapters with `.claude/skills/project-docs/conf/doc-map.yaml`, updates each chapter concerned, and stamps it `Last reviewed: <date> (GH-<n>)`. PROGRESS.md's **Documentation** row lists each chapter updated, or `no doc impact: <reason>` for a mapped chapter left as it is.

Writing rules: plain British English, no em dashes (`AGENT.md`), every chapter linked from its folder's `README.md`, diagrams in Mermaid, no secret.

**Why:** the ticket folders are local and archived; the project documentation is what a newcomer reads. Updated at the end of each ticket, by whoever knows the change best, it never falls behind the code.

**Check before handing over:** `project-docs check --ticket <KEY>` prints nothing. CI runs `project-docs check` (without the PROGRESS.md waivers) on every pull request.

## DOC-3 — Every ticket has a release note and a changelog entry

**Rule:**
1. **At hand-over**, the **release-notes** skill (mode `ticket`) writes:
   - `docs/tickets/GH-<n>/RELEASE-NOTE.md`, for users: what is new, changed or fixed and for whom, how to use it, upgrade or migration steps, known limits, links to the issue, the pull request and the evidence archive. After the push, its text is posted on the issue as a comment starting with `<!-- release-note -->`, so that GitHub keeps it;
   - `changelog.d/GH-<n>.<type>.md` (versioned), one to three lines in the changelog's voice. `<type>` is one of `added`, `changed`, `deprecated`, `removed`, `fixed`, `security` (Keep a Changelog). A breaking change starts with `**Breaking:**`.
2. **At a release** (`release/<x.y.z>` or a hotfix, GIT-8), the skill (mode `release`) runs `release-notes build <x.y.z>`: it adds the section `## [x.y.z] - <date>` to `CHANGELOG.md`, grouped by type, each line linking its issue, and deletes the fragments it used, in the same commit. `release.yml` makes the GitHub Release body from that section and the issues' release-note comments, and attaches the QA reports.
3. The version follows semantic versioning; `release-notes next-version` suggests it from the fragment types.

**Why:** one fragment per ticket never conflicts with another branch, the way a shared `CHANGELOG.md` would. The release note says in users' words what the ticket gives them, and the changelog and the Release gather them per version.

**Check before handing over:** `release-notes check --ticket <KEY>` prints nothing. CI runs `release-notes check` on every pull request: a `feature/` or `bugfix/` branch needs exactly one fragment for its issue, and a `release/` branch needs its `CHANGELOG.md` section and an empty `changelog.d/`.
