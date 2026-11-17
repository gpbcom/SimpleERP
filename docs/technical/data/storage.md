# Storage

Where simple-ERP keeps its data: the database choice (SQL or NoSQL), the databases' configuration and security, and file
and object storage. The data model itself is in [Data model](data-model.md). Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Databases (D409).** PostgreSQL for every company database (one per company, D19): transactions, JSONB for custom
fields, row-level security as a second guard, logical replication for the event outbox and read models; self-hosted, or
a managed PostgreSQL of a European cloud in the hosted edition.

**Custom data (TC-03).** Custom fields stored in a JSONB column per record, defined and validated by typed field
definitions, with indexes generated for the fields users filter on; new custom record types as tables created by the
configuration service through migrations.

**Files (TC-16).** S3-compatible object storage, one bucket per company with lifecycle rules per kind of file
(recordings, media, documents, legal archive), encrypted per company; self-hosted with an S3-compatible server (for
example Garage or MinIO), or a European cloud's object storage in the hosted edition; health data on a certified profile
only.

**Vectors (T8).** Milvus standalone on every profile, the laptop included (the owner's choice); a collection per company
and one shared, read-only collection for the law.

**Encryption.** Encrypted disks and backups everywhere; per-company keys in the vault (D240) for object storage and
backups; field-level encryption for the most sensitive fields (bank details, health data, credentials); TLS between
every service.

Decided in [D409](../../specs/06-decisions/technical/d409-storage-choices.md).

Last reviewed: 2026-11-12 (GH-2)
