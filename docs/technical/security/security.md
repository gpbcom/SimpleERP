# Security

Threats, controls, secrets, sign-in, encryption, audits. Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Sign-in (D414).** Keycloak, self-hosted, for every user: single sign-on with the company's providers (D85), passkeys
preferred and two factors for every user (D450), a fresh sign-in before a link opens a payslip or personal data; short
sessions,
revoked on deactivation.

**Rights.** Rights and record rules (F1) are kept as policies (for example Cedar or OPA) evaluated by one library of the
service kit in every service, so that screens, API, MCP, A2A, search and simulations apply the same decision; every
refusal is audited.

**Secrets.** OpenBao (the open-source fork of Vault), self-hosted, with envelope encryption and per-company keys; in the
hosted edition its master keys sit in a European cloud KMS or an HSM; secrets never appear in configuration, logs or
prompts.

**Compliance (TC-17).** Every framework of D241 is targeted together, with the controls and evidence built once for all:
SecNumCloud on a qualified host, SOC 2 Type II, ISO/IEC 27001 with 27017, 27018 and 27701, HDS, NIS2, DORA, the GDPR,
the Cyber Resilience Act, C5 and ENS, and PCI DSS by never storing card numbers.

Decided in [D414](../../specs/06-decisions/technical/d414-security-design.md).

Last reviewed: 2026-11-12 (GH-2)
