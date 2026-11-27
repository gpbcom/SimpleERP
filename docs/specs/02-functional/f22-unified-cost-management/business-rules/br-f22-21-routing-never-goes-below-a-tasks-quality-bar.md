🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-21 Routing never goes below a task's quality bar

# 📏 BR-F22-21 Routing never goes below a task's quality bar

**Status:** ✅ specified

## Statement

A routing rule is activated, and stays active, only while the model that receives its calls scores at or above the
rule's quality bar on the task kind's evaluation; a score below the bar pauses the rule and sends the calls to the next
model in order.

## Why

A saving that lowers the quality of answers is a cost moved onto the users. The owner asked for model routing savings
([D541](../../../06-decisions/f22-unified-cost-management/d541-benchmark-gaps-f22-unified-cost-management.md)); the
platform already blocks a model or prompt change that drops quality
([BR-F3-37](../../f03-assistant/business-rules/br-f03-37-a-quality-drop-blocks-a-model-or-prompt-change.md)).

## Examples

| Case | Result |
|---|---|
| Bar 0.85, cheaper model scores 0.88 | the rule can be activated |
| Bar 0.85, cheaper model scores 0.81 | the activation is refused |
| An active rule whose latest run scores 0.80 | paused, calls go to the next model |
| Every model below the bar | calls go to the best model and the administrator is warned |
| A task kind with no evaluation set | no rule can be activated: the set is needed first |

## Applies to

- [UC-F22-30](../use-cases/08-credits-saas-and-carbon/uc-f22-30-route-ai-tasks-to-save-costs.md)
- [E-F22-21 Routing rule](../data/e-f22-21-routing-rule.md)
- [BR-F3-37](../../f03-assistant/business-rules/br-f03-37-a-quality-drop-blocks-a-model-or-prompt-change.md)
- [E-F22-16 Savings recommendation](../data/e-f22-16-savings-recommendation.md)

## Exceptions

A call that needs a capability only one model has goes to that model.

## Configurable

The quality bar and the cost cap of each rule, by the administrator.

## Open questions

None.

---

⬅️ [BR-F22-20 Carbon figures carry their method and source](br-f22-20-carbon-figures-carry-their-method-and-source.md) ·
⬆️ [Up](README.md)
