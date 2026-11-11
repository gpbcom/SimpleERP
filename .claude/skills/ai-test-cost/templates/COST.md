# AI test cost: ${ticket}

> Written by the `ai-test-cost` skill after every paid AI test run of this ticket. Do not edit it by hand: the next run overwrites it. The data is in the ledger `${ticket}.json` of the guard's state folder (`~/.local/state/ai-test-cost/` by default).

**Cap:** ${cap} · **Spent:** ${spent} · **Left:** ${remaining} · **Status:** ${status}

**Run status:** done, running, failed, killed at the cap, refused. A cost marked "not final" can still grow: the usage report arrives a few minutes late.

**Measured by:** `usage_report` (the Anthropic Admin API usage report), `estimate` (the run's own estimate, nothing measured), `charged` (a cost measured elsewhere, charged by hand).

Times are local, `YYYY-MM-DD HH:MM`. Costs in USD.

| Run | Status | Source | Label | Command | Started | Finished | Estimate | Cost | Cumulative | Left | Models |
|---|---|---|---|---|---|---|---|---|---|---|---|
${rows}

Prices: ${price_source}.
