🏠 [Specs](../README.md) › ❓ [Questions](README.md) › ❓ Q13 E-invoicing platforms

# ❓ Q13 E-invoicing platforms

**Status:** ✅ answered

## Question

Which e-invoicing platforms (French registered platforms, PA) does simple-ERP connect to, so that invoices are submitted
and received automatically through an API? The owner asked for a benchmark of the API-compatible tools.

## Why it matters

It decides the connector F6 and F7 use to send and receive electronic invoices, and whether an IT provider can use one
platform for all its clients.

## Options

The benchmark of 2026-11-10 lists the platforms with a public API and the criteria a connector must meet:
[E-invoicing platforms](../05-non-functional/e-invoicing-platforms.md#benchmark). Because choice is free, simple-ERP can
support several platforms through one standard connector plus adapters.

## Owner

The owner of simple-ERP.

## Answer

Answered on 2026-11-12 by the owner: "Super PDP + B2BRouter, then more + Any platform through the AFNOR standards.
Document all of that very well." Super PDP and B2Brouter first, then more on demand, and any platform offering AFNOR XP
Z12-013 through one generic adapter; Chorus Pro for public buyers
([D454](../06-decisions/f08-accounting/d454-e-invoicing-platforms.md)).

---

⬅️ [Q12 Payslip availability period](q12-payslip-availability-period.md) · ⬆️ [Up](README.md) ·
➡️ [Q14 A law pack refresh that fails its test set](q14-failing-law-pack-refresh.md)
