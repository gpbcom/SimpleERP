# T0.09: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- A request without a company is refused, and the same user, action and record give the same decision from HTTP and from a direct call ([TICKET.md](TICKET.md)).
- With no policy that allows it, `allowed()` denies by default ([TICKET.md](TICKET.md)).
- A refusal is problem+json with its code, holds no secret, and is logged with who, what and why ([TICKET.md](TICKET.md)).
- AGENT.md: one class per file, at most five files per folder, layers `api` > `service` > `storage` > `models`, no module-level data, data in `conf/catalogs/`, lazy logging.
- The area lock of TKT-16: `backend/models` and [`docs/technical/architecture/backend.md`](../../../docs/technical/architecture/backend.md) are held by other tickets ([PLAN.md](PLAN.md)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Kind of middleware | Pure ASGI class | `BaseHTTPMiddleware` | More code to write by hand |
| [D2](#d2) | One path for rights | `decide` behind `allowed` and `enforce` | Separate HTTP and direct logic | Two thin wrappers |
| [D3](#d3) | Policy language | Pluggable `Policy.vote`, none shipped | Choose Cedar or OPA now | Nothing is allowed until a policy exists |
| [D4](#d4) | Where refusal codes live | Own catalogue of the library | Shared `error_codes.yaml` | Two catalogues for now |
| [D5](#d5) | Body of a refusal | Built from the catalogue only | Use the exception message | Texts are keys until P2 |
| [D6](#d6) | "Logged for the audit" | WARNING log line | Write an audit record | No audit trail yet |
| [D7](#d7) | Missing or invalid company, missing user | Refused with 400 and 401 | Fall back to a default | Strict clients only |

## <a id="d1"></a>D1: Kind of middleware

**Chosen:** a pure ASGI class · **Where:** [`company_context_middleware.py:24`](../../../backend/shared/context/src/erp_context/api/middleware/company_context_middleware.py#L24) · **Source:** read from the diff, with the reason in its docstring

| Option | For | Against |
| --- | --- | --- |
| ✅ Pure ASGI | The `ContextVar` is bound in the task that serves the request and released in a `finally` ([line 190](../../../backend/shared/context/src/erp_context/api/middleware/company_context_middleware.py#L190)); websockets and lifespan are handled explicitly. | Scope, headers and the problem answer are written by hand. |
| `BaseHTTPMiddleware` | Less code. | The class docstring says the context must be bound in the task that serves the request. Whether this alternative breaks that was not measured here: open point. |

**Trade-off:** more hand-written code for a context that is bound where it is read.

**Revisit when:** the code to maintain outweighs the binding concern.

## <a id="d2"></a>D2: One decision path for rights

**Chosen:** `decide` is the only place that decides; `allowed` and `enforce` wrap it · **Where:** [`rights_service.py:80`](../../../backend/shared/context/src/erp_context/service/rights/rights_service.py#L80) · **Source:** PLAN.md, acceptance criterion 2

| Option | For | Against |
| --- | --- | --- |
| ✅ One `decide` | Parity between HTTP and a direct call holds by construction, and is tested in [`test_decision_parity.py`](../../../backend/shared/context/tests/api/rights/test_decision_parity.py). | Callers needing the reason must call `decide`, not `allowed`. |
| Separate logic per entrance | Each can fit its caller. | Criterion 2 could drift. |

**Trade-off:** `allowed` loses the reason, which `decide` keeps.

**Revisit when:** a caller needs both cheaply, or a second kind of entrance appears.

## <a id="d3"></a>D3: Policy language

**Chosen:** a pluggable [`Policy.vote`](../../../backend/shared/context/src/erp_context/service/rights/policy.py#L25), with none shipped, so everything is denied · **Source:** PLAN.md assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ Pluggable, none shipped | The specification names Cedar or OPA only as examples ([security.md](../../../docs/technical/security/security.md)), so nothing is invented. Deny by default holds. | Nothing is allowed until a later ticket supplies a policy. |
| Pick a language now | Allows real use sooner. | The specification has not chosen. |

**Trade-off:** a safe library that cannot yet grant anything.

**Revisit when:** a ticket chooses the policy language.

## <a id="d4"></a>D4: Where refusal codes live

**Chosen:** [`refusal_codes.yaml`](../../../backend/shared/context/conf/catalogs/refusal_codes.yaml) in the library · **Source:** PLAN.md, review follow-up

| Option | For | Against |
| --- | --- | --- |
| ✅ Library catalogue | `backend/models` is locked by another ticket (TKT-16). | Two catalogues beside [`error_codes.yaml`](../../../backend/models/conf/catalogs/error_codes.yaml). |
| Shared catalogue | One place for every code. | Blocked by the area lock. |

**Trade-off:** duplication of place until the area is free.

**Revisit when:** `backend/models` is free: register the codes there or record why not (follow-up).

## <a id="d5"></a>D5: Body of a refusal

**Chosen:** the body comes from the catalogue entry only · **Where:** [`problem_builder.py:51-59`](../../../backend/shared/context/src/erp_context/api/problems/problem_builder.py#L51-L59) · **Source:** PLAN.md, acceptance criterion 4

| Option | For | Against |
| --- | --- | --- |
| ✅ Catalogue only | No header value or exception text can leak; a test checks it. | Title and why are message keys until the translation catalogues of P2. |
| Exception message | More detail for the caller. | Could quote a secret, against criterion 4. |

**Trade-off:** less detail in the body, which the log keeps.

**Revisit when:** the translation catalogues of P2 land.

## <a id="d6"></a>D6: "Logged for the audit"

**Chosen:** a WARNING log line with code, reason, user, company, action and record ([`rights_service.py:63`](../../../backend/shared/context/src/erp_context/service/rights/rights_service.py#L63)) · **Source:** PLAN.md, accepted by the review

| Option | For | Against |
| --- | --- | --- |
| ✅ Log line | The audit writer (I-T03-01) is not in this ticket; AGENT.md's `WARNING` level fits a refusal. | No durable audit trail. |
| Audit record | Durable. | Needs a writer nobody has built. |

**Trade-off:** criterion 5 is met by the log only.

**Revisit when:** the audit writer exists. The text saying it comes in T0.10 is wrong (follow-up).

## <a id="d7"></a>D7: Missing or invalid input is refused

**Chosen:** a missing or invalid company gives 400 `CONTEXT-COMPANY-01`, a missing user 401 `CONTEXT-USER-01` · **Where:** [`company_context_middleware.py:97-116`](../../../backend/shared/context/src/erp_context/api/middleware/company_context_middleware.py#L97-L116) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Refuse | Deny by default; an invalid company is treated as missing. | The headers are trusted as sent: safe only behind the gateway (follow-up). |
| Default company | Easier to call. | Would break company isolation. |

**Trade-off:** strict callers, and trust in the gateway that is not yet written down.

**Revisit when:** the gateway exists and its trust assumption is documented.

## 📝 Assumptions behind the choices

- The gateway has already checked the token and sets the headers: supports [D7](#d7).
- The audit writer is not part of this ticket: supports [D6](#d6).
- Row-level security and the gateway are out of scope: supports [D3](#d3) and [D7](#d7).
