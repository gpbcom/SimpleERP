# MCP

simple-ERP as an MCP server and as an MCP client: tools, rights, confirmations, transport, security (T6). Nothing of the
target is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**simple-ERP as an MCP server (D411).** One public MCP endpoint per install over Streamable HTTP, with OAuth 2.1 sign-in
as the MCP specification requires, routing to one MCP server per business domain. Each MCP server is a pod behind a
Kubernetes Service, autoscaled by KEDA; the same images run under Docker Compose on the laptop profile. Tools are
generated from each service's OpenAPI and filtered by the user's company, modules switched on and rights; resources
expose records and documents; prompts cover common tasks.

**Confirmations.** Read tools run directly; write tools ask the user's confirmation (MCP elicitation) unless the user
pre-approved that tool for a session; deletions, payments, legal sendings and anything irreversible are always
confirmed; every call is audited with its caller (T3). The in-app assistant follows the same rules.

**simple-ERP as an MCP client.** Administrators add remote MCP servers (HTTP) per role (D79, D80); local stdio servers
run only in sandboxed containers; credentials sit in the vault; outside servers' outputs are untrusted content, never
instructions; calls are metered (F22).

**Many tools (TC-07).** Tools are grouped by module and loaded on demand through a tool-search tool, so that a model
sees only the tools a request needs; each tool's description is generated and tested.

Decided in [D411](../../specs/06-decisions/technical/d411-mcp-server-and-client.md).

Last reviewed: 2026-11-12 (GH-2)
