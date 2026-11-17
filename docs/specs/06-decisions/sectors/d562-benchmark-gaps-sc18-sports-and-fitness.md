🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D562 Benchmark gaps of SC18 Sports and fitness

# 📜 D562 Benchmark gaps of SC18 Sports and fitness

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found that industry
packages cover sports and fitness, and that the specifications had no sector for them (G15). The owner confirmed the new
sector in the block-by-block interview with the answer "Sports and fitness", then answered the sector interview: the
extra areas G193 "Courts and facilities, Tournaments and events, Holiday camps, Equipment rental" and the organisations
G194 "Clubs and gyms (Recommended)", that is associative clubs and commercial gyms. Several duties are legal (sports
educator diplomas and professional card, medical certificates, federation licences, the declaration and supervision of
youth holiday camps, equipment rental deposits, the consumer rules for gym subscriptions and their cancellation).

## Options

- G15 Memberships and access: memberships with signed cancellation terms, or a membership with no terms on the contract.
- G15 Memberships and access: direct debit only from a signed mandate, or collection by hand.
- G15 Memberships and access: door access checked against the membership, or a card for everyone.
- G15 Memberships and access: freeze and cancellation with the legal notice, or cancellation by letter only.
- G15 Classes and waiting lists: classes with a capacity, or open sessions with no limit.
- G15 Classes and waiting lists: bookings that close before the class, or bookings until the start.
- G15 Classes and waiting lists: a waiting list in order, or first to call.
- G15 Classes and waiting lists: coaches planned with the diploma checked, or a free planning.
- G15 Licences and competitions: one licence a year per member, or licences entered by hand.
- G15 Licences and competitions: certificates checked before competitions, or certificates kept on paper.
- G15 Licences and competitions: teams of licensed players of the category, or free team sheets.
- G15 Licences and competitions: results published once validated, or results published at once.
- G15 Personal training: coaching packages with their expiry terms, or sessions sold one by one.
- G15 Personal training: programmes within declared health limits, or programmes with no check.
- G15 Personal training: health data kept for the member and the coach, or progress visible to the club.
- G15 Personal training: an AI assistant within the asker's rights, or reports only.
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental: members' rates only for valid
  members, or one public rate.
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental: draws published before the first
  match, or draws shown at the venue.
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental: camps with supervision ratios
  checked, or camps with a free list.
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental: deposits refunded on return in
  good order, or deposits kept.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC18 Sports and fitness is the eighteenth sector, with five flows and twenty use cases, each with its screen, its rule
