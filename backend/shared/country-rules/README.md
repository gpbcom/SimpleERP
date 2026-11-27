# erp_country_rules

`erp_country_rules` reads the rules of the country packs: the rates, thresholds and amounts that the law sets and
changes over time. It holds no business rules of its own. It follows
[D405](../../../docs/specs/06-decisions/technical/d405-architecture-and-scalability.md) and
[I-T11-01](../../../docs/specs/03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md), and sits in the
shared libraries of the layout fixed by [D438](../../../docs/specs/06-decisions/technical/d438-repository-layout.md).

## What it holds

- `CountryRules.value(rule, country, date)` returns the `Decimal` or the `erp_models` `Money` in force on the date of
  the fact.
- The packs are read from `<packs_dir>/<country in lower case>/rules.yaml`. `packs_dir` is a field of
  `CountryRulesConfig`, and is `packs/countries` by default.
- A pack holds `country`, `version` and `rules`.
- Each rule holds versions. Each version has `valid_from`, an optional inclusive `valid_to`, and a `value`.

## Layers

A library has no `api` layer.

- `models`: the pack, the rule, its versions and the configuration.
- `storage`: reads the pack files.
- `service`: answers which value is in force on a date.

## Tests

```bash
uv run --package erp-country-rules pytest backend/shared/country-rules/tests -n 2
```
