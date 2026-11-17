🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-14 Timeline

# 🧩 C-14 Timeline

**Status:** 🔄 waiting for the owner

## Purpose

Shows events in time order: the versions of a configuration, the actions of a provider's session, the lines of a live
transcript, a record's history.

## Anatomy

```text
o 10 Nov 15:02  Marie Dupont   Published 3 changes     [Roll back]
|
o 09 Nov 11:40  Claire Martin  Published 1 change      [Roll back]
```

A line with one mark per event; each event has its date and time, who, what, and an optional action.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-14-timeline-desktop-light.png) | ![Variants and states, dark](../images/c-14-timeline-desktop-dark.png) |

## Variants

- **History:** newest first, as on
  [S-F2-10 Publish and versions](../../../02-functional/f02-no-code-configuration/screens/05-publish-and-roll-back/s-f02-10-publish-and-versions.md)
  and
  [S-F1-11 Provider access log](../../../02-functional/f01-administration/screens/08-provider-and-client-companies/s-f01-11-provider-access-log.md).
- **Live:** oldest first, new events added at the bottom while it runs, as on
  [S-F4-02 Live transcript](../../../02-functional/f04-meetings/screens/01-record-an-online-meeting/s-f04-02-live-transcript.md).
- **Grouped:** (Proposed) events under day headings when there are many.

## States

Loading (Proposed: skeleton events), empty ([C-10 Empty state](c-10-empty-state.md): "Your provider has not entered
simple-ERP."), live (marked as live), more to load (Proposed: "Show earlier"), error
([error message pattern](../patterns/error-messages.md)). The live mark is drawn on
[S-F1-11 Provider access log](../../../02-functional/f01-administration/screens/08-provider-and-client-companies/s-f01-11-provider-access-log.md).

## Tokens

`color-border` for the line, `color-primary` for the marks, `color-success`, `color-warning` or `color-error` for events
of those kinds with an icon; `font-caption` for times, `font-code` for IDs
([Typography](../../visual-identity/typography.md)).

## Accessibility

- An ordered list; each event reads in full ("10 Nov 15:02, Marie Dupont published 3 changes").
- A live timeline announces new events politely and never moves the focus.
- Marks such as plus and tilde are spelt out for screen readers, as on
  [S-F2-10 Publish and versions](../../../02-functional/f02-no-code-configuration/screens/05-publish-and-roll-back/s-f02-10-publish-and-versions.md).

## Do and don't

- Do show who did what and when, with real names and values.
- Do show times in the user's time zone (Proposed).
- Don't hide events the user may see; don't show those they may not
  ([D12](../../../06-decisions/foundations/d12-permissions-model.md)).

## Used in

[S-F1-11 Provider access log](../../../02-functional/f01-administration/screens/08-provider-and-client-companies/s-f01-11-provider-access-log.md),
[S-F2-08 Rule editor](../../../02-functional/f02-no-code-configuration/screens/03-automate-with-a-rule/s-f02-08-rule-editor.md),
[S-F2-10 Publish and versions](../../../02-functional/f02-no-code-configuration/screens/05-publish-and-roll-back/s-f02-10-publish-and-versions.md)
and
[S-F4-02 Live transcript](../../../02-functional/f04-meetings/screens/01-record-an-online-meeting/s-f04-02-live-transcript.md).

## Open questions

None.

---

⬅️ [Stepper](c-13-stepper.md) · ⬆️ [Up](README.md) · ➡️ [Facet panel](c-15-facet-panel.md)
