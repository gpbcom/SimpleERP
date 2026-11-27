🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-13 External data warning

# 📏 BR-F1-13 External data warning

**Status:** ✅ specified

## Statement

Before a connection to an outside MCP server or A2A agent is turned on, the administrator sees that data sent to it
leaves the server, and the list of its tools, and confirms.

## Why

SimpleERP is self-hosted by default; leaving it is an informed choice. See
[D79](../../../06-decisions/f01-administration/d79-any-external-tool-with-warning.md).

Legal values from the France country pack:
[CR-FR-049 Processors and transfers outside the EU](../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md).

## Examples

| Case | Result |
|---|---|
| Connect a GitHub MCP server | Warning, its 40 tools listed, "Turn on" after confirmation |
| A server on the company's own network | Same review, the warning says it stays inside the network |
| The server adds tools later | New tools stay off until the administrator reviews them |

## Applies to

- [UC-F1-07](../use-cases/05-connect-an-external-tool/uc-f01-07-connect-an-external-mcp-server-or-a2a-agent.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-12 Record rule kinds](br-f01-12-record-rule-kinds.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-14 Confirming outside changes](br-f01-14-confirming-outside-changes.md)
