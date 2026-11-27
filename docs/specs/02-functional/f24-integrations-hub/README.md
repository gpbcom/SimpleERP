🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🔌 F24 Integrations hub

# 🔌 F24 Integrations hub

**Status:** ✅ specified

Build step: 2. Platform (Proposed).

## Summary

Every outside tool connected in as few steps as possible: the European open-source office suites first (openDesk and La
Suite numérique, with full read and write access to their components), the 50 leading ATS and CRM by default, then the
rest of the catalogue; every action usable from the AI assistant
([D427](../../06-decisions/f24-integrations-hub/d427-integrations-hub-coverage.md),
[D428](../../06-decisions/f24-integrations-hub/d428-office-suites-full-api.md),
[D429](../../06-decisions/f24-integrations-hub/d429-fewest-steps-for-every-connector.md),
[D430](../../06-decisions/f24-integrations-hub/d430-fifty-ats-and-crm.md)).

## Scope

- **Catalogue and connection:** categories, the fewest steps, rights and costs.
- **Office suites:** [openDesk](https://www.opendesk.eu/de/produkt) (Nubus and Keycloak, Nextcloud, Collabora, OX App
  Suite, Element and Matrix, Jitsi, OpenProject, XWiki, CryptPad, Notes; see its
  [components](https://docs.opendesk.eu/operations/introduction)) and
  [La Suite numérique](https://lasuite.numerique.gouv.fr/) (ProConnect, Docs, Fichiers, Visio, Tchap, Grist, Messagerie,
  France Transfert).
- **CRM and ATS:** the default 50 (BR-F24-05), two-way sync, mapping, history import.
- **Run:** the AI assistant's actions, health, API changes, disconnection, the yearly review, requests.
- **Business tools and icons:** banks, payments, shops, accounting, payroll and HR (Silae, PayFit, Lucca), carriers, the
  e-invoicing platform (D454), automation tools (n8n, Make, Zapier), employees' own connections, and every integration's
  icon in the web interface (D481).

## Personas

[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U01 Employee](../../01-users/personas/u01-employee.md),
[U16 Office worker](../../01-users/personas/u16-office-worker.md),
[U02 Manager](../../01-users/personas/u02-manager.md), [U03 Sales](../../01-users/personas/u03-sales.md),
[U06 HR](../../01-users/personas/u06-hr.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U47 SimpleERP maintainer](../../01-users/personas/u47-simpleerp-maintainer.md).

## Out of scope

- The connector contract and the scraper factory: T12.
- The suites' own administration.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md)
- [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md) (single sign-on)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md) (assistant tools)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)

## Build step

Step 2, Platform, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)) (Proposed): in V1, like everything the
specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [What-if simulation and impact](../f23-what-if-simulation/README.md) · ⬆️ [Up](../README.md) ·
➡️ [DevOps agents (hosted edition)](../f25-devops-agents/README.md)