and, where it has one, its entity and its list. All at full depth now. The organisations are "Clubs and gyms
(Recommended)" (G194): associative clubs with licences and competitions, and commercial gyms with contracts and access,
in one sector with the kind of organisation set in the settings. Each legal duty is written in plain words and marked
(Proposed) until the France-pack rule is written; no article is quoted.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G15 | Memberships and access | UC-SC18-01: contracts state the cancellation terms before signature | "Memberships and access" |
| G15 | Memberships and access | UC-SC18-02: direct debits need a signed mandate | "Memberships and access" |
| G15 | Memberships and access | UC-SC18-03: access needs a valid membership | "Memberships and access" |
| G15 | Memberships and access | UC-SC18-04: cancellation follows the legal notice period | "Memberships and access" |
| G15 | Classes and waiting lists | UC-SC18-05: classes have a capacity | "Classes and waiting lists" |
| G15 | Classes and waiting lists | UC-SC18-06: bookings close before the class starts | "Classes and waiting lists" |
| G15 | Classes and waiting lists | UC-SC18-07: freed places go to the first on the list | "Classes and waiting lists" |
| G15 | Classes and waiting lists | UC-SC18-08: coaches hold the diploma for the activity | "Classes and waiting lists" |
| G15 | Licences and competitions | UC-SC18-09: a licence is issued once a year per member | "Licences and competitions" |
| G15 | Licences and competitions | UC-SC18-10: competitions need a valid certificate | "Licences and competitions" |
| G15 | Licences and competitions | UC-SC18-11: players are licensed for their category | "Licences and competitions" |
| G15 | Licences and competitions | UC-SC18-12: results are published once validated | "Licences and competitions" |
| G15 | Personal training | UC-SC18-13: sessions expire per the package terms | "Personal training" |
| G15 | Personal training | UC-SC18-14: programmes respect declared health limits | "Personal training" |
| G15 | Personal training | UC-SC18-15: health data stays with the member and the coach | "Personal training" |
| G15 | Personal training | UC-SC18-16: an AI assistant within the asker's rights | "Personal training" |
| G193 | Courts and facilities, Tournaments and events, Holiday camps, Equipment rental | UC-SC18-17: members' rates only for valid members | "Courts and facilities, Tournaments and events, Holiday camps, Equipment rental" |
| G193 | Courts and facilities, Tournaments and events, Holiday camps, Equipment rental | UC-SC18-18: draws published before the first match | "Courts and facilities, Tournaments and events, Holiday camps, Equipment rental" |
| G193 | Courts and facilities, Tournaments and events, Holiday camps, Equipment rental | UC-SC18-19: supervision ratios follow the youth rules | "Courts and facilities, Tournaments and events, Holiday camps, Equipment rental" |
| G193 | Courts and facilities, Tournaments and events, Holiday camps, Equipment rental | UC-SC18-20: deposits refunded on return in good order | "Courts and facilities, Tournaments and events, Holiday camps, Equipment rental" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "SC18 Sports and fitness
(new)").

## Consequences

- G15 Memberships and access:
  [UC-SC18-01](../../08-sectors/sc18-sports-and-fitness/use-cases/01-memberships-and-access/uc-sc18-01-sell-a-membership.md),
  [S-SC18-01](../../08-sectors/sc18-sports-and-fitness/screens/01-memberships-and-access/s-sc18-01-membership-sale.md)
  and
  [BR-SC18-01](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-01-contracts-state-the-cancellation-terms.md),
  with [E-SC18-01](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-01-club-membership.md) Club membership and its
  list [S-SC18-L01](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l01-club-memberships.md).
- G15 Memberships and access:
  [UC-SC18-02](../../08-sectors/sc18-sports-and-fitness/use-cases/01-memberships-and-access/uc-sc18-02-collect-dues-by-direct-debit.md),
  [S-SC18-02](../../08-sectors/sc18-sports-and-fitness/screens/01-memberships-and-access/s-sc18-02-dues-collection.md)
  and
  [BR-SC18-02](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-02-direct-debits-need-a-signed-mandate.md),
  with [E-SC18-02](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-02-dues-mandate.md) Dues mandate and its list
  [S-SC18-L02](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l02-dues-mandates.md).
- G15 Memberships and access:
  [UC-SC18-03](../../08-sectors/sc18-sports-and-fitness/use-cases/01-memberships-and-access/uc-sc18-03-control-access-at-the-door.md),
  [S-SC18-03](../../08-sectors/sc18-sports-and-fitness/screens/01-memberships-and-access/s-sc18-03-door-access.md) and
  [BR-SC18-03](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-03-access-needs-a-valid-membership.md),
  with [E-SC18-03](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-03-access-event.md) Access event and its list
  [S-SC18-L03](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l03-access-events.md).
- G15 Memberships and access:
  [UC-SC18-04](../../08-sectors/sc18-sports-and-fitness/use-cases/01-memberships-and-access/uc-sc18-04-freeze-or-cancel-a-membership.md),
  [S-SC18-04](../../08-sectors/sc18-sports-and-fitness/screens/01-memberships-and-access/s-sc18-04-membership-changes.md)
  and
  [BR-SC18-04](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-04-cancellation-follows-the-legal-notice-period.md).
