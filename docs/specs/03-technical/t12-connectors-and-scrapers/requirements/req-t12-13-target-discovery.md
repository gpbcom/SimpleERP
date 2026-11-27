🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-13 Target discovery

# 📌 REQ-T12-13 Target discovery

**Status:** ✅ specified

## Statement

Each connector, scraper or browser task has a target: the address to go to. **Given:** when the customer provides it (a
portal URL, a login page, a site), it is used as given, after a check that it answers and is the expected kind of page.
**Not given:** the system discovers it, cheapest first: (1) a rule-based finder with no model: the company's own records
(the supplier's or partner's website field, links in emails and documents it may read), the tool's known addresses in
the connector catalogue, the site's sitemap and common paths (/login, /portal, /espace-client); (2) a discovery agent
that searches the web and reads candidate pages through the fetch service (REQ-T12-07), within a step cap and a cost
budget. It returns ranked candidates, each with its evidence (where it was found, what the page shows) and a confidence.
A candidate at 90 % confidence or more is used for public reading; any target that will receive credentials,
or below 90 %, needs a person's confirmation; the confirmed target is remembered for the next runs and rechecked when it
fails (REQ-T12-11).

## Why

Customers often know which tool they use, not its address; credentials sent to a wrong or spoofed domain would leak them
([D265](../../../06-decisions/f16-customer-support-agents/d265-target-discovery.md)).

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

1. **Given** a URL from the customer **when** the task starts **then** it is used and checked, with no search.
2. **Given** no URL and the supplier's website in its record **when** the task starts **then** the finder proposes its
   customer area from the site, without a model.
3. **Given** nothing in the records **when** discovery runs **then** the agent returns ranked candidates with evidence,
   within its budget.
4. **Given** a candidate login page **when** credentials would be used **then** a person confirms the domain first.
5. **Given** a confirmed target that starts failing **when** detected **then** discovery is proposed again.

## Measure

Share of targets found without a model; share confirmed at the first candidate; cost per discovery.

## Priority

Must

## Capabilities served

F16, F7 (supplier portals), F8 (bank and tax portals), F6, F15

## Tests

Fixtures of sites with and without sitemaps; a spoofed look-alike domain must never be confirmed
automatically.

## Open questions

None.

---

⬅️ [REQ-T12-12 Lawful collection](req-t12-12-lawful-collection.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-14 Every connector in the fewest steps](req-t12-14-fewest-steps.md)
