🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-20 One side is the master per period

# 📏 BR-F24-20 One side is the master per period

**Status:** 🔄 waiting for the owner

## Statement

For each period exactly one side is the master: only the master changes that period's entries, and a change made on the
other side is held for review and applied, if at all, as a new entry on the master side; the master of a period changes
only by a decision of accounting and the accountant together.

## Why

Two sides editing the same books produce two versions of the truth. The owner asked for accounting firm tools
([D543](../../../06-decisions/f24-integrations-hub/d543-benchmark-gaps-f24-integrations-hub.md)); two-way sync with an
owner per record is already the rule ([BR-F24-07](br-f24-07-two-way-sync-with-ownership.md)) and the accounting is
inalterable ([CR-FR-003](../../../10-country-packs/france/accounting/cr-fr-003-posted-entries-are-inalterable.md)).

## Examples

| Case | Result |
|---|---|
| October mastered by SimpleERP, a firm change to October | held for review |
| The firm takes over the year-end | the master of the closed months moves to the firm by a joint decision |
| A held change accepted | a new entry on the master side, naming the reviewer |
| A period with no master set | the sync does not write to it |
| A master moved by accounting alone | refused: the accountant must agree too |

## Applies to

- [UC-F24-31](../use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-31-sync-with-the-accountants-software.md)
- [E-F24-19 Firm sync](../data/e-f24-19-firm-sync.md)
- [BR-F24-07 Two-way sync with an owner per field](br-f24-07-two-way-sync-with-ownership.md)
- [E-F8-10 Fiscal period](../../f08-accounting/data/e-f08-10-fiscal-period.md)

## Exceptions

None.

## Configurable

The master of each period, by accounting and the accountant together.

## Open questions

None.

---

⬅️ [BR-F24-19 Exports follow field rights and masking](br-f24-19-exports-follow-field-rights-and-masking.md) ·
⬆️ [Up](README.md)
