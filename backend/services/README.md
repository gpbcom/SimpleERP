# backend/services

The back-end services, one per folder, each with its own image. A service holds its `Dockerfile`, `pyproject.toml`,
`conf/`, `src/<service_pkg>/{api,service,storage,models}/` and `tests/`. Its layers call downwards only: `api`, then
`service`, then `storage`, and all three import `models`.

See [D438, the repository layout](../../docs/specs/06-decisions/technical/d438-repository-layout.md) and the
[repository layout](../../docs/technical/architecture/repository-layout.md).
