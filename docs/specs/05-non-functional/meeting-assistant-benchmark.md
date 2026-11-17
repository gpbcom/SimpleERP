🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 🎙️ Meeting assistant benchmark

# 🎙️ Meeting assistant benchmark

**Status:** ✅ research done (2026-11-10)

The owner asked that the meeting assistant cover everything the benchmarked product does
([D232](../06-decisions/f04-meetings/d232-meeting-assistant-parity.md)). A research agent read 19 public pages of the
benchmarked product's public website on 2026-11-10: features, solutions by team, integrations, pricing, security. Not
read: the public-sector page, the template library, comparison pages, per-integration pages and the Trust Center. This
page maps each capability found to where simple-ERP covers it; features the benchmarked product announces but does not
offer yet (voicemail, a sales prospecting agent, a public API) are noted, not required.

## Requirement

Every capability below is covered by F4, or by the capability named, and kept in step when the benchmark is refreshed.

## Capabilities

| Benchmarked capability (2026-11-10) | Covered in simple-ERP by |
|---|---|
| Bot for Meet, Teams, Zoom, Webex; bot name | UC-F4-01, S-F4-07 (Webex, bot name) |
| Recording without a bot (desktop app) | UC-F4-10, announced (D233) |
| In-person recording on mobile, screen locked | UC-F4-03 |
| Phone: own VoIP softphone, inbound on mobile, Aircall, Ringover, 3CX | UC-F4-04, UC-F4-16 (SIP, D236) |
| Calendars: Google, Outlook, Exchange; auto-join | BR-F4-17 (two-way), BR-F4-06 |
| Recording modes: audio and video, audio only, transcript only | UC-F4-10, S-F4-07 |
| Audio or video file upload (not found in the benchmarked product) | UC-F4-10 |
| Transcription in many languages, report language, translation | BR-F4-05 |
| Speakers and timestamps, talk-time | BR-F4-02, UC-F4-12 |
| Live transcription and live assistant | BR-F4-09 (70 % confidence) |
| Custom vocabulary | S-F4-07 |
| Reports by template; custom and AI-generated templates; brand charter | BR-F4-13, F2, D162 |
| Export PDF, Word, text; share by link; slides | UC-F4-11 |
| Action items with owner and due date; task page | BR-F4-14, F3 |
| Follow-up email in the user's style, with attachments | UC-F4-05, BR-F3-11, BR-F3-12 |
| Sales scorecard, criteria out of 5, total out of 100 | UC-F4-12 (D234) |
| Interview evaluation grid, candidate match score | UC-F4-13 (D234, high-risk AI, BR-F4-21) |
| Key moments, clips, chapters | UC-F4-11 |
| Meeting prep brief from calendar and inbox | UC-F4-09 |
| Deal health, stakeholders, deals at risk | UC-F4-12, UC-F4-15 |
| Ask across meetings and emails, cited | UC-F4-06, F3 (emails as a source: F3 extension, Proposed) |
| Slides, emails and scheduled actions from the AI assistant | UC-F4-11, UC-F4-15, F3 |
| MCP server with read-only meeting tools | UC-F4-14, T6 |
| CRM and ATS write-back, field auto-fill with per-field instructions | UC-F4-12 (simple-ERP's own CRM, F6), UC-F4-13 (F9) |
| Notion, Drive, OneDrive, OneNote, SharePoint; Slack and Teams recaps | UC-F4-11, UC-F4-14 |
| Jira, Linear, Trello, ClickUp two-way task sync | UC-F4-14 |
| Zapier, Make, n8n, API and webhooks | UC-F4-14, T5 |
| Folders per client or project; private by default; sharing | Links to records (BR-F4-12), BR-F4-04 |
| Team dashboards, adoption stats, admin lock of settings | F4 reports, S-F4-07 |
| Recruitment: sourcing, campaigns, AI voice pre-screening | F9 (D235) |
| Recruitment: interview reports, debriefs, ATS fields | UC-F4-13 |
| Hosting choice, sovereign mode, models (open source, Claude, Gemini, Mistral) | Self-hosted (D5), F1 AI settings per feature (D82) |
| Encryption, SSO, MFA, retention, deletion in 24 h, no training on data | T2, T9, BR-F4-03, technical design 19f Security |
| ISO 27001, SOC 2, DPA, subprocessors | Technical design 19f Security and 19g Supply chain (to interview) |

## Not found in the benchmarked product

Audio or video file upload, sentiment analysis, keyword extraction, questions-asked analytics, comments on reports, a
coaching module, published transcription accuracy. simple-ERP adds file upload (UC-F4-10).

## Open questions

None.

---

⬆️ [Up](README.md)
