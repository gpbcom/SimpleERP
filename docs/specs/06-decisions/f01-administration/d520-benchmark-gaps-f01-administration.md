🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D520 Benchmark gaps of F1 Administration

# 📜 D520 Benchmark gaps of F1 Administration

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with administration, identity and group features of
the benchmarked suites and offered each gap as an option
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F1 Administration").

## Options

- Take each gap as a use case of F1 in a new flow, or leave it out.
- Where a gap overlaps an existing use case, extend that use case or add a new one.

## Choice

The owner selected all four gaps; each becomes a use case of F1, drawn in
[FL-F1-15 Security and group data](../../02-functional/f01-administration/flows/fl-f01-15-security-and-group-data.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G27 | [UC-F1-24 Manage sessions and trusted devices](../../02-functional/f01-administration/use-cases/15-security-and-group-data/uc-f01-24-manage-sessions-and-trusted-devices.md) | "Sessions and devices" |
| G28 | [UC-F1-25 Set retention and purge personal data](../../02-functional/f01-administration/use-cases/15-security-and-group-data/uc-f01-25-set-retention-and-purge-personal-data.md) | "Retention and purge" |
| G29 | [UC-F1-26 Share master data across the group](../../02-functional/f01-administration/use-cases/15-security-and-group-data/uc-f01-26-share-master-data-across-the-group.md) | "Shared group data" |
| G30 | [UC-F1-27 Act as a user with consent](../../02-functional/f01-administration/use-cases/15-security-and-group-data/uc-f01-27-act-as-a-user-with-consent.md) | "Act as a user" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "Block by block").

## Consequences

- Use cases
  [UC-F1-24 Manage sessions and trusted devices](../../02-functional/f01-administration/use-cases/15-security-and-group-data/uc-f01-24-manage-sessions-and-trusted-devices.md)
  to
  [UC-F1-27 Act as a user with consent](../../02-functional/f01-administration/use-cases/15-security-and-group-data/uc-f01-27-act-as-a-user-with-consent.md),
  screens
  [S-F1-27 Sessions and devices](../../02-functional/f01-administration/screens/15-security-and-group-data/s-f01-27-sessions-and-devices.md)
  to
  [S-F1-30 Act as a user](../../02-functional/f01-administration/screens/15-security-and-group-data/s-f01-30-act-as-user.md),
  rules
  [BR-F1-33 Sessions end on role change or revocation](../../02-functional/f01-administration/business-rules/br-f01-33-sessions-end-on-role-change-or-revocation.md)
  to
  [BR-F1-36 Acting as a user needs consent and is audited](../../02-functional/f01-administration/business-rules/br-f01-36-acting-as-a-user-needs-consent-and-is-audited.md),
  entities [E-F1-23 User session](../../02-functional/f01-administration/data/e-f01-23-user-session.md) to
  [E-F1-26 Act-as session](../../02-functional/f01-administration/data/e-f01-26-act-as-session.md) and their lists
  [S-F1-L23 User sessions](../../02-functional/f01-administration/screens/00-lists/s-f01-l23-user-sessions.md) to
  [S-F1-L26 Act-as sessions](../../02-functional/f01-administration/screens/00-lists/s-f01-l26-act-as-sessions.md).
- Retention minimums come from the country pack, never from this decision.
- Impersonation and group data sharing each need a France pack rule, written later.

## Related

- [FL-F1-15 Security and group data](../../02-functional/f01-administration/flows/fl-f01-15-security-and-group-data.md)
- [D458 F1 Administration: gaps and improvements](d458-f01-gaps-and-improvements.md)
- [Interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)

---

⬅️ [D519 View cards reviewed: list pages and workspaces](../ux/d519-view-cards-reviewed-list-pages-and-workspaces.md) ·
⬆️ [Up](README.md) · ➡️ [D521](../f02-no-code-configuration/d521-benchmark-gaps-f02-no-code-configuration.md)
