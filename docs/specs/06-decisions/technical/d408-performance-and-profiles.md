🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D408 Performance targets and resource profiles

# 📜 D408 Performance targets and resource profiles

**Status:** ✅ decided

## Context

Step 19b of the technical interview, from TC-09 and TC-15. The owner: "I want to be able to run it well in my machine.
But it must also work on the Cloud with more resources."

## Options

- Targets: API, lists, reports and assistant, or the screen target only.
- Laptop budget: 8 GB with small local AI, 6 GB with AI outside, or the whole machine.
- Reporting: read models with an optional columnar store, always columnar, or the main database.
- A shared cache or none.

## Choice

Confirmed by the owner on 2026-11-12: the targets below; a laptop profile within 8 GB of RAM measured on the owner's
machine (6 cores, 12 threads, about 15 GB, integrated graphics only) with small local AI; cloud profiles on the same
images; read models with an optional columnar store; a shared cache keyed per company.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The performance chapter's target design.

Clarified on 2026-11-12 after the review (R15, R16, R25, the owner's yes): these targets replace the use cases' earlier
proposals; the 8 GB laptop budget is proved by a measured prototype before it is promised; Milvus is optional with the
AI turned off; the analytics store keeps companies apart and is reached by erasure (REQ-T01-08).

## Related

- [Performance targets and resource profiles](../../../technical/infrastructure/performance-and-capacity.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D407 Front end](d407-front-end.md) · ⬆️ [Up](README.md) · ➡️ [D409 Storage choices](d409-storage-choices.md)
