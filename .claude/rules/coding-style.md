# Coding style rules

These rules apply to every project: application code, tests and infrastructure. They apply to anyone who writes code for the projects, people and AI agents alike.

## How this file works

- Each rule has an ID (`CS-<n>`) that never changes. Reviews and commit discussions can cite it ("breaks CS-1").
- New rules are added at the end with the next free ID and a row in the summary table. A rule that is dropped stays in the file, marked **Withdrawn** with the date, so that its ID is never reused.
- Each rule uses the same parts: **Rule**, **Why**, **Check before committing**.
- A rule applies to every project unless its **Scope** line narrows it.
- Rules can also come from code reviews: the **pr-review-followup** skill turns a verified review remark that states a convention into a new rule here, with a **Source** line naming the pull request and the comment.
- **`AGENT.md` at the repository root is the main rulebook for simple-erp code** (layout, file shape, lifecycle, imports, typing, naming, docstrings, exceptions, messages, logging, models, tests). These CS rules add to it. Where both cover the same point, `AGENT.md` wins.
- The **Check** snippets run from the repository root. They read every `src/` folder: `src/`, `services/*/src/`, `packages/*/src/` and `.claude/skills/*/src/`.
- Rules CS-1 to CS-16 come from the harness this one was adapted from (2026-11-10). Their **Why** keeps the reason each rule exists.

