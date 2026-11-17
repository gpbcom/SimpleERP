🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-02 Automatic posts follow their event rule

# 📏 BR-F5-02 Automatic posts follow their event rule

**Status:** ✅ specified

## Statement

For an event type set to automatic, a post is built from its template and published with no approval when the event
happens: internal events (a new product, a finished project, a job opening, a review received) or external ones (a
webhook, a feed item, a mention). Guard rails: a daily limit per account, a list of words never published, a
stop switch per account, and a log of every automatic post; the AI mention applies (D164).

Automatic posts are an automation tier of [D439](../../../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md): only
for event types an administrator switched to automatic, within the daily limit, every post audited and a sample checked
by a person.

## Why

Routine announcements should not wait for a person. See
[D246](../../../06-decisions/f05-social-media/d246-social-auto-mode.md).

## Examples

| Case | Result |
|---|---|
| "Job opening published" set to automatic on LinkedIn | The opening is posted from its template at once |
| The daily limit reached | The post waits for the next day and the author is told |
| Stop switch on | Nothing automatic goes out |

## Applies to

Every F5 use case.

## Exceptions

None.

## Configurable

Yes: per event type: automatic or approval, networks, template, guard rails.

## Open questions

None.

---

⬅️ [BR-F5-01 Posts need an approver](br-f05-01-posts-need-an-approver.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F5-03 Posts are adapted per network](br-f05-03-posts-are-adapted-per-network.md)
