🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D555 Benchmark gaps of SC11 Professional firms

# 📜 D555 Benchmark gaps of SC11 Professional firms

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four regulated
professions that SC11 did not cover: notaries, insurance brokers, judicial officers and statutory audit firms. Each
carries a legal duty (the clients' funds at the state deposit bank, the registration, the regulated tariff, the rotation
of the signing partner). The statutory auditor becomes a persona, U49.

## Options

- G167 Notaries: deeds with their funds held per deed, or the funds handled through the general trust account of the
  firm.
- G168 Insurance brokers: policies placed only while the registration is current, or a registration date kept in a note.
- G169 Judicial officers: fees computed from the tariff and cut to it, or fees typed on each bill.
- G170 Audit firms: engagements with the rotation date computed, or the mandate years followed in a sheet.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC11 gets four use cases in one new flow, FL-SC11-07, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist);
no article is quoted.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G167 | Notaries | UC-SC11-21: deed funds held at the state deposit bank, one balance per deed | "Notaries" |
| G168 | Insurance brokers | UC-SC11-22: policies that need a current registration | "Insurance brokers" |
| G169 | Judicial officers | UC-SC11-23: fees within the regulated tariff | "Judicial officers" |
| G170 | Audit firms | UC-SC11-24: rotation of the signing partner followed and warned | "Audit firms" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC11 Professional firms").

## Consequences

- G167 Notaries:
  [UC-SC11-21](../../08-sectors/sc11-professional-firms/use-cases/07-notaries-brokers-officers-and-auditors/uc-sc11-21-run-a-notarys-office.md),
  [S-SC11-21](../../08-sectors/sc11-professional-firms/screens/07-notaries-brokers-officers-and-auditors/s-sc11-21-notary.md)
  and
  [BR-SC11-16](../../08-sectors/sc11-professional-firms/business-rules/br-sc11-16-client-funds-are-held-at-the-state-deposit-bank.md),
  with [E-SC11-16](../../08-sectors/sc11-professional-firms/data/e-sc11-16-deed.md) Deed and its list
  [S-SC11-L16](../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l16-deeds.md).
- G168 Insurance brokers:
  [UC-SC11-22](../../08-sectors/sc11-professional-firms/use-cases/07-notaries-brokers-officers-and-auditors/uc-sc11-22-run-an-insurance-brokerage.md),
  [S-SC11-22](../../08-sectors/sc11-professional-firms/screens/07-notaries-brokers-officers-and-auditors/s-sc11-22-brokerage.md)
  and
  [BR-SC11-17](../../08-sectors/sc11-professional-firms/business-rules/br-sc11-17-brokers-keep-their-orias-registration-current.md),
  with [E-SC11-17](../../08-sectors/sc11-professional-firms/data/e-sc11-17-policy.md) Policy and its list
  [S-SC11-L17](../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l17-policies.md).
- G169 Judicial officers:
  [UC-SC11-23](../../08-sectors/sc11-professional-firms/use-cases/07-notaries-brokers-officers-and-auditors/uc-sc11-23-run-a-judicial-officers-office.md),
  [S-SC11-23](../../08-sectors/sc11-professional-firms/screens/07-notaries-brokers-officers-and-auditors/s-sc11-23-judicial-officer.md)
  and
  [BR-SC11-18](../../08-sectors/sc11-professional-firms/business-rules/br-sc11-18-fees-follow-the-regulated-tariff.md),
  with [E-SC11-18](../../08-sectors/sc11-professional-firms/data/e-sc11-18-service-act.md) Service act and its list
  [S-SC11-L18](../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l18-service-acts.md).
- G170 Audit firms:
  [UC-SC11-24](../../08-sectors/sc11-professional-firms/use-cases/07-notaries-brokers-officers-and-auditors/uc-sc11-24-run-a-statutory-audit-firm.md),
  [S-SC11-24](../../08-sectors/sc11-professional-firms/screens/07-notaries-brokers-officers-and-auditors/s-sc11-24-audit-firm.md)
  and
  [BR-SC11-19](../../08-sectors/sc11-professional-firms/business-rules/br-sc11-19-partners-rotate-as-the-law-requires.md),
  with [E-SC11-19](../../08-sectors/sc11-professional-firms/data/e-sc11-19-audit-engagement.md) Audit engagement and its
  list [S-SC11-L19](../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l19-audit-engagements.md).
- Drawn in
  [FL-SC11-07](../../08-sectors/sc11-professional-firms/flows/fl-sc11-07-notaries-brokers-officers-and-auditors.md)
  Notaries, brokers, judicial officers and audit firms.

## Related

- [FL-SC11-07](../../08-sectors/sc11-professional-firms/flows/fl-sc11-07-notaries-brokers-officers-and-auditors.md)
- [D347 Professional firms sector coverage](d347-professional-firms-sector-coverage.md)
- [D349 SC11 use cases](d349-sc11-use-cases.md)
- [U49 Statutory auditor](../../01-users/personas/u49-statutory-auditor.md)

---

⬅️ [D554 Benchmark gaps of SC10 Real estate](d554-benchmark-gaps-sc10-real-estate.md) · ⬆️ [Up](README.md) ·
➡️ [D556 Benchmark gaps of SC12 Education and training](d556-benchmark-gaps-sc12-education-and-training.md)
