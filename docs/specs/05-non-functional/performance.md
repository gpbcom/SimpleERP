🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › ⚡ Performance

# ⚡ Performance

**Status:** ✅ specified

## Requirement

95 % of screens answer within 1 second, for 250 users working at once on one company
([D25](../06-decisions/foundations/d25-first-version-targets.md), see [Scalability](scalability.md)).

The targets of [D408](../06-decisions/technical/d408-performance-and-profiles.md), which every use case follows:

- 95 % of screens within 1 second for 250 users at once on one company.
- API calls: 95 % within 300 ms.
- Lists of any size paged on the server, the first page within 1 second.
- Reports within 5 seconds, or moved to the background with progress.
- The AI assistant's first words within 3 seconds with a local model on the reference profile.

## Measures

k6 load tests per release against these targets on the three reference sizes, the laptop profile included, on seeded
data (D426).

## Open questions

⬜ To be specified.

---

⬆️ [Up](README.md) · ➡️ [Scalability](scalability.md)