| ID | Rule | Enforced since |
|---|---|---|
| [CS-1](#cs-1--no-duplicated-code-or-behaviour) | No duplicated code or behaviour, in code, tests or infrastructure | 2026-10-07 |
| [CS-2](#cs-2--no-ticket-references-in-code-comments) | No ticket names or references in code comments | 2026-10-07 |
| [CS-3](#cs-3--every-class-declares-its-constructor) | Every class declares its constructor | 2026-10-07 |
| [CS-4](#cs-4--private-methods-sit-under-internal-helpers-methods) | Private methods sit under "Internal Helpers Methods" (Python projects) | 2026-10-08 |
| [CS-5](#cs-5--runnable-children-only-expose-the-abstract-classs-public-methods) | Runnable children only expose the abstract class's public methods | 2026-10-08 |
| [CS-6](#cs-6--structured-data-is-a-pydantic-model-of-the-models-package) | Structured data is a Pydantic model of the models package, never a TypedDict (Python projects) | 2026-10-08 |
| [CS-7](#cs-7--a-folder-holds-at-most-five-source-files) | A folder holds at most five source files: beyond, one sub-folder per entity type (Python projects) | 2026-10-08 |
| [CS-8](#cs-8--no-any-or-object-type-hints-ars-e2e-runner) | ~~No `Any` or `object` type hints, except on `*args` and `**kwargs` (ars-e2e-runner)~~ **Withdrawn 2026-11-10:** `AGENT.md` forbids `Any` everywhere, and `tests/conventions` enforces it | 2026-10-08 |
| [CS-9](#cs-9--state-that-must-outlive-one-invocation-lives-at-module-scope-lambda-handlers) | ~~State that must outlive one invocation (caches, clients, built indexes) lives at module scope, never in what a handler builds per message (Lambda handlers)~~ **Withdrawn 2026-11-10:** simple-erp has no Lambda handlers | 2026-11-05 |
| [CS-10](#cs-10--logs-reuse-computed-results-and-a-per-item-log-stays-short) | Logs reuse what the code already computed, and a log written for every item stays short: counts and ids, lists only on warnings and errors | 2026-11-05 |
| [CS-11](#cs-11--a-failure-returned-as-a-value-is-never-dropped-and-nothing-is-recorded-as-done-before-it-is-done) | A failure returned as a value is never dropped, and nothing is recorded as done before it is done; a recovery path (retry, re-read) handles its own errors like the main path; a state saved under a new version carries over only what is still valid under it | 2026-11-05 |
| [CS-12](#cs-12--new-iam-roles-take-managed-policies-and-new-taggable-resources-carry-the-four-tags) | ~~New IAM roles take their permissions from `AWS::IAM::ManagedPolicy` resources, never inline `Policies`; new taggable resources carry Application, Cost Center, Project and Environment (CloudFormation / SAM templates)~~ **Withdrawn 2026-11-10:** simple-erp has no CloudFormation or SAM templates | 2026-11-05 |
| [CS-13](#cs-13--one-layer-owns-the-retry-of-a-call) | One layer owns the retry of a call: code that retries a call turns the called client's own retry off, so the attempts never multiply | 2026-11-06 |
| [CS-14](#cs-14--no-nested-imports) | No nested imports: every import sits at the top of its module, never inside a function, a method or a class | 2026-11-06 |
| [CS-15](#cs-15--more-than-three-branches-on-one-value-are-a-match) | More than three `if` / `elif` branches in a row are a `match` / `case` (Python) or a `switch` (TypeScript) | 2026-11-06 |
| [CS-16](#cs-16--a-fixed-set-of-string-values-is-an-enum-never-compared-as-raw-strings) | A fixed set of string values is a `StrEnum` (Python) or an enum / union of constants (TypeScript): code compares with its members, never with a raw string literal | 2026-11-06 |

## CS-1 — No duplicated code or behaviour

**Rule:** do not write something that already exists, either as the same code or as code that does the same job in another way.

- **Code:** if a helper, validation, mapping, constant, query or client already exists, reuse it. If it is close to what you need but not quite right, extend it or make it more general. Do not write a second version next to it.
- **Tests:** test each behaviour once at each level (unit, integration, acceptance). Put shared setup in fixtures, factories or helpers. Do not copy test bodies to change one input; parametrize the test instead. Do not add a test that asserts what an existing test at the same level already asserts.
- **Infrastructure:** define each resource, IAM policy, environment variable, pipeline step, Makefile target and template block once, and reference it everywhere else. Do not add a resource that does the same job as an existing one.

**Why:** copies drift apart. A fix applied to one copy leaves the bug in the other, and reviewers have to read the same logic twice.

**Check before committing:**
1. Before writing anything new, search the repository for an existing version: the function name, key strings, endpoint paths, table or resource names.
2. Read the diff and look for blocks that repeat each other or repeat code that is already in the repository.
3. If you think a duplicate cannot be avoided, ask before committing it, and explain why.

## CS-2 — No ticket references in code comments

**Rule:** comments and docstrings in code, tests and infrastructure must not contain:
- ticket names (`GH-12`);
- ticket-process words ("spike", "step 0", "AC3", "as decided in the ticket").

Write the reason itself instead.

| Do not write | Write |
|---|---|
| `# GH-67: skip empty vendors` | `# A vendor with no subscriptions must not appear in the split` |
| `// spike result, see GH-65` | `// Checked on dev1: the API returns amounts in cents` |

Ticket references belong in the commit message (the `[GH-<n>]` title prefix stays), the pull request description and the ticket folder (`docs/tickets/GH-<n>/`).

**Why:** the code outlives the ticket. A reader of the code should understand the reason without opening the issue.

**Check before committing:** this command must return no comment lines:

```bash
git diff origin/develop -U0 | grep -E '^\+.*\bGH-[0-9]+'
```

## CS-3 — Every class declares its constructor

**Rule:** every class written by hand declares its constructor: `__init__` in Python, `constructor` in TypeScript. The constructor sets every instance attribute and documents its arguments. This also applies when the class has no state yet:
- a stateless service takes at least its logger;
- a class with only class methods still declares a constructor;
- a subclass of a framework class (`QObject`, `yaml.SafeLoader`, an `ABC`…) declares one that calls the parent's.

Exceptions: the constructor is written by the language or a framework, or is forbidden by it.

| Case | Why it has no hand-written constructor |
|---|---|
| `@dataclass`, Pydantic models, enums, `TypedDict` | The constructor is generated from the fields (a `TypedDict` cannot declare one) |
| Exception classes that only add a docstring | The base project exception holds the constructor |
| A subclass with no attribute of its own, whose parent declares the constructor | A pass-through constructor would repeat the parent's (CS-1) |
| pytest `Test*` classes | pytest does not collect a test class that has an `__init__` |

**Why:** a reader finds everything an instance holds in one place, and adding a dependency (logger, client, configuration) later does not change every caller.

**Check before committing:** this Python check lists the classes with no `__init__` of their own or from a project parent, leaving out the exceptions above. Run it from the project root; it must print nothing:

```bash
python3 - <<'PY'
import ast, pathlib
GENERATED = {"BaseModel", "BaseSettings", "Enum", "StrEnum", "IntEnum", "Exception", "TypedDict"}
classes = {}
for path in (p for p in pathlib.Path(".").glob("**/src/**/*.py") if not {".venv", "node_modules"} & set(p.parts)):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.ClassDef):
            bases = {getattr(base.value if isinstance(base, ast.Subscript) else base, "id", getattr(base, "attr", "")) for base in node.bases}
            decorators = {getattr(d, "id", getattr(getattr(d, "func", None), "id", "")) for d in node.decorator_list}
            declared = any(isinstance(item, ast.FunctionDef) and item.name == "__init__" for item in node.body)
            generated = "dataclass" in decorators or bool(bases & GENERATED) or any(base.endswith("Error") for base in bases)
            classes[node.name] = (f"{path}:{node.lineno}", bases, declared or generated)
def passes(name, seen=frozenset()):
    location, bases, ok = classes[name]
    return ok or any(base in classes and base not in seen and passes(base, seen | {name}) for base in bases)
for name, (location, bases, ok) in sorted(classes.items()):
    if not passes(name):
        print(location, name)
PY
```

## CS-4 — Private methods sit under "Internal Helpers Methods"

**Scope:** Python code only. Front ends follow the rules of their framework.

**Rule:** a class body is ordered in banner sections: the dunder methods first, then `# Internal Helpers Methods #`, then `# Publicly Exposed Methods #`. Every method whose name starts with `_` (dunders excepted) sits in the "Internal Helpers Methods" section, never among the public ones.

```python
    ############################
    # Internal Helpers Methods #
    ############################

    def _job_path(self) -> str:
        ...

    ############################
    # Publicly Exposed Methods #
    ############################

    async def run(self, *args: List[Any], **kwargs: Dict[str, Any]) -> AsyncGenerator[JenkinsBuild, None]:
        ...
```

**Why:** a reader sees at once what a class offers to its callers and what only serves its own implementation.

**Check before committing:** this Python check lists the private methods outside the section. Run it from the project root; it must print nothing:

```bash
python3 - <<'PY'
import ast, pathlib, re
BANNER = re.compile(r"^\s*#\s*(.+?)\s*#\s*$")
for path in sorted((p for p in pathlib.Path(".").glob("**/src/**/*.py") if not {".venv", "node_modules"} & set(p.parts))):
    lines = path.read_text().splitlines()
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name.startswith("_") and not item.name.startswith("__"):
                    start = (item.decorator_list[0].lineno if item.decorator_list else item.lineno) - 1
                    banners = [m.group(1) for m in map(BANNER.match, lines[node.lineno:start]) if m and set(m.group(1)) - {"#"}]
                    if not banners or banners[-1] != "Internal Helpers Methods":
                        print(f"{path}:{item.lineno} {node.name}.{item.name}")
PY
```

## CS-5 — Runnable children only expose the abstract class's public methods

**Rule:** a class that inherits from `Runnable` or `AsyncRunnable` (`AGENT.md`, "Lifecycle and factories"; the harness tools use `harness_core.lifecycle`) exposes no public method other than the ones the base class declares: `initialize`, `run`, `close` and `execute`. Everything else a child needs is a private method (`_name`, CS-4). An intermediate abstract class (e.g. `BaseAPIClient`) follows the rule too: the helpers it gives its children are private.

**Why:** every Runnable is used the same way: built by its factory, then `execute()`, and its results read from its attributes. A caller never depends on an extra method of one implementation, so implementations can be swapped and tested the same way.

**Check before committing:** this Python check lists the public methods a Runnable child adds. Run it from the project root; it must print nothing:

```bash
python3 - <<'PY'
import ast, pathlib
ALLOWED = {"initialize", "run", "close", "execute"}
classes = {}
for path in (p for p in pathlib.Path(".").glob("**/src/**/*.py") if not {".venv", "node_modules"} & set(p.parts)):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.ClassDef):
            bases = [getattr(b.value if isinstance(b, ast.Subscript) else b, "id", "") for b in node.bases]
            public = [i.name for i in node.body if isinstance(i, (ast.FunctionDef, ast.AsyncFunctionDef)) and not i.name.startswith("_")]
            classes[node.name] = (f"{path}:{node.lineno}", bases, public)
def runnable(name, seen=()):
    return any(b in {"Runnable", "AsyncRunnable"} or (b in classes and b not in seen and runnable(b, seen + (b,))) for b in classes[name][1])
for name, (location, bases, public) in sorted(classes.items()):
    extra = [method for method in public if method not in ALLOWED]
    if name not in {"Runnable", "AsyncRunnable"} and runnable(name) and extra:
        print(location, name, extra)
PY
```

## CS-6 — Structured data is a Pydantic model of the models package

**Scope:** Python code only. Front ends follow the rules of their framework.

**Rule:** a structure with named fields (a record, an API payload, a workflow state such as a LangGraph state or its input) is a Pydantic model (`BaseModel`) in the `models` package of its service or tool (`AGENT.md`, "Pydantic models"), one model per file. Never a `TypedDict`, and never a plain `dict` passed around with known keys. Each field has its type, a `description` and `examples` in `Field(...)`. A state shared by several steps keeps its merge rules on the field (e.g. `Annotated[List[str], operator.add]`).

**Why:** a model validates its data where it is built, documents each field once, and gives typed attribute access (`state.branch`, not `state["branch"]`), so a typo fails at type-check time instead of at run time. Keeping every model in `models/` makes them easy to find and to reuse instead of redefining them.

**Check before committing:** this must print nothing:

```bash
grep -rn --include="*.py" "TypedDict" src services packages .claude/skills/*/src 2>/dev/null
```

## CS-7 — A folder holds at most five source files

**Scope:** Python code only. Front ends follow the rules of their framework.

**Rule:** a source folder holds at most five source files (`__init__.py` and `conftest.py` not counted). When a sixth one comes, group the files into sub-folders, one per entity type (e.g. `workers/ticket/`, `workers/jenkins/`); the base class the others share stays at the folder's root. The tests mirror the same sub-folders.

**Why:** a short folder reads at a glance, and its sub-folders name the entities of the code, so a new file finds its place and a reader finds a class by what it is about.

**Check before committing:** this lists the folders over the limit. Run it from the project root; it must print nothing:

```bash
for d in $(find src tests services packages .claude/skills -type d -not -path "*__pycache__*" -not -path "*/.venv*" -not -path "*/node_modules*" 2>/dev/null); do
  n=$(find "$d" -maxdepth 1 -name "*.py" ! -name "__init__.py" ! -name "conftest.py" | wc -l)
  [ "$n" -gt 5 ] && echo "$n $d"
done
```

## CS-8 — No `Any` or `object` type hints (ars-e2e-runner)

**Withdrawn 2026-11-10:** `AGENT.md` forbids `Any` everywhere, and `tests/conventions` enforces it. The ID is kept so that it is never reused.

## CS-9 — State that must outlive one invocation lives at module scope (Lambda handlers)

**Withdrawn 2026-11-10:** simple-erp has no Lambda handlers. The ID is kept so that it is never reused.

## CS-10 — Logs reuse computed results, and a per-item log stays short

**Rule:**
- **A log never recomputes business results.** The code that builds a result returns what the log needs with it (a summary, counts); the log does not call a second entry point that re-runs ranking, matching or placement.
- **A log written for every item (a customer, a message, a row) stays short:** counts, ids and statuses. A list whose length grows with the data (names, lines, items) goes only on a `warning` or `error` log, and only with the entries that need action. A list bounded by a fixed set of literals (field names, statuses) is fine.

**Source:** inherited from the harness this one was adapted from (2026-11-10).

**Why:** a second pipeline written for a log can drift from the one that built the result (CS-1), and costs CPU on every item. Long per-item lines multiply the log volume and its cost by the number of items, and bury the few lines someone must act on.

**Check before committing:** this check is read for Python code: a log call inside a loop logs counts and ids only. For a front end in TypeScript with a `logEvent` helper, the script below runs from its folder and must print nothing. It lists the fields of `logEvent({status: 'success', …})` calls whose type is a list that grows with the data. Re-running a pipeline for a log has no automatic check: read the diff for log helpers that call the domain again.

```bash
node - <<'JS'
// Lists the fields of success logs (logEvent({status: 'success', ...})) whose type is an array.
const ts = require('typescript');
const path = require('path');
const config = ts.getParsedCommandLineOfConfigFile('tsconfig.json', {}, {...ts.sys, onUnRecoverableConfigFileDiagnostic: () => {}});
const program = ts.createProgram(config.fileNames.filter((file) => file.includes('/src/')), config.options);
const checker = program.getTypeChecker();
for (const source of program.getSourceFiles()) {
    if (source.isDeclarationFile || !source.fileName.includes('/src/')) continue;
    const visit = (node) => {
        if (ts.isCallExpression(node) && node.expression.getText(source) === 'logEvent' && node.arguments[0] && ts.isObjectLiteralExpression(node.arguments[0])) {
            const props = node.arguments[0].properties;
            const success = props.some((p) => ts.isPropertyAssignment(p) && p.name.getText(source) === 'status' && p.initializer.getText(source) === "'success'");
            if (success) {
                for (const p of props) {
                    if (!ts.isPropertyAssignment(p) && !ts.isShorthandPropertyAssignment(p)) continue;
                    const type = checker.getTypeAtLocation(p.name);
                    const element = checker.isArrayType(type) ? checker.getTypeArguments(type)[0] : undefined;
                    // A list bounded by a fixed set of literals (field names, statuses) does not grow with the data.
                    const bounded = element !== undefined && (element.isUnion() ? element.types : [element]).every((t) => t.isStringLiteral() || t.isNumberLiteral());
                    if ((checker.isArrayType(type) || checker.isTupleType(type)) && !bounded) {
                        const {line} = source.getLineAndCharacterOfPosition(p.getStart(source));
                        console.log(`${path.relative(process.cwd(), source.fileName)}:${line + 1} success log field '${p.name.getText(source)}' is a list (${checker.typeToString(type)}): log its count, keep the names for warnings and errors`);
                    }
                }
            }
        }
        ts.forEachChild(node, visit);
    };
    visit(source);
}
JS
```

## CS-11 — A failure returned as a value is never dropped, and nothing is recorded as done before it is done

**Rule:** when a step reports its failure **as a value** instead of throwing (`'failed'`, `{ok: false}`, an outcome enum, a `failures` list), and does not throw so that the rest of the run goes on:
- **its caller checks it**: the failure reaches what the run reports (the failure list a handler throws from, the error log, the alarm). A step whose outcome nobody reads is a swallowed exception;
- **the state records an action as done only when it was done**. A "sent", "notified", "processed" or "seen" marker is written from the step's success, not from the decision to try. Otherwise the next run skips work that never happened;
- **a recovery path is guarded like the main path**. Every awaited call inside a retry, a re-read after a conflict, a fallback or a cleanup sits in the same failure handling as the first attempt. An exception escaping there skips everything the run still had to save.
- **a state saved under a new version carries over only what is still valid under it**. When a state records the version its decisions were made with (a prompt version, a source document's date, a schema version) and the run saves it with its own version, the decisions of the old version are either decided again in this run or dropped, never copied as they are (`{...state.seen, ...newDecisions}`). Copied, they pass for current ones: the items the run could not redo (over a cap, in a failed batch, not reported) are skipped for good.

**Source:** inherited from the harness this one was adapted from (2026-11-10).

**Why:** a value-returned failure is invisible unless someone reads it. The run looks clean, the alarm stays silent, and a marker written too early turns a one-off failure into a permanent loss (here, products nobody would ever be told about). Unit tests written with succeeding fakes never see it.

**Check before committing:** this check is read, not scripted. For each function the change adds or edits that returns a failure as a value:
1. find its callers, and check that each failure value reaches the run's failure report;
2. find every state or marker written after it, and check that it depends on the step's success;
3. in each retry, re-read or fallback block, check that the awaited calls are inside the failure handling;
4. find every state saved with a new version marker, and check that the entries it carries over are filtered by the rule that judges them current (`grep -n '\.\.\.state\.' ` on the changed files lists the copies to read);
5. add one spec per path, with a fake that fails: the run reports the failure, and the marker is not written; for a versioned state, a spec chaining two runs across a version change, with an item the first run could not redo.

## CS-12 — New IAM roles take managed policies, and new taggable resources carry the four tags

**Withdrawn 2026-11-10:** simple-erp has no CloudFormation or SAM templates. The ID is kept so that it is never reused.

## CS-13 — One layer owns the retry of a call

**Rule:** a call is retried by **one** layer only. When code wraps a call in its own retry (a loop over attempts, a retry on an answer it cannot parse), the client it calls must not retry as well. Turn the client's retry off on that call (`maxRetries: 0` on an `AIModelClient` request; `maxAttempts: 1` on an AWS SDK client), or drop the outer loop and configure the client. A comment next to the loop states the total number of attempts per call.

The rule is about the **same failure** retried at two layers. A loop that retries only a failure the client never retries is not nested: for example, a conditional-write conflict (HTTP 412) re-read and merged again, where the SDK retries only throttling and server errors.

**Source:** inherited from the harness this one was adapted from (2026-11-10).

**Why:** nested retries multiply: two layers of three attempts make nine calls. That costs latency and money on paid calls (a lost response is billed every time), lengthens outages through stacked backoffs, and breaks any written limit ("one retry"). Each layer looks right on its own, and test doubles hide the inner one.

**Check before committing:** this check is read, not scripted. The command lists the retry loops the branch adds; for each one, open the call inside it and confirm that the client's own retry is off on that call, and that a spec asserts it (for example `call.args[0].maxRetries` equals `0` on every call).

```bash
git diff origin/develop -U0 -- '*.py' '*.ts' | grep -E '^\+.*\b(attempts?|retr(y|ies)|ATTEMPTS|RETRIES)\b' | grep -vE '^\+\s*(//|\*|/\*)'
```

## CS-14 — No nested imports

**Rule:** every import sits at the top of its module, in its import group (`# Standard library imports`, `# Third-party imports`, `# First-party imports`, as `AGENT.md` shows). No import inside a function, a method or a class body, including a lazy import ("only this command needs it") or an optional one (`try: import x` / `except ImportError` inside a function). In TypeScript, the same holds for `require()` and `await import()` inside a function.

- **Start-up time is not a reason.** If a module is slow to load, measure it; when it really matters (a hook run on every call), split the entry point so the fast path's module does not import the slow one.
- **An optional dependency is not a reason either.** The code that needs it lives in a module that only the callers where it is installed import.
- A module-level `if TYPE_CHECKING:` block is at the top of the module, so it is allowed.

**Source:** inherited from the harness this one was adapted from (2026-11-10).

**Why:**
- A reader sees a module's dependencies at once in its import sections. A nested import hides one.
- A nested import fails only when its path runs: an `ImportError` in the middle of a run instead of at start-up.
- An optional import degrades silently: the feature disappears and nothing says why.

**Check before committing:** run from the project root. It must print nothing. It lists the Python imports placed inside a function, a method or a class.

```bash
python3 - <<'PY'
import ast, pathlib
for path in sorted(p for p in pathlib.Path(".").rglob("*.py") if not any(part in {".venv", "node_modules", ".git", "__pycache__"} for part in p.parts)):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            for inner in ast.walk(node):
                if isinstance(inner, (ast.Import, ast.ImportFrom)):
                    print(f"{path}:{inner.lineno} {ast.unparse(inner)}")
PY
```

For TypeScript, this must print nothing either (the indented lines are the ones inside a block):

```bash
git diff origin/develop -U0 -- '*.py' '*.ts' | grep -E '^\+\s+.*(\brequire\(|await import\()'
```

## CS-15 — More than three branches on one value are a match

**Rule:** a chain of more than three `if` / `elif` (`if` / `else if`) in a row is written as a `match` / `case` in Python, a `switch` in TypeScript. Each branch is a `case`; a decision on several values matches a tuple of them, with guards (`case (str() as session_id, LiveSession() as running, _, _) if not running.in_vscode:`); the catch-all is `case _:` (`default:`).

Guard clauses that each `return` early count as such a chain when they decide between outcomes of the same decision (how a session is reached, which command runs).

**Source:** inherited from the harness this one was adapted from (2026-11-10).

**Why:** a `match` shows at once that the branches are the cases of one decision, lists them at the same indentation, and keeps the fallback explicit. A long `elif` chain hides which value each branch tests and invites a branch that tests something else.

**Check before committing:** run from the project root. It must print nothing. It lists the Python `if` / `elif` chains of more than three branches.

```bash
python3 - <<'PY'
import ast, pathlib
for path in sorted(p for p in pathlib.Path(".").rglob("*.py") if not any(part in {".venv", "node_modules", ".git"} for part in p.parts)):
    chained = set()
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.If) and id(node) not in chained:
            branches, current = 1, node
            while len(current.orelse) == 1 and isinstance(current.orelse[0], ast.If):
                current = current.orelse[0]
                chained.add(id(current))
                branches += 1
            if branches > 3:
                print(f"{path}:{node.lineno} {branches} if/elif branches: use match/case")
PY
```

## CS-16 — A fixed set of string values is an enum, never compared as raw strings

**Rule:** when a value can only take a known set of strings (a state, a result, a command name, a kind), the set is a `StrEnum` (Python, `@unique`, in its own file under the models package, as `AGENT.md` says) or an enum / a union of named constants (TypeScript). Model fields are typed with it, so the value is validated where it is read, and the code compares with its members: `state == PullRequestStatus.MERGED`, `result in {BuildResult.FAILURE, BuildResult.ABORTED}`, `match command: case PrWatchCommand.LOG:`. Never `state == "MERGED"` nor `state in ("DECLINED", "SUPERSEDED")`.

The `if __name__ == "__main__":` idiom is not concerned. Free text (a log line, a substring searched in a console) is not a fixed set of values.

**Source:** inherited from the harness this one was adapted from (2026-11-10).

**Why:** a typo in a raw string (`"FAILLED"`) is a branch that never runs, silently. An enum member that does not exist fails at once, the type checker sees it, the set of values is written once and documented, and a value nobody expected is refused where it enters (pydantic validation) instead of falling through every comparison.

**Check before committing:** run from the project root. It must print nothing. It lists the Python comparisons of a value with a string literal (`==`, `!=`, or `in` a literal tuple, list or set of strings).

```bash
python3 - <<'PY'
import ast, pathlib
for path in sorted(p for p in pathlib.Path(".").rglob("*.py") if not any(part in {".venv", "node_modules", ".git", "tests"} for part in p.parts)):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Compare) and ast.unparse(node) != "__name__ == '__main__'":
            for operator, right in zip(node.ops, node.comparators):
                literal = any(isinstance(value, ast.Constant) and isinstance(value.value, str) for value in (node.left, right))
                literals = isinstance(right, (ast.Tuple, ast.List, ast.Set)) and right.elts and all(isinstance(element, ast.Constant) and isinstance(element.value, str) for element in right.elts)
                if (isinstance(operator, (ast.Eq, ast.NotEq)) and literal) or (isinstance(operator, (ast.In, ast.NotIn)) and literals):
                    print(f"{path}:{node.lineno} {ast.unparse(node)}: compare with an enum member")
PY
```

