🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-39 Prospects are kept only as long as the sequence needs them

# 📏 BR-F9-39 Prospects are kept only as long as the sequence needs them

**Status:** ✅ specified

## Statement

A prospect who becomes an applicant follows the 2-year term of [BR-F9-11](br-f09-11-candidate-data-has-a-term.md);
a prospect who refuses or never answers is erased at the end of the sequence, and one never shortlisted when
the search closes, 30 days after its last run at the latest; of a person who refused, only the LinkedIn
profile ID stays, on a do-not-contact list, so that they are never contacted again.

## Why

Personal data is kept no longer than its purpose needs
([CR-FR-052](../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md),
[CR-FR-195](../../../10-country-packs/france/data-protection/cr-fr-195-candidate-data.md)); the owner asked for the
2-year term of [BR-F9-11](br-f09-11-candidate-data-has-a-term.md) to apply
([D518](../../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)).

## Examples

| Case | Result |
|---|---|
| Sonia M. became an applicant | kept 2 years after the last contact (BR-F9-11) |
| Karim D. declined on day 4, the sequence ends on day 60 | erased on day 60; his profile ID stays on the do-not-contact list |
| Marc T. never shortlisted, the search closed | erased at the closing |
| A person asks to be erased on day 5 | erased at once (BR-F9-11) |

## Applies to

- [UC-F9-40 Search and rank LinkedIn profiles](../use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md)
- [UC-F9-41 Run a LinkedIn outreach sequence](../use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
- [E-F9-44 Sourcing search](../data/e-f09-44-sourcing-search.md)
- [E-F9-45 Prospect](../data/e-f09-45-prospect.md)
- [E-F9-47 Outreach message](../data/e-f09-47-outreach-message.md)

## Exceptions

None.

## Configurable

The 30 days, shorter only.

## Open questions

None.

---

⬅️ [BR-F9-38](br-f09-38-sourced-people-told-at-the-first-contact.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-40 No search criterion the law forbids in hiring](br-f09-40-no-criterion-the-law-forbids-in-hiring.md)
