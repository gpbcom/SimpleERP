🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛡️ F1 Administration

# 🛡️ F1 Administration

**Status:** ✅ specified

Build step: 2. Platform.

## Summary

The screens an administrator uses to set simple-ERP up and keep it running: the company and its sites, the users, the
roles and record rules, and the connections and AI settings. See
[D52](../../06-decisions/f01-administration/d52-f1-scope.md).

## Scope

- **Company and sites setup:** legal identity, logo, currency, fiscal year, and sites with their address and hours,
  stock, staff and manager ([D36](../../06-decisions/f07-purchasing-and-stock/d36-what-a-location-holds.md)). A
  brand-new company starts with a guided setup and a sector pack, which can be left and resumed
  ([D54](../../06-decisions/f01-administration/d54-guided-setup.md)).
- **Users lifecycle:** invite, change role or site, deactivate, offboard, reset two-factor. Accounts come from an email
  invitation or from single sign-on with automatic creation
  ([D55](../../06-decisions/technical/d55-user-onboarding.md)).
- **Roles and record rules editor:** copy and edit the ready-made roles, and add record rules such as "own customers
  only" or "own site only" ([D12](../../06-decisions/foundations/d12-permissions-model.md)).
- **Connections and AI settings:** external MCP servers and A2A agents
  ([D6](../../06-decisions/foundations/d06-mcp-and-a2a-both-ways.md)), the AI provider of each feature
  ([D5](../../06-decisions/foundations/d05-where-the-ai-runs.md)), single sign-on
  ([D13](../../06-decisions/foundations/d13-sign-in.md)), email sending.
- **Provider access:** an IT provider administrator can enter any client company at any time
  ([D53](../../06-decisions/ux/d53-provider-access-always.md)).
- **Gaps and improvements round ([D458](../../06-decisions/f01-administration/d458-f01-gaps-and-improvements.md),
  2026-11-12):** automatic provisioning and bulk invites, site-scoped administration, approval delegation, the manager's
  team page, access review campaigns, portal accounts, API tokens and service accounts, security policies, audit search
  with SIEM export, and closing a company with a full export.

## Personas

- [U07 Administrator](../../01-users/personas/u07-administrator.md)
- [U11 IT provider administrator](../../01-users/personas/u11-provider-admin.md)
- [U13 Owner](../../01-users/personas/u13-owner.md), who administers in a small company
- [U01 Employee](../../01-users/personas/u01-employee.md)
- [U02 Manager](../../01-users/personas/u02-manager.md)
- [U23 Store manager](../../01-users/personas/u23-store-manager.md)
- [U09 Customer](../../01-users/personas/u09-customer.md)
- [U10 Supplier](../../01-users/personas/u10-supplier.md)

## Out of scope

- Bulk import of users and self sign-up ([D55](../../06-decisions/technical/d55-user-onboarding.md)).
- No-code configuration of forms, fields and workflows: [F2](../f02-no-code-configuration/README.md).
- The plugin store: [F14](../f14-plugin-store/README.md).

## Technical capabilities used

- [T1 Companies and data isolation](../../03-technical/t01-companies-and-data-isolation/README.md)
- [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T10 Translations and notifications](../../03-technical/t10-translations-and-notifications/README.md)

## Build step

Step 2, Platform, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
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

⬆️ [Up](../README.md) · ➡️ [No-code configuration](../f02-no-code-configuration/README.md)
