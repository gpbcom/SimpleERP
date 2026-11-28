# Performance and capacity

Sizing per company size and capacity planning for IT providers (D25). Nothing of it is built yet.

## Today

### Memory at rest of the laptop profile (measured)

The P0 stack of the laptop profile with the AI off, 60 s after every service is healthy with no request, the memory of
each container from `docker stats`, measured with `infra/compose/measure-memory.sh` (the outputs are in
[`memory-at-rest.txt`](../../tickets/T0.25/tests-evidences/memory-at-rest.txt)). The images were built from the commit
`61ef36896` with `docker build`, as local images, and the measure ran on that commit.

| Date | Machine | Container | Memory at rest (MiB) |
|---|---|---|---|
| 2026-11-28 | 30768 MiB of memory, 22 cores | simpleerp-backoffice-1 | 24.3 |
| 2026-11-28 | 30768 MiB of memory, 22 cores | simpleerp-platform-1 | 53.3 |
| 2026-11-28 | 30768 MiB of memory, 22 cores | simpleerp-postgres-1 | 34.2 |
| 2026-11-28 | 30768 MiB of memory, 22 cores | Total | 111.8 |

This is the P0 stack only, so the 8 GB promise waits for the whole stack in P2 (P0 risks,
[P0 foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#risks)).

## Target design (specified in GH-2, not built yet)

**Targets (D408).** 95 % of screens within 1 second for 250 users at once on one company (as specified); API calls 95 %
within 300 ms; lists of any size paged on the server, first page within 1 second; reports within 5 seconds or moved to
the background with progress; the assistant's first words within 3 seconds with a local model on the reference profile.
Tested on each release against seeded data.

**Resource profiles.**

| Profile | Machine | Budget for SimpleERP |
|---|---|---|
| Laptop | 6 cores, 12 threads, 16 GB, no graphics card (the owner's machine) | The whole stack in Docker Compose within 8 GB of RAM and 4 cores at normal load, to be proved by a measured prototype before it is promised; small quantised local models on CPU or an outside provider per feature; transcriptions and simulations in the background |
| Cloud small, medium, large | Kubernetes nodes | The same images with more memory, replicas and optional GPU nodes |

Milvus standalone runs on every profile, the laptop included (D409), and takes about 2 to 4 GB of the laptop's budget,
so the other services run lean there. With the AI turned off, Milvus is optional and not installed (D22, REQ-T08-01).

**Reporting (TC-15).** Read models and materialised views next to each company's database when self-hosted; a columnar
analytics store (for example ClickHouse) fed by events for IT providers, the hosted edition and time series (F17
signals, F22 usage). The columnar store keeps each company apart (a database or partition per company, reached only with
the company context) and is reached by a company's deletion and a person's erasure (REQ-T01-08).

**Cache.** A self-hosted in-memory cache (for example Valkey) for sessions, rights, country-pack values and hot reads,
every key prefixed by the company, invalidated by events; never personal data without expiry.

Decided in [D408](../../specs/06-decisions/technical/d408-performance-and-profiles.md).

Last reviewed: 2026-11-28 (GH-2)
