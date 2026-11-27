🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎯 [Decisions: Vision](README.md) ›
📜 D440 Local by default, outside only by an administrator's choice

# 📜 D440 Local by default, outside only by an administrator's choice

**Status:** ✅ decided

## Context

R2: the promise "the company's data is never copied to a third party" and "every part, the AI included, runs on the
operator's servers" against outside models used by F20 and F25 and GitHub (United States) holding USER issues.

## Options

- Reword the promise to what is true, with a list of the hosted edition's providers.
- Keep the promise and drop every outside model and service.

## Choice

Local by default, outside only by choice. **Self-hosted:** everything runs on the operator's servers unless an
administrator chooses an outside provider for a feature (D82), shown and logged. **Hosted edition:** the publisher lists
the providers it may use, their regions and their processing terms (a data processing agreement under GDPR article 28,
processing in the EU where the provider offers it); outside that list, nothing leaves. **Customers' data never goes into
GitHub:** USER tickets hold a sanitised summary only (D433).

## Decided by

The owner, on 2026-11-12 at 14:53, round 1 of the decisions on the independent review (R2, PROGRESS.md, step 21).

## Consequences

Revises D373 (the promise reworded: local by default, outside only by an administrator's choice) and D388 (the closed
services use only the listed providers). The list itself is in Privacy and GDPR, (Proposed) until the providers are
named at launch. The vision pages say it plainly.

## Related

- [Positioning](../../00-vision/product/positioning.md)
- [Objectives](../../00-vision/product/objectives.md)
- [Privacy and GDPR](../../05-non-functional/privacy-gdpr.md)
- [D373](d373-sovereign-ai-native-suite.md)
- [D388](d388-hosted-edition-open-core.md)
- [Independent review of 2026-11-12](../../../tickets/GH-2/review/2026-11-12-review.md)

---

⬅️ [D439 AI autonomy tiers per feature](../f03-assistant/d439-ai-autonomy-tiers.md) · ⬆️ [Up](README.md) ·
➡️ [D441 The approval label reported and reverted](../f25-devops-agents/d441-approval-label-reported-and-reverted.md)
