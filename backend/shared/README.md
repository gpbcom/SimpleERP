# backend/shared

The libraries the services share, with no business rules: lifecycle, logging, configuration, company context and
rights, event outbox, metering client, country-pack rules and test helpers. Each library is one uv package in
`backend/shared/<lib>/`, added by its own later ticket. A service never imports another service, so the code they share
goes here.

See [D438, the repository layout](../../docs/specs/06-decisions/technical/d438-repository-layout.md) and the
[repository layout](../../docs/technical/architecture/repository-layout.md).
