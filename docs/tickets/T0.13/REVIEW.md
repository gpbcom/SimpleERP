## Review: T0.13 (round 2, checking the fixes)

**Verdict:** approve. The one blocking finding from round 1 is fixed, and the fix adds no blocking defect.

### What changed in this round
- The `company_context` fixture now gets its company from the user builder (`user_builder.company`), the same company the user was built for. Before, it built a second company with a different id. Now the context's company, the user's `company_id` and the `RequestContext` user's `company_id` all name the same company, so data a test seeds with `user.company_id` stays in the company the context reads from (D426).
- The fixture no longer asks for `company_builder` directly. That builder still reaches it through `user_builder`, so nothing else changes.
- A new test checks that the three company ids are equal. The old test only checked `is not None`.
- The check evidence was re-run in `tests-evidences/`: ruff check and ruff format pass, mypy finds no issues in 432 files, and pytest passes for every package the ticket touches (shared testing: 321 passed, 4 skipped; repository `tests/`: 1307 passed, 3 skipped).

### Acceptance criteria
This round only re-checks AC1. The other criteria were checked in round 1 and are not affected by this fix.
- AC1, the company-context fixture: met. Evidence: `test_the_company_context_fixture_user_belongs_to_the_context_company` in `backend/shared/testing/tests/plugin/test_testing_plugin.py`, and `tests-evidences/pytest-backend-shared-testing.txt` (321 passed).

### What to look at first
- `/home/guillaume/Documents/Projects/Others/simple-erp/backend/shared/testing/src/erp_testing/plugin/testing_plugin.py` lines 124-138: the context is built from `user_builder.company` and `user_builder.build()`. `UserBuilder.build()` sets `company_id=self.company.id` (user_builder.py:94), and `SyntheticCompanyContext` builds `UserContext(company_id=self.company.id)` (synthetic_company_context.py:63), so the ids match by construction.
- `/home/guillaume/Documents/Projects/Others/simple-erp/backend/shared/testing/tests/plugin/test_testing_plugin.py` lines 74-78: the equality test that would have caught the bug.

### Assumptions accepted
None were reported in this round.

### Follow-ups
- `SyntheticCompanyContext` could refuse a user whose `company_id` is not its company's id, so that a test building the context by hand cannot recreate the mismatch.
