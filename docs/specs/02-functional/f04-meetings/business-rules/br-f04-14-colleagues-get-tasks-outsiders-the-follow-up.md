🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-14 Colleagues get tasks, outsiders the follow-up

# 📏 BR-F4-14 Colleagues get tasks, outsiders the follow-up

**Status:** ✅ specified

## Statement

At review, each action for a colleague is offered as a task (owner, due date, linked to the meeting) through the
confirmation card (UC-F3-03); each action for an outside person is listed in the follow-up email draft, which the user
sends (BR-F3-12).

## Why

Tasks are for people in the ERP. See [D225](../../../06-decisions/f04-meetings/d225-actions-to-tasks.md).

## Examples

| Case | Result |
|---|---|
| "Paul sends the plan by Friday" | Task for Paul, due Friday, after confirmation |
| "Durand confirms the colour" | In the follow-up email to Durand |

## Applies to

- [UC-F4-05](../use-cases/03-review-a-meeting/uc-f04-05-review-a-meeting.md)
- [UC-F4-26 Receive and confirm the agreed actions](../use-cases/13-outside-people-and-follow-up/uc-f04-26-receive-and-confirm-the-agreed-actions.md)
- [UC-F4-27 Keep meeting actions in step with tasks](../use-cases/13-outside-people-and-follow-up/uc-f04-27-keep-meeting-actions-in-step-with-tasks.md)

## Exceptions

HR meetings follow UC-F4-07.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F4-13 Summaries follow the meeting kind](br-f04-13-summaries-follow-the-meeting-kind.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-15 Unreviewed meetings publish as not checked](br-f04-15-unreviewed-meetings-publish-as-not-checked.md)
