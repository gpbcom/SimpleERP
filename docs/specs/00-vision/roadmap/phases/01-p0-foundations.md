# 🛣️ P0: Foundations

**Status:** 🟡 Draft · **Sprints:** S01 to S04 · **Dates:** 7 Dec 2026 to 12 Feb 2027 · **Tickets:** 25

> [!NOTE]
> P0 builds what every later ticket stands on: the D438 folders and workspaces, the shared models and the service kit of `backend/shared/`, a first service with its image and its generated OpenAPI, the Compose, Helm and Terraform skeletons, and the back-office shell with its design tokens, languages and test scaffolds; it comes first because no capability can be built, tested or shipped without them.
> It delivers no F or T capability of its own: each ticket builds the base that a later capability completes, mostly in [P2 Platform core](README.md#phases).

## <a id="goal"></a>🎯 Goal

At the end of P0, on Friday 29 January 2027, a [SimpleERP maintainer](../../../01-users/personas/u47-simpleerp-maintainer.md)
and the agents of the harness can start any ticket of P1 and P2 on a repository that already has its shape:

- **The layout of [D438](../../../06-decisions/technical/d438-repository-layout.md).** `backend/models/`, `backend/shared/<lib>/`, `backend/services/<service>/`,
  `frontend/backoffice/`, `frontend/portals/`, `frontend/mobile/`, `frontend/packages/<pkg>/`, `plugins/`, `sdk/`,
  `infra/{compose,helm,terraform}/` and `packs/`, with one uv lock and one pnpm lock, as
  [Repository layout](../../../../technical/architecture/repository-layout.md) and [AGENT.md](../../../../../AGENT.md)
  ("Mono-repo") describe it. The harness, the CI/CD pipeline and `tests/conventions/` exist since 2026-11-27; P0 extends
  them to the new packages and does not recreate them.
- **One model per contract, one kit for every service.** `erp_models` (the base model, enums, `SE` exceptions and the
  error codes of [D122](../../../06-decisions/ux/d122-error-message-standard.md)) and the libraries of [Back end](../../../../technical/architecture/backend.md) ([D406](../../../06-decisions/technical/d406-back-end.md)):
  lifecycle with factories, logging, configuration loading ([D413](../../../06-decisions/technical/d413-configuration-layers.md)), the company-context and rights middleware
  ([REQ-T01-02](../../../03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md), [I-T02-02](../../../03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md)), the event outbox ([D405](../../../06-decisions/technical/d405-architecture-and-scalability.md)), the metering client (TC-21), the country-pack rules
  library ([I-T11-01](../../../03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md)) and the test helpers ([D426](../../../06-decisions/technical/d426-testing-strategy.md)). They hold no business rules.
- **A first service, contract first.** `backend/services/platform` with its layers, its multi-stage image and its
  OpenAPI generated from the code ([REQ-T05-01](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md)), problem+json errors ([REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)), a contract check in CI
  ([REQ-T05-05](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)), the typed client of the front end and the Bruno collection generated from the same document.
- **Runs the same everywhere.** `compose.e2e.yaml`, the laptop and one-server Compose profiles ([D408](../../../06-decisions/technical/d408-performance-and-profiles.md), [D421](../../../06-decisions/technical/d421-infrastructure-cncf.md),
  [REQ-T09-02](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md), [REQ-T09-03](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md)), the Helm umbrella chart and the Terraform module skeletons ([REQ-T09-08](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md)), all from
  the same images. The full install, backups and upgrades are built in P2 (T9).
- **A back-office shell to build every screen in.** Vue 3, Vite, Pinia and the router ([D407](../../../06-decisions/technical/d407-front-end.md)); design tokens
  generated from the [visual identity](../../../04-ux/visual-identity/README.md) and
  [Tokens](../../../04-ux/design-system/tokens.md); the app shell of [D47](../../../06-decisions/ux/d47-app-shell.md) with the sidebar and the
  [symbol](../../../../assets/symbol.svg), light and dark ([D43](../../../06-decisions/ux/d43-light-and-dark.md)); the i18n base in French and English ([D21](../../../06-decisions/foundations/d21-languages.md)); the
  Playwright scaffold against the real images (TKT-21) and the Bruno scaffold.

## <a id="scope"></a>🧺 Scope

**Capabilities.** None of its own. P0 builds the foundations that the technical capabilities of P2 complete:
[T1 Companies and data isolation](../../../03-technical/t01-companies-and-data-isolation/README.md),
[T2 Identity and access](../../../03-technical/t02-identity-and-access/README.md),
[T5 API and webhooks](../../../03-technical/t05-api-and-webhooks/README.md),
[T9 Install, backups and updates](../../../03-technical/t09-install-backups-and-updates/README.md),
[T10 Translations and notifications](../../../03-technical/t10-translations-and-notifications/README.md) and
[T11 Legal corpora](../../../03-technical/t11-legal-corpora/README.md).

**Technical requirements touched (foundations only, closed in P2)**

| Requirement | What P0 builds | Closed in |
| --- | --- | --- |
| [REQ-T01-02](../../../03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md) | The company context read at the edge of every service and carried to storage, a request without it refused | P2 (T1, with row-level security) |
| [REQ-T02-02](../../../03-technical/t02-identity-and-access/requirements/req-t02-02-policies-one-library.md) | The one policy library interface `allowed(user, action, record)` of [I-T02-02](../../../03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md), with a deny-by-default policy | P2 (T2) |
| [REQ-T05-01](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md) | OpenAPI generated from the code of `platform`, served by it, the version in the path | P2 (T5, behind the gateway of [I-T05-01](../../../03-technical/t05-api-and-webhooks/interfaces/i-t05-01-api-gateway.md)) |
| [REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) | problem+json bodies carrying the error codes of [D122](../../../06-decisions/ux/d122-error-message-standard.md), no secret in them | P2 (T5) |
| [REQ-T05-05](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md) | The contract check: a field removed fails CI, a field added passes | P2 (T5, every service) |
| [REQ-T09-02](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md) | Compose and Helm from the same images, skeletons that install `platform` and the back office | P2 (T9) |
| [REQ-T09-03](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md) | The laptop profile and the installer's machine check, memory at rest measured for the P0 stack | P2 (T9, once the whole stack exists) |
| [REQ-T09-08](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md) | The Terraform layout `modules/`, `ovhcloud/`, `scaleway/` behind one interface, validated in CI | P2 (T9) |
| [REQ-T10-01](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md) | Translation catalogues in French and English, a missing key failing CI | P2 (T10, with the review workflow) |
| [REQ-T10-03](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md) | Money as an exact decimal with its currency in `erp_models` | P2 (T10 and T11, rounding by pack) |
| [REQ-T11-02](../../../03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md) | The rules library reading a value by the date of the fact ([I-T11-01](../../../03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md)) | P2 (T11, with signed packs of [REQ-T11-01](../../../03-technical/t11-legal-corpora/requirements/req-t11-01-signed-packs.md)) |

**Technical design pages**

| Page | What P0 builds from it |
| --- | --- |
| [Repository layout](../../../../technical/architecture/repository-layout.md) | The folders and the uv and pnpm workspaces ([D438](../../../06-decisions/technical/d438-repository-layout.md)) |
| [Architecture](../../../../technical/architecture/architecture.md) | One service per business domain, the outbox per service, the metering gateway, country packs read by one library ([D405](../../../06-decisions/technical/d405-architecture-and-scalability.md)) |
| [Back end](../../../../technical/architecture/backend.md) | FastAPI, OpenAPI from the code, the service kit, business rules as pure functions ([D406](../../../06-decisions/technical/d406-back-end.md)) |
| [Front end](../../../../technical/architecture/frontend.md) | Vue 3, TypeScript, Vite, Pinia, components on the design tokens ([D407](../../../06-decisions/technical/d407-front-end.md)) |
| [Configuration](../../../../technical/architecture/configuration.md) | `conf/app.yaml` with every default, overridden by environment variables or Helm values, secrets by name only ([D413](../../../06-decisions/technical/d413-configuration-layers.md), [D240](../../../06-decisions/security-and-compliance/d240-credential-vault.md)) |
| [API](../../../../technical/interfaces/api.md) | `/v1`, problem+json, idempotency keys and cursor paging conventions in the base models ([D410](../../../06-decisions/technical/d410-api-style-and-auth.md), [REQ-T05-02](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md)) |
| [CI/CD and stages](../../../../technical/delivery/ci-cd-and-stages.md) | The existing pipeline now finds packages, images, `compose.e2e.yaml`, Playwright and Bruno ([D419](../../../06-decisions/technical/d419-ci-cd-and-registry.md)) |
| [Tests and traceability](../../../../technical/delivery/tests-and-traceability.md) | Test helpers, synthetic data only, Playwright and Bruno scaffolds ([D426](../../../06-decisions/technical/d426-testing-strategy.md)) |
| [Release and versioning](../../../../technical/delivery/release-and-versioning.md) | Every package and image carries the product's semantic version ([D423](../../../06-decisions/technical/d423-release-train-and-lts.md)) |
| [Deployment](../../../../technical/infrastructure/deployment.md) and [Infrastructure deployment](../../../../technical/infrastructure/infrastructure.md) | Compose and Helm from the same images, Terraform modules per cloud behind one interface ([D421](../../../06-decisions/technical/d421-infrastructure-cncf.md)) |
| [Performance and capacity](../../../../technical/infrastructure/performance-and-capacity.md) | The laptop profile within 8 GB, measured ([D408](../../../06-decisions/technical/d408-performance-and-profiles.md)) |
| [Observability](../../../../technical/operations/observability.md) | Logs tagged with the service, the company as an opaque id and the request ([D416](../../../06-decisions/technical/d416-observability-design.md)) |
| [Supply chain and licences](../../../../technical/security/supply-chain-and-licences.md) | Pinned dependencies in both locks, licences compatible with AGPL-3.0 ([D415](../../../06-decisions/technical/d415-supply-chain-controls.md)) |

**UX pages:** [Visual identity](../../../04-ux/visual-identity/README.md) ([colours](../../../04-ux/visual-identity/colours.md),
[typography](../../../04-ux/visual-identity/typography.md), [logo](../../../04-ux/visual-identity/logo.md)),
[Tokens](../../../04-ux/design-system/tokens.md), [C-08 Navigation](../../../04-ux/design-system/components/c-08-navigation.md),
[Error messages](../../../04-ux/design-system/patterns/error-messages.md),
[Responsive](../../../04-ux/design-system/responsive.md), [Accessibility](../../../04-ux/design-system/accessibility.md);
decisions [D41](../../../06-decisions/ux/d41-indigo-primary.md), [D42](../../../06-decisions/ux/d42-density-per-role.md), [D43](../../../06-decisions/ux/d43-light-and-dark.md), [D44](../../../06-decisions/ux/d44-typefaces.md), [D45](../../../06-decisions/ux/d45-lucide-icons.md), [D46](../../../06-decisions/ux/d46-accessibility-standard.md), [D47](../../../06-decisions/ux/d47-app-shell.md), [D122](../../../06-decisions/ux/d122-error-message-standard.md).

**Non-functional requirements:** [installation](../../../05-non-functional/installation.md),
[performance](../../../05-non-functional/performance.md), [localisation](../../../05-non-functional/localisation.md),
[accessibility](../../../05-non-functional/accessibility.md), [security](../../../05-non-functional/security.md),
[observability](../../../05-non-functional/observability.md).

**Out of scope:** Keycloak and sign-in ([REQ-T02-01](../../../03-technical/t02-identity-and-access/requirements/req-t02-01-keycloak-sign-in.md)), the gateway, one database per company ([D19](../../../06-decisions/foundations/d19-one-database-per-company.md),
[REQ-T01-01](../../../03-technical/t01-companies-and-data-isolation/requirements/req-t01-01-company-stores.md)) with row-level security, the event bus itself, the metering service, signed country packs, the customer
and supplier portals and the mobile app: P2 and later phases. The back-office shell has no business screen.

## <a id="epics"></a>🪜 Epics

The folder names of the libraries under `backend/shared/` (`lifecycle`, `logging`, `config`, `context`, `outbox`,
`metering`, `country-rules`, `testing`) and of the packages under `frontend/packages/` (`config`, `tokens`, `ui`,
`i18n`, `api-client`) are (Proposed): the specifications name what they hold, not their folders.

| ID | Epic | Delivers | Where | Tickets | Parallel tasks for the agents |
| --- | --- | --- | --- | --- | --- |
| E0.1 | Layout and conventions | The folders and workspaces of [D438](../../../06-decisions/technical/d438-repository-layout.md); the convention tests and front-end lint rules extended to them | Repository root, `tests/conventions`, `frontend/packages/config` | 2: T0.01 to T0.02 | Folder skeletons with their READMEs; uv members and pnpm workspace; import rules of `backend/shared` and `plugins`; eslint and strict TypeScript settings |
| E0.2 | Shared models | `erp_models`: base model, money, ids and times, enums, `SE` exceptions and the [D122](../../../06-decisions/ux/d122-error-message-standard.md) error codes | `backend/models` | 2: T0.03 to T0.04 | Base model and its six tests; money and paging models; exception packages; error code catalogue |
| E0.3 | Service kit | The libraries of [Back end](../../../../technical/architecture/backend.md): lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers | `backend/shared/<lib>` | 7: T0.05 to T0.06, T0.09 to T0.13 | One library per agent: each has its own folder, tests and pyproject |
| E0.4 | First service and contracts | `backend/services/platform`, its image, its OpenAPI, the contract check, the typed client and the Bruno collection ([REQ-T05-01](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md), [REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md), [REQ-T05-05](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)) | `backend/services/platform`, `frontend/packages/api-client`, `bruno/`, `.github/` | 4: T0.14, T0.18, T0.20, T0.24 | Layers and factories; Dockerfile; OpenAPI export and diff; client generator; Bruno generator |
| E0.5 | Run anywhere | `compose.e2e.yaml`, the Compose profiles, the laptop check, the Helm and Terraform skeletons ([REQ-T09-02](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md), [REQ-T09-03](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md), [REQ-T09-08](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md)) | `infra/compose`, `infra/helm`, `infra/terraform` | 4: T0.08, T0.19, T0.21, T0.25 | Terraform modules per cloud; Helm charts per image; Compose profiles; installer check and memory measure |
| E0.6 | Back-office foundation | Tokens, base components, i18n, the app shell, the error pattern on screen and the Playwright scaffold ([D407](../../../06-decisions/technical/d407-front-end.md), [D47](../../../06-decisions/ux/d47-app-shell.md), [D43](../../../06-decisions/ux/d43-light-and-dark.md), [D21](../../../06-decisions/foundations/d21-languages.md), [D122](../../../06-decisions/ux/d122-error-message-standard.md)) | `frontend/packages/<pkg>`, `frontend/backoffice` | 6: T0.07, T0.15 to T0.17, T0.22 to T0.23 | Token generator; components; catalogues; sidebar and top bar; Playwright configuration |

**Total: 6 epics, 25 tickets.**

## <a id="sprints"></a>🗓️ Sprint plan

Sprints last two weeks, the Christmas fortnight (21 December 2026 to 1 January 2027) left out, as in every phase of
the [phases](README.md#phases) table; S04 ends on Friday 12 February 2027 and P1 starts on Monday 15 February.

| Sprint | Dates | Tickets | Sprint goal | What can be shown |
| --- | --- | --- | --- | --- |
| [S01](#s01) | 7 to 18 Dec 2026 | T0.01 Mono-repo folders and workspaces · T0.02 Conventions for the shared libraries and the front ends · T0.03 Shared base model and enums · T0.04 SE exceptions and error codes · T0.05 Lifecycle and factories library · T0.06 Logging and configuration library · T0.07 Design tokens package · T0.08 Terraform module skeletons | The layout, its rules and the first shared code | A clean clone installs both workspaces; a broken sample package fails the conventions; the tokens build in light and dark |
| [S02](#s02) | 4 to 15 Jan 2027 | T0.09 Company context and rights middleware · T0.10 Event outbox library · T0.11 Metering client · T0.12 Country-pack rules library · T0.13 Test helpers library · T0.14 Platform service skeleton and image · T0.15 Base UI components | The service kit and the first service | `platform` answers in its container; a request without a company is refused; an outbox event survives a restart |
| [S03](#s03) | 18 to 29 Jan 2027 | T0.16 Internationalisation base · T0.17 Back-office app shell · T0.18 OpenAPI generation and contract check · T0.19 Helm umbrella chart skeleton · T0.20 Typed API client package | The contracts and the shell | The shell in light and dark, in French and English; a removed field fails CI |
| [S04](#s04) | 1 to 12 Feb 2027 | T0.21 Compose stack and its profiles · T0.22 Playwright scaffold against the real images · T0.23 Error messages on screen · T0.24 Bruno collection scaffold · T0.25 Laptop profile check and memory measure | Foundations ready | The [demo](#demo) of this page |

**Total: 25 tickets** (S01 8, S02 7, S03 5, S04 5).

### <a id="s01"></a>S01, 7 to 18 December 2026: layout, rules and first shared code

| Ticket | Delivers | Where | Done when |
| --- | --- | --- | --- |
| T0.01 Mono-repo folders and workspaces | Every folder of the layout of [D438](../../../06-decisions/technical/d438-repository-layout.md) ([Repository layout](../../../../technical/architecture/repository-layout.md)), each with a README saying what it holds; the uv workspace members (Python 3.13, [D406](../../../06-decisions/technical/d406-back-end.md)); the pnpm workspace (`package.json`, `pnpm-workspace.yaml`, `pnpm-lock.yaml`, Node 22, [D407](../../../06-decisions/technical/d407-front-end.md)); [Configuration](../../../../technical/architecture/configuration.md) and README updated | `backend/models`, `backend/shared`, `backend/services`, `frontend/backoffice`, `frontend/mobile`, `frontend/packages`, `plugins`, `sdk`, `infra/compose`, `infra/helm`, `infra/terraform`, `packs/countries`, `packs/sectors`, `docs` | `uv sync --locked` and `pnpm install --frozen-lockfile` pass from a clean clone ([D415](../../../06-decisions/technical/d415-supply-chain-controls.md): both locks pinned); CI's change detection lists the new folders; the README's quick start works |
| T0.02 Conventions for the shared libraries and the front ends | `tests/conventions/` extended to the D438 rules a test can enforce: `erp_models` imports no library or service, `backend/shared` imports `erp_models` and other libraries but never a service, `plugins/` and `sdk/` import only `erp_models`; the front ends' shared eslint and strict TypeScript settings in `frontend/packages/config` | `tests/conventions`, `frontend/packages/config` | A deliberately broken fixture fails each new rule once ([AGENT.md](../../../../../AGENT.md), "Rules a test enforces"); adding an empty library or front-end package needs no change to the tests ([D438](../../../06-decisions/technical/d438-repository-layout.md)) |
| T0.03 Shared base model and enums | `erp_models`: the base model (extra fields forbidden, frozen where it must not change), ids, UTC times, the company id of [E-T01-01](../../../03-technical/t01-companies-and-data-isolation/data/e-t01-01-company.md) as an opaque type, money as an exact decimal with its currency ([REQ-T10-03](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)), the cursor page and idempotency key models of [REQ-T05-02](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md), `StrEnum` conventions, `YamlCatalog` | `backend/models` | Each model has the six model tests of AGENT.md; a sum of money lines has no float error ([REQ-T10-03](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md) criterion 2); conventions pass |
| T0.04 SE exceptions and error codes | The `SE` exception bases of AGENT.md ("Exceptions") and the error code catalogue of the pattern of [D122](../../../06-decisions/ux/d122-error-message-standard.md) ([Error messages](../../../04-ux/design-system/patterns/error-messages.md)): each code with its title key, its why key, its action key and its support reference, as data in `conf/catalogs/` | `backend/models` | Every code resolves to its three message keys and its reference; an unknown code is refused by the catalogue's model; no message holds a secret ([REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) criterion 2) |
| T0.05 Lifecycle and factories library | `Runnable` and `AsyncRunnable` (`initialize`, `run`, `close`, `execute`) and the abstract factory base of AGENT.md ("Lifecycle and factories") | `backend/shared/lifecycle` | `execute()` closes after a failed `initialize`; the convention test that requires a lifecycle base accepts its subclasses; tests pass |
| T0.06 Logging and configuration library | The logging setup of `conf/logger.yaml` (coloured console and rotating file, JSON lines for collection, each line tagged with the service, the company as an opaque id and the request, [D416](../../../06-decisions/technical/d416-observability-design.md)); configuration loading of `conf/app.yaml` with every default, overridden by environment variables ([D413](../../../06-decisions/technical/d413-configuration-layers.md)), `_key` fields naming vault entries only ([D240](../../../06-decisions/security-and-compliance/d240-credential-vault.md)) | `backend/shared/logging`, `backend/shared/config` | An environment variable overrides a default; a `_key` value never appears in a log; a log line carries the three tags; tests pass |
| T0.07 Design tokens package | The colour, spacing, density, typography, radius and elevation tokens of [Tokens](../../../04-ux/design-system/tokens.md), generated from [Colours](../../../04-ux/visual-identity/colours.md) and [Typography](../../../04-ux/visual-identity/typography.md) into CSS variables and a TypeScript module, light and dark ([D41](../../../06-decisions/ux/d41-indigo-primary.md), [D42](../../../06-decisions/ux/d42-density-per-role.md), [D43](../../../06-decisions/ux/d43-light-and-dark.md)); the three typefaces served by the package itself ([D44](../../../06-decisions/ux/d44-typefaces.md)) | `frontend/packages/tokens` | Changing a value in the token source changes the build output; every text colour pair meets the contrast of [Colours](../../../04-ux/visual-identity/colours.md) ([D46](../../../06-decisions/ux/d46-accessibility-standard.md)), checked by a test; no font is fetched from a third party |
| T0.08 Terraform module skeletons | `infra/terraform/modules/` (network, Kubernetes cluster, storage, registry, DNS, Helm release) behind one interface, and the `ovhcloud/` and `scaleway/` roots calling them ([REQ-T09-08](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md), [D421](../../../06-decisions/technical/d421-infrastructure-cncf.md)); state kept outside the repository | `infra/terraform` | `terraform fmt -check` and `terraform validate` pass on both roots in CI; the two roots differ only in their provider module; no credential in a file |

### <a id="s02"></a>S02, 4 to 15 January 2027: the service kit and the first service

| Ticket | Delivers | Where | Done when |
| --- | --- | --- | --- |
| T0.09 Company context and rights middleware | The middleware that reads the company and the user of each request and carries them to the service and storage layers ([REQ-T01-02](../../../03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md)); the rights interface `allowed(user, action, record)` of [I-T02-02](../../../03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md) with a deny-by-default policy ([REQ-T02-02](../../../03-technical/t02-identity-and-access/requirements/req-t02-02-policies-one-library.md)); refusals as problem+json with their code ([REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)) and logged for the audit ([REQ-T02-06](../../../03-technical/t02-identity-and-access/requirements/req-t02-06-refusals-audited.md)) | `backend/shared/context` | A request without a company is refused ([REQ-T01-02](../../../03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md) criterion 1); the same user, action and record give the same decision from HTTP and from a direct call ([REQ-T02-02](../../../03-technical/t02-identity-and-access/requirements/req-t02-02-policies-one-library.md) criterion 1); every refusal is logged with its code |
| T0.10 Event outbox library | The outbox of [Architecture](../../../../technical/architecture/architecture.md) ([D405](../../../06-decisions/technical/d405-architecture-and-scalability.md)): an event written in the same transaction as the change, a relay that publishes it at least once behind a publisher interface, an event envelope in `erp_models`; the audit writer of [I-T03-01](../../../03-technical/t03-audit-trail/interfaces/i-t03-01-audit-writer.md) will use it | `backend/shared/outbox` | An event written then the process stopped is published after the restart; a rolled-back change publishes nothing; a test publisher stands in for the bus (chosen in P2) |
| T0.11 Metering client | The client every paid call goes through (TC-21, [Architecture](../../../../technical/architecture/architecture.md)): budget check, reservation, call, settlement and a usage event through the outbox; a legal-duty flag that bypasses the stop | `backend/shared/metering` | Against a stand-in metering server: a call over budget is refused before it is made, a settled call emits one usage event, a legal-duty call passes an exhausted budget |
| T0.12 Country-pack rules library | The rules library of [I-T11-01](../../../03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md), `value(rule, country, date)`, reading a pack catalogue of values with validity dates ([REQ-T11-02](../../../03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md)); money values exact ([REQ-T10-03](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)) | `backend/shared/country-rules` | With a test pack: last year's fact gets last year's value and a future-dated value applies from its date ([REQ-T11-02](../../../03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md) criteria 1 and 2); tests per date as [REQ-T11-06](../../../03-technical/t11-legal-corpora/requirements/req-t11-06-tests-per-date.md) asks |
| T0.13 Test helpers library | The helpers of [Tests and traceability](../../../../technical/delivery/tests-and-traceability.md) ([D426](../../../06-decisions/technical/d426-testing-strategy.md)): a local HTTP stand-in server, a PostgreSQL test server started per session, a company-context fixture, log capture, synthetic data builders; no mock library | `backend/shared/testing` | The kit's own tests use them; a stand-in's default answer is a valid empty value of the real model (TEST-2); no production data in any fixture |
| T0.14 Platform service skeleton and image | `backend/services/platform` as an AGENT.md service (`api`, `service`, `storage`, `models` under its own package, factories, `conf/app.yaml`), FastAPI under `/v1` with a health endpoint, the problem+json handler of [REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md), the context middleware; its multi-stage Dockerfile with the repository root as context ([D419](../../../06-decisions/technical/d419-ci-cd-and-registry.md)) | `backend/services/platform` | The image builds in CI and starts; the health call answers; a refused call returns problem+json with its [D122](../../../06-decisions/ux/d122-error-message-standard.md) code ([REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) criterion 1); conventions pass on the new service with no change to them |
| T0.15 Base UI components | `frontend/packages/ui` on the tokens: button, form field, navigation item, toast, modal and card, light and dark, keyboard reachable with visible focus ([D46](../../../06-decisions/ux/d46-accessibility-standard.md)), Lucide icons served by the package ([D45](../../../06-decisions/ux/d45-lucide-icons.md)) | `frontend/packages/ui` | Vitest component tests pass in both themes; an automated accessibility check finds no violation on each component ([Accessibility](../../../04-ux/design-system/accessibility.md)) |

### <a id="s03"></a>S03, 18 to 29 January 2027: contracts and the shell

| Ticket | Delivers | Where | Done when |
| --- | --- | --- | --- |
| T0.16 Internationalisation base | `frontend/packages/i18n`: message catalogues per language, French and English at launch ([D21](../../../06-decisions/foundations/d21-languages.md), [Localisation](../../../05-non-functional/localisation.md)), dates, numbers and money formatted per locale, the user's language applied without reloading; a check that fails when a key misses in one language ([REQ-T10-01](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md)); the review workflow comes in P2 | `frontend/packages/i18n` | A key added in English only fails CI; switching language re-renders a component; money keeps its exact decimals when formatted ([REQ-T10-03](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)) |
| T0.17 Back-office app shell | `frontend/backoffice`: Vue 3, Vite, Pinia and the router ([D407](../../../06-decisions/technical/d407-front-end.md)); the app shell of [D47](../../../06-decisions/ux/d47-app-shell.md) and [C-08 Navigation](../../../04-ux/design-system/components/c-08-navigation.md): the collapsible sidebar with the [symbol](../../../../assets/symbol.svg), the top bar with places for search, the assistant ([D49](../../../06-decisions/ux/d49-assistant-side-panel.md)), notifications, the site switcher and the user menu; the bottom tab bar on phones ([Responsive](../../../04-ux/design-system/responsive.md)); light and dark following the device with a manual switch ([D43](../../../06-decisions/ux/d43-light-and-dark.md)); the "skip to content" link and `aria-current` ([D46](../../../06-decisions/ux/d46-accessibility-standard.md)); its own image | `frontend/backoffice` | Its Vitest tests pass; the shell renders in both themes and both languages; the sidebar collapses to icons; the image builds in CI. Its screens are listed for the Playwright tests of T0.22 (TKT-21) |
| T0.18 OpenAPI generation and contract check | The OpenAPI document of `platform` generated from its code and served by it ([REQ-T05-01](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md) criterion 1, [I-T05-02](../../../03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md)), committed, and a CI check that fails when it is stale or when a change breaks it ([REQ-T05-05](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)) | `backend/services/platform`, `.github` | A removed field fails CI and an added one passes ([REQ-T05-05](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md) criteria 1 and 2); a stale document fails CI |
| T0.19 Helm umbrella chart skeleton | `infra/helm`: an umbrella chart and one chart per image (`platform`, `backoffice`), values with every default written out, the image tag from the commit, no secret in values ([REQ-T09-02](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md), [D421](../../../06-decisions/technical/d421-infrastructure-cncf.md)) | `infra/helm` | `helm lint` and `helm template` pass in CI; the rendered manifests validate against the Kubernetes schemas; the same images as Compose |
| T0.20 Typed API client package | `frontend/packages/api-client` generated from the OpenAPI of T0.18 ([D406](../../../06-decisions/technical/d406-back-end.md): clients generated from the contract), problem+json mapped to a typed error with its [D122](../../../06-decisions/ux/d122-error-message-standard.md) code | `frontend/packages/api-client` | The generated client is up to date in CI or the build fails; a type check catches a renamed field; a refused call gives its code to the caller |

### <a id="s04"></a>S04, 1 to 12 February 2027: end to end

| Ticket | Delivers | Where | Done when |
| --- | --- | --- | --- |
| T0.21 Compose stack and its profiles | `compose.e2e.yaml` at the root starting the real images (`platform`, `backoffice`, PostgreSQL) for Playwright and the stages ([CI/CD and stages](../../../../technical/delivery/ci-cd-and-stages.md)); the laptop and one-server profiles in `infra/compose/` from the same images ([D408](../../../06-decisions/technical/d408-performance-and-profiles.md), [D421](../../../06-decisions/technical/d421-infrastructure-cncf.md), [REQ-T09-02](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md) criterion 1, [D18](../../../06-decisions/foundations/d18-installation.md)) | `infra/compose` | `docker compose -f compose.e2e.yaml up --wait` passes in CI's images job and in `stage.yml`; the one-server profile starts with one command ([Installation](../../../05-non-functional/installation.md)) |
| T0.22 Playwright scaffold against the real images | `frontend/backoffice/e2e/`: the Playwright configuration (trace, video and screenshot kept on failure), the first `@smoke` tests of the shell in light and dark, in French and English, and an accessibility check, run against `compose.e2e.yaml` (TKT-21, [D426](../../../06-decisions/technical/d426-testing-strategy.md)) | `frontend/backoffice` | `.github/scripts/playwright.sh` runs them in CI and in `stage.yml`; a failure uploads the HTML report; the shell's screens of T0.17 each have a test |
| T0.23 Error messages on screen | The pattern of [D122](../../../06-decisions/ux/d122-error-message-standard.md) ([Error messages](../../../04-ux/design-system/patterns/error-messages.md)) as a component: title, why, the action button, the faulty field highlighted and the small support reference, from the problem+json code through the API client and the catalogues of T0.16, in both languages | `frontend/packages/ui`, `frontend/backoffice`, `frontend/packages/i18n` | A refused call of `platform` shows its title, why and action in French and in English, with its reference; a Playwright test proves it against the real images |
| T0.24 Bruno collection scaffold | `bruno/platform/` generated from the OpenAPI of `platform` ([D406](../../../06-decisions/technical/d406-back-end.md): the Bruno collection generated from the contract), with tests on the health call and on one refused call ([REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)); no credential in a committed file (TEST-1) | `backend/services/platform`, `.github` | `stage.yml` runs it headless on dev and keeps its JUnit and JSON reports; a stale collection fails CI |
| T0.25 Laptop profile check and memory measure | The installer's machine check of [REQ-T09-03](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md) (memory, cores, disk against the 8 GB budget of [D408](../../../06-decisions/technical/d408-performance-and-profiles.md)) and a measure of the memory at rest of the P0 stack on the laptop profile, written to [Performance and capacity](../../../../technical/infrastructure/performance-and-capacity.md); Milvus left out when the AI is off ([REQ-T08-01](../../../03-technical/t08-rag-platform/requirements/req-t08-01-milvus-collections.md), [D22](../../../06-decisions/foundations/d22-no-graphics-card-needed.md)) | `infra/compose` | A machine under the budget installs and a machine too small is told so ([REQ-T09-03](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md) criteria 1 and 2, with a simulated machine); the measured memory at rest is recorded with its date; the 8 GB promise itself waits for the whole stack (P2) |

## <a id="demo"></a>🎤 Demo

On Friday 29 January 2027, a [SimpleERP maintainer](../../../01-users/personas/u47-simpleerp-maintainer.md) shows:

1. **A clean clone.** `uv sync --locked` and `pnpm install --frozen-lockfile` install both workspaces; the folders of
   [D438](../../../06-decisions/technical/d438-repository-layout.md) are there, each with its README.
2. **The rules hold.** A sample library that imports a service fails `tests/conventions/`; an empty new library passes
   with no change to the tests.
3. **One service, contract first.** `docker compose -f compose.e2e.yaml up --wait` starts `platform`, the back office
   and PostgreSQL. `/v1/health` answers; the OpenAPI is served ([REQ-T05-01](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md)); a call without a company is refused
   with a problem+json body and its code ([REQ-T01-02](../../../03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md), [REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)).
4. **The contract guards itself.** A pull request that removes a field fails the contract check; one that adds a field
   passes ([REQ-T05-05](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)). The typed client and the Bruno collection follow the document.
5. **The shell.** The back office opens with its sidebar and the symbol, in light then dark mode, in English then
   French ([D47](../../../06-decisions/ux/d47-app-shell.md), [D43](../../../06-decisions/ux/d43-light-and-dark.md), [D21](../../../06-decisions/foundations/d21-languages.md)); the refused call shows the error pattern of [D122](../../../06-decisions/ux/d122-error-message-standard.md) with its action and its
   reference.
6. **Measured and packaged.** The Playwright and Bruno reports of the dev stage; `helm template` of the umbrella chart;
   `terraform validate` on the OVHcloud and Scaleway roots; the memory at rest of the laptop profile, and the installer
   refusing a machine that is too small ([REQ-T09-03](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md)).

## <a id="exit"></a>🚪 Exit criteria

**Layout and rules**

- [ ] Every folder of [D438](../../../06-decisions/technical/d438-repository-layout.md) exists; both workspaces install from a clean clone with their locks ([D415](../../../06-decisions/technical/d415-supply-chain-controls.md)).
- [ ] `tests/conventions/` enforces the import rules of `backend/shared`, `plugins/` and `sdk/`, and covers a new
  library or service without change.

**Shared code**

- [ ] `erp_models` holds the base model, money ([REQ-T10-03](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)), paging and idempotency ([REQ-T05-02](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-02-paging-and-idempotency.md)), the `SE`
  exceptions and the [D122](../../../06-decisions/ux/d122-error-message-standard.md) error codes, each model with its six tests.
- [ ] The eight libraries of `backend/shared/` pass their tests and hold no business rule ([D406](../../../06-decisions/technical/d406-back-end.md)).
- [ ] A request without a company is refused ([REQ-T01-02](../../../03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md) criterion 1); rights go through `allowed(user, action,
  record)` ([I-T02-02](../../../03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md)).
- [ ] The rules library returns the value in force at the date of the fact ([REQ-T11-02](../../../03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md)).

**Service and contracts**

- [ ] `platform` serves its generated OpenAPI ([REQ-T05-01](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md) criterion 1) and problem+json errors ([REQ-T05-03](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)).
- [ ] CI fails on a removed field and passes on an added one ([REQ-T05-05](../../../03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)); the typed client and the Bruno collection
  are generated from the same document ([D406](../../../06-decisions/technical/d406-back-end.md)).

**Packaging**

- [ ] `compose.e2e.yaml` and the one-server profile start the real images; the Helm umbrella chart renders the same
  images ([REQ-T09-02](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-02-compose-and-helm.md)).
- [ ] Both Terraform roots validate in CI ([REQ-T09-08](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-08-terraform-ovhcloud-scaleway.md)).
- [ ] The installer's check refuses a machine below the budget, and the P0 stack's memory at rest is measured
  ([REQ-T09-03](../../../03-technical/t09-install-backups-and-updates/requirements/req-t09-03-laptop-profile.md)).

**Front end**

- [ ] The back-office shell follows [D47](../../../06-decisions/ux/d47-app-shell.md) and [C-08 Navigation](../../../04-ux/design-system/components/c-08-navigation.md),
  in light and dark ([D43](../../../06-decisions/ux/d43-light-and-dark.md)), in French and English ([D21](../../../06-decisions/foundations/d21-languages.md)), with the tokens of
  [Tokens](../../../04-ux/design-system/tokens.md); a missing translation fails CI ([REQ-T10-01](../../../03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md)).
- [ ] Errors are shown with the pattern of [D122](../../../06-decisions/ux/d122-error-message-standard.md).
- [ ] Playwright runs against the real images in CI and on the dev stage, with an accessibility check ([D46](../../../06-decisions/ux/d46-accessibility-standard.md)).

## <a id="dependencies"></a>⛓️ Dependencies

**Previous phases:** none: P0 is the first phase. It starts from the specifications of `docs/specs/` and from what was
set up on 2026-11-27: the Claude Code harness ([.claude/rules/tickets.md](../../../../../.claude/rules/tickets.md)), the
CI/CD pipeline of [CI/CD and stages](../../../../technical/delivery/ci-cd-and-stages.md) (`ci`, `python`, `typescript`,
`images`, `stage`, `release`, `automerge`, `gitflow`) and `tests/conventions/`.

**What P0 hands to the next phases**

| Phase | Takes from P0 |
| --- | --- |
| P1 DevOps agents | The layout and its conventions, `platform` as the template of a service, the scaffolds the agents' pull requests are checked with |
| P2 Platform core | `erp_models`, the service kit (context and rights for T1 and T2, outbox for T3, rules library for T11, metering for T7), the OpenAPI, client and Bruno generation for T5, the Compose, Helm and Terraform skeletons for T9, the i18n base for T10 |
| P3 and later | The back-office shell, the tokens and components every screen is built with, the error pattern, the Playwright scaffold |

## <a id="risks"></a>🎲 Risks

| Risk | Why it matters in P0 | Response in P0 |
| --- | --- | --- |
| Foundations that grow without end | P0 has no capability to show, so it can absorb any amount of work | Each library is the interface plus what its tests need; the full behaviour is named in the P2 capability that closes it (Scope table) |
| A library shape that P2 must undo | Context, rights, outbox and metering are written before Keycloak, the gateway, the bus and the metering service exist | Each library is written against an interface named in the specifications ([I-T02-02](../../../03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md), [I-T11-01](../../../03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md), [I-T03-01](../../../03-technical/t03-audit-trail/interfaces/i-t03-01-audit-writer.md), TC-21) with a stand-in behind it, so that P2 replaces the stand-in, not the interface |
| The 8 GB laptop budget | [D408](../../../06-decisions/technical/d408-performance-and-profiles.md) promises nothing before a measured prototype | T0.25 measures from the first stack and records it; the promise waits for the full stack in P2 |
| The event bus is not chosen | [Architecture](../../../../technical/architecture/architecture.md) says "for example NATS or Kafka" | The outbox publishes through an interface with a test publisher; the choice is made in P2 |

---

⬆️ [Phases](README.md) · 🗺️ [Roadmap](../roadmap.md)
