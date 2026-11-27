# Plugin SDK and developer experience

How third parties build, test, sign and publish plugins (T4, F14). Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**SDK (D425).** A plugin SDK in Python for back-end logic and in TypeScript for custom widgets; a CLI that scaffolds,
tests, packages and signs a plugin; a local sandbox with a seeded company (Docker Compose); the same automated checks as
the store (F14); documentation generated from the API. Plugins reach the ERP only through the public API with their
declared permissions, in the sandbox of D405. The feature factory (F19) builds its plugins with the same SDK.

Decided in [D425](../../specs/06-decisions/technical/d425-plugin-sdk-and-cli.md).

Last reviewed: 2026-11-12 (GH-2)
