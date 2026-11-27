# T0.04: SE exceptions and error codes

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 December 2026: The layout, its rules and the first shared code
- **Epic:** [E0.2 Shared models](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): `erp_models`: base model, money, ids and times, enums, `SE` exceptions and the D122 error codes

## What it delivers

- The `SE` exception bases of AGENT.md ("Exceptions") in `backend/models`: the layer base `SE<Domain>Error`, the model base `SEInvalid<Model>Exception` and their naming, one exception per file, re-exported by the package's `exceptions/__init__.py`, as [AGENT.md](../../../AGENT.md).
- The error code catalogue of the pattern of D122, as data in `conf/catalogs/`: each code with its title key, its why key, its action key and its support reference, as [🧵 Error messages](../../specs/04-ux/design-system/patterns/error-messages.md).
- A catalogue model that resolves every code to its three message keys and its reference, and refuses an unknown code, built on `YamlCatalog` of [T0.03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), as [🏗️ Back end](../../technical/architecture/backend.md).

## Features, use cases and business rules

- [📜 D122 Error message standard](../../specs/06-decisions/ux/d122-error-message-standard.md): a short title, one sentence saying why, the action that fixes it, and a small support reference at the bottom.
- [📌 REQ-T05-03 problem+json errors](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md): errors carry the codes of the error pattern, and no secret is in an error.
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md): the back-end design the shared models belong to.
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): `backend/models` holds the shared models, `erp_models`.

## Technical pages it builds on

- [🏗️ Back end](../../technical/architecture/backend.md): `erp_models` is the shared home of the public contracts and their `SE` exceptions.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): the place of `backend/models`.
- [🏗️ Configuration](../../technical/architecture/configuration.md): `conf/catalogs/` holds data that would otherwise be hard-coded, loaded by `YamlCatalog` models.
- [🏗️ API](../../technical/interfaces/api.md): errors are `application/problem+json` carrying the error codes of the D122 pattern.

## Screens touched

- ➖ No screen: the ticket adds shared models and a data catalogue in `backend/models`, and changes no front end (the error pattern on screen is the work of T0.23).

## Budgets touched

- The ticket touches no budget.

## Acceptance criteria

1. **Given** any code of the catalogue, **when** it is resolved, **then** it gives its title key, its why key, its action key and its support reference. ([📜 D122](../../specs/06-decisions/ux/d122-error-message-standard.md))
2. **Given** a code that is not in the catalogue, **when** the catalogue's model is asked for it, **then** it is refused. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md))
3. **Given** every message of the catalogue, **when** it is read, **then** none holds a secret. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) criterion 2)
4. **Given** the `SE` exception bases, **when** `tests/conventions/` runs, **then** they follow AGENT.md ("Exceptions"): one exception per file, named `SE...`, re-exported through a sorted `__all__`. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))

## Out of scope

- The base model, ids, money and enums, see [T0.03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- The problem+json handler of the first service, see [T0.14](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- The error messages on screen, see [T0.23](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The translation catalogues behind the message keys, see [REQ-T10-01](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md), closed in P2.

## Assumptions

- The specifications fix no list of error codes: the catalogue holds the codes the exception bases need and the sample codes of the D122 pattern ("SITE-CLOSE-01"); later tickets add their own.
- The roadmap row has no anchor of its own, so the ticket links to its sprint anchor `#s01`.
- The message keys are keys only: their French and English texts belong to the translation catalogues of P2 (T10).
- No budget is given to this ticket by the roadmap row or the specifications.
