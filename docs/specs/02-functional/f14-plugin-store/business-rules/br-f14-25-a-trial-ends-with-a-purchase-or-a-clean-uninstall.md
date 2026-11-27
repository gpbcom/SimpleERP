🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-25 A trial ends with a purchase or a clean uninstall

# 📏 BR-F14-25 A trial ends with a purchase or a clean uninstall

**Status:** ✅ specified

## Statement

A trial always ends in one of two ways: a purchase, or a clean uninstall that exports what the plugin created and
removes the plugin and its data; it never renews by itself and never bills without a purchase the administrator
confirmed.

## Why

A trial that quietly turns into a subscription, or leaves a plugin's data behind, would break the trust the store needs.
The owner asked for free trials
([D533](../../../06-decisions/f14-plugin-store/d533-benchmark-gaps-f14-plugin-store.md));
[BR-F14-04 Uninstall keeps an export](br-f14-04-uninstall-keeps-an-export.md) already keeps an export at every
uninstall.

## Examples

| Case | Result |
|---|---|
| A trial ends with no purchase | the plugin is switched off, the export offered, the data removed after 30 days |
| The administrator buys on day 10 | the trial is converted and the plugin keeps its data |
| A trial reaching its end date | no charge is made |
| A second trial of the same plugin | refused |
| A purchase during the grace period | the plugin is switched on again with its data |

## Applies to

- [UC-F14-30](../use-cases/08-trials-instances-and-partners/uc-f14-30-try-a-paid-plugin-free.md)
- [E-F14-23 Trial](../data/e-f14-23-trial.md)
- [E-F14-02 Plugin installation](../data/e-f14-02-plugin-installation.md)

## Exceptions

None.

## Configurable

The length of a trial and one extension, per price plan, by the publisher.

## Open questions

None.

---

⬅️ [BR-F14-24 Test instances hold demo data only](br-f14-24-test-instances-hold-demo-data-only.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F14-26 Partner rankings are transparent](br-f14-26-partner-rankings-are-transparent.md)
