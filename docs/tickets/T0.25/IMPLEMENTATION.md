# T0.25: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- The installer checks the machine against the 8 GB budget, and tells a machine that is too small (acceptance criteria 1 and 2 of [TICKET.md](TICKET.md)).
- The measure is recorded with its date in the performance and capacity page ([`docs/technical/infrastructure/performance-and-capacity.md`](../../../docs/technical/infrastructure/performance-and-capacity.md#L7-L22)).
- With the AI off, Milvus is not installed (criterion 4).
- No command line in `backend/`, `plugins/` or `sdk/` ([AGENT.md](../../../AGENT.md)): the scripts live in `infra/compose/`, which is outside that rule.
- Tests prefer real things to mocks ([AGENT.md](../../../AGENT.md)): the scripts run for real against a stand-in `docker` and `df` ([`tests/infra/compose/helpers.py:13-53`](../../../tests/infra/compose/helpers.py#L13-L53)).
- The laptop overlay is laid over the base file shipped by T0.21 ([`infra/compose/README.md:41-52`](../../../infra/compose/README.md#L41-L52)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Where the measure's images come from | Built locally from the measured commit | Pull the published images by commit SHA | The measure is of local builds, not the shipped images |
| [D2](#d2) | How the scripts hold the Compose files | A bash array, `compose_files`, used by every call | Write both `-f` in each call, or export `COMPOSE_FILE` | Needs bash arrays, which the scripts already need |
| [D3](#d3) | What the tests check on Compose calls | Every call carries exactly [base, overlay] in order | Check only the `up` call | Stricter: fails if a call drops `-f` |
| [D4](#d4) | The Total row of the measure table | Kept, with the machine column filled | Leave the machine empty on that row | The machine is repeated on each row |
| [D5](#d5) | Where the thresholds live | One env file, `laptop-profile.env` | Numbers written in each script | One more file to read |

## <a id="d1"></a>D1: Where the measure's images come from

**Chosen:** build the P0 images locally from the measured commit · **Where:** [`docs/technical/infrastructure/performance-and-capacity.md:7-12`](../../../docs/technical/infrastructure/performance-and-capacity.md#L7-L12) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ Local build from `61ef36896` | Measures what this commit builds, needs no registry access | The images are not the shipped ones |
| Pull the published images tagged with the commit SHA | Would measure what ships | The registry images were not available (K10's reason) |
| Stop as blocked until the person runs the measure | Nothing recorded from a stand-in | Leaves criterion 3 unmet |

**Trade-off:** a measure of local builds, said so on the page, because REQ-T09-03 asks for a measured prototype.

**Revisit when:** the images are published, or when P2 completes the stack and the 8 GB promise is tested.

## <a id="d2"></a>D2: How the scripts hold the Compose files

**Chosen:** a bash array used by `down`, `up` and `ps` · **Where:** [`infra/compose/measure-memory.sh:36`](../../../infra/compose/measure-memory.sh#L36) · **Source:** K13

| Option | For | Against |
| --- | --- | --- |
| ✅ Array `compose_files` | The list is written once, so the calls cannot drift apart | Needs a bash array |
| Both `-f` in each of three calls | No array | Three places to keep equal |
| Export `COMPOSE_FILE` | Short calls | Named by K13 as an alternative; no reason against recorded (open point) |

**Trade-off:** bash arrays are fine because the script already requires bash. [`infra/compose/install.sh:35`](../../../infra/compose/install.sh#L35) uses the same shape for its `compose` array.

**Revisit when:** a script must run under plain `sh`.

## <a id="d3"></a>D3: What the tests check on Compose calls

**Chosen:** every compose call has exactly [base, overlay] in order · **Where:** [`tests/infra/compose/measure_memory/test_measure_memory.py:62-72`](../../../tests/infra/compose/measure_memory/test_measure_memory.py#L62-L72) and [`tests/infra/compose/install/test_install.py`](../../../tests/infra/compose/install/test_install.py#L15-L16) · **Source:** K11

| Option | For | Against |
| --- | --- | --- |
| ✅ Every call | Matches the brief "every compose call"; catches a `ps` or `down` on the wrong project files | Fails if a script drops `-f` on `ps` or `down` |
| Only `up` | Looser | A `down` without the overlay would pass unseen |

**Trade-off:** stricter tests, which a harmless refactor of `ps` may break. The base name `compose.yaml` is written in the tests (accepted assumption).

**Revisit when:** T0.21 renames the base file.

## <a id="d4"></a>D4: The Total row of the measure table

**Chosen:** keep the row with the machine filled · **Where:** [`docs/technical/infrastructure/performance-and-capacity.md:14-19`](../../../docs/technical/infrastructure/performance-and-capacity.md#L14-L19) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ Machine filled | Every row reads the same way | Repeats the machine |
| Machine empty on Total | Less repetition | The brief asked for it filled |

**Trade-off:** a little repetition for a uniform table.

**Revisit when:** the table gets many rows per date.

## <a id="d5"></a>D5: Where the thresholds live

**Chosen:** one file, read by the scripts and by the tests · **Where:** [`infra/compose/laptop-profile.env:3-13`](../../../infra/compose/laptop-profile.env#L3-L13) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ `laptop-profile.env` | One change moves the check, the measure and the tests ([`tests/infra/compose/helpers.py:56-65`](../../../tests/infra/compose/helpers.py#L56-L65) reads it) | Scripts must `source` it |
| Numbers in each script | Self-contained scripts | They could differ; the unmeasured disk assumption would be hidden in code |

**Trade-off:** one more file, with each value commented with its source. The review accepted the disk value as visible and easy to change.

**Revisit when:** the specifications give a disk size, or the budget of D408 changes.

## 📝 Assumptions behind the choices

- 20 GiB of free disk and 4 cores: supports [D5](#d5).
- Base file `compose.yaml` and resolved path comparison (K11): supports [D3](#d3).
- Images built locally because the registry images were not available (K10): supports [D1](#d1).
