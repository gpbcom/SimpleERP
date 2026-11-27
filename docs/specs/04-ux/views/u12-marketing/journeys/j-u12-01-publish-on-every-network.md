🏠 [Specs](../../../../README.md) › 🎨 [UX](../../../README.md) › 🪟 [Views](../../README.md) ›
📣 [Marketing and communication: app shell and home](../README.md) › 🧭 [Journeys](README.md) ›
🧭 J-U12-01 Publish on every network

# 🧭 J-U12-01 Publish on every network

**Status:** ✅ specified

## Persona

[U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Goal

Publish consistent posts on every network from one place and know what works.

## Journey

Satisfaction at each step, from 1 (painful) to 5 (effortless): these scores are drawn from the
specs and confirmed by the owner (D572).

```mermaid
journey
  title Publish on every network
  section FL-F5-04 Connect accounts
    Connects the company's accounts: 3: U12
  section FL-F5-01 Publish a post
    Prepares and schedules a post: 4: U12
    Arranges the editorial calendar: 4: U12
  section FL-F5-03 Inbox and statistics
    Answers comments and messages: 4: U12
    Reads what worked in the statistics: 5: U12
```

## Flowchart

The same steps; each problem is the first error flow of the step's use case (once per use case), shown with the error
message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)).

```mermaid
flowchart TD
  S1["1. Connects the company's accounts"]
  S1 -- problem --> E1["The network refuses the app (not reviewed): the steps to get it reviewed are shown."]
  E1 -. fixed .-> S1
  S2["2. Prepares and schedules a post"]
  S2 -- problem --> E2["A format a network refuses: flagged."]
  E2 -. fixed .-> S2
  S1 -- done --> S2
  S3["3. Arranges the editorial calendar"]
  S3 -- problem --> E3["Moving a post into a network's limit: refused with the reason."]
  E3 -. fixed .-> S3
  S2 -- done --> S3
  S4["4. Answers comments and messages"]
  S4 -- problem --> E4["A private message the API does not expose: a link to answer in the network."]
  E4 -. fixed .-> S4
  S3 -- done --> S4
  S5["5. Reads what worked in the statistics"]
  S5 -- problem --> E5["A network's statistics API unavailable: last figures shown with their date."]
  E5 -. fixed .-> S5
  S4 -- done --> S5
```

## Steps

| Step | Screen | Use case | What the persona does | What the system does |
|---|---|---|---|---|
| 1 | [S-F5-07 Social accounts](../../../../02-functional/f05-social-media/screens/04-connect-accounts/s-f05-07-social-accounts.md) | [UC-F5-07 Connect the company's accounts](../../../../02-functional/f05-social-media/use-cases/04-connect-accounts/uc-f05-07-connect-the-company-s-accounts.md) | Connects the company's accounts | Keeps the app's keys in the vault (BR-F5-07). |
| 2 | [S-F5-01 Post composer](../../../../02-functional/f05-social-media/screens/01-publish-a-post/s-f05-01-post-composer.md) | [UC-F5-01 Prepare and schedule a post](../../../../02-functional/f05-social-media/use-cases/01-publish-a-post/uc-f05-01-prepare-and-schedule-a-post.md) | Prepares and schedules a post | Adapts the post per network (BR-F5-03) and suggests times. |
| 3 | [S-F5-04 Automatic post rules](../../../../02-functional/f05-social-media/screens/01-publish-a-post/s-f05-04-automatic-post-rules.md) | [UC-F5-04 Manage the editorial calendar](../../../../02-functional/f05-social-media/use-cases/01-publish-a-post/uc-f05-04-manage-the-editorial-calendar.md) | Arranges the editorial calendar | Shows every post by day and network, with gaps and suggested times. |
| 4 | [S-F5-05 Social inbox](../../../../02-functional/f05-social-media/screens/03-inbox-and-statistics/s-f05-05-social-inbox.md) | [UC-F5-05 Answer comments and messages](../../../../02-functional/f05-social-media/use-cases/03-inbox-and-statistics/uc-f05-05-answer-comments-and-messages.md) | Answers comments and messages | Lists comments and messages (BR-F5-05); the AI suggests a reply; links known customers. |
| 5 | [S-F5-06 Social statistics](../../../../02-functional/f05-social-media/screens/03-inbox-and-statistics/s-f05-06-social-statistics.md) | [UC-F5-06 Read statistics](../../../../02-functional/f05-social-media/use-cases/03-inbox-and-statistics/uc-f05-06-read-statistics.md) | Reads what worked in the statistics | Shows reach, engagement, clicks and the leads and orders traced (BR-F5-06). |

This persona's images of these flows (D120):
[FL-F5-01 Publish a post](../../../../02-functional/f05-social-media/images/01-publish-a-post/u12-marketing/README.md),
[FL-F5-03 Inbox and statistics](../../../../02-functional/f05-social-media/images/03-inbox-and-statistics/u12-marketing/README.md).

## Open questions

None.

---

⬆️ [Up](README.md)
