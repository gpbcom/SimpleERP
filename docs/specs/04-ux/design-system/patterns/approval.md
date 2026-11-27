🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧵 [Patterns](README.md) ›
🧵 Approval

# 🧵 Approval

**Status:** 🔄 waiting for the owner

## Purpose

How a request waits for someone's yes before it takes effect, and how the approver decides fast, from anywhere.

## When to use

Whenever a rule asks for an approval: time off, expenses, purchases
([D267](../../../06-decisions/f07-purchasing-and-stock/d267-purchase-approval.md)), quotes above a discount or below a
margin floor ([D255](../../../06-decisions/f06-customers-and-sales/d255-discount-approval.md)), social posts
([D244](../../../06-decisions/f05-social-media/d244-social-approval.md)), the pay run, fixes and agents' tickets. Not
for a change the user may make alone.

## Anatomy

```text
+-----------------------------------------------------+
| Time off: Luc Bernard          (Waiting for you)    |
| 23 Dec to 2 Jan, 6 days. Balance after: 6.5 days    |
| Team: 2 others off on those days                    |
| [Refuse...]                           [Approve]     |
|-----------------------------------------------------|
| o Requested 10 Nov by Luc Bernard                   |
| o Approved 11 Nov by the manager (step 1 of 2)      |
+-----------------------------------------------------+
```

1. **What is asked,** with the facts the approver needs to decide (the balance, the budget, the margin).
2. **The state:** a badge with a word (Draft, Waiting for you, Approved, Refused).
3. **The decision:** Approve and Refuse; refusing asks for a reason.
4. **The history:** a [C-14 Timeline](../components/c-14-timeline.md) of who asked, who decided and when.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/approval-desktop-light.png) | ![Variants and states, dark](../images/approval-desktop-dark.png) |

## Behaviour

- The request goes to the approvers the rule names, in one or several steps (for example a manager, then the owner above
  a second amount, [D267](../../../06-decisions/f07-purchasing-and-stock/d267-purchase-approval.md)).
- Approvers see the request in "My tasks" on their home screen ([D48](../../../06-decisions/ux/d48-home-screen.md)) and
  are told in the app and by email ([D92](../../../06-decisions/f01-administration/d92-notification-channels.md)); they
  can decide on a phone ([D34](../../../06-decisions/ux/d34-phone-experience.md)).
- A refusal goes back to the requester with its reason; (Proposed) they can change and send it again.
- Until approved, the request has no effect (a post is not published, a quote not sent).
- Every step is kept in the audit trail.

## Accessibility

- The state is a word, never a colour alone.
- (Proposed) Approve and Refuse are real buttons that name the request ("Approve Luc Bernard's time off").
- (Proposed) The reason field of a refusal is labelled and required.

## Used in

[S-F9-09 Time off](../../../02-functional/f09-hr-and-projects/screens/03-time/s-f09-09-time-off.md),
[S-F9-13 Approvals and lunch](../../../02-functional/f09-hr-and-projects/screens/05-workplace-services/s-f09-13-approvals-and-lunch.md),
[S-F5-02 Approval](../../../02-functional/f05-social-media/screens/01-publish-a-post/s-f05-02-approval.md),
[S-F22-09 Approvals](../../../02-functional/f22-unified-cost-management/screens/02-budgets-and-stops/s-f22-09-approvals.md),
[S-F20-06 Fix approval](../../../02-functional/f20-hosted-support-assistant/screens/02-diagnose-and-fix/s-f20-06-fix-approval.md)
and [S-F25-12 Approvals](../../../02-functional/f25-devops-agents/screens/04-approve-and-govern/s-f25-12-approvals.md);
and each flow whose use case names an approval.

---

⬅️ [Wizard](wizard.md) · ⬆️ [Up](README.md) · ➡️ [Search and filter](search-and-filter.md)
