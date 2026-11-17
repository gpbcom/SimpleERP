🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 👥 [HR and projects](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Employee (U01, U14) | Manager (U02) | HR (U06) | Office (U16) | Customer (U09) | Administrator (U07) |
|---|---|---|---|---|---|---|
| Own data, documents, requests | ✅ (key data validated) | ✅ own | ✅ all | ✅ own | - | - |
| Team's work data | - | ✅ | ✅ | - | - | - |
| Private HR data | own | - | ✅ | - | - | - |
| Contracts and templates | - | - | ✅ | - | - | - |
| Recruitment | refer | interview, decide | ✅ | - | - | - |
| LinkedIn sourcing and outreach (D518) | - | (Proposed) reads the shortlist of their job | ✅ | - | - | connects Unipile, sets the caps |
| Time off, overtime, timesheets | request, log | approve, validate | ✅ | - | - | - |
| Appraisals | self | ✅ team | ✅ | - | - | - |
| Shifts | see, swap | ✅ plan | ✅ | - | - | - |
| Projects | tasks assigned | ✅ | - | - | shared parts | - |
| Fleet, lunch, visitors | request, order | approve | ✅ fleet | ✅ visitors | - | settings |

## Record rules

- Private HR data only to HR and the person (BR-F9-02).
- Activity drafts only to their employee (BR-F9-07); positions shown to the employee (BR-F9-06).
- Customers see only the project parts shared with them.
- LinkedIn prospects and their messages only to the HR user who owns the search, and HR; the administrator sees the
  counts of the caps, never a profile or a message
  ([UC-F9-41](use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
