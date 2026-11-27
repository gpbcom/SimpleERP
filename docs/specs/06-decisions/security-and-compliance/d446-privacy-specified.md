🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: Security and compliance](README.md) ›
📜 D446 Privacy and retention specified

# 📜 D446 Privacy and retention specified

**Status:** ✅ decided

## Context

R8: privacy and GDPR unspecified (privacy-gdpr.md all ⬜), 277 entities pointing to country rules that do not exist for
their kinds, no subprocessor list, no data processing agreement, no impact assessment.

## Options

- Specify privacy now, defaults (Proposed).
- Leave it to the build.

## Choice

Privacy is specified now: the roles (the company is the controller; the publisher in the hosted edition and an IT
provider for its client companies are processors under a data processing agreement; the project is neither for a
self-hosted install), the hosted edition's subprocessors, transfers, impact assessments for meetings, call scoring,
candidate and worker evaluation and health data, and a retention schedule per kind of entity. Defaults the owner has not
set are (Proposed).

## Decided by

The owner, on 2026-11-12 at 14:55, round 2 of the decisions on the independent review (R8, PROGRESS.md, step 21).

## Consequences

Privacy and GDPR and Data retention are written; every entity's retention points to the schedule; D293 is revised for
entities whose kind has no rule in the pack.

## Related

- [Security](../../05-non-functional/security.md)
- [Privacy and GDPR](../../05-non-functional/privacy-gdpr.md)
- [Data retention](../../05-non-functional/data-retention.md)
- [D293](../country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)
- [Independent review of 2026-11-12](../../../tickets/GH-2/review/2026-11-12-review.md)

---

⬅️ [D445 Electronic payslips available 50 years from issue](../f13-payroll/d445-payslips-fifty-years-from-issue.md) ·
⬆️ [Up](README.md) · ➡️ [D447](../vision/d447-country-pack-updates-free-hosted-only-named.md)