- G15 Classes and waiting lists:
  [UC-SC18-05](../../08-sectors/sc18-sports-and-fitness/use-cases/02-classes-and-waiting-lists/uc-sc18-05-publish-the-class-timetable.md),
  [S-SC18-05](../../08-sectors/sc18-sports-and-fitness/screens/02-classes-and-waiting-lists/s-sc18-05-class-timetable.md)
  and [BR-SC18-05](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-05-classes-have-a-capacity.md), with
  [E-SC18-04](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-04-class.md) Class and its list
  [S-SC18-L04](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l04-classes.md).
- G15 Classes and waiting lists:
  [UC-SC18-06](../../08-sectors/sc18-sports-and-fitness/use-cases/02-classes-and-waiting-lists/uc-sc18-06-book-a-class.md),
  [S-SC18-06](../../08-sectors/sc18-sports-and-fitness/screens/02-classes-and-waiting-lists/s-sc18-06-class-booking.md)
  and
  [BR-SC18-06](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-06-bookings-close-before-the-class-starts.md),
  with [E-SC18-05](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-05-class-booking.md) Class booking and its list
  [S-SC18-L05](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l05-class-bookings.md).
- G15 Classes and waiting lists:
  [UC-SC18-07](../../08-sectors/sc18-sports-and-fitness/use-cases/02-classes-and-waiting-lists/uc-sc18-07-handle-the-waiting-list.md),
  [S-SC18-07](../../08-sectors/sc18-sports-and-fitness/screens/02-classes-and-waiting-lists/s-sc18-07-waiting-list.md)
  and
  [BR-SC18-07](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-07-freed-places-go-to-the-first-on-the-list.md).
- G15 Classes and waiting lists:
  [UC-SC18-08](../../08-sectors/sc18-sports-and-fitness/use-cases/02-classes-and-waiting-lists/uc-sc18-08-plan-coaches.md),
  [S-SC18-08](../../08-sectors/sc18-sports-and-fitness/screens/02-classes-and-waiting-lists/s-sc18-08-coach-planning.md)
  and
  [BR-SC18-08](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-08-coaches-hold-the-diploma-for-the-activity.md).
- G15 Licences and competitions:
  [UC-SC18-09](../../08-sectors/sc18-sports-and-fitness/use-cases/03-licences-and-competitions/uc-sc18-09-issue-federation-licences.md),
  [S-SC18-09](../../08-sectors/sc18-sports-and-fitness/screens/03-licences-and-competitions/s-sc18-09-federation-licences.md)
  and
  [BR-SC18-09](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-09-a-licence-is-issued-once-a-year-per-member.md),
  with [E-SC18-06](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-06-licence.md) Licence and its list
  [S-SC18-L06](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l06-licences.md).
- G15 Licences and competitions:
  [UC-SC18-10](../../08-sectors/sc18-sports-and-fitness/use-cases/03-licences-and-competitions/uc-sc18-10-check-medical-certificates.md),
  [S-SC18-10](../../08-sectors/sc18-sports-and-fitness/screens/03-licences-and-competitions/s-sc18-10-medical-certificates.md)
  and
  [BR-SC18-10](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-10-competitions-need-a-valid-certificate.md),
  with [E-SC18-07](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-07-medical-certificate.md) Medical certificate
  and its list
  [S-SC18-L07](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l07-medical-certificates.md).
- G15 Licences and competitions:
  [UC-SC18-11](../../08-sectors/sc18-sports-and-fitness/use-cases/03-licences-and-competitions/uc-sc18-11-run-teams-and-competitions.md),
  [S-SC18-11](../../08-sectors/sc18-sports-and-fitness/screens/03-licences-and-competitions/s-sc18-11-teams-and-competitions.md)
  and
  [BR-SC18-11](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-11-players-are-licensed-for-their-category.md),
  with [E-SC18-08](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-08-team.md) Sports team and its list
  [S-SC18-L08](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l08-teams.md).
- G15 Licences and competitions:
  [UC-SC18-12](../../08-sectors/sc18-sports-and-fitness/use-cases/03-licences-and-competitions/uc-sc18-12-record-results.md),
  [S-SC18-12](../../08-sectors/sc18-sports-and-fitness/screens/03-licences-and-competitions/s-sc18-12-results.md) and
  [BR-SC18-12](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-12-results-are-published-once-validated.md),
  with [E-SC18-09](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-09-result.md) Result and its list
  [S-SC18-L09](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l09-results.md).
