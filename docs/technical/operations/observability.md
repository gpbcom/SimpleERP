# Observability

Logs, metrics and dashboards (Loki, Prometheus, Grafana), alerts. Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Signals (D416).** Logs to Loki, metrics to Prometheus, traces through OpenTelemetry to Tempo, dashboards and alerts in
Grafana; every signal tagged with the service, the company (as an opaque id) and the request; personal data and secrets
masked at collection; the same stack, smaller, on the laptop profile.

**What customers see.** A public status page for the hosted edition; each company sees its own service health, usage and
incidents in the app; IT providers see their clients'; raw logs stay with operators and the hosted support assistant
(F20).

**Service levels.** Service level objectives per user journey (sign-in, invoicing, till, assistant) with error budgets;
alerts on symptoms users feel, routed to on-call ([DevOps](devops.md)); targets per hosted plan, for example 99.9 %
monthly availability for business plans.

**AI.** Each AI call is traced with its model, prompt template version, tools used, tokens, cost, latency and outcome
(inputs masked), linked to the user's request; quality scores from evaluations and user ratings sit on the same
dashboards.

Decided in [D416](../../specs/06-decisions/technical/d416-observability-design.md).

Last reviewed: 2026-11-12 (GH-2)
