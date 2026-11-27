🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-38 A sourced person is told at the first contact at the latest

# 📏 BR-F9-38 A sourced person is told at the first contact at the latest

**Status:** ✅ specified

## Statement

A person whose data comes from their LinkedIn profile is told, in the first message at the latest, who processes their
data and why, where it was found, that an AI assistant helped rank the profiles and HR chose, how long it is kept and
their rights, with a link to the company's privacy notice for candidates.

## Why

GDPR, [Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj), article 14 applies to data not obtained
from the person; when the data is used to communicate with them, they are told at the latest at the first communication
(article 14(3)(b)). Candidates are told of any automated sorting
([CR-FR-195](../../../10-country-packs/france/data-protection/cr-fr-195-candidate-data.md)). The owner's request:
[D518](../../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md).

## Examples

| Case | Result |
|---|---|
| Invitation note with a sentence and the notice link | passes |
| Invitation note without the notice link | fails: the sequence cannot be approved |
| The notice says profiles are ranked with an AI assistant and HR chooses | passes |

## Applies to

- [UC-F9-41 Run a LinkedIn outreach sequence](../use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
- [UC-F9-42 Turn a positive reply into an applicant](../use-cases/02-recruit/uc-f09-42-turn-a-positive-reply-into-an-applicant.md)
- [E-F9-46 Outreach sequence](../data/e-f09-46-outreach-sequence.md)

## Exceptions

None.

## Configurable

The wording; the link is required.

## Open questions

None.

---

⬅️ [BR-F9-37](br-f09-37-outreach-stops-at-a-reply-a-refusal-or-day-60.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-39](br-f09-39-prospects-kept-only-as-long-as-needed.md)
