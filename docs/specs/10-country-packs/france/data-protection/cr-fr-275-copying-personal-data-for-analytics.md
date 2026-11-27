🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🔒 [Data protection](README.md) › ⚖️ CR-FR-275 Copying personal data for analytics

# ⚖️ CR-FR-275 Copying personal data for analytics

**Status:** ✅ specified

## Statement

Personal data copied to an analytics warehouse are processed for a purpose of their own: that purpose must not be
incompatible with the purpose of collection, the data are limited to what it needs and kept identifiable no longer than
it needs, and kept secure ([GDPR, art. 5(1)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679),
read 2026-11-27); without consent or a law, the controller checks compatibility against the link between the purposes,
the context, the nature of the data, the consequences and the safeguards, such as encryption or pseudonymisation
([GDPR, art. 6(4)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679), read 2026-11-27);
statistical use is not incompatible when it has the safeguards of art. 89(1), and is done without identifying people
where it can ([GDPR, art. 5(1)(b) and 89(1)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679),
read 2026-11-27). People are told of the new purpose before it starts
([GDPR, art. 13(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679), read 2026-11-27). The
export is a processing in the record ([CR-FR-048](cr-fr-048-record-of-processing.md)), designed for privacy
([CR-FR-050](cr-fr-050-privacy-by-design.md)), and a destination outside the EU follows
[CR-FR-274](cr-fr-274-transfers-to-cloud-suites.md).

## Values

- Principles (art. 5(1)): purpose limitation (b), data minimisation (c), storage limitation (e), integrity and
  confidentiality (f); the controller can show it complies (art. 5(2)).
- Compatibility test (art. 6(4), kept as data): (a) link between the purposes; (b) context of collection and the
  relationship with the people; (c) nature of the data, special categories and offences in particular; (d) possible
  consequences; (e) safeguards such as encryption or pseudonymisation.
- Statistics (art. 89(1)): technical and organisational measures for data minimisation, pseudonymisation where it
  serves, and data that no longer identify people wherever the purpose allows.
- Information (art. 13(3)): before the further processing, the new purpose and the information of art. 13(2).
- A copy in the warehouse does not replace the books the company must keep
  ([CR-FR-002](../accounting/cr-fr-002-accounting-records-kept-ten-years.md)).
- SimpleERP enforces: each export names its purpose, takes only the fields that purpose needs, pseudonymises personal
  fields by default and is added to the record of processing.

## Legal references

- [Regulation (EU) 2016/679 (GDPR), art. 5, 6(4), 13(3) and 89(1)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679),
  read 2026-11-27.

## Effective dates

Since 2018-05-25.

## Enforced by

- [UC-F24-30 Export data to a warehouse](../../../02-functional/f24-integrations-hub/use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-30-export-data-to-a-warehouse.md)

## When the law changes

Watched in the law corpus: GDPR art. 5, 6, 13 and 89. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

As in [CR-FR-050](cr-fr-050-privacy-by-design.md): up to 10 000 000 EUR or 2 % of turnover (GDPR art. 83(4)).

## Exceptions

Processing based on consent or on a Union or Member State law needs no compatibility test (art. 6(4)).

## Open questions

None: the texts were read on 2026-11-27.

---

⬅️ [CR-FR-274 Transfers outside the EU to a cloud suite](cr-fr-274-transfers-to-cloud-suites.md) · ⬆️ [Up](README.md) · ➡️ [CR-FR-276 Removal quotes and delivery reserves](../transport/cr-fr-276-removal-quotes.md)
