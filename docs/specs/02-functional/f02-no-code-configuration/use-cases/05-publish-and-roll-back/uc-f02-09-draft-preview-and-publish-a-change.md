🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F2-05 Publish and roll back](README.md) › 📝 UC-F2-09 Draft, preview and publish a change

# 📝 UC-F2-09 Draft, preview and publish a change

**Status:** ✅ specified

## Summary

Every configuration change is a draft, previewed with real data, then published by its configurator; administrators are
told.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96, D98)

## Goal

Users never see a half-made change, and every change can be undone.

## Trigger

Any change of UC-F2-01 to UC-F2-08.

## Frequency

With every change.

## Preconditions

A draft exists.

## Postconditions

A new configuration version is live; the administrators have its summary; the previous version is kept (UC-F2-10).

## Main flow

1. The configurator opens Publish.
2. SimpleERP lists the draft's changes in plain words ("Field Vehicle added to Quotes").
3. They preview as any role, on real records, on desktop and phone.
4. They publish ([D131](../../../../06-decisions/f02-no-code-configuration/d131-configurators-publish.md)); the new
   version is live within seconds.
5. The administrators get a notification with the summary.

## Alternative flows

- Discard the draft.
- Two configurators' drafts on the same record type: the second one sees the first's draft and publishes on top of it.

## Error flows

- A draft that breaks a rule (a required field missing from a layout, a status no transition reaches):
  publishing is refused, each problem explained in plain words.

## Business rules

- [BR-F2-07 Layout is not security](../../business-rules/br-f02-07-layout-is-not-security.md)

## Entities

- [E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md)
- [E-F2-26 Configuration draft](../../data/e-f02-26-configuration-draft.md)

## Permissions

The administrator; the Configurator role, for their own drafts.

## Notifications

The administrators, with the summary (D131).

## Audit events

Version published: who, when, the list of changes.

## AI involvement

The AI assistant writes the summary of changes in plain words.

## API, MCP and A2A exposure

None.

## Screens

- [S-F2-10 Publish and versions](../../screens/05-publish-and-roll-back/s-f02-10-publish-and-versions.md)

## Flowchart

See [FL-F2-05 Publish and roll back](../../flows/fl-f02-05-publish-and-roll-back.md#flowchart).

## Sequence diagram

See [UC-F2-10](uc-f02-10-roll-a-configuration-back.md#sequence-diagram).

## Acceptance criteria

1. **Given** a draft **when** not published **then** no user sees it.
2. **Given** a published version **when** live **then** the administrators get its summary.
3. **Given** a draft with a problem **when** published **then** it is refused with each problem in plain words.

## Non-functional notes

A published version is live within 5 seconds on every channel.

## Regulatory references

None.

## Related use cases

UC-F2-10; UC-F2-01 to UC-F2-08.

- [UC-F2-23 See the impact of a change before publishing](../10-change-safely/uc-f02-23-see-the-impact-of-a-change-before-publishing.md)

- [UC-F2-24 Test rules and workflows with test cases](../10-change-safely/uc-f02-24-test-rules-and-workflows-with-test-cases.md)
- [UC-F2-30 Set up a request type](../12-set-up-request-types/uc-f02-30-set-up-a-request-type.md)

## Open questions

None.

---

⬅️ [UC-F2-08 Design a visual workflow](../04-design-a-visual-workflow/uc-f02-08-design-a-visual-workflow.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F2-10 Roll a configuration back](uc-f02-10-roll-a-configuration-back.md)
