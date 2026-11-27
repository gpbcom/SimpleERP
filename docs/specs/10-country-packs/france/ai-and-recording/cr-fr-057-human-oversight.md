🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🤖 [AI and recording](README.md) › ⚖️ CR-FR-057 Human oversight of high-risk AI

# ⚖️ CR-FR-057 Human oversight of high-risk AI

**Status:** ✅ specified

## Statement

A high-risk AI system is built so that the people overseeing it can understand its output, avoid relying on it blindly,
decide not to use it, override or reverse it, and stop it; the company using it assigns that oversight to people with
the competence and authority to do it. SimpleERP's own rule that a person confirms the AI assistant's writes, and that
no AI pays, sends a legal document, deletes or decides about a person alone, is a product decision (D157, D439), not
this article's duty.

## Values

- High-risk uses in SimpleERP: candidate scoring and worker evaluation (CR-FR-058).
- Provider: oversight built in (explanations, override, stop).
- Deployer: named overseers with the competence and authority; logs kept.

## Legal references

- [AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) art. 14 (provider) and art. 26
  (deployer).

## Effective dates

High-risk duties: application dates to be checked at build.

## Enforced by

- [Regulatory](../../../02-functional/f03-assistant/regulatory.md)
- [BR-F4-20 Scores come with their evidence](../../../02-functional/f04-meetings/business-rules/br-f04-20-scores-come-with-their-evidence.md)
- [Regulatory](../../../02-functional/f04-meetings/regulatory.md)
- [AI governance](../../../05-non-functional/ai-governance.md)

## When the law changes

Watched in the law corpus: AI Act art. 14 and 26. A change flags this rule and warns the administrators; the corrected
rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-056 People know they deal with an AI](cr-fr-056-people-know-they-deal-with-an-ai.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-058 AI in recruitment and work is high-risk](cr-fr-058-high-risk-ai-in-employment.md)
