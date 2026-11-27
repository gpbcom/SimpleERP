🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🩺 [SC09 Health practices](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC09-02 Patient

# 🗃️ E-SC09-02 Patient

**Status:** 🔄 waiting for the owner

## Purpose

A patient's administrative file.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| identity, birth date | text, date | yes | - | - | J. Martin, 1980 | yes | no |
| insurance, complementary | records | no | BR-SC09-06 | - | general scheme | yes | no |
| consents, objections | list | no | - | - | SMS, national record | yes | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-SC09-03
```

## Indexes and search

(Proposed) By number, date, partner.

## Retention

No legal period for private practice; 20 years after the last visit advised:
[CR-FR-131 Patients' access to their medical record](../../../10-country-packs/france/health-practice/cr-fr-131-medical-record-access.md);
on certified hosting:
[CR-FR-055 Health data hosting](../../../10-country-packs/france/data-protection/cr-fr-055-health-data-hosting.md).

## Audit

Every change.

## Import and export

(Proposed) CSV, FEC where relevant.

## Used by

- [UC-SC09-03](../use-cases/02-patient-file-and-care/uc-sc09-03-register-patients-and-their-insurance.md)
- [UC-SC09-17](../use-cases/06-compliance-and-certification/uc-sc09-17-honour-patients-rights.md)

## Open questions

None.

---

⬅️ [E-SC09-01 Appointment](e-sc09-01-appointment.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC09-03 Clinical record entry](e-sc09-03-clinical-record-entry.md)
