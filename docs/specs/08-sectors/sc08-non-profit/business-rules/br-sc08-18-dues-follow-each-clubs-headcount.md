🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🤲 [SC08 Non-profit association](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC08-18 Dues follow each club's headcount

# 📏 BR-SC08-18 Dues follow each club's headcount

**Status:** ✅ specified

## Statement

The dues of a club follow its headcount: a fixed part plus an amount per licensed member declared for the season, at the
scale of the statutes. A club with no declaration pays the minimum and is flagged, and the votes of the club follow the
same headcount.

## Why

Dues not tied to the real headcount are disputed by clubs that pay for members they do not have, and the assembly's
votes must match the dues paid. The owner asked for federations
([D552](../../../06-decisions/sectors/d552-benchmark-gaps-sc08-non-profit.md)).

## Examples

| Case | Result |
|---|---|
| 142 members, scale 200 + 6.50 | dues 1,123.00 |
| 10 members added in March | dues recomputed from the date |
| No declaration | minimum dues, club flagged |
| Club leaves in January | dues pro rata to the leaving date |
| 142 members, 1 vote per 20 members | 7 votes |

## Applies to

- [UC-SC08-23](../use-cases/07-foundations-integration-and-federations/uc-sc08-23-run-a-federation-of-member-clubs.md)
- [E-SC08-18 Member organisation](../data/e-sc08-18-member-organisation.md)
- [E-SC08-02 Dues payment](../data/e-sc08-02-dues-payment.md)

## Exceptions

None.

## Configurable

The scale, the minimum dues and the weighting of the votes follow the statutes and are entered by the secretary.

## Open questions

None.

---

⬅️ [BR-SC08-17 Aid per position follows the approval](br-sc08-17-aid-per-position-follows-the-approval.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC08-19](br-sc08-19-funds-go-to-the-association-never-the-page-owner.md)
