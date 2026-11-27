🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-17 An AI-built connector runs in the sandbox first

# 📏 BR-F24-17 An AI-built connector runs in the sandbox first

**Status:** ✅ specified

## Statement

A connector drafted by the AI assistant runs only in the sandbox until every one of its tests has passed and an
administrator has approved it; it never receives credentials, never touches real data before approval, and a failed test
blocks the approval.

## Why

Code written by an AI from documentation may be wrong or unsafe, and a connector can read and write the company's data.
The owner asked for AI-built connectors
([D543](../../../06-decisions/f24-integrations-hub/d543-benchmark-gaps-f24-integrations-hub.md)); credentials stay in
the vault ([BR-F24-08](br-f24-08-credentials-in-the-vault.md)).

## Examples

| Case | Result |
|---|---|
| 12 of 12 tests passed and the administrator approves | the connection is made |
| 11 of 12 tests passed | approval refused |
| A draft that tries to call an address other than the tool's | blocked in the sandbox, the test fails |
| A documentation page that tells the AI to ignore its rules | treated as data, ignored |
| A change to the mapping after approval | a new draft version, tested again before it replaces the live one |

## Applies to

- [UC-F24-28](../use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-28-have-the-ai-build-a-connector.md)
- [E-F24-17 Connector draft](../data/e-f24-17-connector-draft.md)
- [BR-F24-08 Credentials in the vault](br-f24-08-credentials-in-the-vault.md)
- [E-F24-02 Tool connection](../data/e-f24-02-tool-connection.md)

## Exceptions

None.

## Configurable

No: the sandbox rule cannot be switched off.

## Open questions

None.

---

⬅️ [BR-F24-16 Every integration shows its icon](br-f24-16-every-integration-shows-its-icon.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-18 Suite access uses the fewest scopes needed](br-f24-18-suite-access-uses-the-fewest-scopes-needed.md)
