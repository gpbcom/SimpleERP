🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-36 Acting as a user needs consent and is audited

# 📏 BR-F1-36 Acting as a user needs consent and is audited

**Status:** ✅ specified

## Statement

An administrator acts as a user only after that user grants a request that gives the reason and the duration, for at
most 60 minutes; the session shows a banner to both, can be stopped by either, keeps the user's rights and no more,
never changes the user's password, second factor or rights, and every action is audited under both names.

## Why

Acting under someone's name is the most sensitive support action: it needs the person's agreement and a trace. The
owner's answer: "Act as a user"
([D520](../../../06-decisions/f01-administration/d520-benchmark-gaps-f01-administration.md)).

## Examples

| Case | Result |
|---|---|
| A request without a reason | refused: a reason is required |
| The user grants 30 minutes | the session opens and ends at 30 minutes |
| The user does not answer within 24 hours | the request expires |
| The administrator posts an expense in the session | the audit shows Sonia and the administrator |
| The administrator tries to change the user's second factor | refused |
| Ask to act as the owner | refused |

## Applies to

- [UC-F1-27 Act as a user with consent](../use-cases/15-security-and-group-data/uc-f01-27-act-as-a-user-with-consent.md)
- [E-F1-26 Act-as session](../data/e-f01-26-act-as-session.md)
- [UC-F1-11 Enter a client company to support it](../use-cases/08-provider-and-client-companies/uc-f01-11-enter-a-client-company-to-support-it.md)

## Exceptions

None: the provider's support access to a client company follows its own consent
([UC-F1-11](../use-cases/08-provider-and-client-companies/uc-f01-11-enter-a-client-company-to-support-it.md)).

## Configurable

Yes: the default duration and the maximum, up to 60 minutes, in the security policy
([UC-F1-21](../use-cases/13-security-and-audit/uc-f01-21-set-the-security-policies.md)).

## Open questions

None.

---

⬅️ [BR-F1-35 Shared records keep one owner company](br-f01-35-shared-records-keep-one-owner-company.md) ·
⬆️ [Up](README.md)
