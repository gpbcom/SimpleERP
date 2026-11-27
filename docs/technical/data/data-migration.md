# Data migration

Imports from Odoo, Dolibarr, Sage, EBP and spreadsheets, at scale (D61). Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Importers (D424).** Importers for Odoo, Dolibarr, Sage, EBP and spreadsheets on day one, then others, all on one
mapping model (source field to SimpleERP field, with rules). A dry run on a copy shows what will be created, merged or
refused before anything is written; opening balances and history are imported; the assistant helps map unknown fields.
The guided onboarding (F21) runs them.

Decided in [D424](../../specs/06-decisions/technical/d424-importers.md).

Last reviewed: 2026-11-12 (GH-2)
