🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 🎙️ Meeting recording

# 🎙️ Meeting recording

**Status:** ✅ specified

## Requirement

- The bot joins under a clear name, "SimpleERP recorder", and posts a notice in the meeting's chat.
- The invitation says that the meeting is recorded.
- Any participant can ask the bot to stop recording or to leave.
- The organiser is responsible for informing the participants. See
  [D23](../06-decisions/foundations/d23-meeting-bot-consent.md).

## Measures

- Every recording is announced and stoppable (BR-F4-01), in person by the organiser's confirmation and on the phone by a
  spoken message (D213).
- Audio deleted once the transcript is checked, 7 days by default (BR-F4-03).
- No voice prints (BR-F4-02).
- Transcripts stay with participants; HR meetings with HR and the employee (BR-F4-04, BR-F4-18).

- Phone calls are recorded only once switched on per purpose, the staff committee consulted
  ([D449](../06-decisions/f04-meetings/d449-call-recording-off-by-default.md), BR-F4-11).

## Country pack

The legal values this page relies on, from the France country pack (D293):

- [CR-FR-059 Recordings are announced](../10-country-packs/france/ai-and-recording/cr-fr-059-recordings-are-announced.md)
- [CR-FR-206 Staff committee consulted before monitoring tools](../10-country-packs/france/labour/cr-fr-206-cse-consulted-on-monitoring.md)
- [CR-FR-207 Call recording at work kept proportionate](../10-country-packs/france/data-protection/cr-fr-207-call-recording-proportionate.md)

## Open questions

⬜ To be specified.

---

⬅️ [AI governance](ai-governance.md) · ⬆️ [Up](README.md) · ➡️ [Legal rules in France](legal-france.md)
