# Operations

What runs where, and how to look at it.

## What runs

Nothing is hosted yet. The stages are ephemeral (see [CI/CD and stages](ci-cd-and-stages.md)): each one lives for the
duration of its workflow run.

## Images

`ghcr.io/<owner>/simple-erp-<service or front end>`, tagged with the commit SHA (from `develop` and `master`), and with
the version and `latest` at a release. Each service and front end has exactly one image, built from its multi-stage
`Dockerfile` with the repository root as context.

## Logs

- Locally, the coloured console and `logs/` (rotating, see [Configuration](configuration.md)).
- On a stage, the services' logs are saved in the run's `stage-reports` artifact (`compose-logs.txt`).
- The harness tools log to `~/.local/state/claude-harness/<tool>.log`, never to the console.

Last reviewed: 2026-11-10 (GH-1)
