# Data model

The business data of simple-erp, its models and what stores them.

## Models

None yet. Models are Pydantic classes in `src/models/` (later `services/<service>/src/<service>/models/`), one per
file, each field with a description and a validator that raises its own exception (`AGENT.md`, "Pydantic models").

## Storage

None yet. Storage classes live in `src/storage/` and only read and write data.

Last reviewed: 2026-11-10 (GH-1)
