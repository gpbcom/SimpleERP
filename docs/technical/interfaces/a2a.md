# A2A

SimpleERP as an A2A agent and as a caller of outside agents: skills, discovery, trust, rights (T6). Nothing of the
target is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**SimpleERP as an A2A agent (D412).** Agent cards published per business domain (sales, purchasing, accounting, HR,
support, what-if), each listing skills built from the specified use cases. Each A2A agent is a pod behind a Kubernetes
Service, autoscaled by KEDA, like the MCP servers. Tasks run with the caller's OAuth token and rights; long tasks are
streamed and resumable on the workflow engine.

**Calling outside agents.** Administrators allow-list outside agents per role, by their agent card; a delegated task
carries only the rights it needs, its budget (F22) and a time limit; results are untrusted content; every exchange is
audited.

**Trust.** Agent cards are signed; every call uses OAuth 2; known partner agents (an IT provider's platform, the hosted
edition's services) also use mutual TLS; no agent acts across companies.

**One set of rules.** The in-app assistant (F3), support agents (F16), the feature factory (F19), the hosted support
assistant (F20), the what-if assistant (F23) and outside agents all act through the same MCP tools and A2A skills, under
the same rights, confirmations, budgets and audit.

Decided in [D412](../../specs/06-decisions/technical/d412-a2a-agents.md).

Last reviewed: 2026-11-12 (GH-2)
