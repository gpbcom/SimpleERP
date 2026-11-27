🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 👥 [HR and projects](README.md) ›
🔗 Integrations

# 🔗 Integrations

**Status:** ✅ specified

## API

Employees, time off, attendance, timesheets, projects through the API (T5), within roles.

## Webhooks

Employee hired or left, time off approved, timesheet validated.

## MCP tools

Every F9 action as an AI assistant tool within roles (BR-F3-34).

## A2A skills

None in v1.

## External services

URSSAF (DPAE), job boards and sourcing providers, LinkedIn, e-signature, calendars (BR-F4-17), badge and RFID readers;
through T12.

Unipile, an F24 connector, reaches LinkedIn for sourcing: search, invitations and messages on each HR user's own
account, linked on Unipile's hosted sign-in page; its API key stays in the secret store (D518, UC-F9-40, UC-F24-02).
The search is the one the account offers, as Unipile reports it, or Recruiter or Sales Navigator when the account has
one ([D571](../../06-decisions/f09-hr-and-projects/d571-linkedin-sourcing-uses-the-users-search.md)). Each invitation
and message is prepared and goes when the HR user clicks Send; automatic sending is an option the administrator turns
on for the company ([D570](../../06-decisions/f09-hr-and-projects/d570-linkedin-sending-prepared-by-default.md)).

## Open questions

None.

---

⬅️ [Reports](reports.md) · ⬆️ [Up](README.md) · ➡️ [AI](ai.md)
