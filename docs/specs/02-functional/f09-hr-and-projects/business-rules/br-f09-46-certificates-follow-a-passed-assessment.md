🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-46 Certificates follow a passed assessment

# 📏 BR-F9-46 Certificates follow a passed assessment

**Status:** ✅ specified

## Statement

A certificate is issued only to the learner who reached the pass mark of the course's final assessment, within the
attempts allowed, and each certificate names the learner, the course, the date, the score and its validity; a learner
who only followed the modules gets a statement of attendance, never a certificate.

## Why

A certificate is proof for an employer or an auditor. Issuing it without a result would make every certificate
worthless. The owner's answer: "Sell online courses"
([D528](../../../06-decisions/f09-hr-and-projects/d528-benchmark-gaps-f09-hr-and-projects.md)).

## Examples

| Case | Result |
|---|---|
| Pass mark 80, score 86 | certificate issued |
| Score 70, 2 attempts left | no certificate, the learner may try again |
| Modules followed, no assessment taken | a statement of attendance |
| A certificate valid 2 years | the learner is invited to renew before it ends |
| The coordinator asks to issue a certificate by hand | refused: only a result issues it |

## Applies to

- [UC-F9-47 Publish and sell online courses](../use-cases/15-work-location-headcount-and-learning/uc-f09-47-publish-and-sell-online-courses.md)
- [E-F9-52 Online course](../data/e-f09-52-online-course.md)
- [UC-F9-25 Run the training plan with OPCO funding](../use-cases/09-train-and-protect/uc-f09-25-run-the-training-plan-with-opco-funding.md)

## Exceptions

A course with no assessment issues only a statement of attendance.

## Configurable

Yes: the pass mark, the attempts allowed and the validity are set per course.

## Open questions

None.

---

⬅️ [BR-F9-45 A change request applies only once approved](br-f09-45-a-change-request-applies-only-once-approved.md) ·
⬆️ [Up](README.md)
