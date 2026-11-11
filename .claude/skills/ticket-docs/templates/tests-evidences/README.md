# <KEY> — Test evidence

One folder per run: `<where>-<YYYY-MM-DD>-<check>/` (`local`, `ci`, `dev`, `qa`), written by `ticket-docs record-run`, with a `README.md` (what was run, command, commit, kind, place, date, result, catalogue IDs and ACs) and the raw reports. How each level runs: [TESTS-NOTICE.md](../TESTS-NOTICE.md).

Rules:
- Every code step has a red run (`local-<date>-tdd-red-<step>`) on its tests-only commit, then a green run (`local-<date>-unit-<step>`) on its code commit (TEST-7).
- Every ✅ or PASS in [PROGRESS.md](../PROGRESS.md) or [EXPLAIN.md](../EXPLAIN.md) links to a folder here (TEST-8).
- No folder is ever deleted, failed and invalid runs included (TEST-9). No file over 5 MB.
- Scratchpad outputs are not evidence: re-run into a folder here.
- No secret, token, password or signed URL in any file.
- `history/` holds the branch's commits saved before each squash (GIT-4). `COST.md` is written by `ai-cost` (TEST-5).

Planned folders (PLAN.md): <`local-<date>-tdd-red-<step>`, `local-<date>-unit-<step>`, `ci-<date>-checks`, `dev-<date>-stage`, `qa-<date>-stage`…>.

## Index

| Folder | Date | Where | Kind | Check | Result | IDs / ACs |
|---|---|---|---|---|---|---|
