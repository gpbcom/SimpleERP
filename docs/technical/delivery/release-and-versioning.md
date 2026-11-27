# Release and versioning

Semantic versions, long-term support, upgrade paths. Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Versions (D423).** Semantic versions for the product; one minor release a month; one long-term-support version a year,
supported 24 months. Country packs, sector packs and plugins are versioned apart, each declaring the product versions it
works with; a country pack can ship between releases (D294).

**Upgrade paths.** Upgrades are allowed from any version of the last 12 months; database migrations stay
backward-compatible for one release (expand, then contract), so that services can roll one at a time; the changelog and
release notes are written by `release.yml` (TKT-26).

Decided in [D423](../../specs/06-decisions/technical/d423-release-train-and-lts.md).

Last reviewed: 2026-11-12 (GH-2)
