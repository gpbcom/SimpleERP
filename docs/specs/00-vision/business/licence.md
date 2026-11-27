🏠 [Specs](../../README.md) › 🎯 [Vision](../README.md) › 💼 [Business](README.md) › 📃 Licence

# 📃 Licence

**Status:** ✅ specified

## Licence

AGPL-3.0.

## Why

SimpleERP must be truly open, with no paid edition holding back features, and a product of its own. See
[D9](../../06-decisions/foundations/d09-licence-agpl.md).

The services that only the hosted edition offers are named: F18 websites and domains, F19 the feature factory, F20 the
support assistant and F25 the DevOps agents
([D447](../../06-decisions/vision/d447-country-pack-updates-free-hosted-only-named.md)); every ERP feature, country-pack
updates included, stays open and free.

## Consequences

- 🌐 **Network use:** whoever runs a modified SimpleERP for others, an IT provider for example, offers its users the
  modified source.
- 🧩 **Plugins and sector packs:** AGPL-3.0 too ([D377](../../06-decisions/vision/d377-plugins-agpl-only.md)); a paid
  plugin sells support, updates and hosting, with no enforced licence check and no seats; a lawyer confirms before
  launch ([D443](../../06-decisions/vision/d443-paid-plugins-sell-support-updates-hosting.md)).
- ✍️ **Contributions:** DCO sign-off, no copyright transfer, so no relicensing and no dual licence
  ([D376](../../06-decisions/vision/d376-contributions-dco-then-foundation.md)).
- 📦 **Dependencies:** compatible with AGPL-3.0 only.
- 🔒 **Hosted edition:** the publisher's hosting services (websites and domains, the feature factory, the support
  assistant, the DevOps agents) are separate, closed programs that reach SimpleERP through its public API and MCP and,
  to run the hosting, through Kubernetes' own interfaces as D388's consequences list them, never
  linking or copying AGPL code; a lawyer confirms the boundary before launch
  ([D388](../../06-decisions/vision/d388-hosted-edition-open-core.md)).
- 🏭 **Generated features:** the plugins the feature factory writes are AGPL-3.0 like every plugin
  ([D389](../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md)).

---

⬅️ [Business model](business-model.md) · ⬆️ [Up](README.md) · ➡️ [Country rules](country-rules.md)
