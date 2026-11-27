🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F5-01 Posts need an approver

# 📏 BR-F5-01 Posts need an approver

**Status:** ✅ specified

## Statement

A post is published only after someone with the approver right on that account approves it; a company can drop approval
for an account; automatic posts follow BR-F5-02 instead.

## Why

What a company says publicly is its image. See [D244](../../../06-decisions/f05-social-media/d244-social-approval.md).

## Examples

| Case | Result |
|---|---|
| A marketing draft for LinkedIn | Waits for an approver |
| The account set to no approval | Published at its time |

## Applies to

Every F5 use case.

## Exceptions

None.

## Configurable

Yes: approvers and approval per account.

## Open questions

None.

---

⬆️ [Up](README.md) ·
➡️ [BR-F5-02 Automatic posts follow their event rule](br-f05-02-automatic-posts-follow-their-event-rule.md)
