🏠 [Specs](../README.md) › 👤 [Users](README.md) › 🔑 Roles

# 🔑 Roles

**Status:** 🔄 waiting for the owner

## Ready-made roles

- Ready-made roles, such as manager, sales, purchasing, accounting, HR and employee, which an administrator copies and
  edits.
- **Configurator:** configures fields, statuses, forms, record types, templates and workflows (F2), limited to the
  capabilities the user's other roles can see. See
  [D96](../06-decisions/f02-no-code-configuration/d96-configurator-role.md).
- **Cashier, Waiter, Kitchen:** the point-of-sale roles (F10): selling, refunds within limits and the till session;
  tables, orders and bills; preparation screens. (Proposed) Refunds, discounts and price changes beyond a limit need a
  manager's PIN (BR-F10-05).
- **Cashier, Waiter, Kitchen:** the point-of-sale roles (F10): selling, refunds within limits and the till session;
  tables, orders and bills; preparation screens. Refunds, discounts and price changes beyond a limit need a manager's
  PIN (D297).
- **Production operator, Production planner:** the manufacturing roles (F12): operations, quantities, scrap and checks
  at the work centre; bills of materials, routings, plans, orders, quality, maintenance and costs.
- **Site manager:** the construction role (SC01): sites, crews, equipment, subcontractors, site purchases, progress
  bills to prepare, acceptance and reservations.
- **Store manager:** the retail role (SC02): the store's stock, transfers, counts, labels, sales periods, staff
  schedules, targets and customers.
- **Engagement manager:** the services role (SC03): engagements, statements of work, staffing, time and expense
  approval, billing proposals, budgets and client portal.
- **Care coordinator:** the home-care planning role (SC04): recipients, care plans, rounds, replacements, incidents,
  quality and funders' reports.
- **Carer:** the home-care visiting role (SC04): own rounds, check-in and check-out, the care log and incidents of the
  recipients visited.
- **Quality manager:** the quality-system role (SC05): controlled documents, audits, corrective and preventive actions,
  supplier quality, complaints, calibration and the management review.
- **Hotel receptionist:** the hotel front-desk role (SC06): bookings, check-in and check-out, folios, the tourist tax
  and housekeeping requests.
- **Dispatcher:** the transport planning role (SC07): orders, trips, vehicles, drivers, chartering, incidents and fleet
  costs.
- **Driver:** the driving role (SC07): own trips, stops, scans, consignment notes, proofs of delivery, incidents, fuel
  and tolls.
- **Treasurer:** the association finance role (SC08): dues, donations, tax receipts, grants, expenses and accounts.
- **Volunteer:** the volunteer role (SC08): own missions, hours, expenses and events.
- **Medical secretary:** the practice reception role (SC09): agenda, patient registration, billing and rejections, mail
  and documents; clinical content only as the practitioner allows.
- **Property manager:** the property and co-ownership management role (SC10): leases, rents, deposits, charges, landlord
  statements, assemblies, budgets and works.
- **Real-estate agent:** the agency role (SC10): mandates, listings, viewings, offers and fees.
- **Professional:** the professional-firm role (SC11): matters, documents, deadlines, time, fees and the firm's
  compliance duties.
- **Professional's assistant:** the firm assistant role (SC11): client files and identity checks, the deadline diary,
  documents and bills, within the access walls. Not to be confused with the AI assistant (D516).
- **Training coordinator:** the training organisation role (SC12): catalogue, sessions, enrolments, funding, attendance,
  certificates, quality file and yearly report.
- **Trainer:** the teaching role (SC12): own sessions and classes, attendance, assessments and grades.
- **Farmer:** the farm role (SC13): plots, crops, herds, registers, harvests, machinery, seasonal workers, aid and
  sales.
- **Customer success manager:** the customer success role (SC14): accounts, health, renewals, expansion and feature
  requests.
- **Sales representative:** the field sales role (SC15): own customers and route, orders, prices and promotions, stock
  and credit checks, visit reports.
- **Event producer:** the event role (SC16): events, budgets, venues, artists, ticketing set-up, staff, sponsors,
  safety, declarations and reports.
- **Box-office agent:** the box-office role (SC16): ticket sales, exchanges, refunds, access scanning and
  accreditations.
- **Payroll officer:** the payroll role (F13): pay inputs, pay runs, payslips, declarations, payments, corrections and
  end-of-contract documents.
- **Plugin publisher:** the publisher role (F14): own plugins, releases, prices, payouts and reviews, in the publisher
  portal.
- **SimpleERP maintainer:** the repository role (D452): review and approve pull requests, the DevOps agents' included,
  remove the approval label, merge and release; hosting is the Hosting engineer's role.
- **Hosting engineer:** the hosted edition's operations (F18 to F22, F25): fixes approved on customers' namespaces,
  incidents, domains, feature reviews, platform costs and the DevOps agents' runners; never a company's business data
  beyond what a fix needs.

## Planner roles and the map right

- **Planner roles** plan other people's work: they see the work requests, the proposals and the scheduling board, and
  the positions of the people their record rules cover
  ([BR-F9-32](../02-functional/f09-hr-and-projects/business-rules/br-f09-32-who-sees-a-position.md)). The ready-made
  planner roles (D517): Dispatcher (U29), Care coordinator (U25), Site manager (U22), Engagement manager (U24),
  Production planner (U21), Store manager (U23), Training coordinator (U38), Property manager (U34), Event producer
  (U43), Hotel receptionist (U28).
- **The map right** shows records on a map
  [BR-F1-32](../02-functional/f01-administration/business-rules/br-f01-32-map-right-for-planners-and-managers.md).
  Planner roles and manager roles hold it (D502); the managers are the Manager role (U02) and the owner
  (U13) (D517). Everyone else sees the same records as lists and addresses.
- Field workers have no map: an address on their phone shows a "Directions" button that opens their own
  navigation app (D517).

## Role × capability × action matrix

⬜ To be specified.

## Record rules

- Record rules on top, such as "a salesperson sees only their own customers".
- **The assistant, the API, MCP and A2A obey the same permissions as the screens.** None of them may show or change
  what the user could not. See [D12](../06-decisions/foundations/d12-permissions-model.md).

---

⬅️ [Personas](personas/README.md) · ⬆️ [Up](README.md) · ➡️ [Example companies](example-companies/README.md)
