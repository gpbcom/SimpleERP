🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-14 Confirming outside changes

# 📏 BR-F1-14 Confirming outside changes

**Status:** ✅ specified

## Statement

When the AI assistant is about to call an external tool that changes something outside, it asks the user to confirm,
unless the connection is set as trusted; read-only calls never ask.

## Why

The administrator chooses per connection how much to trust it. See
[D81](../../../06-decisions/f01-administration/d81-confirmation-per-connection.md).

## Examples

| Connection setting | Call | Result |
|---|---|---|
| Always ask | Open a GitHub issue | The AI assistant shows the issue's text and target; the user approves |
| Trusted | Open a GitHub issue | Called at once; shown in the answer |
| Either | Read a Crunchbase company | Called at once |

## Applies to

- [UC-F1-07](../use-cases/05-connect-an-external-tool/uc-f01-07-connect-an-external-mcp-server-or-a2a-agent.md); the
  AI assistant (F3).

## Exceptions

None.

## Configurable

Yes: per connection. A new connection starts as "always ask".

## Open questions

None.

---

⬅️ [BR-F1-13 External data warning](br-f01-13-external-data-warning.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-15 Only what the request needs](br-f01-15-only-what-the-request-needs.md)
