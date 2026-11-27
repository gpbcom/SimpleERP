🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D574 Legal items no official source settles are reviewed by a lawyer before launch

# 📜 D574 Legal items no official source settles are reviewed by a lawyer before launch

**Status:** ✅ decided

## Context

After [D572](d572-proposals-confirmed-in-bulk.md), the legal and tax values of the specifications were read against
official sources in four passes on 2026-11-27: three reading passes of the France country pack, the last one with a
headed browser to reach the sites that refuse plain fetching, then the propagation of the values read to the product
pages. Some items still have no official answer: a value no law sets (it lives in a collective agreement, a fund's rules,
a standard or an appellation's specifications), a law not yet promulgated (the French transposition of NIS2), a text
the tools could not read, or a penalty no article states. Kept as "(Proposed)", they looked like gaps in the
specifications, although nothing more can be specified without a lawyer.

## Options

- Keep them marked "(Proposed)" until a lawyer has read them, as gaps of the specifications.
- Drop them and let the build decide.
- Settle them as specified, with an explicit lawyer review before launch.

## Choice

A legal item that no official source settles after the four reading passes is **specified as it stands** and carries
the marker **"(⚖️ lawyer review before launch, D574)"**, with the text the lawyer must read. Its page has the status
**"✅ specified, ⚖️ lawyer review before launch (D574)"** (a decision page: "✅ decided, ⚖️ lawyer review before launch
(D574)"). These items are no longer gaps of the specifications.

## Decided by

The owner, on 2026-11-27.

## Consequences

- The [waiting list](../../09-waiting/README.md) becomes the lawyer's checklist: every page holding the marker, in the
  France country pack and in the product pages, grouped by area, with the text to read on each page.
- A ticket that implements a page carrying the marker builds it as specified and carries the lawyer's review as an
  **external acceptance item**: the ticket is done when its own acceptance criteria pass; the feature launches once the
  lawyer has confirmed or corrected the item, and a correction ships as a country-pack update
  ([D294](../country-packs/d294-flag-then-pack-update.md)).
- The "(Proposed, lawyer review)" markers written by the reading passes became this marker; the pages that had the
  status `🔄 waiting for the legal reading` or `🔄 waiting for the owner` only because of such items moved to the new
  status, and the README index tables show ✅.
- A legal value later read in an official source loses the marker and cites its country-pack rule, as the reading
  passes did.
- A standard (ISO, IEC, EN, NF, VSME) or a mailbox provider's sender rule is a product reference, not a lawyer item: its
  page cites it as a design reference, with no marker
  ([D575](d575-answers-of-2026-11-27-on-the-last-open-points.md)).

## Related

- [D572 The owner's proposals confirmed in bulk](d572-proposals-confirmed-in-bulk.md)
- [D573 Which page wins when two specification pages disagree](d573-precedence-between-spec-pages.md)
- [D575 The owner's answers of 2026-11-27 on the last open points](d575-answers-of-2026-11-27-on-the-last-open-points.md)
- [Legal rules in France](../../05-non-functional/legal-france.md)
- [France country pack](../../10-country-packs/france/README.md)

---

⬅️ [D573](d573-precedence-between-spec-pages.md) · ⬆️ [Up](README.md) ·
➡️ [D575](d575-answers-of-2026-11-27-on-the-last-open-points.md)
