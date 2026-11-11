# Testing rules

These rules apply to simple-erp and to the harness tools in `.claude/skills/`. They apply to anyone who writes or runs tests, people and AI agents alike.

## How this file works

- Each rule has an ID (`TEST-<n>`) that never changes. Reviews and discussions can cite it ("breaks TEST-7").
- New rules are added at the end with the next free ID and a row in the summary table. A rule that is dropped stays in the file, marked **Withdrawn** with the date, so that its ID is never reused.
- Each rule uses the same parts: **Rule**, **Why**, **How to apply**, **Check before handing over**.
- A rule applies to the whole repository unless its **Scope** line narrows it.
- How each test level runs is in [TESTS-NOTICE.md](TESTS-NOTICE.md). `AGENT.md` ("Tests") says how tests are written.
- Rules TEST-1 to TEST-5 come from the harness this one was adapted from (2026-11-10).

| ID | Rule | Enforced since |
|---|---|---|
| [TEST-1](#test-1--an-api-change-updates-the-bruno-collection-and-runs-it-on-the-stage) | An API change updates the Bruno collection and runs it, headless, on the stage | 2026-11-10 |
| [TEST-2](#test-2--a-stand-in-returns-the-shape-of-what-it-replaces) | A stand-in returns the shape of what it replaces: its default answer is a valid empty value of the real type | 2026-11-10 |
| [TEST-3](#test-3--a-new-matching-or-lookup-is-checked-on-real-values-before-hand-over) | A new matching or lookup is checked on real values before hand-over: each branch fires on the stage, or the pull request says which never does | 2026-11-10 |
| [TEST-4](#test-4--withdrawn) | ~~Every new Lambda handler has its unit spec~~ **Withdrawn 2026-11-10:** simple-erp has no Lambda handlers. TEST-7 covers every new entry point | 2026-11-10 |
| [TEST-5](#test-5--a-test-calling-a-paid-ai-runs-through-the-cost-guard-20-per-ticket) | A test calling a paid AI runs through the cost guard (`ai-cost run`): $20 cumulative per ticket, killed at 90 %, COST.md in tests-evidences | 2026-11-10 |
| [TEST-6](#test-6--a-front-end-change-has-playwright-tests-run-against-the-real-images) | A front-end change has Playwright tests, run against the real images | 2026-11-10 |
| [TEST-7](#test-7--tests-are-written-and-seen-failing-before-the-code) | Tests are written, committed and seen failing (red run recorded) before the code they test. No exemption | 2026-11-10 |
| [TEST-8](#test-8--nothing-passes-without-its-evidence) | Nothing passes without its evidence: command, commit, raw output and verdict in an evidence folder | 2026-11-10 |
| [TEST-9](#test-9--every-test-report-is-kept) | Every test report (unit, GUI, E2E) is kept for traceability, failed and invalid runs included, and archived with the ticket | 2026-11-10 |

## TEST-1 — An API change updates the Bruno collection and runs it on the stage

**Scope:** the HTTP APIs of the services. The collection lives in `bruno/` (OpenCollection YAML, one folder per service). It is created by the first ticket that adds an endpoint.

**Rule:** a ticket that adds or changes an endpoint, or the shape or behaviour of what an endpoint returns (a new field, a changed rule, a new error case):

1. **updates the Bruno collection** for the endpoints concerned, before the hand-over:
   - a new endpoint gets a new request;
   - a changed response gets `tests` in the request that assert the new behaviour, plus one request per error case the ticket adds or changes;
   - an existing test that no longer matches the API is fixed, not deleted;
   - **no password, token or personal data in a committed file**: variables come from the environment or from a previous request;
2. **runs it headless with the Bruno CLI against the stage** where the ticket's commit runs (`stage.yml` runs the whole collection on dev and QA);
3. **keeps the run as evidence** (TEST-8, TEST-9): the JSON and JUnit reports, the console and a README.

**Why:**
- The collection is what people use to try the API by hand. When an API change does not update it, its requests drift, and the next person loses time on false failures.
- Running it on the stage tests what the unit tests cannot: the real image, its configuration and its routes.
- A headless run gives a report that can be kept and compared.

**How to apply:** `npx --yes @usebruno/cli@4.2.1 run <folder> --env stage --reporter-json <evidence>/bruno-report.json --reporter-junit <evidence>/bruno-junit.xml --reporter-skip-all-headers --reporter-skip-body`. The two `--reporter-skip-*` flags are mandatory: without them, the report holds headers and bodies, credentials included.

**Check before handing over:** this must print nothing (run from the repository root, with the evidence folder as argument):

```bash
python3 -I - <evidence folder> <<'PY'
import pathlib, re, subprocess, sys
folder = pathlib.Path(sys.argv[1])
changed = subprocess.run(["git", "diff", "--name-only", "origin/develop...HEAD"], capture_output=True, text=True).stdout.split()
api = [p for p in changed if re.search(r"/api/(http|routes)/", p)]
if api and not any(p.startswith("bruno/") for p in changed):
    print("the HTTP API changed but the Bruno collection did not")
if not (folder / "bruno-junit.xml").is_file():
    print(f"{folder}: bruno-junit.xml missing")
elif re.search(r"<failure|<error", (folder / "bruno-junit.xml").read_text()):
    print(f"{folder}: the run has failures: explain them in the README or fix them")
for path in folder.glob("*"):
    if path.is_file() and re.search(r"eyJ[A-Za-z0-9_-]{20,}|(?i:\"password\"\s*:\s*\"[^\"]+)", path.read_text(errors="ignore")):
        print(f"{path}: looks like a token or a password")
PY
```

## TEST-2 — A stand-in returns the shape of what it replaces

**Rule:** `AGENT.md` says tests use real things rather than mocks: a local test server, a git sandbox, a fake executable on a temporary `PATH`, an `httpx.MockTransport` whose handler is a class. When such a stand-in has a default answer, it is a valid value of the type the real thing returns: an empty page `{"items": [], "total": 0}` for a search, an empty list of the right model, never `None`, `{}` or an id where the real thing returns an object. Prefer a fixture built from the real model (`Customer.model_validate(...)`) to a hand-written literal.

**Why:** a stand-in accepts anything, so the type checker does not catch a wrong default. A test that relies on it later gets missing fields and an error deep in the code under test, often turned into a degraded result far from the cause.

**How to apply:** when adding or changing a stand-in, give each default answer the real type's empty value, and add one test that uses the defaults and asserts a sane result.

**Check before handing over:** this check is read, not scripted: for each stand-in the branch adds or changes, its default answers validate against the real model.

## TEST-3 — A new matching or lookup is checked on real values before hand-over

**Rule:** a ticket that matches data from one source against keys from another (names, codes, categories: a mapping table, a lookup, a join) proves on the stage, with the stage's seeded data set, that **each branch of the matching fires at least once**: each key family, each fallback meant to be rare. A branch that cannot fire is removed from the change, or named in the pull request description as not live. A risk measured as "this part never matches" blocks the hand-over.

**Why:** unit tests use fixtures written with the keys the author expects, so they pass whatever the real data holds. Only real data shows a join that never matches, and a feature that silently shows its fallback looks correct on screen.

**How to apply:**
1. List the branches of the matching in PLAN.md's acceptance table.
2. On the dev stage, count how many records take each branch and keep the counts in the run's evidence folder: one row per branch.
3. A branch at 0: find out why. If the keys can never match, drop or disable that part, or state it in the pull request description and in EXPLAIN §6.

**Check before handing over:** the stage evidence README has one row per matching branch with its count, and every branch at 0 is explained there and in EXPLAIN §6. This check is read, not scripted.

## TEST-4 — Withdrawn

**Withdrawn 2026-11-10:** simple-erp has no Lambda handlers. TEST-7 makes every new entry point start with its tests. The ID is kept so that it is never reused.

## TEST-5 — A test calling a paid AI runs through the cost guard, $20 per ticket

**Scope:** every test, check or run that makes a paid AI call, directly or through a service on a stage. Claude Code's own sessions are not concerned.

**Rule:**
1. The AI tests of a ticket cost **$20 at most, all runs together**.
2. Each such run goes through `ai-cost run --ticket <KEY> --estimate-usd <n> … -- <command>` (`ai-test-cost` skill). It is refused when its estimate does not fit, measured while it runs, and killed at 90 % of the cap, which blocks the ticket.
3. Only the person who owns the ticket raises its cap (`ai-cost raise-cap`, in their own terminal). The hook refuses it from a Claude session.
4. Every run is in the ticket's `tests-evidences/COST.md`, written by the guard. The evidence README of a paid test names its run id.

**Why:** a paid suite run in a loop can cost tens of dollars unnoticed. A cap enforced while the run goes, on the calls the run really made, is the only limit that holds.

**How to apply:** the `ai-test-cost` skill. A `PreToolUse` hook refuses a command of `.claude/skills/ai-test-cost/conf/paid-commands.yaml` that is not run through the guard. A new paid command is added there.

**Check before handing over:** run from the ticket folder. It must print nothing.

```bash
python3 -I - <<'PY'
import pathlib, re
evidence = pathlib.Path("tests-evidences")
texts = " ".join(p.read_text(errors="ignore") for p in evidence.rglob("*.md") if p.name != "COST.md") if evidence.is_dir() else ""
if re.search(r"(?i)\bclaude-(fable|opus|sonnet|haiku)|anthropic api|-m llm|\bllm judge", texts) and not (evidence / "COST.md").is_file():
    print("tests-evidences mention paid AI runs but COST.md is missing: run them through ai-cost run")
PY
```

## TEST-6 — A front-end change has Playwright tests, run against the real images

**Scope:** `frontends/<frontend>/`.

**Rule:** a change to a front end adds or updates Playwright tests in `frontends/<frontend>/e2e/` for every screen, element and flow it touches. They run against the real images started by `compose.e2e.yaml`, never against a development server (`AGENT.md`, "Front-end tests"). Tests tagged `@smoke` run on the dev stage; the whole suite runs on QA.

**Why:** a front end is tested where it ships: the built image, behind its real back end. A development server hides build, routing and configuration errors.

**How to apply:** write the Playwright tests first (TEST-7), run them locally with `docker compose -f compose.e2e.yaml up -d --wait` then `npx playwright test`, and keep the HTML report and `results.json` (TEST-9). Configure `trace`, `video` and `screenshot` as `retain-on-failure`.

**Check before handing over:** this must print nothing:

```bash
git diff --name-only origin/develop...HEAD | python3 -I -c "
import sys, collections
changed = [l.strip() for l in sys.stdin if l.startswith('frontends/')]
fronts = collections.defaultdict(lambda: [False, False])
for p in changed:
    name = p.split('/')[1]
    fronts[name][0 if '/src/' in p else 1] |= ('/src/' in p) or ('/e2e/' in p)
for name, (src, e2e) in fronts.items():
    if src and not e2e:
        print(f'frontends/{name}: src changed but no Playwright test in e2e/')
"
```

## TEST-7 — Tests are written and seen failing before the code

**Rule:** for every code step of a ticket, in this order, with no exemption:

1. **Write the tests first** (unit, and Playwright or Bruno when TEST-1 or TEST-6 applies), and commit them in a **tests-only commit**: test files, fixtures and configuration, no production code.
2. **Run them and record the red run** in `tests-evidences/local-<YYYY-MM-DD>-tdd-red-<step>/` (TEST-8), on that commit. The run must fail **on the new tests only**, and each failure must point at the code the step will write: an assertion, or the module or name the step adds. A syntax error, a broken fixture or a failing unrelated test is not a red run: fix it and run again.
3. **Then write the production code**, commit it, and record the green run on that commit in `tests-evidences/local-<YYYY-MM-DD>-unit-<step>/`.

A bug fix starts with a test that reproduces the bug, seen red.

Production code means `src/`, `services/*/src/`, `frontends/*/src/`, `packages/` and `.claude/skills/*/src/`.

**Why:**
- A test written after the code tends to describe what the code does, not what it must do. Seen failing first, it proves it can catch the missing behaviour.
- The tests-only commit and the red run make the order provable, not a matter of trust.

**How to apply:**
- `ticket-docs record-run` writes the evidence folder, with the commit, the command and the reports.
- A `PreToolUse` hook (`ticket-docs git-gate`) refuses a `git commit` on a ticket branch (`feature/`, `bugfix/`, `hotfix/` with a `GH-<n>` key) that stages production code while:
  - it also stages **new** test files (tests come in their own, earlier commit; changing an existing test with the code is allowed);
  - or the ticket has no red run whose commit is an ancestor of `HEAD` and is newer than the ticket's latest green run.
- **GIT-4 squashes the branch before its pull request.** Before squashing, `ticket-docs history-bundle <KEY>` saves the branch's commits in `tests-evidences/history/pre-squash-<date>.bundle`, so that the order stays provable after the squash. The squash commit adds tests and code together: the gate lets it through only with the owner's one-shot permit, `ticket-docs allow-squash <KEY>` run in their own terminal after `git reset --soft <base>`, confirmed by typing back the code shown on `/dev/tty` (GIT-4).
- The gate also reads every `git commit` on the safe side: abbreviated or unknown options, `-a`/`-i`/`-o`/`-p`/paths and index-writing commands on the same line count every working-tree change; `git apply`, `stash`, `reset`, `merge`… must run on their own line. On a ticket branch it refuses `commit-tree`, `update-ref`, `replace`, `hash-object -w`, `branch -f` onto the current branch and a `reset` outside the branch's history.
- `ticket-docs file-gate` (`PreToolUse` on Write, Edit, MultiEdit, NotebookEdit) refuses a file in the squash permits or the AI test ledgers, and `git-gate` refuses a Bash command naming either folder or running `allow-squash`.
- **What these barriers stop, and what they cannot:** `git-gate`, `file-gate` and the `/dev/tty` code stop accidents and a Claude session going down the wrong path: a squash without the owner, a permit or an AI cost ledger written by a tool call, `allow-squash` or `raise-cap` run from Claude's Bash (it has no terminal). They cannot stop a deliberate forgery by a process running as the same user, which can write any file and drive a pseudo-terminal: Claude runs as the owner's own user and there is no other account to hold a secret. `ticket-docs check <KEY>` at hand-over, CI and the review are the enforcement of TEST-7 and GIT-4.

**Check before handing over:** `ticket-docs check <KEY>` prints nothing. It checks that every code step of PROGRESS.md has a red run whose raw output shows failures, recorded on a tests-only commit that is an ancestor of the step's first production-code commit.

## TEST-8 — Nothing passes without its evidence

**Rule:** a test, check or stage run counts as passing only when its evidence folder `tests-evidences/<where>-<YYYY-MM-DD>-<check>/` exists and its `README.md` gives:
- **Command:** the exact command, with credentials read from the environment, never pasted;
- **Commit:** the full commit hash it ran on, and the branch;
- **Kind:** `unit`, `gui`, `e2e` or `check`;
- **Where:** `local`, `ci`, `dev` or `qa`;
- **Result:** the verdict with its counts;
- **Artefacts:** the raw output files (console, reports, the Actions run URL and its downloaded artifacts).

A ✅, "PASS", "green", "passes" or "works", in a reply, PROGRESS.md, EXPLAIN.md or a pull request description, without a link to such a folder is **not** passing. A run on an older commit than the one claimed does not count. A scratchpad output is never evidence. A run whose environment failed is ⚠️ invalid and run again.

**Why:** a claim is only as good as what lets someone else check it. The commit ties the result to the code. The raw output lets a reviewer see what really happened.

**How to apply:** record every run with `ticket-docs record-run`. Link the folder wherever the result is stated.

**Check before handing over:** `ticket-docs check <KEY>` prints nothing. It checks every ✅ and PASS of PROGRESS.md and EXPLAIN.md, and every evidence README.

## TEST-9 — Every test report is kept

**Rule:** every test report is kept for traceability: unit, GUI (Playwright on a front end) and E2E (a stage run), passed, failed, red or invalid.

1. **Per run**, in the ticket's evidence folder:
   - **unit:** `report.xml` (JUnit), `report.html` and `console.txt`;
   - **GUI and E2E:** the Playwright HTML report and `results.json`, the Bruno JUnit and JSON reports, and the screenshots, traces and videos of failed tests (`retain-on-failure`);
   - **CI and stage runs:** the run URL, and the artifacts downloaded with `gh run download <run-id>` (workflows upload them with `if: always()`; they expire after 90 days, the copy does not).
2. **No evidence folder is ever deleted**, failed and invalid runs included. They are marked ❌ or ⚠️.
3. **No file over 5 MB** in an evidence folder: a bigger one stays in the run's artifacts or the Release assets, and the README links to it.
4. **The index** `docs/tickets/README.md` is generated by `ticket-docs report-index`, never written by hand: one row per run with the ticket, kind, place, commit, verdict, counts and folder.
5. **Archive:** `docs/tickets/` is not versioned. At every hand-over and every review round, `ticket-docs archive <KEY>` zips the ticket folder and uploads it to the GitHub pre-release `evidence-GH-<n>` (`GH-<n>-<YYYYMMDD-HHMM>.zip`, earlier assets kept), and the issue gets a comment with the link.
6. **Releases:** `release.yml` attaches the QA run's reports to the version's GitHub Release.

**Why:** a test result is evidence only while someone can open it. Ticket folders live on one machine, and Actions artifacts expire: the archive and the Release assets keep the proof as long as the code it tested.

**How to apply:** `ticket-docs record-run` for every run, `ticket-docs report-index` after it, `ticket-docs archive <KEY>` at hand-over.

**Check before handing over:** `ticket-docs check <KEY>` prints nothing. It checks the report files of each run folder, the 5 MB limit, the index, and once handed over, that the pre-release has an asset newer than the newest evidence folder.
