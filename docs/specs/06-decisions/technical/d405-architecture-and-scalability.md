🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D405 Architecture and scalability

# 📜 D405 Architecture and scalability

**Status:** ✅ decided

## Context

Step 19a of the technical interview, from the technical challenges TC-01, TC-02, TC-04, TC-06, TC-11, TC-14, TC-21 and
TC-22.

## Options

- Services by business domain, about 12; one per capability; or a few large ones.
- Tenancy: shared services and a database per company; a namespace or a cluster per customer.
- HTTP and events; events only; HTTP only.

## Choice

Confirmed by the owner on 2026-11-12: about 12 back-end services by business domain; shared services per cluster with a
database, bucket and vector collection per company; HTTP for reads and commands and an event bus with an outbox for what
happened; plugins sandboxed by trust level; three reference sizes; offline-first apps; country packs as signed data read
by one rules library; a durable workflow engine for long runs; one metering gateway.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The architecture chapter's target design.

## Related

- [Architecture and scalability](../../../technical/architecture/architecture.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D404 F23 use cases](../f23-what-if-simulation/d404-f23-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D406 Back end](d406-back-end.md)
