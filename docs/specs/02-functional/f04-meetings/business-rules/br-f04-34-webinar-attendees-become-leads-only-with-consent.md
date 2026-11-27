🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-34 Webinar attendees become leads only with consent

# 📏 BR-F4-34 Webinar attendees become leads only with consent

**Status:** ✅ specified

## Statement

A webinar attendee is created as a lead only if they ticked, at registration, a separate unticked box agreeing to be
contacted about the company's offers; the others appear only as an aggregate count and an attendance record that holds
no marketing use; the replay and the reminders do not need that agreement.

## Why

Registering for a talk is not agreeing to be marketed to. The owner's answer: "Webinars"
([D523](../../../06-decisions/f04-meetings/d523-benchmark-gaps-f04-meetings.md)); consent for marketing messages is
[CR-FR-063](../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md).

## Examples

| Case | Result |
|---|---|
| Attendee ticks 'contact me about offers' | a lead is created after the webinar |
| Attendee leaves the box unticked | no lead, only the count |
| A pre-ticked box | refused by the form |
| An attendee who later withdraws | the lead is erased or marked do not contact |

## Applies to

- [UC-F4-29 Host a webinar](../use-cases/14-video-messages-and-webinars/uc-f04-29-host-a-webinar.md)
- [E-F4-28 Webinar](../data/e-f04-28-webinar.md)
- [UC-F6-01 Capture and qualify a lead](../../f06-customers-and-sales/use-cases/01-lead-to-quote/uc-f06-01-capture-and-qualify-a-lead.md)

## Exceptions

None.

## Configurable

Yes: the wording of the agreements, approved by the company.

## Open questions

None.

---

⬅️ [BR-F4-33 Video messages follow meeting retention](br-f04-33-video-messages-follow-meeting-retention.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F4-35](br-f04-35-ai-filled-template-fields-stay-drafts-until-reviewed.md)
