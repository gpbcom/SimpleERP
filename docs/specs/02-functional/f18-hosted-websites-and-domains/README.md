🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) ›
🌐 F18 Hosted websites and domains (hosted edition)

# 🌐 F18 Hosted websites and domains (hosted edition)

**Status:** ✅ specified

Build step: 10. Hosted edition services.

## Summary

In the hosted edition, each customer's website built interactively from its ERP data and visual identity, with a contact
page and a careers page synchronised with LinkedIn and Indeed, its domain, DNS, certificates and mail records managed
through the providers' APIs, and every publication tested and approved first
([D385](../../06-decisions/f18-hosted-websites-and-domains/d385-hosted-websites-coverage.md),
[D386](../../06-decisions/f18-hosted-websites-and-domains/d386-website-publication-gate.md)). A closed hosted service
around the open product ([D388](../../06-decisions/vision/d388-hosted-edition-open-core.md)).

## Scope

- **Build:** the guided builder, identity, pages from ERP data, contact, legal pages, languages, the shop link.
- **Careers:** the careers page, LinkedIn and Indeed postings, one pipeline of applications.
- **Domain:** buy, transfer or connect; DNS zone, certificates, mail records.
- **Publish:** private preview, automatic checks, the customer's yes, rollback.
- **Run:** audience, uptime, renewals.
- **Content and care:** a blog fed by F5 posts, sector page templates, search basics, redirects of an old site,
  mailboxes on the domain, spam protection of forms, daily backups and restore (D475).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U12 Marketing](../../01-users/personas/u12-marketing.md),
[U06 HR](../../01-users/personas/u06-hr.md), [U07 Administrator](../../01-users/personas/u07-administrator.md),
[U48 Hosting engineer](../../01-users/personas/u48-hosting-engineer.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Out of scope

- Self-hosted installations: the open product has no site builder (D388).
- The online shop itself: F11.
- Recruiting beyond applications: F9.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (registrars, DNS providers,
  LinkedIn, Indeed)
- [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md) (the only way into the product, D388)
- [T10 Translations and notifications](../../03-technical/t10-translations-and-notifications/README.md)
- [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md)

## Build step

Step 10, Hosted edition services, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the
specifications hold.

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
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Competitive analysis](../f17-competitive-analysis/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Feature factory (hosted edition)](../f19-feature-factory/README.md)
