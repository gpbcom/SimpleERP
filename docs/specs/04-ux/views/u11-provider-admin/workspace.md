🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🖧 [IT provider administrator: app shell and home](README.md) › 🧰 U11 IT provider administrator: workspace

# 🧰 U11 IT provider administrator: workspace

**Status:** ✅ specified

## Purpose

The views [U11 IT provider administrator](../../../01-users/personas/u11-provider-admin.md) works with, embedded on
their [home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators and the planner roles), else
"Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F1-L01 Companies](../../../02-functional/f01-administration/screens/00-lists/s-f01-l01-companies.md) | Administration | All | UC-F1-10, UC-F1-23 |
| [S-F1-L03 Users](../../../02-functional/f01-administration/screens/00-lists/s-f01-l03-users.md) | Administration | All | UC-F1-13, UC-F1-14 |
| [S-F1-L04 Invitations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l04-invitations.md) | Administration | Needs attention | UC-F1-14 |
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | All | UC-F1-20 |
| [S-F1-L10 Single sign-on settings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l10-single-sign-on-settings.md) | Administration | All | UC-F1-13 |
| [S-F1-L11 Company templates](../../../02-functional/f01-administration/screens/00-lists/s-f01-l11-company-templates.md) | Administration | Needs attention | UC-F1-10 |
| [S-F1-L12 Provider sessions](../../../02-functional/f01-administration/screens/00-lists/s-f01-l12-provider-sessions.md) | Administration | Open: Live | UC-F1-11 |
| [S-F1-L14 Provisioning settings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l14-provisioning-settings.md) | Administration | All | UC-F1-13 |
| [S-F1-L15 Bulk invitation batches](../../../02-functional/f01-administration/screens/00-lists/s-f01-l15-bulk-invitation-batches.md) | Administration | Needs attention | UC-F1-14 |
| [S-F1-L18 API tokens](../../../02-functional/f01-administration/screens/00-lists/s-f01-l18-api-tokens.md) | Administration | Needs attention | UC-F1-20 |
| [S-F1-L21 Company closings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l21-company-closings.md) | Administration | Needs attention | UC-F1-23 |
| [S-F2-L08 Automation rules](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l08-automation-rules.md) | No-code configuration | Needs attention | UC-F2-31 |
| [S-F2-L09 Workflows](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l09-workflows.md) | No-code configuration | Needs attention | UC-F2-31 |
| [S-F2-L10 Configuration versions](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l10-configuration-versions.md) | No-code configuration | All | UC-F2-25 |
| [S-F2-L11 Configuration packs](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l11-configuration-packs.md) | No-code configuration | All | UC-F2-11, UC-F2-25 |
| [S-F2-L26 Configuration drafts](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l26-configuration-drafts.md) | No-code configuration | All | UC-F2-11 |
| [S-F2-L30 Script steps](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l30-script-steps.md) | No-code configuration | Needs attention | UC-F2-31 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F8-L27 FEC files](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l27-fec-files.md) | Accounting | All | UC-F1-23 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F14-L01 Store listings](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l01-store-listings.md) | Plugin store | Open: New, Complete, Refused | UC-F14-19, UC-F14-23 |
| [S-F14-L03 Plugin versions](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l03-plugin-versions.md) | Plugin store | All | UC-F14-10 |
| [S-F14-L06 Plugin reviews](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l06-plugin-reviews.md) | Plugin store | All | UC-F14-19 |
| [S-F14-L07 Plugin check reports](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l07-plugin-check-reports.md) | Plugin store | All | UC-F14-10, UC-F14-21 |
| [S-F14-L09 Seller reports](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l09-seller-reports.md) | Plugin store | All | UC-F14-14 |
| [S-F14-L10 Private stores](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l10-private-stores.md) | Plugin store | All | UC-F14-15 |
| [S-F14-L11 Plugin withdrawals](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l11-plugin-withdrawals.md) | Plugin store | All | UC-F14-16 |
| [S-F14-L12 Refunds](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l12-refunds.md) | Plugin store | All | UC-F14-17 |
| [S-F14-L14 Software bill of materials](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l14-software-bill-of-materials.md) | Plugin store | All | UC-F14-21 |
| [S-F14-L16 Maintainer transfers](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l16-maintainer-transfers.md) | Plugin store | Open: Asked, Approved, Refused | UC-F14-23 |
| [S-F14-L17 Rollouts](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l17-rollouts.md) | Plugin store | Open: Beta, Running, Paused | UC-F14-25 |
| [S-F14-L21 Plugin security reviews](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l21-plugin-security-reviews.md) | Plugin store | All | UC-F14-10, UC-F14-23 |
| [S-F21-L03 Set-up templates](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l03-set-up-templates.md) | Onboarding and module activation | All | UC-F21-19 |
| [S-F21-L12 Provider set-ups](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l12-provider-set-ups.md) | Onboarding and module activation | All | UC-F21-19 |
| [S-F22-L09 Allocation rules](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l09-allocation-rules.md) | Unified platform cost management | All | UC-F22-16 |
| [S-F22-L13 Usage invoices](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l13-usage-invoices.md) | Unified platform cost management | All | UC-F22-16 |
| [S-F22-L17 Re-billing rules](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l17-re-billing-rules.md) | Unified platform cost management | All | UC-F22-16, UC-F22-25 |
| [S-F22-L18 Client usage statements](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l18-client-usage-statements.md) | Unified platform cost management | Needs attention | UC-F22-16, UC-F22-26 |
| [S-F24-L02 Tool connections](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l02-tool-connections.md) | Integrations hub | All | UC-F24-28 |
| [S-F24-L06 Sync jobs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l06-sync-jobs.md) | Integrations hub | All | UC-F24-30 |
| [S-F24-L07 Field mappings](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l07-field-mappings.md) | Integrations hub | All | UC-F24-28 |
| [S-F24-L08 Sync log entries](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l08-sync-log-entries.md) | Integrations hub | All | UC-F24-30 |
| [S-F24-L17 Connector drafts](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l17-connector-drafts.md) | Integrations hub | Needs attention | UC-F24-28 |
| [S-F24-L18 Export pipelines](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l18-export-pipelines.md) | Integrations hub | Needs attention | UC-F24-30 |
| [S-SC09-L13 Certified modules](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l13-certified-modules.md) | Health practices | Needs attention | UC-SC09-19 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Plugin store](../../../02-functional/f14-plugin-store/screens/00-lists/README.md),
[Unified platform cost management](../../../02-functional/f22-unified-cost-management/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U11 | desktop | ![Workspace, U11, light](mockups/workspace-desktop-light.png) | ![Workspace, U11, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U11 | phone | ![Workspace, U11, light](mockups/workspace-phone-light.png) | ![Workspace, U11, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
