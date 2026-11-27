🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-18 Suite access uses the fewest scopes needed

# 📏 BR-F24-18 Suite access uses the fewest scopes needed

**Status:** ✅ specified

## Statement

A suite connection requests only the permissions that the enabled features need, read-only wherever a feature only
reads; each permission is shown with the feature that needs it, and disabling a feature revokes its permission.

## Why

A broad permission on a company's mailbox or files is a standing risk. The owner asked for the Google and Microsoft
suites ([D543](../../../06-decisions/f24-integrations-hub/d543-benchmark-gaps-f24-integrations-hub.md)); the open suites
already give read and write only within what the company grants ([BR-F24-03](br-f24-03-suites-full-read-write.md)).

## Examples

| Case | Result |
|---|---|
| Calendar feature only | calendar permissions, nothing for mail |
| A feature that only reads files | read access to the chosen folder, not to every file |
| A feature switched off | its permission revoked |
| A new feature that needs a new permission | the administrator approves it first |
| A permission nobody uses for 90 days | listed for review |

## Applies to

- [UC-F24-29](../use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-29-connect-google-workspace-or-microsoft-365.md)
- [BR-F24-03 Office suites: full read and write](br-f24-03-suites-full-read-write.md)

## Exceptions

None.

## Configurable

No: the list of permissions follows the features enabled.

## Open questions

None.

---

⬅️ [BR-F24-17](br-f24-17-an-ai-built-connector-runs-in-the-sandbox-first.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-19 Exports follow field rights and masking](br-f24-19-exports-follow-field-rights-and-masking.md)
