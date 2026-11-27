# T0.17: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- Vue 3, Vite, Pinia and a router, per D407 and [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md) ([TICKET.md](TICKET.md)).
- Exactly one nav landmark at a time and the skip link first, `aria-current` on the current page (D46, criterion 6).
- Sidebar collapsed to icons, tab bar on phones, theme following the device with a manual override, French and English (criteria 2 to 7).
- One image per front end, built from the repository root (D438, criterion 8; [`AGENT.md`](../../../AGENT.md) CI/CD section). Images must pass Trivy.
- Tests mount the real app and need it independent of the browser history ([`createBackofficePlugins.ts:11-14`](../../../frontend/backoffice/src/app/createBackofficePlugins.ts#L11-L14)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Layout swap | Grid with `v-if` | Hide with CSS | Remount on resize |
| [D2](#d2) | Skip link | Click handler focusing main | Plain hash anchor | Needs JavaScript |
| [D3](#d3) | Mount time | After `router.isReady()` | Mount at once | Slightly later mount |
| [D4](#d4) | nginx base | Mainline unprivileged plus `apk upgrade` | `stable-alpine` | Less reproducible builds |
| [D5](#d5) | Workspace install | Two filters | One filter | More installed |
| [D6](#d6) | Package builds | Explicit steps | Graph filter | Manual update per package |
| [D7](#d7) | nginx config | `conf.d/default.conf` | Replace `nginx.conf` | No global directives |
| [D8](#d8) | Healthcheck | busybox `wget` | `curl` | None known |
| [D9](#d9) | Test typing of TABS | Explicit element type | Cast or `as const` | None |
| [D10](#d10) | Image documentation | Described as not built | Document as built, or omit | Wrong once K17 landed |
| [D11](#d11) | T0.22 link | Phase page | Ticket folder, or no link | Coarser link |
| [D12](#d12) | README shape | Prose and folder table | Mermaid diagram | No picture |

## <a id="d1"></a>D1: How the sidebar and tab bar swap

**Chosen:** a CSS grid with `v-if` · **Where:** [`AppShell.vue:22`](../../../frontend/backoffice/src/shell/AppShell.vue#L22) and [`:31`](../../../frontend/backoffice/src/shell/AppShell.vue#L31) · **Source:** K16

| Option | For | Against |
| --- | --- | --- |
| ✅ `v-if` in a grid with its own tab bar row | One `nav` landmark in the DOM, as the tests require; no padding on main | The component is recreated when the width crosses 768 px |
| Hide with CSS | No recreation | A hidden duplicate `nav` stays in the DOM |
| `position: fixed` tab bar and padded main | Familiar pattern | Padding to keep in step with the bar height |

**Trade-off:** state of the hidden component is lost on resize; the sidebar state lives in the store, so little is lost.

**Revisit when:** the tab bar gets state of its own, such as a badge count. The leftover `position: fixed` of [`BottomTabBar.vue:32`](../../../frontend/backoffice/src/shell/BottomTabBar.vue#L32) is a follow-up.

## <a id="d2"></a>D2: The skip link

**Chosen:** `preventDefault` then focus `#main-content` · **Where:** [`SkipLink.vue:6-9`](../../../frontend/backoffice/src/shell/SkipLink.vue#L6-L9) · **Source:** K16

| Option | For | Against |
| --- | --- | --- |
| ✅ Click handler | The URL does not change, so it does not fight the memory and web routers | Needs JavaScript |
| Plain hash anchor | No script | Changes the URL and conflicts with the router |

**Trade-off:** a router app already needs JavaScript. **Revisit when:** the router handles in-page hashes.

## <a id="d3"></a>D3: When the app mounts

**Chosen:** after `router.isReady()` · **Where:** [`main.ts:8-10`](../../../frontend/backoffice/src/main.ts#L8-L10) · **Source:** K16

| Option | For | Against |
| --- | --- | --- |
| ✅ Wait for the first navigation | The first paint shows the right route | Mount waits for the lazy route to load |
| Mount at once | Earliest paint | A flash of an empty page |

**Trade-off:** a short wait for no flash. **Revisit when:** a loading screen is specified.

## <a id="d4"></a>D4: The nginx base image

**Chosen:** `nginxinc/nginx-unprivileged:alpine` plus `apk upgrade` · **Where:** [`Dockerfile:14-17`](../../../frontend/backoffice/Dockerfile#L14-L17) · **Source:** K17

| Option | For | Against |
| --- | --- | --- |
| ✅ Mainline unprivileged | nginx 1.31.7 passes Trivy; runs non-root; `apk upgrade` fixes the zlib CVE | The tag moves, builds are less reproducible; needs a brief `USER root` |
| `stable-alpine` | A steadier tag | nginx 1.30.6 has 6 fixable HIGH CVEs that fail Trivy |
| `nginx:alpine` with a custom user | Official image | More to maintain for the non-root user |

**Trade-off:** reproducibility for a clean scan. **Revisit when:** images are pinned by digest (follow-up) or stable catches up.

## <a id="d5"></a>D5: Which workspace packages to install

**Chosen:** `--filter "./frontend/backoffice..." --filter "./frontend/packages/*"` · **Where:** [`Dockerfile:9`](../../../frontend/backoffice/Dockerfile#L9) · **Source:** K17

| Option | For | Against |
| --- | --- | --- |
| ✅ Two filters | Gets the dev dependencies the packages need for `vue-tsc` | Installs a bit more |
| Only the backoffice filter (the brief) | Smallest | Fails: workspace packages' dev dependencies are missing |
| Plain `pnpm install` | Simple | Also installs mobile and the portals |

**Trade-off:** a larger build stage only. **Revisit when:** a package the back office does not use appears under `frontend/packages/`.

## <a id="d6"></a>D6: Building the packages

**Chosen:** build tokens, ui, then the app by name · **Where:** [`Dockerfile:10-12`](../../../frontend/backoffice/Dockerfile#L10-L12) · **Source:** K17

| Option | For | Against |
| --- | --- | --- |
| ✅ Explicit steps | Deterministic; the exports of tokens and ui point to `dist/` | Must be edited when another package needs building |
| `--filter "./frontend/backoffice^..."` | Automatic | Did not build tokens before ui in this workspace |
| `pnpm -r run build` | Simple | Builds every front end |

**Trade-off:** manual upkeep. **Revisit when:** the graph filter orders the builds correctly, or more packages are needed.

## <a id="d7"></a>D7: Where the nginx server block goes

**Chosen:** `conf.d/default.conf`, with immutable `/assets/` and no-cache elsewhere · **Where:** [`Dockerfile:18`](../../../frontend/backoffice/Dockerfile#L18), [`nginx.conf:9-21`](../../../frontend/backoffice/nginx.conf#L9-L21) · **Source:** K17

| Option | For | Against |
| --- | --- | --- |
| ✅ Server block only | Keeps the image's tested main config, with pid and temp paths writable by non-root | Global directives cannot change |
| Replace `/etc/nginx/nginx.conf` | Full control | Must redo the non-root paths |

**Trade-off:** no global directives. **Revisit when:** a global setting is needed.

## <a id="d8"></a>D8: The healthcheck tool

**Chosen:** busybox `wget` · **Where:** [`Dockerfile:21-22`](../../../frontend/backoffice/Dockerfile#L21-L22) · **Source:** K17

| Option | For | Against |
| --- | --- | --- |
| ✅ `wget` | Already in the alpine base | None named |
| `curl` | Common | Absent from the image, so a package to install |

**Trade-off:** none known. **Revisit when:** the base image changes.

## <a id="d9"></a>D9: Typing the tab table in the test

**Chosen:** an explicit element type with `locale: 'en' | 'fr'` · **Where:** [`BottomTabBar.spec.ts:6`](../../../frontend/backoffice/tests/shell/BottomTabBar.spec.ts#L6) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ Explicit type | Clean call site, mutable arrays | A type to maintain |
| Cast at the call site | Short | Noise at every use |
| `as const` | Short | Makes the arrays readonly |

**Trade-off:** none worth noting. **Revisit when:** the table is shared with other tests.

## <a id="d10"></a>D10: How the README describes the image

**Chosen:** "not yet built", with the target command · **Where:** [`README.md:64-71`](../../../frontend/backoffice/README.md#L64-L71) · **Source:** K18

| Option | For | Against |
| --- | --- | --- |
| ✅ Not yet built | Matched the files K18 saw | K17 ran beside K18 and delivered the Dockerfile, so it is now wrong |
| Document as built | Matches the brief's wording | Would have described files K18 could not see |
| Omit | Short | Hides a D438 obligation |

**Trade-off:** the reviewer rejected the result and made it a follow-up. **Revisit when:** the follow-up is done. Open point: the plan did not order K17 before K18.

## <a id="d11"></a>D11: The T0.22 link

**Chosen:** link to the P0 phase page · **Where:** [`frontend.md:13`](../../../docs/technical/architecture/frontend.md#L13) · **Source:** K18

| Option | For | Against |
| --- | --- | --- |
| ✅ Phase page | It exists, so the link resolves | Not the ticket's own row; the `#s04` anchor is a follow-up |
| `docs/tickets/T0.22/` | Precise | No such folder yet |
| No link | No broken link | Loses the pointer |

**Trade-off:** a coarse link. **Revisit when:** T0.22 is planned.

## <a id="d12"></a>D12: README shape

**Chosen:** prose and a folder table · **Where:** [`README.md:31`](../../../frontend/backoffice/README.md#L31) · **Source:** K18

| Option | For | Against |
| --- | --- | --- |
| ✅ Prose and table | Easy to scan; keeps the existing shape | No picture |
| Mermaid diagram | Visual | Not asked for; would repeat D47 |
| Bullets only | Simple | Less scannable for folders |

**Trade-off:** no diagram. **Revisit when:** the shell gains more parts.

## 📝 Assumptions behind the choices

- K16: no focus-ring token, so `--color-primary`: supports [D1](#d1).
- K17: installing `frontend/packages/*` and building tokens then ui first: supports [D5](#d5) and [D6](#d6).
- K17: the unprivileged image's main config is kept: supports [D7](#d7).
- K18: T0.22 linked to the phase page: supports [D11](#d11).
