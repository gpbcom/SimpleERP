🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-34 All capabilities via the AI assistant

# 📏 BR-F3-34 All capabilities via the AI assistant

**Status:** ✅ specified

## Statement

Every action a user can do in a capability's screens (F1 to F16) can also be triggered by asking the AI assistant: each
action is published as an AI assistant tool through the one action contract (REQ-T12-04). The AI assistant sees only the
tools the user's roles allow in the company (D12, F1's role matrix), with the same record rules and field visibility;
every call is checked again on the server, never trusted from the model. Reading needs no confirmation; changes are
shown and confirmed (D140, BR-F3-07 to BR-F3-10); irreversible or outward acts (validating an invoice, sending, paying,
signing, deleting) are prepared by the AI assistant and finished by the user's own click. A plugin (F14) that adds
actions publishes them as tools the same way.

The AI assistant is usable by everyone, every persona inside or outside the company, each for their own requests
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md), VC-7: "The AI assitant MUST be
usabe by everyone BUT disable the tools that could grant an Employee an unlegitimate access."). Its tools are filtered
by the user's rights: a tool that would read or change what the user's role may not, such as giving a role or an access
the user may not give, is disabled for that user: not offered, not callable, and refused on the server if called.

## Why

See [D276](../../../06-decisions/f03-assistant/d276-assistant-reaches-every-capability.md).

## Examples

| Case | Result |
|---|---|
| A buyer: "order 800 m of cable from Rexel" | A purchase order prepared, confirmation card, then created |
| A sales person: "create the user Paul" | Refused: creating users needs the administrator role |
| An accountant: "validate invoice F-2026-0512" | Prepared and opened; the accountant clicks Validate |
| A manager: "approve Léa's leave" | Shown, confirmed, approved |
| A new payroll plugin | Its actions appear as tools for the roles it grants |
| An employee: "give me the administrator role" | Refused: the role tool is disabled for the employee's role |
| A customer on the portal: "what do I owe?" | Answered from their own invoices only |

## Applies to

Every capability F1 to F16, and every plugin. Every persona uses the AI assistant within these tools (D519).

## Exceptions

Actions that a law or a rule reserves to a person's own act stay prepared, never done by the AI assistant (BR-F3-07).

## Configurable

Through roles only: what a role may do, it may ask the AI assistant to do.

## Open questions

None.

---

⬅️ [BR-F3-33 Usage reports never show content](br-f03-33-usage-reports-never-show-content.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-35 Agents follow thresholds and amount limits](br-f03-35-agents-follow-thresholds-and-limits.md)
