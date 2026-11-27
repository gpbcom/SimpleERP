🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🩺 [SC09 Health practices](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC09-19 Prosthetics need the regulated quote before care

# 📏 BR-SC09-19 Prosthetics need the regulated quote before care

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

No prosthetic act is planned or done before the patient has received the regulated quote and signed it. The quote
follows annex III of the dentists' national agreement: the treatment, each act and its code, the device and its
materials, the fees, the reimbursement base and the amount the health insurance pays, the basket of each act, the place
of manufacture, the alternatives with no or a moderate remaining cost, the date and the validity; it is due from a fee
overrun of 70 EUR and for every made-to-measure device. The complementary cover's share and the remaining cost are not
part of the regulated quote: SimpleERP may show them apart, as information. An act outside the quote is flagged.

## Why

The patient has the right to know what the care costs before it starts, and the dentist may not charge more than what
was accepted. The owner asked for dental practices
([D553](../../../06-decisions/sectors/d553-benchmark-gaps-sc09-health-practices.md)). The France-pack rule is
[CR-FR-238 Regulated dental quote](../../../10-country-packs/france/health-practice/cr-fr-238-dental-regulated-quote.md).

## Examples

| Case | Result |
|---|---|
| Quote signed, crown done | the act is linked to its line |
| Quote sent, not signed, care planned | refused |
| Plan changed after signature | a new version, signed again |
| Act in the package with no remaining cost | the price is capped by the pack |
| Emergency care | the quote follows as soon as possible, with the reason |

## Applies to

- [UC-SC09-24](../use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-24-quote-dental-work-with-the-regulated-quote.md)
- [E-SC09-17 Dental quote](../data/e-sc09-17-dental-quote.md)
- [E-SC09-03 Clinical record entry](../data/e-sc09-03-clinical-record-entry.md)
- France-pack rule, (⚖️ lawyer review before launch, D574) until the dentists' national agreement 2023-2028 (its quote article and annex III) is read, for
  the patient's acceptance before the care:
  [CR-FR-238 Regulated dental quote](../../../10-country-packs/france/health-practice/cr-fr-238-dental-regulated-quote.md)

## Exceptions

Urgent care that cannot wait may start with the reason recorded; the quote follows.

## Configurable

The price caps and the acts of the package, as data of the country pack; the reminder delay, by the dentist.

## Open questions

None.

---

⬅️ [BR-SC09-18 Dispensed medicines enter the register](br-sc09-18-dispensed-medicines-enter-the-register.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC09-20](br-sc09-20-activity-is-reported-to-the-regional-health-agency.md)
