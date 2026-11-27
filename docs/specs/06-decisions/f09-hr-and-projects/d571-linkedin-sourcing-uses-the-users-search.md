🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D571 LinkedIn sourcing uses the HR user's own search

# 📜 D571 LinkedIn sourcing uses the HR user's own search

**Status:** ✅ decided

## Context

The owner asked for a rich set of search criteria ([D518](d518-linkedin-sourcing-through-unipile.md)), and LinkedIn
offers different criteria to a classic account, Sales Navigator and Recruiter.
[Q19](../../07-questions/q19-which-linkedin-search-sourcing-uses.md) asked which search a sourcing search runs on.

## Options

- The search the HR user's account offers, as Unipile reports it, the AI assistant applying the criteria it lacks.
- The classic search only, the same for every company.
- Recruiter or Sales Navigator required for LinkedIn sourcing.

## Choice

By default a sourcing search runs on **the search the HR user's own LinkedIn account offers**, as Unipile reports it;
the criteria that search lacks are applied by the AI assistant to the profiles returned, and the screen says which
criteria LinkedIn applied and which the assistant applied. **Recruiter or Sales Navigator is an option**: when the
linked account has one, its search and its extra criteria are used.

## Decided by

The owner, on 2026-11-27.

## Consequences

- [UC-F9-40](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md),
  [E-F9-44 Sourcing search](../../02-functional/f09-hr-and-projects/data/e-f09-44-sourcing-search.md),
  [S-F9-37 LinkedIn sourcing search](../../02-functional/f09-hr-and-projects/screens/02-recruit/s-f09-37-linkedin-sourcing-search.md)
  and the Unipile [tool connection](../../02-functional/f24-integrations-hub/data/e-f24-02-tool-connection.md) say so.
- A criterion applied by the AI assistant stays a job-related criterion under human oversight
  ([BR-F9-40](../../02-functional/f09-hr-and-projects/business-rules/br-f09-40-no-criterion-the-law-forbids-in-hiring.md),
  [BR-F4-21](../../02-functional/f04-meetings/business-rules/br-f04-21-candidate-scoring-is-high-risk-ai.md)).

## Related

- [D518 LinkedIn sourcing through Unipile](d518-linkedin-sourcing-through-unipile.md)
- [D570 LinkedIn messages are prepared by default, sent with one click](d570-linkedin-sending-prepared-by-default.md)
- [Q19 Which LinkedIn search sourcing uses](../../07-questions/q19-which-linkedin-search-sourcing-uses.md)

---

⬅️ [D570](d570-linkedin-sending-prepared-by-default.md) · ⬆️ [Up](README.md) ·
➡️ [D572](../foundations/d572-proposals-confirmed-in-bulk.md)
