🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 📣 F5 Social media and marketing

# 📣 F5 Social media and marketing

**Status:** ✅ specified

Build step: 8. Growth and insight.

## Summary

Prepare, approve, schedule and publish posts on the company's social networks, with AI drafts and media, an automatic
mode for routine events, replies and statistics ([D242](../../06-decisions/f05-social-media/d242-social-networks.md) to
[D246](../../06-decisions/f05-social-media/d246-social-auto-mode.md)).

## Scope

- **Networks:** LinkedIn, Facebook, Instagram, X, YouTube, TikTok, Mastodon, Bluesky, Threads, Google Business Profile,
  through official APIs (T12), tokens in the vault (D240).
- **Formats:** text, images, carousels, videos, short videos, stories, links, adapted per network.
- **Approval:** by role; scheduled posts in a calendar.
- **Automatic mode:** per event type, internal or external, from templates, no approval, with guard rails.
- **AI:** drafts, images and videos, times and hashtags, reply suggestions; content marked (D164).
- **Benchmark additions (D303):** email and SMS campaigns, marketing journeys, events with registrations and tickets,
  surveys and live polls, leads from social posts; consent from the country pack.
- **Gaps and improvements round ([D462](../../06-decisions/f05-social-media/d462-f05-gaps-and-improvements.md),
  2026-11-12):** contact segments, proof of consent and deliverability; landing pages and forms; WhatsApp Business;
  campaign budget, cost per lead and return on investment; the one events and ticketing model shared with F10 and the
  sectors ([D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md)); a brand kit and asset library; A/B
  tests on posts, emails and SMS; and the shared flow split into email and SMS, audiences, events and ticketing, and
  pages and forms.

## Personas

[U12 Marketing](../../01-users/personas/u12-marketing.md), [U13 Owner](../../01-users/personas/u13-owner.md) (approver),
[U02 Manager](../../01-users/personas/u02-manager.md) (approver for a team's account),
[U07 Administrator](../../01-users/personas/u07-administrator.md) (connects accounts),
[U03 Sales](../../01-users/personas/u03-sales.md), [U06 Human resources](../../01-users/personas/u06-hr.md),
[U09 Customer](../../01-users/personas/u09-customer.md),
[U16 Office worker](../../01-users/personas/u16-office-worker.md),
[U43 Event producer](../../01-users/personas/u43-event-producer.md),
[U44 Box-office agent](../../01-users/personas/u44-box-office-agent.md),
[U23 Store manager](../../01-users/personas/u23-store-manager.md).

## Out of scope

- Paid advertising campaigns (ads managers).
- Personal accounts of employees.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md) (external events)

## Build step

Step 8, Growth and insight, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the
specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Meetings](../f04-meetings/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Customers and sales](../f06-customers-and-sales/README.md)
