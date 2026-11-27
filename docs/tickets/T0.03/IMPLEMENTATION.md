# T0.03: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- Money is an exact decimal with its currency, and a sum has no float error ([REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)).
- Company ids are opaque types ([E-T01-01](../../specs/03-technical/t01-companies-and-data-isolation/data/e-t01-01-company.md)); lists are paged by a cursor and a repeated write carries an idempotency key ([REQ-T05-02](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md)).
- Rounding belongs to the country pack ([D293](../../specs/06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)); the shared SE bases and error codes belong to T0.04 ([TICKET.md](TICKET.md)).
- [`AGENT.md`](../../../AGENT.md) rules: one class per file, no `Any`, no underscore attributes, a validator per field raising its own exception, `Optional`/`List` typing, no module-level constants.
- `erp_models` imports no service and no library of `backend/shared/` ([README](../../../backend/models/README.md)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Shape of ids and keys | Frozen model with a `value` field | `RootModel[str]`, `Annotated[str, ...]` or `NewType` | Contracts nest `{"value": ...}` |
| [D2](#d2) | Base of the model exceptions | `Exception` | `ValueError` | Pydantic does not collect them |
| [D3](#d3) | Money amount input | `Decimal`, int or decimal text; floats refused | Accept floats | Callers must convert |
| [D4](#d4) | Value objects behaviour | Methods on the model (`add`, `total`, `now`) | Plain data with functions elsewhere | Small logic in the models |
| [D5](#d5) | `has_more` on the page | Plain property | `@computed_field` | Absent from dumps and schema |

## <a id="d1"></a>D1: Shape of ids and keys

**Chosen:** `OpaqueId` with a `value` field · **Where:** [`opaque_id.py:25-29`](../../../backend/models/src/erp_models/base/opaque_id.py#L25-L29) · **Source:** read from the diff, named in the review note

| Option | For | Against |
| --- | --- | --- |
| ✅ Frozen model with `value` | Same base as every model, equality by type and value so `CompanyId` is never a `RecordId`; one validator in one place, each subclass only sets its exception | Serialises as `{"value": "C-12"}`, not a bare string |
| `RootModel[str]` | Would serialise as a bare string | Not chosen by any worker. Reason open: no worker recorded why |
| `Annotated[str, ...]` or `NewType` | Bare string | A `CompanyId` would equal and mix with any string, against the opaque type of E-T01-01 |

**Trade-off:** a nested shape in every API contract for type safety between ids.

**Revisit when:** before the first API resource uses an id (review follow-up K09/K10/K14).

## <a id="d2"></a>D2: Base of the model exceptions

**Chosen:** `Exception` · **Where:** [`se_opaque_id_invalid_value.py`](../../../backend/models/src/erp_models/base/exceptions/se_opaque_id_invalid_value.py) · **Source:** read from the diff, review note

| Option | For | Against |
| --- | --- | --- |
| ✅ `Exception` | Pydantic raises it as it is, so callers catch the specific `SE` exception, as AGENT.md asks (`pytest.raises(SE...)`) | A missing required field still raises `ValidationError`, so two error kinds exist |
| `ValueError` | Collected into a `ValidationError` | Callers would not catch the specific exception; the specific `SE` type would be lost |

**Trade-off:** two error paths until T0.04 adds the shared SE bases.

**Revisit when:** T0.04 lands.

## <a id="d3"></a>D3: Money amount input

**Chosen:** refuse floats, booleans, NaN and Infinity, keep the scale, round nothing · **Where:** [`money.py:36-79`](../../../backend/models/src/erp_models/money/money.py#L36-L79) · **Source:** PLAN, REQ-T10-03

| Option | For | Against |
| --- | --- | --- |
| ✅ Exact input only | Sums have no float error (criterion 2); rounding left to the pack (D293) | Callers convert floats themselves |
| Accept floats | Convenient | A float already holds the error REQ-T10-03 forbids |

**Trade-off:** `1.0` and `1.00` are equal and the scale is kept; JSON carries the amount as a string.

**Revisit when:** a country pack defines rounding.

## <a id="d4"></a>D4: Value objects behaviour

**Chosen:** `Money.add`, `Money.total`, `UtcTimestamp.now` on the models · **Where:** [`money.py:124-158`](../../../backend/models/src/erp_models/money/money.py#L124-L158), [`utc_timestamp.py:73`](../../../backend/models/src/erp_models/times/utc_timestamp.py#L73) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Methods on the model | The currency check lives with the type; criterion 2 is testable on the model | Business-like logic in `erp_models` |
| Data only, logic in a service | `erp_models` holds only contracts | Every service would repeat the sum. Open point: no worker gave the reason |

**Trade-off:** a tiny, rule-free arithmetic in the shared models.

**Revisit when:** a pack needs rounding or conversion.

## <a id="d5"></a>D5: `has_more` on the page

**Chosen:** plain `@property` · **Where:** [`cursor_page.py:79`](../../../backend/models/src/erp_models/paging/cursor_page.py#L79) · **Source:** read from the diff, review follow-up K13/K16

| Option | For | Against |
| --- | --- | --- |
| ✅ `@property` | Simple, nothing stored | Missing from `model_dump` and the JSON schema |
| `@computed_field` | Appears in dumps and schema | Part of the contract before any resource uses it |

**Trade-off:** the field is derived only.

**Revisit when:** the API resources are built.

## 📝 Assumptions behind the choices

- Pydantic and pyyaml already pinned in [`uv.lock`](../../../uv.lock) (K17): supports [D3](#d3) and [D1](#d1) as dependencies cost no new pin.
- The model and currency names are chosen in the plan, with a plain ISO 4217 text: supports [D3](#d3).
- Criterion 3 limited to REQ-T05-02: supports [D5](#d5).
