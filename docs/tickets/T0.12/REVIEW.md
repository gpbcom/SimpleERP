# T0.12: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A new shared library, `erp_country_rules`. `CountryRules.value(rule, country, date)` (I-T11-01) returns the value in force on the day of the fact (REQ-T11-02).
- A pack is a YAML catalogue stored as `<packs_dir>/<cc>/rules.yaml`. Each rule has dated versions, and `valid_to` is inclusive and optional. Versions that overlap are refused when the pack loads, so only one value can ever be in force on a given day. A date that falls in a gap or before the first version is refused.
- A value is an exact `Decimal` or an `erp_models.Money`. A YAML float is refused (REQ-T10-03).
- The repository checks the country code before it builds any path, and keeps each pack in memory after the first read.
- `uv.lock` now adds only the new member on top of the committed lock, which fixes the blocking finding of the earlier run. The two design pages describe the library.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Last year's invoice gets last year's value | `test_values_by_date.py::test_an_invoice_of_last_year_gets_last_years_rate`, tests-evidences/pytest-backend-shared-country-rules.txt | ✅ Pass |
| 2. A future-dated value applies from its date, and the earlier one applies before it | `test_a_future_dated_rule_applies_from_its_date` (2027-06-30, 2027-07-01, 2035-01-01) | ✅ Pass |
| 3. A rate change has tests before and after its date | `test_the_value_in_force_on_each_boundary_day`, and `test_every_rate_change_has_a_case_before_and_on_its_date`, which fails when a change in the pack has no case | ✅ Pass |
| 4. A money value is an exact decimal with its currency, and a sum has no float error | `test_money_values.py::test_two_values_sum_exactly_where_floats_do_not`, `test_three_lines_of_ten_cents_sum_exactly_to_thirty_cents` | ✅ Pass |
| 5. The conventions and the library's own tests pass | tests-evidences/pytest.txt (1174 passed, `tests/` with conventions), pytest-backend-shared-country-rules.txt (173 passed), ruff-check.txt, ruff-format.txt, mypy.txt | ✅ Pass |

## Look at first

- **Version lookup and the overlap rule.** `CountryRule.validate_periods` checks that versions are in order and never overlap, and `CountryRules._find_version` picks the one in force. Together they guarantee a single value per day. Files: `backend/shared/country-rules/src/erp_country_rules/models/rules/country_rule.py`, `backend/shared/country-rules/src/erp_country_rules/service/rules/country_rules.py`.
- **Reading values.** Floats are refused, and Money mappings are delegated to `erp_models.Money`. File: `backend/shared/country-rules/src/erp_country_rules/models/rules/rule_version.py`.
- **Path guard and cache.** The country code must match `[A-Z]{2}` before any path is built. A pack is cached per repository instance, and a failed load is not cached. Read this file line by line. File: `backend/shared/country-rules/src/erp_country_rules/storage/packs/country_pack_repository.py`.
- **Company data isolation.** Not affected. Packs are shared legal reference data, not company data, and no rule value is ever logged.
- **The lock.** `uv.lock` adds only `erp-country-rules`, and its dependencies match `backend/shared/country-rules/pyproject.toml`.

## Assumptions accepted

- The package name `erp_country_rules` is accepted, following the naming of the other shared libraries.
- The pack fields (`country`, `version`, `rules`, `valid_from`, `valid_to`, `value`) are accepted: they are the main fields of E-T11-01 and E-T11-02.
- An inclusive, optional `valid_to`, with no overlaps allowed and gaps refused, is accepted as the most conservative reading of REQ-T11-02.
- A value that is a Decimal or Money, with floats refused, is accepted under REQ-T10-03.
- The test pack for the synthetic country ZZ with fixed dates is accepted under D426.
- The default `packs/countries` with no real pack data is accepted: D438 fixes the folder, and real data is out of scope.
- No api layer and no factory is accepted, because a library is not a runnable.
- Leaving REQ-T11-06 criterion 2 out of scope is accepted, because it concerns the release, not the library.
- Changing `uv.lock` outside the ticket's area is accepted, because a new workspace member needs it.

## Follow-ups

- When a pack file fails validation, the repository neither logs it at ERROR nor documents the error correctly.
- The repository does not check that `pack.country` matches the requested code.
- Passing a `datetime` to `value()` raises a `TypeError` instead of an SE error.
- The default `packs_dir` resolves from the service's working folder. How a service sets it is still to be settled.
- The `erp_models` imports are under the wrong group comment.
- The `country_rules` fixture parameter is not annotated in `test_refusals.py`.
