🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-19 Personal connections for allowed services

# 📏 BR-F3-19 Personal connections for allowed services

**Status:** ✅ specified

## Statement

Besides company connections, a user may connect their own account (their calendar, their mailbox) by signing in to it,
only for the services the administrator allows; a personal connection is used only for that user, and the user can
remove it at any time.

## Why

Personal tools help, within the company's limits. See
[D171](../../../06-decisions/f03-assistant/d171-personal-connections.md).

## Examples

| Case | Result |
|---|---|
| Allowed: Google Calendar; Marie connects hers | The AI assistant can read and, with confirmation, add to Marie's calendar |
| Not allowed: Dropbox | Not offered in My connections |
| Marie leaves the company | Her personal connections are removed with her account |

## Applies to

- [UC-F3-06](../use-cases/06-use-an-outside-tool/uc-f03-06-use-an-outside-tool-through-the-assistant.md)

## Exceptions

None.

## Configurable

Yes: the list of allowed services, by the administrator.

## Open questions

None.

---

⬅️ [BR-F3-18 Outside results are marked](br-f03-18-outside-results-are-marked.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-20 Outside call caps](br-f03-20-outside-call-caps.md)
