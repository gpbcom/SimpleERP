🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D572 The owner's proposals confirmed in bulk, the legal values kept for the legal reading

# 📜 D572 The owner's proposals confirmed in bulk, the legal values kept for the legal reading

**Status:** ✅ decided

## Context

The specifications mark everything Claude proposed and the owner did not confirm with the marker "Proposed" in
brackets, and the [waiting list](../../09-waiting/README.md) listed about 1,640 pages holding such items, with statuses
such as
`🔄 waiting for the owner`, `🔄 drawn in step 36j ...` (marked) and `🔄 draft (GH-2 step S4b ...)`. Legal readers
check legal values against official sources, so those cannot be confirmed on the owner's word alone.

## Options

- Confirm every proposal page by page in further interview rounds.
- Confirm every proposal as it stands, except the legal and tax values.
- Confirm everything, the legal values included.

## Choice

The owner confirms **every marked item outside the country pack as it stands**: product choices such as a
default, a delay to reopen, a reminder lead time, a screen layout, a placement, a role, a wording, a retention period
the product sets or a business threshold. **Legal and tax values keep the marker**: rates, amounts, thresholds, legal
time limits, penalties, retention periods imposed by law, filings, and the sentences saying that a France-pack rule is
still to read. Each occurrence was judged on its own: a value that restates the law is kept, a product choice is
confirmed.

## Decided by

The owner, on 2026-11-27.

## Consequences

- About 2,860 markers were removed outside the country pack: 2,754 plain markers and about 110 variants such as a
  "Proposed placement" note or a "Proposed: 30" default, which now reads "(default: 30)". Six mock-ups lost the marker
  on screen.
- About 1,745 pages moved to `✅ specified` (`✅ decided` for decision pages), the drafts of GH-2 included; the README
  index tables show the new icons.
- **Kept for the legal reading:** 398 markers on 360 pages, for example the "France-pack rule ... until its law is read"
  lines of the business rules, the "to read: ..." regulatory references, retention periods that follow the law (10 years
  with the accounts or the invoices, 5 years with pay records, the anti-money-laundering period, 3 years after the last
  contact with a prospect or customer, call recordings), legal time limits (24 hours for the NIS2 facts, 15 days for the
  profit-sharing choice), legal thresholds (50 employees over 5 years for profit-sharing, groups under 3 left out of the
  pay-gap index), the hours of SMS marketing and tax treatments still to confirm with a tax adviser. A page whose only
  items left are legal has the status `🔄 waiting for the legal reading`.
- **Entity fields derived from the specs on 2026-11-27, confirmed by the owner:** the 69 entities created from the flow
  charts ([D516](d516-naming-rules-and-the-seven-classes-of-names.md)) had no fields, relations, indexes or imports yet.
  They were derived from the use cases, business rules, flows, screens, list views and mock-ups that use each entity,
  with their sources cited on each page, the most conservative option taken where the specs say nothing; the owner
  confirmed them and the pages are `✅ specified`.
- The France country pack (`10-country-packs/`) is outside this decision: its rules are being read.
- **After the legal reading of 2026-11-27:** the values read in official sources replaced the kept markers and cite their
  country-pack rule, and the contradictions between pages were settled by
  [D573](d573-precedence-between-spec-pages.md). What no official source settles is reviewed by a lawyer before launch
  ([D574](d574-lawyer-review-before-launch.md)): of the 398 markers kept outside the country pack, 160 items on 152
  pages remain, marked for that review, with 68 items on 34 rules of the country pack. No page
  has the status `🔄 waiting for the legal reading` any more.
- **How to find what is left:** the [waiting list](../../09-waiting/README.md) lists every page still holding a
  marked item, grouped by area and kind; a fixed-string search for the marker in `docs/specs` finds the same pages.

## Related

- [Waiting for the owner](../../09-waiting/README.md)
- [D569 Roadmap option A, cut into twelve phases](../vision/d569-roadmap-option-a-in-twelve-phases.md)
- [Legal rules in France](../../05-non-functional/legal-france.md)

---

⬅️ [D571](../f09-hr-and-projects/d571-linkedin-sourcing-uses-the-users-search.md) · ⬆️ [Up](README.md) ·
➡️ [D573](d573-precedence-between-spec-pages.md)
