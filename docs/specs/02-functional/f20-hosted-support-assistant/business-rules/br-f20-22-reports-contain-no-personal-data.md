🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-22 Reports contain no personal data

# 📏 BR-F20-22 Reports contain no personal data

**Status:** ✅ specified

## Statement

A health report holds only technical figures and plain-words advice: it never contains a name, an email address, an
address, a token or any other data that identifies a person, and a report in which the check finds such data is held,
not sent.

## Why

A report is emailed and forwarded, so it must be safe in any inbox; the point is the health of the service, not the data
it holds. The owner asked for a monthly health report
([D539](../../../06-decisions/f20-hosted-support-assistant/d539-benchmark-gaps-f20-hosted-support-assistant.md)).

## Examples

| Case | Result |
|---|---|
| Availability, incident minutes, storage used | allowed |
| An incident's text naming a user | held until edited |
| A count of requests | allowed, counts only |
| A company with health data | figures only, as for any other |
| An error message containing an email address | removed before the report is built |

## Applies to

- [UC-F20-31](../use-cases/08-engineers-sharing-and-reports/uc-f20-31-read-the-monthly-health-report.md)
- [E-F20-21 Health report](../data/e-f20-21-health-report.md)
- [E-F20-05 Cluster reading](../data/e-f20-05-cluster-reading.md)
- [E-F20-07 Service incident](../data/e-f20-07-service-incident.md)

## Exceptions

None.

## Configurable

The recipients of the report and its language, by the administrator.

## Open questions

None.

---

⬅️ [BR-F20-21 Access ends at its time limit and is audited](br-f20-21-access-ends-at-its-time-limit-and-is-audited.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F20-23](br-f20-23-service-times-are-the-same-in-every-supported-language.md)
