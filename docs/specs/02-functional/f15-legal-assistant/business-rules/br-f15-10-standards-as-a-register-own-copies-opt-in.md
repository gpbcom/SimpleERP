🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-10 Standards as a register, own copies opt-in

# 📏 BR-F15-10 Standards as a register, own copies opt-in

**Status:** ✅ specified

## Statement

For a copyrighted standard (AFNOR, ISO, CEN, other national bodies), the shared corpus holds only a register entry:
reference, title, edition and status, the legal texts that make it mandatory or cite it, the sectors it concerns, where
to obtain it, and a note in SimpleERP's own words; never its text. The AI assistant answers "what applies and where to
get it" and points to clauses without quoting them. A company may upload its own copies into its private corpus only
after attesting, per document, an AI-use licence from the rights holder; without it, only the reference and clause
titles are indexed.

Standards are never fetched by the unattended pulls of D205
([D448](../../../06-decisions/f15-legal-assistant/d448-law-texts-and-signed-rule-packs.md)).

## Why

Rights holders forbid AI use of standards without a licence. See
[D207](../../../06-decisions/f15-legal-assistant/d207-copyrighted-standards-register.md).

Legal values from the France country pack:
[CR-FR-060 Copyrighted standards and text mining](../../../10-country-packs/france/ai-and-recording/cr-fr-060-text-and-data-mining-opt-out.md).

## Examples

| Case | Result |
|---|---|
| "Which standard for timber frames?" | "NF DTU 31.2, required in practice by insurers; get it from AFNOR, CSTB Reef, or free through Qualibat's member area for holders" |
| A company uploads NF C 15-100 with its AI-use licence attested | Indexed in its own corpus only |
| The same without an attestation | Reference and clause titles only |

## Applies to

- [UC-F15-01](../use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)
- [UC-F15-06](../use-cases/04-set-up-the-legal-assistant/uc-f15-06-keep-the-standards-register.md)

## Exceptions

Standards made free by their owners for reuse, such as EN 16931-1 and -2 (e-invoicing): indexed in full.

## Configurable

The opt-in for companies' own copies, by an administrator.

## Open questions

None.

---

⬅️ [BR-F15-09 Law packs pull official sources on their own](br-f15-09-law-packs-pull-official-sources-on-their-own.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F15-11 Every dated duty has an owner and reminders](br-f15-11-every-dated-duty-has-an-owner-and-reminders.md)
