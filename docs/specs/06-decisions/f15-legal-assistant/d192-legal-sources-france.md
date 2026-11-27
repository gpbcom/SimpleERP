🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D192 French legal sources

# 📜 D192 French legal sources

**Status:** ✅ decided

## Context

Which French sources go into the corpus.

## Options

- The codes: travail, commerce, général des impôts.
- Collective agreements (IDCC).
- Official guidance: BOSS, URSSAF, service-public.fr, the Labour ministry.
- Case law.

## Choice

All four. Case law is labelled as such and never presented as the text of the law.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

T11 ingests Légifrance (codes, KALI), official guidance sites and case law (Judilibre), each with its licence and
refresh.

## Related

- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md)
- [D28](../foundations/d28-legal-assistant.md)

---

⬅️ [D191 Answers for the real situation](d191-legal-answers-from-erp-data.md) · ⬆️ [Up](README.md) ·
➡️ [D193 Legal warnings on by default](d193-legal-warnings-on-by-default.md)
