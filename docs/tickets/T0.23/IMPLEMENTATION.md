# T0.23: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- A refusal shows its title, why, action and reference in French and English, and nothing from the raw body (D122 and REQ-T05-03, see the specifications of [PLAN.md](PLAN.md)).
- Texts follow the active language without a reload (D21), and messages are announced with the colour backed by an icon and words (D46).
- The e2e test runs against the real images, never a development server ([AGENT.md](../../../AGENT.md), "Front ends").
- [`AGENT.md`](../../../AGENT.md) has no rule for `frontend/` code beyond the `@simpleerp` scope, and the image is the multi-stage Dockerfile of [`frontend/backoffice/Dockerfile`](../../../frontend/backoffice/Dockerfile), built from the repository root.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How the proxy finds platform | nginx template with `ERP_PLATFORM_URL` and a run-time resolver | Fixed `http://platform:8000` | No URI rewriting, a DNS lookup every 10 s |
| [D2](#d2) | What the store holds | Message keys, params and a reference | The translated text or the problem body | Each text is looked up on render |
| [D3](#d3) | How the front end knows the D122 codes | Its own catalogue, tested against the back-end YAML | Reading the YAML at run time | Two copies to keep in step |
| [D4](#d4) | Where a refusal shows | Banner for the load check, dialog by default, field next to it | One presentation for all | Choice not stated by the pattern |
| [D5](#d5) | Something to refuse at start | A `/v1/health` check at start | No call in P0 | One request at every start |

## <a id="d1"></a>D1: How the proxy finds platform

**Chosen:** the `nginx-unprivileged` envsubst template with `ERP_PLATFORM_URL` and a resolver variable · **Where:** [`frontend/backoffice/nginx.conf:18-21`](../../../frontend/backoffice/nginx.conf#L18-L21) and [`frontend/backoffice/Dockerfile:18-20`](../../../frontend/backoffice/Dockerfile#L18-L20) · **Source:** K24

| Option | For | Against |
| --- | --- | --- |
| ✅ Template, `ERP_PLATFORM_URL`, run-time resolver | The upstream is set per deployment, for example a Helm release host. nginx starts when the host does not exist yet, so the image runs alone | `proxy_pass` through a variable does no URI rewriting. DNS is looked up every 10 s |
| Keep the fixed `http://platform:8000` | Simplest | nginx exits where no `platform` host exists (the image alone) and the address cannot change per deployment |
| Generate the config in a custom entrypoint script | Full control | More code to maintain than the base image's own template step |

**Trade-off:** the `/v1/` path goes through unchanged, which is all that is needed, and the value takes no path. The lookup cost is small.

**Revisit when:** a route needs rewriting, or the Helm chart sets the address (see the follow-ups of [EXPLAIN.md](EXPLAIN.md)).

## <a id="d2"></a>D2: What the store holds

**Chosen:** keys, params and a reference only · **Where:** [`frontend/backoffice/src/errors/Refusal.ts:7-17`](../../../frontend/backoffice/src/errors/Refusal.ts#L7-L17), [`toRefusal.ts:27-58`](../../../frontend/backoffice/src/errors/toRefusal.ts#L27-L58) · **Source:** read from the diff, [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ Keys and params | A language switch re-renders without replaying the call (D21). The raw body and detail are never stored (REQ-T05-03) | The outlet translates at each render |
| Store the translated text | Simpler to render | Stays in the old language after a switch |
| Store the problem body | Nothing is lost | Breaks the rule that the body is never kept |

**Trade-off:** `field` and `values` are read from the error object by a cast ([`toRefusal.ts:44`](../../../frontend/backoffice/src/errors/toRefusal.ts#L44)), because the typed client does not expose them yet (a follow-up in [PROGRESS.md](PROGRESS.md)).

**Revisit when:** the API client keeps `field` and `values`.

## <a id="d3"></a>D3: How the front end knows the D122 codes

**Chosen:** a copy in [`errorCatalog.ts`](../../../frontend/packages/i18n/src/errors/errorCatalog.ts), kept equal to the YAML by a test · **Source:** [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ Own catalogue plus a test | No run-time file read. The test fails on drift ([`errorCatalog.test.ts:26-29`](../../../frontend/packages/i18n/tests/errors/errorCatalog.test.ts#L26-L29)) | Two copies, and a `yaml` dev dependency |
| Read the YAML in the browser | One source | The YAML is back-end data, not served to the browser |

**Trade-off:** a new back-end code needs a front-end entry, and the test says so. **Revisit when:** a generated catalogue shared by both sides exists.

## <a id="d4"></a>D4: Where a refusal shows

**Chosen:** a banner for a call the user did not start, a dialog by default, the field when one is named · **Where:** [`platformClient.ts:26`](../../../frontend/backoffice/src/api/platformClient.ts#L26), [`toRefusal.ts:45-46`](../../../frontend/backoffice/src/errors/toRefusal.ts#L45-L46) · **Source:** [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ Three presentations by case | Follows the pattern ("a dialog or a banner") and D46 | The pattern does not say which one when, so the split is an assumption |
| Dialog for everything | One path | A background failure would interrupt the person |

**Revisit when:** the pattern page says which one when.

## <a id="d5"></a>D5: Something to refuse at start

**Chosen:** one `/v1/health` call at start · **Where:** [`main.ts:11`](../../../frontend/backoffice/src/main.ts#L11), [`checkPlatform.ts:7-18`](../../../frontend/backoffice/src/api/checkPlatform.ts#L7-L18) · **Source:** [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ A health check at start | The criterion "against the real images, a refused call shows the message" has a call to test. The e2e reroutes it to a call platform really refuses ([`refused-call.e2e.ts:11-12`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L11-L12)), so no response is faked | An extra request at every start |
| No call in P0 | No extra request | Nothing to show in the shell, nothing to test |

The plan asked the person to confirm this at approval. **Revisit when:** a real screen calls platform.

## 📝 Assumptions behind the choices

- K24 evidence by hand and the 8081 port: support [D1](#d1) (only evidence, no change of choice).
- "No screen" and no budget: support [D4](#d4) (the pattern is built in the shell, tested by Playwright).
