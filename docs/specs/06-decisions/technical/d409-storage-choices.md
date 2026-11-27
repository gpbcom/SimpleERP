🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D409 Storage choices

# 📜 D409 Storage choices

**Status:** ✅ decided

## Context

Step 19c of the technical interview, from TC-01, TC-03, TC-05, TC-08 and TC-16.

## Options

- PostgreSQL, PostgreSQL with MongoDB, or MongoDB.
- Custom fields as JSONB, real columns or rows per value.
- S3-compatible object storage or files on disk.
- Milvus Lite, standalone or pgvector on the laptop.
- Encryption: disks, per-company keys and sensitive fields, or disks only.

## Choice

Confirmed by the owner on 2026-11-12: PostgreSQL for every company database; custom fields as JSONB with typed
definitions; S3-compatible object storage, a bucket per company; Milvus standalone everywhere; encrypted disks,
per-company keys and field-level encryption of the most sensitive fields.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The storage chapter's target design; [data model](../../../technical/data/data-model.md) follows it.

Clarified on 2026-11-12 after the review (R16, the owner's yes): Milvus is optional with the AI turned off (D22).

## Related

- [Storage choices](../../../technical/data/storage.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D408 Performance targets and resource profiles](d408-performance-and-profiles.md) · ⬆️ [Up](README.md) ·
➡️ [D410 API style and authentication](d410-api-style-and-auth.md)
