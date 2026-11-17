# Operations

What runs where, and how to look at it.

## What runs

Nothing is hosted yet. The stages are ephemeral (see [CI/CD and stages](../delivery/ci-cd-and-stages.md)): each one
lives for the duration of its workflow run.

## Images

`ghcr.io/<owner>/simple-erp-<service or front end>`, tagged with the commit SHA (from `develop` and `master`), and with
the version and `latest` at a release. Each service and front end has exactly one image, built from its multi-stage
`Dockerfile` with the repository root as context.

## Logs

- Locally, the coloured console and `logs/` (rotating, see [Configuration](../architecture/configuration.md)).
- On a stage, the services' logs are saved in the run's `stage-reports` artifact (`compose-logs.txt`).
- The harness tools log to `~/.local/state/claude-harness/<tool>.log`, never to the console.

## Target design (specified in GH-2, not built yet)

**Backups (D422).** Continuous PostgreSQL archiving with point-in-time recovery (15 minutes at most lost, RPO), daily
object-storage and vector snapshots, all encrypted per company and kept in another region; recovery within 4 hours
(RTO). One company can be restored without touching others. An automatic restore test runs every month. Self-hosted
installs get the same tooling with a simpler default (daily backups kept 30 days, D24). The hosted edition and IT
providers' platforms keep daily backups 30 days and monthly backups 12 months (D444).

**Upgrades.** Every upgrade is first run on a copy, then applied, with automatic rollback on failure; generated
features' and plugins' tests run first (TC-12, TC-18); versions and paths are in
[Release and versioning](../delivery/release-and-versioning.md).

Decided in [D422](../../specs/06-decisions/technical/d422-backups-and-recovery.md).

Last reviewed: 2026-11-12 (GH-2)
