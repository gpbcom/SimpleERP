🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧰 [Decisions: F14 Plugin store](README.md) ›
📜 D533 Benchmark gaps of F14 Plugin store

# 📜 D533 Benchmark gaps of F14 Plugin store

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four store
features that F14 did not cover: test environments for publishers, free trials of paid plugins, a directory of
implementation partners and website themes. Each touches trust: demo data only, a trial that cannot bill by itself, a
ranking that can be explained, and themes everyone can read.

## Options

- G79 Publisher test instances: test instances with demo data only, or publishers run their own environment.
- G80 Free trials: a trial that ends with a purchase or a clean uninstall, or a trial that renews by itself.
- G81 Partner directory: a directory with a transparent ranking, or a plain list.
- G82 Website themes: themes that pass accessibility checks, or themes with no check.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F14 gets four use cases in one new flow, FL-F14-08, each with its screen, its rule, its entity and its list. All at full
depth now. The partner is the new persona U51.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G79 | Publisher test instances | UC-F14-29: test instances that hold demo data only | "Publisher test instances" |
| G80 | Free trials | UC-F14-30: trials that end with a purchase or a clean uninstall | "Free trials" |
| G81 | Partner directory | UC-F14-31: a partner directory with a ranking whose factors are shown | "Partner directory" |
| G82 | Website themes | UC-F14-32: themes that pass the accessibility checks | "Website themes" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F14 Plugin store").

## Consequences

- G79 Publisher test instances:
  [UC-F14-29](../../02-functional/f14-plugin-store/use-cases/08-trials-instances-and-partners/uc-f14-29-get-a-publisher-test-instance.md),
  [S-F14-27](../../02-functional/f14-plugin-store/screens/08-trials-instances-and-partners/s-f14-27-test-instances.md)
  and [BR-F14-24](../../02-functional/f14-plugin-store/business-rules/br-f14-24-test-instances-hold-demo-data-only.md),
  with [E-F14-22](../../02-functional/f14-plugin-store/data/e-f14-22-test-instance.md) Test instance and its list
  [S-F14-L22](../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l22-test-instances.md).
- G80 Free trials:
  [UC-F14-30](../../02-functional/f14-plugin-store/use-cases/08-trials-instances-and-partners/uc-f14-30-try-a-paid-plugin-free.md),
  [S-F14-28](../../02-functional/f14-plugin-store/screens/08-trials-instances-and-partners/s-f14-28-free-trials.md) and
  [BR-F14-25](../../02-functional/f14-plugin-store/business-rules/br-f14-25-a-trial-ends-with-a-purchase-or-a-clean-uninstall.md),
  with [E-F14-23](../../02-functional/f14-plugin-store/data/e-f14-23-trial.md) Trial and its list
  [S-F14-L23](../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l23-trials.md).
- G81 Partner directory:
  [UC-F14-31](../../02-functional/f14-plugin-store/use-cases/08-trials-instances-and-partners/uc-f14-31-find-an-implementation-partner.md),
  [S-F14-29](../../02-functional/f14-plugin-store/screens/08-trials-instances-and-partners/s-f14-29-partner-directory.md)
  and [BR-F14-26](../../02-functional/f14-plugin-store/business-rules/br-f14-26-partner-rankings-are-transparent.md),
  with [E-F14-24](../../02-functional/f14-plugin-store/data/e-f14-24-partner-listing.md) Partner listing and its list
  [S-F14-L24](../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l24-partner-listings.md).
- G82 Website themes:
  [UC-F14-32](../../02-functional/f14-plugin-store/use-cases/08-trials-instances-and-partners/uc-f14-32-install-a-website-theme.md),
  [S-F14-30](../../02-functional/f14-plugin-store/screens/08-trials-instances-and-partners/s-f14-30-website-themes.md)
  and
  [BR-F14-27](../../02-functional/f14-plugin-store/business-rules/br-f14-27-themes-pass-the-accessibility-checks.md),
  with [E-F14-25](../../02-functional/f14-plugin-store/data/e-f14-25-theme.md) Theme and its list
  [S-F14-L25](../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l25-themes.md).
- Drawn in [FL-F14-08](../../02-functional/f14-plugin-store/flows/fl-f14-08-trials-instances-and-partners.md) Trials,
  test instances, partners and themes.

## Related

- [FL-F14-08](../../02-functional/f14-plugin-store/flows/fl-f14-08-trials-instances-and-partners.md)
- [D471 F14 Plugin store: gaps and improvements](d471-f14-gaps-and-improvements.md)
- [D443](../vision/d443-paid-plugins-sell-support-updates-hosting.md)
- [U51 Reseller partner](../../01-users/personas/u51-reseller-partner.md)

---

⬅️ [D532 Benchmark gaps of F13 Payroll](../f13-payroll/d532-benchmark-gaps-f13-payroll.md) · ⬆️ [Up](README.md) ·
➡️ [D534 Benchmark gaps of F15 Legal assistant](../f15-legal-assistant/d534-benchmark-gaps-f15-legal-assistant.md)
