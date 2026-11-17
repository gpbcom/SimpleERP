🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-02 Information, not advice

# 📏 BR-F15-02 Information, not advice

**Status:** ✅ specified

## Statement

Every legal answer ends with "This is legal information, not legal advice." For a dispute, a dismissal, discrimination
or harassment, a health and safety emergency, or a question the corpus does not cover, the AI assistant says what it
does
not know and refers the person to who can help: a lawyer, the labour inspectorate (with the office for the company's
site), the staff representatives (CSE), the Défenseur des droits; for an emergency, the emergency numbers first.

## Why

An ERP must not pose as a lawyer. See [D195](../../../06-decisions/f15-legal-assistant/d195-legal-referral.md) and
[Legal advice limits](../../../05-non-functional/legal-advice-limits.md).

## Examples

| Case | Result |
|---|---|
| "How many RTT days do I have?" | The answer, then the notice |
| "I think I am being harassed" | Your rights, the procedure, the CSE and labour inspectorate contacts, the Défenseur des droits; never a judgement on the facts |
| A question on another country's law not enabled | "I don't know: the law of that country is not in my sources." |

## Applies to

Every answer of the legal assistant.

- [UC-F15-12 Hand a question over to a lawyer](../use-cases/01-ask-a-legal-question/uc-f15-12-hand-a-question-over-to-a-lawyer.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-01 Every statement cites the law in force](br-f15-01-every-statement-cites-the-law-in-force.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F15-03 Legal questions stay private](br-f15-03-legal-questions-stay-private.md)
