# T0.25: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- An installer for the laptop profile, `install.sh [--ai on|off]`, first runs a machine check. The check reads memory, cores and Docker root from `docker info`, and free disk from `df`. It compares them with 8192 MiB, 4 cores and 20 GiB, set in `laptop-profile.env`, and exits 0 (fits), 1 (too small, one line per shortfall) or 2 (Docker missing).
- With the AI off (the default), the installer does not pass the Compose profile `ai`. A test fails if any Milvus service in `infra/compose` lacks the `ai` profile, so a future Milvus service can never start on the laptop with the AI off.
- A measure script starts the laptop profile with the AI off, waits 60 s after it is healthy, then reads `docker stats` per container and prints the total. It always takes the stack down when it ends.
- The measure ran on 2026-11-28 on images built locally from `61ef36896`: 111.8 MiB at rest for the P0 stack. It is recorded with its date and machine in the "Today" section of the performance and capacity page.
- The Compose files are set in a single array per script, so the `up`, `ps` and `down` calls cannot drift apart (K13). Tests check that every Compose call uses exactly [base, overlay] (K11).

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Given a machine under the budget, when the installer checks it, then it installs | `TestInstall::test_a_machine_under_the_budget_installs`, `TestCheckMachine::test_a_machine_exactly_at_every_minimum_fits`, tests-evidences/pytest.txt | ✅ Pass |
| 2. Given a machine too small, when the installer checks it, then it tells so | `TestInstall::test_a_machine_too_small_is_told_so`, `TestCheckMachine::test_one_value_below_its_minimum_makes_the_machine_too_small`, tests-evidences/pytest.txt | ✅ Pass |
| 3. Given the P0 stack on the laptop profile at rest, its measured memory is recorded with its date in Performance and capacity | tests-evidences/memory-at-rest.txt, docs/technical/infrastructure/performance-and-capacity.md (Today section) | ✅ Pass |
| 4. Given the AI is off, when the laptop profile starts, then Milvus is not installed | `TestInstall::test_with_the_ai_off_milvus_is_not_installed`, `TestMeasureMemory::test_no_call_enables_the_ai_profile`, `TestMilvusProfile::test_every_milvus_service_is_only_started_by_the_ai_profile` | ✅ Pass |

## Look at first

- The thresholds and how they are read, including the fallback to the script folder when the Docker root is not on this host (as on Docker Desktop): `infra/compose/laptop-profile.env`, `infra/compose/check-machine.sh`.
- The exit codes of the installer and the AI switch: `infra/compose/install.sh`.
- The measure's clean-up trap and the parsing of units: `infra/compose/measure-memory.sh`. It shares the project name `simpleerp` with a real install (see the follow-ups).
- How the measure was taken (local images, AI off, P0 only) and the fact that the 8 GB promise still waits for P2: `docs/technical/infrastructure/performance-and-capacity.md`.
- The stand-in `docker` and `df` that simulate the machine (no mocks, as AGENT.md asks): `tests/infra/compose/helpers.py`.
- No identity, permission or company data is touched. No secret is in code or logs: the PostgreSQL password file was created for the measure and removed, and git ignores it.

## Assumptions accepted

- 4 cores (from the design page) and 20 GiB of free disk (no disk size in the specifications): accepted. Both are recorded and easy to change in `laptop-profile.env`.
- Base file `compose.yaml` hard-coded in the tests, with paths compared resolved (K11): accepted. This is the file T0.21 ships.
- The earlier test failures belonged to the tasks of install.sh and measure-memory.sh (K12, K14), and K13 ran only the measure tests: accepted. The final run shows 1412 passed, 3 skipped.
- Images built locally from `61ef36896` for the measure (K10): accepted. REQ-T09-03 asks for a measured prototype on the owner's machine, and the page says how the images were built.
- Secret file created and removed, Last reviewed date set to 2026-11-28, machine described as 30768 MiB and 22 cores (K10): accepted.

## Follow-ups

- README: the install section should name `ERP_IMAGE_TAG` and the PostgreSQL secret file that install.sh still needs. The "measured later, by ticket T0.25" line is now stale.
- measure-memory.sh: use its own Compose project name, or refuse when the profile is already running, so that its `down` never stops a real install. Guard against an empty container list before `docker stats`.
- test_measure_memory.py: move the module constants `VERBS` and `THREE` into the class as `ClassVar`s, or into helpers.py.
- check-machine.sh: say on stderr when the disk check falls back to the script folder, and test a Docker root path that contains a space.
