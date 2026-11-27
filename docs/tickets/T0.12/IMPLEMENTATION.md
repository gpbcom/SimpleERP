# T0.12: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- One value is in force on a given day, and last year's fact gets last year's value (REQ-T11-02, I-T11-01, see [PLAN.md](PLAN.md)).
- Money and rates are exact decimals, never floats (REQ-T10-03).
- A rate change is tested the day before and the day of the change (REQ-T11-06, criterion 1).
- Layout of D438: a shared library lives in `backend/shared/<lib>`, holds no business rules of a service and imports no service (AGENT.md, "Mono-repo").
- AGENT.md rules enforced by `tests/conventions/`: one class per file, at most five files per folder, a validator per field raising its own exception.
- Tests use synthetic data only (D426).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How periods may relate | Inclusive optional `valid_to`, no overlap, gaps refused | Pick the latest version on overlap | Stricter packs, no ambiguity |
| [D2](#d2) | Type of a value | `Decimal` or `Money`, floats refused | Accept floats and convert | Authors quote numbers in YAML |
| [D3](#d3) | Where the overlap check lives | In the model, at load | In the lookup | A bad pack fails at load, not at use |
| [D4](#d4) | Country guard | Two ASCII letters before any path | Trust the caller | A little code for path safety |
| [D5](#d5) | Pack loading | Cached per repository instance | Read the file on every call | A changed file needs a new instance |
| [D6](#d6) | Package name | `erp_country_rules` | Another name | Prefix to match `erp_models` |
| [D7](#d7) | Layers | models, storage, service, no api or factory | Full service layout | Not a runnable |

## <a id="d1"></a>D1: How periods may relate

**Chosen:** `valid_to` inclusive and optional, versions listed by date, never overlapping, gaps allowed but refused at lookup · **Where:** [`backend/shared/country-rules/src/erp_country_rules/models/rules/country_rule.py:86-102`](../../../backend/shared/country-rules/src/erp_country_rules/models/rules/country_rule.py#L86-L102), [`backend/shared/country-rules/src/erp_country_rules/service/rules/country_rules.py:79-85`](../../../backend/shared/country-rules/src/erp_country_rules/service/rules/country_rules.py#L79-L85) · **Source:** PLAN.md assumption, accepted by the reviewer

| Option | For | Against |
| --- | --- | --- |
| ✅ No overlap, gap refused | The library never chooses between two values, the most conservative reading of REQ-T11-02. A missing rate cannot be guessed silently | A pack with a hole cannot answer a date inside it |
| Latest version wins on overlap | Packs are easier to write | Hides an authoring error in a legal value. Nobody asked for it |
| Fall back to the nearest version in a gap | Always answers | A legal rate invented for a date it does not cover |

**Trade-off:** stricter packs in exchange for a single, unambiguous value per day.

**Revisit when:** a real pack needs overlapping periods (open point: no specification says it will).

## <a id="d2"></a>D2: Type of a value

**Chosen:** an exact `Decimal` or an `erp_models` `Money`; a YAML float is refused · **Where:** [`backend/shared/country-rules/src/erp_country_rules/models/rules/rule_version.py:117-158`](../../../backend/shared/country-rules/src/erp_country_rules/models/rules/rule_version.py#L117-L158) · **Source:** PLAN.md, REQ-T10-03

| Option | For | Against |
| --- | --- | --- |
| ✅ Decimal or Money, no float | Exact sums, tested by `test_two_values_sum_exactly_where_floats_do_not`. Reuses `Money` from T0.03 | Pack authors write `"19.6"` as text, not `19.6` |
| Accept floats and convert | Natural YAML | `19.6` is already inexact when parsed, against REQ-T10-03 |
| Also text and boolean values | More rule kinds | No ticket needs them yet. Left to later tickets |

**Trade-off:** a slightly awkward pack syntax for exactness.

**Revisit when:** a rule needs a text or boolean value.

## <a id="d3"></a>D3: Where the overlap check lives

**Chosen:** a `model_validator` of `CountryRule` · **Where:** [`backend/shared/country-rules/src/erp_country_rules/models/rules/country_rule.py:86`](../../../backend/shared/country-rules/src/erp_country_rules/models/rules/country_rule.py#L86) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ In the model | AGENT.md: cross-field rules go in `model_validator(mode="after")`. A bad pack fails once at load | None found |
| In the lookup | One place for all date logic | Fails on every read, for the first caller to hit it, and the lookup loop would then need to pick one |

**Trade-off:** none worth noting.

**Revisit when:** versions come from a source other than a validated pack.

## <a id="d4"></a>D4: Country guard

**Chosen:** strip, upper-case, require `[A-Z]{2}` before building the path · **Where:** [`backend/shared/country-rules/src/erp_country_rules/storage/packs/country_pack_repository.py:61-67`](../../../backend/shared/country-rules/src/erp_country_rules/storage/packs/country_pack_repository.py#L61-L67) · **Source:** PLAN.md assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ Pattern check first | A country such as `../x` cannot leave the packs folder | Refuses codes of other shapes |
| Check only that the file exists | Less code | A traversal could reach another file |

**Trade-off:** only two-letter codes are served.

**Revisit when:** a pack needs a code that is not two letters (open point).

## <a id="d5"></a>D5: Pack loading

**Chosen:** a dictionary per repository instance, a failed load not kept · **Where:** [`backend/shared/country-rules/src/erp_country_rules/storage/packs/country_pack_repository.py:68-82`](../../../backend/shared/country-rules/src/erp_country_rules/storage/packs/country_pack_repository.py#L68-L82) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Cache per instance | A rule is read for every fact, so no file read each time | A pack changed on disk needs a new instance |
| Read on every call | Always fresh | A file read and validation per fact. No measure was made, so the cost is unknown |

**Trade-off:** freshness for speed, on a guess about call volume.

**Revisit when:** packs are updated while a service runs (REQ-T11-01 signed packs).

## <a id="d6"></a>D6: Package name

**Chosen:** import `erp_country_rules`, distribution `erp-country-rules` · **Where:** [`backend/shared/country-rules/pyproject.toml:2`](../../../backend/shared/country-rules/pyproject.toml#L2), [`backend/shared/country-rules/pyproject.toml:20`](../../../backend/shared/country-rules/pyproject.toml#L20) · **Source:** PLAN.md

D438 names only the folder. The `erp_` prefix matches `erp_models` and avoids clashes in the one shared uv environment (AGENT.md, "Services"). No other name was named by a worker, so no alternative is compared.

**Revisit when:** the specifications name the package.

## <a id="d7"></a>D7: Layers

**Chosen:** `models`, `storage` and `service` only · **Where:** [`backend/shared/country-rules/src/erp_country_rules/service/rules/country_rules.py:20`](../../../backend/shared/country-rules/src/erp_country_rules/service/rules/country_rules.py#L20) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ No api layer, no factory | The library is not a runnable and has no lifecycle (AGENT.md, "Lifecycle and factories") | Callers build `CountryRules` with their repository by hand |
| A full service layout | Same shape as a service | Nothing to serve, and an `api` layer would be empty |

**Trade-off:** no factory until a caller needs one.

**Revisit when:** a service wires it and wants a shared construction.

## 📝 Assumptions behind the choices

- Inclusive optional `valid_to`, no overlaps, gaps refused: supports [D1](#d1) and [D3](#d3).
- Decimal or Money, floats refused (REQ-T10-03): supports [D2](#d2).
- Country checked as two ASCII letters: supports [D4](#d4).
- Package `erp_country_rules`: supports [D6](#d6).
- No api layer and no factory: supports [D7](#d7).
