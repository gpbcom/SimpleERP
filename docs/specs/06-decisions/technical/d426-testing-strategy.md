🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D426 Testing strategy

# 📜 D426 Testing strategy

**Status:** ✅ decided

## Context

Step 19o of the technical interview, from TC-20.

## Options

- Specs-driven tests with seeded sectors on the real images, or unit and E2E only.
- k6 per release with failure tests in staging, or load tests before major releases.
- Synthetic data, or anonymised copies.

## Choice

Confirmed by the owner on 2026-11-12: specs-driven tests on the real images with seeded sectors; k6 per release and
failure tests in staging; and "Synthetic data, seeded by sector + full coverage 100 %, testing errors and edge cases".

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The tests chapter's target design; TEST-1 to TEST-9 apply.

## Related

- [Testing strategy](../../../technical/delivery/tests-and-traceability.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D425 Plugin SDK and developer tools](d425-plugin-sdk-and-cli.md) · ⬆️ [Up](README.md) ·
➡️ [D427 Integrations hub](../f24-integrations-hub/d427-integrations-hub-coverage.md)
