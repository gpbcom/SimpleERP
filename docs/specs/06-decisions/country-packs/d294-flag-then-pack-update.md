🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🌍 [Decisions: Country packs](README.md) ›
📜 D294 A law change flags the rule, a pack update fixes it

# 📜 D294 A law change flags the rule, a pack update fixes it

**Status:** ✅ decided

## Context

How an enforced rule follows the law. The law texts are pulled unattended (D205).

## Options

- Flag, then pack update: the rule is flagged when a cited article changes, administrators are warned, the corrected
  rule ships in a pack update (recommended).
- Fully automatic: an AI rewrites and applies the rule.
- Administrator edits: each company adjusts the values itself.

## Choice

Each rule lists the articles it rests on and its values with their effective dates. When the law corpus sees one of
those articles change, the rule is flagged, administrators are warned, and the corrected rule ships in a pack update;
the values keep their history by date, so a past document is checked against the law of its date.

## Decided by

The owner, on 2026-11-11, in the specification interview.

## Consequences

The pack update is a plugin update (T9); the legal assistant can explain a flagged rule (F15); no rule value changes
without a release.

## Related

- [🇫🇷 France country pack](../../10-country-packs/france/README.md)

---

⬅️ [D293 Capabilities take legal rules from the country pack](d293-capabilities-take-legal-rules-from-the-pack.md) ·
⬆️ [Up](README.md) · ➡️ [D295 Point of sale coverage](../f10-point-of-sale/d295-pos-coverage.md)
