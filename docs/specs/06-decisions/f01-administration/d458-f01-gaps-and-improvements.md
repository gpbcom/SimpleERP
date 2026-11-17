🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D458 F1 Administration: gaps and improvements

# 📜 D458 F1 Administration: gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F1 and the sectors that rely on it.

## Options

- **Approval delegation during absences.** No deputy or out-of-office hand-over of approval rights anywhere in the
  specs; managers approve leave, purchases and expenses in every sector. Serves U02, U13, all sectors.
- **Automatic provisioning (SCIM) and bulk invites.** SSO creates accounts on first login (D55), but nothing removes
  them from the identity provider's side, and bulk import is out of scope. Seasonal and shift staff come in batches
  (SC13, SC16, SC08). Noota sells SSO with provisioning (B02). Serves U07, U11.
- **Company exit and full export.** No use case to close a company or export all its data when it leaves the hosted
  edition. The EU Data Act switching duty is cited only in SC14 and F24. Serves U13, U11.
- **External (portal) account management.** F1 manages internal users only. There is no use case to invite, block, reset
  or audit customers, suppliers, families, tenants or learners. Serves SC04, SC10, SC12, SC14.
- **Security policies screen.** No password rules, session length, 2FA required per role, or IP and device limits
  (absent). Serves U07, SC09, SC11.
- **API tokens and service accounts.** No use case to create, scope and revoke integration users and tokens; only T12
  mentions keys. Serves SC14, SC15 (EDI), U07.
- **Audit-trail search and SIEM export.** Add a filterable audit screen. Competitors score ✅ on B04 (ERPClaw has a
  checksum chain, Nebesta exports to a SIEM).
- **Periodic access review campaign.** "Access review" is only a report. Make it a use case where managers certify their
  team's rights each quarter (ISO 27001 controls, A12).
- **Site-scoped administration.** Store or hotel managers manage their own site's users only. Serves SC02, SC06.
- **More manager use cases.** U02 has 1 use case; add team accounts and pending requests.
- **Screen states.** Add the missing states: 6 of 12 screens have no empty state, 11 no loading state, 7 no read-only
  state.

## Choice

Confirmed by the owner on 2026-11-12:

- F1 Administration: gaps: All six: delegation and portal users; SCIM and bulk invites; company exit and export;
  security policies and API tokens
- F1 Administration: improvements: All four: audit search and SIEM; access review campaign; site-scoped admin; manager
  use cases
- F1 Administration: proposals: "Confirm all of F1"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F1.
- F1's waiting proposals are confirmed (D457).

## Related

- [F1 Administration](../../02-functional/f01-administration/README.md)

---

⬅️ [D457 Gaps and improvements round: what applies to every block](../sectors/d457-gaps-and-improvements-round.md) ·
⬆️ [Up](README.md) · ➡️ [D459](../f02-no-code-configuration/d459-f02-gaps-and-improvements.md)