- G15 Personal training:
  [UC-SC18-13](../../08-sectors/sc18-sports-and-fitness/use-cases/04-personal-training/uc-sc18-13-sell-coaching-packages.md),
  [S-SC18-13](../../08-sectors/sc18-sports-and-fitness/screens/04-personal-training/s-sc18-13-coaching-packages.md) and
  [BR-SC18-13](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-13-sessions-expire-per-the-package-terms.md),
  with [E-SC18-10](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-10-coaching-package.md) Coaching package and its
  list [S-SC18-L10](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l10-coaching-packages.md).
- G15 Personal training:
  [UC-SC18-14](../../08-sectors/sc18-sports-and-fitness/use-cases/04-personal-training/uc-sc18-14-plan-a-training-programme.md),
  [S-SC18-14](../../08-sectors/sc18-sports-and-fitness/screens/04-personal-training/s-sc18-14-training-programme.md) and
  [BR-SC18-14](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-14-programmes-respect-declared-health-limits.md),
  with [E-SC18-11](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-11-training-programme.md) Training programme and
  its list [S-SC18-L11](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l11-training-programmes.md).
- G15 Personal training:
  [UC-SC18-15](../../08-sectors/sc18-sports-and-fitness/use-cases/04-personal-training/uc-sc18-15-follow-progress.md),
  [S-SC18-15](../../08-sectors/sc18-sports-and-fitness/screens/04-personal-training/s-sc18-15-progress.md) and
  [BR-SC18-15](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-15-health-data-stays-with-the-member-and-coach.md),
  with [E-SC18-12](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-12-progress-record.md) Progress record and its
  list [S-SC18-L12](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l12-progress-records.md).
- G15 Personal training:
  [UC-SC18-16](../../08-sectors/sc18-sports-and-fitness/use-cases/04-personal-training/uc-sc18-16-ask-the-assistant-about-the-club.md),
  [S-SC18-16](../../08-sectors/sc18-sports-and-fitness/screens/04-personal-training/s-sc18-16-club-assistant.md) and
  [BR-SC18-16](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-16-answers-follow-the-askers-rights.md).
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental:
  [UC-SC18-17](../../08-sectors/sc18-sports-and-fitness/use-cases/05-facilities-events-camps-and-rentals/uc-sc18-17-book-courts-and-facilities.md),
  [S-SC18-17](../../08-sectors/sc18-sports-and-fitness/screens/05-facilities-events-camps-and-rentals/s-sc18-17-court-booking.md)
  and
  [BR-SC18-17](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-17-members-rates-apply-only-to-valid-members.md),
  with [E-SC18-13](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-13-court-booking.md) Court booking and its list
  [S-SC18-L13](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l13-court-bookings.md).
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental:
  [UC-SC18-18](../../08-sectors/sc18-sports-and-fitness/use-cases/05-facilities-events-camps-and-rentals/uc-sc18-18-run-tournaments-and-events.md),
  [S-SC18-18](../../08-sectors/sc18-sports-and-fitness/screens/05-facilities-events-camps-and-rentals/s-sc18-18-tournaments.md)
  and
  [BR-SC18-18](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-18-draws-are-published-before-the-first-match.md),
  with [E-SC18-14](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-14-tournament.md) Tournament and its list
  [S-SC18-L14](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l14-tournaments.md).
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental:
  [UC-SC18-19](../../08-sectors/sc18-sports-and-fitness/use-cases/05-facilities-events-camps-and-rentals/uc-sc18-19-run-holiday-camps.md),
  [S-SC18-19](../../08-sectors/sc18-sports-and-fitness/screens/05-facilities-events-camps-and-rentals/s-sc18-19-holiday-camps.md)
  and
  [BR-SC18-19](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-19-supervision-ratios-follow-the-youth-rules.md),
  with [E-SC18-15](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-15-camp-registration.md) Camp registration and
  its list [S-SC18-L15](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l15-camp-registrations.md).
