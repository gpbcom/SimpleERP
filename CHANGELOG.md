# Changelog

Every notable change of SimpleERP. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
the versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

A release adds its own section here, started with `/release`: the release workflow writes it on `release/<version>`
from the pull requests merged since the last release. Never edit a released section.

## [Unreleased]

### Added

- The specifications v1 in [docs/specs/](docs/specs/README.md): vision, users, the functional capabilities F1 to F25,
  the technical capabilities T1 to T13, UX, non-functional requirements, decisions, sectors, country packs and the
  roadmap.
- The Claude Code harness in [.claude/](.claude/): the roadmap tickets planned and run by an agent team under the TKT
  rules, with a person's approval of each plan and code review before each push, the board, GitFlow hooks and
  releases.
