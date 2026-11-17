🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-16 Every integration shows its icon

# 📏 BR-F24-16 Every integration shows its icon

**Status:** 🔄 waiting for the owner

## Statement

Every integration shows its icon wherever it appears in the web interface (the catalogue, the connection screens, lists,
health, costs, the AI assistant's actions): the vendor's logo when its brand terms allow it, otherwise the Lucide icon
of its category (D45); the icon always has the integration's name as its accessible name and is never the only sign of a
state.

## Why

The owner's request in the round of 2026-11-12: "Also add icons in the web UI for the different integration" (D481).

## Examples

| Case | Result |
|---|---|
| HubSpot with a logo allowed by its brand terms, SVG | passes: logo shown |
| Connector whose brand terms forbid use | passes: category icon (banks: Lucide "landmark") (Proposed) |
| Logo without a dark-mode variant | passes: shown on a light tile in dark mode |
| Logo larger than (Proposed) 50 KB or not SVG or PNG | fails: refused in the icon library |
| Icon without accessible name | fails: refused |

## Applies to

- [UC-F24-21 Connect a bank, payment, shop, accounting or carrier tool](../use-cases/06-business-tools/uc-f24-21-connect-a-bank-payment-shop-accounting-or-carrier-tool.md)
- [UC-F24-25 Connect my own calendar and mail on the phone](../use-cases/07-employees-and-their-tools/uc-f24-25-connect-my-own-calendar-and-mail-on-the-phone.md)
- [UC-F24-27 Keep the integration icons](../use-cases/05-keep-the-catalogue/uc-f24-27-keep-the-integration-icons.md)
- [UC-F24-01 Browse the connector catalogue](../use-cases/01-find-and-connect/uc-f24-01-browse-the-connector-catalogue.md)
- [UC-F24-02 Connect a tool in the fewest steps](../use-cases/01-find-and-connect/uc-f24-02-connect-a-tool-in-the-fewest-steps.md)
- [UC-F24-14 Ask the AI assistant to act in a connected tool](../use-cases/04-run-and-control/uc-f24-14-ask-the-assistant-to-act-in-a-connected-tool.md)
- [UC-F24-15 Follow each connector's health and sync log](../use-cases/04-run-and-control/uc-f24-15-follow-each-connector-s-health-and-sync-log.md)

## Exceptions

None.

## Configurable

No; (Proposed) logos are shown at 24 px in lists and 40 px on the connector page, on a tile with 4 px padding, from SVG
or a PNG of at least 80 px.

## Open questions

None.

---

⬅️ [BR-F24-15](br-f24-15-the-e-invoicing-platform-connected-step-by-step.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-17](br-f24-17-an-ai-built-connector-runs-in-the-sandbox-first.md)
