# Shared front-end packages

This folder holds the TypeScript packages the front ends share: the design tokens, the components and the API client.
Each one lives in its own `frontend/packages/<pkg>/` folder and is added by its own later ticket.

The apps of `frontend/` use only these tokens and components, and reach the back end only through the API client.

See [D438, the repository layout](../../docs/specs/06-decisions/technical/d438-repository-layout.md) and
[the repository layout design page](../../docs/technical/architecture/repository-layout.md).
