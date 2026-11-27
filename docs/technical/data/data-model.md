# Data model

The business data of SimpleERP, its models and what stores them.

## Models

None yet. Models are Pydantic classes in `src/models/` (later `services/<service>/src/<service>/models/`), one per
file, each field with a description and a validator that raises its own exception (`AGENT.md`, "Pydantic models").

## Storage

None yet. Storage classes live in `src/storage/` and only read and write data.

## Target design (specified in GH-2, not built yet)

**Where the data lives (D409).** Each company has its own PostgreSQL database (D19); every business domain service owns
its tables in it, in its own schema, and no service reads another service's tables: it calls that service's API or
listens to its events.

**Entities.** The entities specified per capability (the `data/` pages of `docs/specs/02-functional/`) map to tables of
their domain service. Every record carries its id, its company (also guarded by row-level security), its creation and
change times and authors (for the audit trail, T3), and a JSONB column for custom fields defined by typed field
definitions (TC-03).

**Legal records (TC-05).** Posted entries, invoices and till data are append-only and hash-chained per company (and per
till); personal data that may need erasure is kept in separate tables referenced by id, so that erasing it leaves the
books whole.

**Other stores.** Files in the company's object-storage bucket, vectors in its Milvus collection, read models and time
series in the reporting store, events in the bus; each is rebuilt from the company's database and events when needed
([Storage](storage.md)).

Decided in [D409](../../specs/06-decisions/technical/d409-storage-choices.md).

Last reviewed: 2026-11-12 (GH-2)