- G193 Courts and facilities, Tournaments and events, Holiday camps, Equipment rental:
  [UC-SC18-20](../../08-sectors/sc18-sports-and-fitness/use-cases/05-facilities-events-camps-and-rentals/uc-sc18-20-rent-out-equipment.md),
  [S-SC18-20](../../08-sectors/sc18-sports-and-fitness/screens/05-facilities-events-camps-and-rentals/s-sc18-20-equipment-rental.md)
  and
  [BR-SC18-20](../../08-sectors/sc18-sports-and-fitness/business-rules/br-sc18-20-deposits-are-refunded-on-return-in-good-order.md),
  with [E-SC18-16](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-16-rental-item.md) Rental item and its list
  [S-SC18-L16](../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l16-rental-items.md).
- Drawn in [FL-SC18-01](../../08-sectors/sc18-sports-and-fitness/flows/fl-sc18-01-memberships-and-access.md) Memberships
  and access.
- Drawn in [FL-SC18-02](../../08-sectors/sc18-sports-and-fitness/flows/fl-sc18-02-classes-and-waiting-lists.md) Classes
  and waiting lists.
- Drawn in [FL-SC18-03](../../08-sectors/sc18-sports-and-fitness/flows/fl-sc18-03-licences-and-competitions.md) Licences
  and competitions.
- Drawn in [FL-SC18-04](../../08-sectors/sc18-sports-and-fitness/flows/fl-sc18-04-personal-training.md) Personal
  training.
- Drawn in
  [FL-SC18-05](../../08-sectors/sc18-sports-and-fitness/flows/fl-sc18-05-facilities-events-camps-and-rentals.md)
  Facilities, events, camps and rentals.
- G194 "Clubs and gyms (Recommended)":
  [UC-SC18-01](../../08-sectors/sc18-sports-and-fitness/use-cases/01-memberships-and-access/uc-sc18-01-sell-a-membership.md)
  records the kind of organisation on each membership, and the association's licences
  [UC-SC18-09](../../08-sectors/sc18-sports-and-fitness/use-cases/03-licences-and-competitions/uc-sc18-09-issue-federation-licences.md)
  and competitions
  [UC-SC18-11](../../08-sectors/sc18-sports-and-fitness/use-cases/03-licences-and-competitions/uc-sc18-11-run-teams-and-competitions.md)
  sit beside the gym's contracts and access
  [UC-SC18-03](../../08-sectors/sc18-sports-and-fitness/use-cases/01-memberships-and-access/uc-sc18-03-control-access-at-the-door.md).
- The sector list of the specifications and [D114](d114-sixteen-sectors.md) are updated by the main session; this round
  adds the pages of the sector only.
- New entities relate to capability entities rather than replace them:
  [E-SC18-01](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-01-club-membership.md) to
  [E-F6-07](../../02-functional/f06-customers-and-sales/data/e-f06-07-subscription-contract.md),
  [E-SC18-05](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-05-class-booking.md) and
  [E-SC18-13](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-13-court-booking.md) to
  [E-F2-18](../../02-functional/f02-no-code-configuration/data/e-f02-18-resource-booking.md).

## Related

- [FL-SC18-01](../../08-sectors/sc18-sports-and-fitness/flows/fl-sc18-01-memberships-and-access.md)
- [D114 Sixteen sectors](d114-sixteen-sectors.md)
- [U53 Coach](../../01-users/personas/u53-coach.md)
- [U13 Owner](../../01-users/personas/u13-owner.md)
- [D561](d561-benchmark-gaps-sc17-beauty-and-wellness.md)

---

⬅️ [D561 Benchmark gaps of SC17 Beauty and wellness](d561-benchmark-gaps-sc17-beauty-and-wellness.md) ·
⬆️ [Up](README.md) ·
➡️ [D563 Benchmark gaps of SC19 Trades and home services](d563-benchmark-gaps-sc19-trades-and-home-services.md)
