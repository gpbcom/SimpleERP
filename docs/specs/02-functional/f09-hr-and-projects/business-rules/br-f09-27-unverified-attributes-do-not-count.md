🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-27 Unverified or expired attributes do not count

# 📏 BR-F9-27 Unverified or expired attributes do not count

**Status:** 🔄 draft (GH-2 step S4b, from VD-26 / D508)

## Statement

An attribute counts for scheduling only when it is verified and current on the day of the work: one that is "to
verify", rejected or past its expiry date counts as missing; reminders go out before an expiry (Proposed: 90 days, as in
BR-F9-17).

## Why

- The owner's decision VD-26
  [D508](../../../06-decisions/f09-hr-and-projects/d508-hr-confirms-every-ai-reading-before-it-counts.md): until HR
  confirms an AI reading, the attribute is "to verify" and scheduling ignores it.
- An expired training or licence already blocks the work that needs it
  ([BR-F9-17](br-f09-17-mandatory-trainings-must-be-current-for-the-work-that-needs-them.md)); this rule extends it to
  every attribute.

## Examples

| Case | Result |
|---|---|
| A CACES read by the AI yesterday, not yet confirmed by HR | Does not count: "not eligible: to verify" |
| A degree confirmed by HR | Counts |
| A food-hygiene training expired on 2026-10-31; work on 2026-11-14 | Does not count |
| A licence expiring on 2026-11-20 | Counts for work on 2026-11-19, not for work on 2026-11-21 |
| A qualification HR rejected | Does not count |
| A certificate expiring in 90 days | Counts; the person and HR get a reminder |

## Applies to

- [E-F9-12 Qualification](../data/e-f09-12-certification.md)
- [E-F9-29 Degree](../data/e-f09-29-degree.md)
- [E-F9-31 Attribute reading](../data/e-f09-31-attribute-reading.md)
- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [UC-F9-38](../use-cases/13-keep-qualifications/uc-f09-38-record-degrees-and-qualifications.md)
- [UC-F9-39](../use-cases/13-keep-qualifications/uc-f09-39-read-documents-and-verify.md)

## Exceptions

None.

## Configurable

The reminder delay (Proposed: 90 days). Not whether an unverified or expired attribute counts.

## Open questions

None.

---

⬅️ [BR-F9-26 Legal requirements are never relaxed](br-f09-26-legal-requirements-never-relaxed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-28 HR confirms every AI reading](br-f09-28-hr-confirms-every-ai-reading.md)
