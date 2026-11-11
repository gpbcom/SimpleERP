# <KEY> — Tests catalog (exhaustive, per acceptance criterion)

Every test of the ticket, one block per acceptance criterion of [TICKET.md](TICKET.md#acceptance-criteria), with its edge cases. How to run each level: [TESTS-NOTICE.md](TESTS-NOTICE.md). Files each test lives in: [IMPLEMENTATION.md §0](IMPLEMENTATION.md#0-files-modified--exact-list).

## How to read this catalog

**State** of a test:
- **kept**: an existing test that already proves the criterion; unchanged and must stay green.
- **fixed**: an existing test whose expectation changes with the ticket.
- **new**: written by this ticket.

**Level:** U = unit, G = GUI (Playwright), B = Bruno, S = stage run, M = manual. ID prefixes: <letter = area, e.g. D = domain, S = storage schema>.

## Fixtures

| Fixture | Holds | Used by |
|---|---|---|
| <name> | <data, edge cases> | <IDs> |

## T1 — <topic>

### AC1 — <criterion, short>

| ID | Level | File | Given / when / then | State |
|---|---|---|---|---|
| <D01> | U | `<path>` | **Given** <…> **when** <…> **then** <…> | new |

Edge cases: <empty, zero, negative, rounding, missing field, older data>.

## Development rules (checks, not unit tests)

| Rule | Check | When |
|---|---|---|
| <ID> | <command or script> | <step> |

## AC → tests matrix

| AC | Tests |
|---|---|
| AC1 | <IDs> |

## Counts

| Level | New | Fixed | Kept | Total |
|---|---|---|---|---|
| U | 0 | 0 | 0 | 0 |
