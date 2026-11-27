🏠 [Specs](../../README.md) › 🎯 [Vision](../README.md) › 💼 [Business](README.md) › 💼 Business model

# 💼 Business model

**Status:** ✅ specified

## Revenue

Five sources around the free product ([D374](../../06-decisions/vision/d374-revenue-and-pricing.md)):

- ☁️ **Managed hosting:** the publisher hosts SimpleERP on European clouds only
  ([D375](../../06-decisions/vision/d375-managed-hosting-eu-only.md));
- 🛟 **Support subscriptions:** support and guaranteed updates (country-pack updates are free for everyone,
  [D447](../../06-decisions/vision/d447-country-pack-updates-free-hosted-only-named.md)), for self-hosting companies and
  IT providers;
- 🧩 **Plugin store share:** a share of paid plugins and sector packs (F14), which sell support, updates and hosting with
  no enforced licence check and no seats
  ([D443](../../06-decisions/vision/d443-paid-plugins-sell-support-updates-hosting.md)), since they are AGPL too
  ([D377](../../06-decisions/vision/d377-plugins-agpl-only.md));
- 🧑‍🔧 **Services:** installation, migration from other tools, training, custom development;
- 🏭 **Feature factory (hosted edition):** each feature built for a customer costs 300 EUR a month excluding VAT;
  a customer who promotes its feature to every hosted customer earns 50 % of what they pay, as a credit on its
  own invoices ([D390](../../06-decisions/f19-feature-factory/d390-feature-price-and-promotion-credit.md)).

The hosted edition's services (websites and domains, the feature factory, the support assistant, the DevOps agents) are
closed programs
of the publisher around the open product ([D388](../../06-decisions/vision/d388-hosted-edition-open-core.md)).

## Offers

| Offer | Who | Price |
|---|---|---|
| 🆓 Self-hosted | A company or an IT provider on its own servers | Free, AI included with its own models |
| ☁️ Hosted | A company hosted by the publisher in the EU, with its website, domain and support assistant (F18, F20) | Flat fee per company, plus metered AI use (meeting minutes, agent tickets): an included monthly quota of AI, connector and scraping usage, then units at a published price list, or the company's own keys ([D399](../../06-decisions/f22-unified-cost-management/d399-hosted-usage-billing.md)) |
| 🏭 Feature factory | Hosted companies | 300 EUR a month excluding VAT per feature; 50 % of a promoted feature's revenue credited to its author (D390) |
| 🛟 Support | Self-hosting companies, IT providers | Subscription |
| 🧑‍🔧 Services | Any customer | Quote |

No price per user and no price per app.

## Community

Contributors sign their commits (DCO) and keep their copyright
([D376](../../06-decisions/vision/d376-contributions-dco-then-foundation.md)). The project moves to a foundation or an
association once several companies stand behind it. The community writes plugins, sector packs, country packs and
translations.

---

⬆️ [Up](README.md) · ➡️ [Licence](licence.md)
