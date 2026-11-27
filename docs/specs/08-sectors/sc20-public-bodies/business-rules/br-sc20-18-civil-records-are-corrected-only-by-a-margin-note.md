🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-18 Civil records are corrected only by a margin note

# 📏 BR-SC20-18 Civil records are corrected only by a margin note

**Status:** ✅ specified

## Statement

A civil act is never changed after its signature: it is corrected only by a margin note with its legal basis, a
rectification ordered by the president of the tribunal or, for a purely material error, made by the civil-status officer
or on the prosecutor's order. Extracts are issued only to those entitled and every extract and access is logged.

## Why

The register is the legal proof of people's status; an altered act has no value
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). The France-pack rule is
[CR-FR-260 Civil registry records](../../../10-country-packs/france/company/cr-fr-260-civil-registry.md): a later event
is added as a margin note within 3 days (Code civil 49); a rectification is ordered by the president of the tribunal, or
made by the civil-status officer or on the prosecutor's order for a purely material error (99, 99-1); it binds everyone
once published on the registers, and a copy is issued only with it (100, 101). Full copies of birth and marriage
acts go only to the person, close family, the legal representative, a mandated person, the prosecutor, the officer, the
notary and the authorised administrations; death acts to anyone; the others need the prosecutor's leave (décret
n° 2017-890, art. 30). A registry kept by automated processing meets the security and integrity characteristics set by
decree, which also exempts it from the second copy (40); no certification of the software is required.

## Examples

| Case | Result |
|---|---|
| Birth act signed | registered, read-only |
| Correction ordered by a court | margin note with the decision |
| Misspelt first name, a material error | corrected by the officer, margin note with the decision |
| Edit of a registered act | refused, margin note offered |
| Citizen asks for their own extract | issued and logged |
| Stranger asks for a full copy | refused |

## Applies to

- [UC-SC20-18](../use-cases/05-council-registry-permits-and-assets/uc-sc20-18-keep-the-civil-registry.md)
- [E-SC20-13 Civil record](../data/e-sc20-13-civil-record.md)
- France-pack rule:
  [CR-FR-260 Civil registry records](../../../10-country-packs/france/company/cr-fr-260-civil-registry.md)

## Exceptions

None.

## Configurable

The kinds of act and who may receive which copy, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC20-17](br-sc20-17-deliberations-are-sent-to-the-prefecture-to-become-enforceable.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC20-19](br-sc20-19-silence-after-the-legal-delay-counts-as-the-law-says.md)
