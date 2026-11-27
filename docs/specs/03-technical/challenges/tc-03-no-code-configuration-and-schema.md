🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🔧 TC-03 No-code configuration against schema and upgrades

# 🔧 TC-03 No-code configuration against schema and upgrades

**Status:** ✅ listed for the technical interviews

## Challenge

Let business users add fields, statuses, forms, document templates and workflows, apply sector packs, and still upgrade
every company safely.

## Raised by

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)
- [F21 Onboarding and module activation](../../02-functional/f21-onboarding-and-modules/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)

## Why it is hard

- Custom fields must be searchable, reportable, importable, exportable and visible to the AI assistant like built-in
  ones.
- A workflow written by a user can loop, call outside systems or break when a field is renamed.
- Sixteen sector packs and each company's own settings must survive every upgrade.

## Already decided

- [D26](../../06-decisions/foundations/d26-technical-and-functional-capabilities.md) Technical and functional
  capabilities

## Options to weigh

- Custom fields as typed columns, as a document column (JSON), or as separate rows.
- Workflows on a durable workflow engine, or as simple event rules.
- Configuration exported and versioned as files, so that it can be tested and moved between environments.

## Settled in

- 19c Storage ([chapter](../../../technical/data/storage.md))
- 19e Configuration ([chapter](../../../technical/architecture/configuration.md))
- 19k Backups, recovery and upgrades ([chapter](../../../technical/operations/operations.md))
- Then the technical capabilities: [T1 Companies and data isolation](../t01-companies-and-data-isolation/README.md),
  [T4 Plugin runtime](../t04-plugin-runtime/README.md).

## Questions for the interview

- How far may a workflow go: outside calls, loops, scheduled runs?
- Is configuration promoted from a test company to the live one?

---

⬅️ [TC-02 Modules switched on in one click, and a plugin-first core](tc-02-modules-and-plugins-at-runtime.md) ·
⬆️ [Up](README.md) · ➡️ [TC-04 The country pack as a versioned rule engine](tc-04-country-pack-rule-engine.md)
