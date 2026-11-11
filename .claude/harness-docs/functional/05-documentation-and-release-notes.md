# 5. Documentation and release notes

At the end of every ticket, before its pull request, Claude writes what users and developers will read later.

| What | Rule | Skill | Versioned |
|---|---|---|---|
| `README.md`, `docs/functional/`, `docs/technical/` | DOC-2 | project-docs | Yes |
| `changelog.d/GH-<n>.<type>.md` | DOC-3 | release-notes | Yes |
| `RELEASE-NOTE.md`, then a comment on the issue | DOC-3 | release-notes | Archived with the ticket |
| `EXPLAIN.md` | DOC-1 | ticket-docs | Archived with the ticket |

- **project-docs** maps the branch's changed files to the chapters concerned (`conf/doc-map.yaml`), updates them, and
  stamps them `Last reviewed: <date> (GH-<n>)`. A chapter left unchanged is justified in PROGRESS.md.
- **release-notes** writes the user-facing note and a one-to-three-line changelog fragment, typed added, changed,
  deprecated, removed, fixed or security. CI refuses a feature or bugfix pull request without its fragment.
- **At a release,** the fragments become a `CHANGELOG.md` section, and the GitHub Release gathers the issues' notes.

In `docs/`, only `specs/`, `functional/` and `technical/` are versioned.
