🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D414 Security design

# 📜 D414 Security design

**Status:** ✅ decided

## Context

Step 19f of the technical interview, from TC-01, TC-11, TC-13 and TC-17.

## Options

- Keycloak or built-in sign-in.
- Policies as data in one library, or checks in each service.
- OpenBao or each cloud's secret manager.
- Compliance: ISO 27001 first, SecNumCloud first, SOC 2 first.

## Choice

Confirmed by the owner on 2026-11-12: Keycloak with passkeys and two-factor authentication; policies as data in one
library; OpenBao with a KMS or HSM when hosted; and "I want all the compliance targets".

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The security chapter's target design; D241 applies in full.

Revised by D450 on 2026-11-12: two factors for every user, not only privileged roles; a fresh sign-in before a link
opens a payslip or personal data.

## Related

- [Security design](../../../technical/security/security.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D413 Configuration layers](d413-configuration-layers.md) · ⬆️ [Up](README.md) ·
➡️ [D415 Supply chain controls](d415-supply-chain-controls.md)
