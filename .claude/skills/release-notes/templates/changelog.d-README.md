# Changelog fragments

One file per ticket, written at hand-over by the `release-notes` skill (rule DOC-3): `GH-<n>.<type>.md`, where
`<type>` is `added`, `changed`, `deprecated`, `removed`, `fixed` or `security`.

- One to three lines, in the changelog's voice: what changed for users, not how.
- A breaking change starts with `**Breaking:**`.
- `release-notes build <x.y.z>` moves the fragments into `CHANGELOG.md` and deletes them, on the release branch.
