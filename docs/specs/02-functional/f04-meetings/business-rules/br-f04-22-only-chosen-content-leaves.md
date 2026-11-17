🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-22 Only chosen content leaves

# 📏 BR-F4-22 Only chosen content leaves

**Status:** ✅ specified

## Statement

For each outside tool (Notion, Google Drive, OneDrive, SharePoint, Slack, Teams, Jira, Linear, Trello, ClickUp, Zapier,
Make, n8n, webhooks, MCP clients), the administrator chooses what may leave: summary, transcript, actions, recording;
nothing else leaves; a review before sending can be required per tool; outside calls follow F3's data
categories and caps (BR-F3-17, BR-F3-20).

## Why

Meetings hold sensitive content; integrations must not leak it.

## Examples

| Case | Result |
|---|---|
| Slack allowed summaries | The summary posts to #sales; the transcript never |
| Jira allowed actions | Actions become Jira issues, synced both ways |

## Applies to

- [UC-F4-11](../use-cases/08-share-and-reuse-outside/uc-f04-11-share-export-and-clip-a-meeting.md)
- [UC-F4-14](../use-cases/08-share-and-reuse-outside/uc-f04-14-use-meetings-from-outside-tools.md)
- [UC-F4-15](../use-cases/08-share-and-reuse-outside/uc-f04-15-schedule-recurring-digests.md)

## Exceptions

None.

## Configurable

Yes: per tool, by an administrator.

## Open questions

None.

---

⬅️ [BR-F4-21 Candidate scoring is high-risk AI](br-f04-21-candidate-scoring-is-high-risk-ai.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-23 Bookings never overlap](br-f04-23-bookings-never-overlap.md)
