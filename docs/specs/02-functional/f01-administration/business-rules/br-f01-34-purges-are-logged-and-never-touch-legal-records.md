🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-34 Purges are logged and never touch legal records

# 📏 BR-F1-34 Purges are logged and never touch legal records

**Status:** ✅ specified

## Statement

Every purge run writes a log line with its counts, and a record the law requires the company to keep is never purged
before its legal period ends: the policy cannot set a period under the legal minimum, and the run lists such records as
kept with the reason.

## Why

The company must keep some records and must not keep others longer than needed: both duties need proof. The owner's
answer: "Retention and purge"
([D520](../../../06-decisions/f01-administration/d520-benchmark-gaps-f01-administration.md)).

## Examples

| Case | Result |
|---|---|
| Invoices, legal minimum 10 years, policy 5 years | refused: the minimum is 10 years |
| A customer with an invoice inside its legal period | kept, or anonymised where the law allows, listed as kept |
| A run that purged 412 records | one log line: policy, 412 purged, 38 kept with reasons, run time |
| The purge log | holds counts and reasons, never the purged content |

## Applies to

- [UC-F1-25 Set retention and purge personal data](../use-cases/15-security-and-group-data/uc-f01-25-set-retention-and-purge-personal-data.md)
- [E-F1-24 Retention policy](../data/e-f01-24-retention-policy.md)
- [UC-F1-23 Close a company and export all its data](../use-cases/14-close-a-company/uc-f01-23-close-a-company-and-export-all-its-data.md)

## Exceptions

A record under a legal hold set by a court or an authority is kept until the hold is lifted, whatever its period.

## Configurable

The periods above the legal minimum are set by the administrator.

## Open questions

None.

---

⬅️ [BR-F1-33 Sessions end on role change or revocation](br-f01-33-sessions-end-on-role-change-or-revocation.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F1-35 Shared records keep one owner company](br-f01-35-shared-records-keep-one-owner-company.md)
