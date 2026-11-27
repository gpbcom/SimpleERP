<!-- Ticket template (TKT-2). Replace every {{NAME}} and delete these comments in the written ticket. -->
<!-- The ticket states only what the specifications and the roadmap state. Check it with check_ticket.py. -->

# {{ID}}: {{Title}}

**Status:** 🟡 Planned

## Roadmap

<!-- The phase page and the ticket anchor come from the roadmap row. -->

- **Ticket:** [{{ID}}](../../specs/00-vision/roadmap/phases/{{phase page}}#{{anchor}}) in [🛣️ {{Phase}}](../../specs/00-vision/roadmap/phases/{{phase page}})
- **Phase:** [🛣️ {{Phase}}](../../specs/00-vision/roadmap/phases/{{phase page}})
- **Sprint:** [{{Sprint}}](../../specs/00-vision/roadmap/phases/{{phase page}}#{{sprint anchor}}), {{dates}}: {{sprint goal}}
- **Epic:** [{{Epic}}](../../specs/00-vision/roadmap/phases/{{phase page}}#{{epic anchor}}): {{what the epic delivers}}

## What it delivers

<!-- Bullets, each one thing the ticket delivers, with a link to the design page or technical requirement it follows. -->

- {{What is delivered}}, as [{{Design page}}](../../technical/{{theme}}/{{page}}.md#{{heading anchor}}).

## Features, use cases and business rules

<!-- Every page of docs/specs/ whose file name carries an ID, its ID in the link text, as its title writes it. -->
<!-- Example: [📝 UC-F6-01: Capture and qualify a lead](../../specs/02-functional/f06-customers-and-sales/use-cases/01-lead-to-quote/uc-f06-01-capture-and-qualify-a-lead.md) -->
<!-- Likewise for business rules [📏 BR-F6-01: ...](.../business-rules/br-f06-01-<slug>.md), entities E-F6-01 -->
<!-- (data/e-f06-01-<slug>.md), flows FL-F6-01 (flows/fl-f06-01-<slug>.md), technical requirements REQ-T01-01 -->
<!-- (../../specs/03-technical/t01-<slug>/requirements/req-t01-01-<slug>.md) and decisions D438 -->
<!-- (../../specs/06-decisions/<theme>/d438-<slug>.md). The feature number is not padded in the ID (F6) and is in -->
<!-- the file name (f06). When the roadmap names none, write the line below and nothing else. -->

- {{The roadmap names no use case, business rule, entity, flow, requirement or decision for this ticket.}}

## Technical pages it builds on

<!-- Design pages of docs/technical/ or pages of a technical capability of docs/specs/03-technical/. -->

- [🏗️ {{Design page title}}](../../technical/{{theme}}/{{page}}.md#{{heading anchor}}): {{what the ticket takes from it}}.

## Screens touched

<!-- Link the page of every screen the ticket builds, its ID in the link text, or write the line saying the ticket
touches no screen. A ticket that changes a front end (frontend/) lists every screen it builds, and its plan has a
Playwright test task for them in frontend/<app>/e2e/ (TKT-21). The HTML mock-ups of each screen state are in
docs/specs/04-ux/mockups/src/. When it really builds none, write "- ➖ No screen: <why>" instead. -->

- [🖥️ S-F{{n}}-{{mm}}: {{Screen title}}](../../specs/02-functional/f{{nn}}-{{slug}}/screens/{{flow}}/s-f{{nn}}-{{mm}}-{{slug}}.md)
- {{The ticket touches no screen.}}

## Budgets touched

<!-- Link to the non-functional requirement pages whose measures the ticket must keep, or write the line saying none. -->

- [⏱️ {{Requirement}}](../../specs/05-non-functional/{{page}}.md#measures): {{the measure this ticket must keep}}.
- {{The ticket touches no budget.}}

## Acceptance criteria

<!-- One numbered item per criterion. Each names the business rule and the use case it verifies. -->
<!-- Format: **Given** {{context}}, **when** {{action}}, **then** {{result}}. (BR-F{{n}}-{{mm}}, UC-F{{n}}-{{mm}}) -->

1. **Given** {{context}}, **when** {{action}}, **then** {{result}}. ([📏 BR-F{{n}}-{{mm}}](../../specs/02-functional/f{{nn}}-{{slug}}/business-rules/br-f{{nn}}-{{mm}}-{{slug}}.md), [📝 UC-F{{n}}-{{mm}}](../../specs/02-functional/f{{nn}}-{{slug}}/use-cases/{{flow}}/uc-f{{nn}}-{{mm}}-{{slug}}.md))

## Out of scope

<!-- Bullets, each one linked to the ticket or page that takes it. -->

- {{What is not delivered here}}, see [{{ticket}}](../../specs/00-vision/roadmap/phases/{{phase page}}#{{anchor}}).

## Assumptions

<!-- Facts the specifications do not settle. Each one is an assumption the reviewer checks (TKT-8). -->

- {{The most conservative option taken, and why}}.
