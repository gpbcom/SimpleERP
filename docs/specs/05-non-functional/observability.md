🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 🔭 Observability

# 🔭 Observability

**Status:** ✅ specified

## Requirement

- **Logs, metrics and traces on one stack**
  ([D416](../06-decisions/technical/d416-observability-design.md)): logs to Loki, metrics to Prometheus, traces through
  OpenTelemetry to Tempo, dashboards and alerts in Grafana; the same stack, smaller, on the laptop profile
  ([observability design](../../technical/operations/observability.md)).
- **Every signal is tagged** with the service, the company (as an opaque id) and the request; personal data and secrets
  are masked at collection ([observability design](../../technical/operations/observability.md)).
- **Service level objectives with error budgets**, per user journey (sign-in, invoicing, till, assistant); alerts on the
  symptoms users feel, routed to on-call; targets per hosted plan, for example 99.9 % monthly availability for
  business plans ([D416](../06-decisions/technical/d416-observability-design.md),
  [observability design](../../technical/operations/observability.md)). Every technical capability's operations page
  names its logs, metrics and traces with SLOs, for example
  [T2 Operations](../03-technical/t02-identity-and-access/operations.md) and
  [T7 Operations](../03-technical/t07-ai-providers-and-models/operations.md).
- **What customers see** ([D416](../06-decisions/technical/d416-observability-design.md)): a public status page for the
  hosted edition ([UC-F20-10](../02-functional/f20-hosted-support-assistant/use-cases/03-incidents/uc-f20-10-handle-a-wide-incident-with-a-status-page.md),
  [S-F20-10](../02-functional/f20-hosted-support-assistant/screens/03-incidents/s-f20-10-status-page.md)); each company
  sees its own service health, usage and incidents in the app, and an IT provider its clients'; raw logs stay with the
  operators and the hosted support assistant (F20).
- **Every AI call is traced** ([D416](../06-decisions/technical/d416-observability-design.md),
  [D417](../06-decisions/technical/d417-ai-operations-design.md)) with its model, prompt template version, tools used,
  tokens, cost, latency and outcome, its inputs masked, linked to the user's request; the quality scores of the
  evaluations and the users' ratings sit on the same dashboards. AI and agent actions also record the model, the tools
  and the confirmation in the audit trail
  ([REQ-T03-04](../03-technical/t03-audit-trail/requirements/req-t03-04-ai-actions.md)).
- **Operations signals are not the audit trail**: the audit trail (T3) records who did what to which record, while the
  metrics and logs serve operations ([T3 Audit trail](../03-technical/t03-audit-trail/README.md)). A company may stream
  its audit events to its own security tool (SIEM)
  ([UC-F1-22](../02-functional/f01-administration/use-cases/13-security-and-audit/uc-f01-22-search-the-audit-trail-and-export-it-to-a-siem.md)).
- **Retention**: logs, metrics and traces are kept 13 months
  ([Data retention](data-retention.md), [D572](../06-decisions/foundations/d572-proposals-confirmed-in-bulk.md)).

## Measures

- The performance targets the SLOs watch are those of [Performance](performance.md)
  ([D408](../06-decisions/technical/d408-performance-and-profiles.md)): 95 % of screens within 1 second, API calls 95 %
  within 300 ms, reports within 5 seconds or in the background.
- Each technical capability's operations page lists its monitoring
  ([D416](../06-decisions/technical/d416-observability-design.md)); the observability chapter is built from step 2 of the
  [roadmap](../00-vision/roadmap/roadmap.md), the platform.

## Open questions

None.

---

⬅️ [Data retention](data-retention.md) · ⬆️ [Up](README.md) · ➡️ [Localisation](localisation.md)
