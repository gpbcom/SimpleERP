🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🙋 [Customer: app shell and home](README.md) › 🧰 U09 Customer: workspace

# 🧰 U09 Customer: workspace

**Status:** ✅ specified

## Purpose

The views [U09 Customer](../../../01-users/personas/u09-customer.md) works with, embedded on their
[home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators and the planner roles), else
"Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F1-L04 Invitations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l04-invitations.md) | Administration | Open: Sent, Accepted, NotDelivered | UC-SC12-05 |
| [S-F1-L17 Portal accounts](../../../02-functional/f01-administration/screens/00-lists/s-f01-l17-portal-accounts.md) | Administration | All | UC-F1-19, UC-F2-20 |
| [S-F2-L05 Record types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l05-record-types.md) | No-code configuration | Open: Draft, Live | UC-F2-20 |
| [S-F2-L14 Signature requests](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l14-signature-requests.md) | No-code configuration | Open: Sent, Signed, Refused | UC-SC19-20 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Open: Draft, Published | UC-F2-19 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-F2-19, UC-SC06-08, UC-SC09-01, UC-SC16-11 |
| [S-F2-L19 Portal exposures](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l19-portal-exposures.md) | No-code configuration | Open: Draft, Published | UC-F2-20 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Open: Draft, Published | UC-F16-16 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Open: Planned, Live, WaitingForReview | UC-F4-25, UC-F4-26 |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-23 |
| [S-F4-L04 Action items](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l04-action-items.md) | Meetings | Open: Open | UC-F4-26 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L11 Appointment types](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l11-appointment-types.md) | Meetings | All | UC-F4-18 |
| [S-F4-L14 Speaker requests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l14-speaker-requests.md) | Meetings | Open: Received, Refused | UC-F4-23 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | UC-F4-25 |
| [S-F4-L28 Webinars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l28-webinars.md) | Meetings | Mine: host | UC-F4-29 |
| [S-F5-L04 Social messages](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l04-social-messages.md) | Social media and marketing | All | UC-F5-20 |
| [S-F5-L07 Registration events](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l07-registration-events.md) | Social media and marketing | Open: Draft, Planned, Published | UC-F5-11, UC-SC08-12 |
| [S-F5-L08 Surveys](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l08-surveys.md) | Social media and marketing | Open: Draft, Sent | UC-F5-12 |
| [S-F5-L10 Consent and suppression records](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l10-consent-and-suppression-records.md) | Social media and marketing | Mine: contact | UC-F5-15, UC-F5-19 |
| [S-F5-L12 Event tickets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l12-event-tickets.md) | Social media and marketing | Mine: holder | UC-SC08-12, UC-SC16-05 |
| [S-F5-L13 Landing page and forms](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l13-landing-page-and-forms.md) | Social media and marketing | All | UC-F5-19 |
| [S-F5-L14 WhatsApp templates](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l14-whatsapp-templates.md) | Social media and marketing | All | UC-F5-20 |
| [S-F5-L18 Contacts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l18-contacts.md) | Social media and marketing | All | UC-F5-15 |
| [S-F5-L22 Referrals](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l22-referrals.md) | Social media and marketing | All | UC-F5-25 |
| [S-F5-L23 Push campaigns](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l23-push-campaigns.md) | Social media and marketing | All | UC-F5-26 |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-F6-11, UC-F10-25 |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Open: Draft, ToApprove, Sent | UC-F6-04, UC-F6-11, UC-F11-27 |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-F5-25, UC-F6-29, UC-F6-31, UC-SC02-17 and more |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F6-11, UC-F6-22, UC-F6-23, UC-F6-24 |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-F6-07 |
| [S-F6-L07 Subscription contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l07-subscription-contracts.md) | Customers and sales | All | UC-F6-11 |
| [S-F6-L09 Rentals](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l09-rentals.md) | Customers and sales | All | UC-F6-15 |
| [S-F6-L14 Funder agreements](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l14-funder-agreements.md) | Customers and sales | Open: Active | UC-SC04-01 |
| [S-F6-L15 Pro-forma invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l15-pro-forma-invoices.md) | Customers and sales | Open: Issued, Superseded | UC-F6-22 |
| [S-F6-L16 Instalment plans](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l16-instalment-plans.md) | Customers and sales | Open: Proposed, Accepted, Broken | UC-F6-23 |
| [S-F6-L17 Invoice disputes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l17-invoice-disputes.md) | Customers and sales | All | UC-F6-24 |
| [S-F6-L20 Leads](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l20-leads.md) | Customers and sales | All | UC-F5-19 |
| [S-F6-L21 Payment reminders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l21-payment-reminders.md) | Customers and sales | All | UC-F6-24 |
| [S-F6-L25 Frame contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l25-frame-contracts.md) | Customers and sales | All | UC-F6-29 |
| [S-F6-L27 Warranties](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l27-warranties.md) | Customers and sales | All | UC-F6-31, UC-SC19-18 |
| [S-F7-L03 Purchase orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l03-purchase-orders.md) | Purchasing and stock | All | UC-SC02-17 |
| [S-F7-L14 Repair orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l14-repair-orders.md) | Purchasing and stock | Open: ToDo, InRepair, Invoiced | UC-F7-17 |
| [S-F8-L18 Grants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l18-grants.md) | Accounting | Open: Granted, Received | UC-SC12-19 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-35 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Open: New, Planned, Active | UC-F9-17, UC-F9-31 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Mine: person | UC-F9-35, UC-F16-17 |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Mine: chosen | UC-F9-35 |
| [S-F9-L32 Live positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l32-live-positions.md) | HR and projects | Mine: employee | UC-F16-17 |
| [S-F9-L51 Change requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l51-change-requests.md) | HR and projects | Mine: project | UC-F9-46 |
| [S-F9-L52 Online courses](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l52-online-courses.md) | HR and projects | Mine: learner | UC-F9-47 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-05, UC-F10-11, UC-F10-12, UC-F10-13 and more |
| [S-F10-L04 Till payments](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l04-till-payments.md) | Point of sale (plugin) | All | UC-F10-11, UC-F10-13 |
| [S-F10-L05 Receipts](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l05-receipts.md) | Point of sale (plugin) | All | UC-F10-05 |
| [S-F10-L10 Loyalty card and gift cards](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l10-loyalty-card-and-gift-cards.md) | Point of sale (plugin) | Mine: customer | UC-F10-07 |
| [S-F10-L11 Floor and tables](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l11-floor-and-tables.md) | Point of sale (plugin) | All | UC-F10-12 |
| [S-F10-L13 Preparation tickets](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l13-preparation-tickets.md) | Point of sale (plugin) | All | UC-F10-29 |
| [S-F10-L14 Point of sale devices](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l14-point-of-sale-devices.md) | Point of sale (plugin) | All | UC-F10-19 |
| [S-F10-L19 Clienteling profiles](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l19-clienteling-profiles.md) | Point of sale (plugin) | All | UC-F10-25 |
| [S-F10-L21 Table QR codes](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l21-table-qr-codes.md) | Point of sale (plugin) | All | UC-F10-12 |
| [S-F10-L22 Takeaway orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l22-takeaway-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-29 |
| [S-F11-L03 Online products](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l03-online-products.md) | Online shop (plugin) | All | UC-F11-04, UC-F11-12, UC-F11-13 |
| [S-F11-L04 Carts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l04-carts.md) | Online shop (plugin) | Mine: owner | UC-F11-05 |
| [S-F11-L05 Checkouts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l05-checkouts.md) | Online shop (plugin) | All | UC-F11-05, UC-F11-06, UC-F11-08, UC-F11-21 |
| [S-F11-L06 Payment providers](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l06-payment-providers.md) | Online shop (plugin) | All | UC-F11-06 |
| [S-F11-L07 Delivery methods](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l07-delivery-methods.md) | Online shop (plugin) | All | UC-F11-07 |
| [S-F11-L08 Withdrawal requests](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l08-withdrawal-requests.md) | Online shop (plugin) | All | UC-F11-09 |
| [S-F11-L09 Customer accounts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l09-customer-accounts.md) | Online shop (plugin) | Mine: contact | UC-F11-10, UC-F11-11 |
| [S-F11-L10 Product reviews](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l10-product-reviews.md) | Online shop (plugin) | Open: ToCheck, Published | UC-F11-15 |
| [S-F11-L16 Fraud checks](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l16-fraud-checks.md) | Online shop (plugin) | All | UC-F11-21 |
| [S-F11-L21 Pre-order and reservations](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l21-pre-order-and-reservations.md) | Online shop (plugin) | Open: Open, Shipped, Released | UC-F11-26 |
| [S-F11-L22 Punch-out sessions](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l22-punch-out-sessions.md) | Online shop (plugin) | Open: Open, Returned | UC-F11-27 |
| [S-F11-L24 Donations](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l24-donations.md) | Online shop (plugin) | Mine: donor | UC-F11-30 |
| [S-F11-L25 Wishlists](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l25-wishlists.md) | Online shop (plugin) | Mine: owner | UC-F11-31 |
| [S-F11-L26 Gift cards](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l26-online-gift-cards.md) | Online shop (plugin) | Mine: buyer | UC-F11-32 |
| [S-F11-L27 Country price lists](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l27-country-price-lists.md) | Online shop (plugin) | Mine: website | UC-F11-33 |
| [S-F12-L14 Product compliance files](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l14-product-compliance-files.md) | Manufacturing (plugin) | All | UC-F12-30 |
| [S-F12-L24 Product passports](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l24-product-passports.md) | Manufacturing (plugin) | All | UC-F12-30 |
| [S-F13-L02 Employee pay profiles](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l02-employee-pay-profiles.md) | Payroll (plugin) | Mine: employee | UC-SC04-18 |
| [S-F15-L08 Data-subject requests](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l08-data-subject-requests.md) | Legal assistant | All | UC-F15-10 |
| [S-F16-L01 Customer requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l01-customer-requests.md) | Customer support agents | Open: New, InProgress, Waiting | UC-F16-01, UC-F16-11, UC-F16-09, UC-F16-12 and more |
| [S-F16-L08 Satisfaction ratings](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l08-satisfaction-ratings.md) | Customer support agents | Open: Asked, Answered | UC-F16-01, UC-F16-09 |
| [S-F16-L09 Help-centre articles](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l09-help-centre-articles.md) | Customer support agents | Open: Draft, Published | UC-F16-10 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Mine: confirmed by | UC-F9-35, UC-F16-16, UC-F16-17 |
| [S-F16-L13 Forum posts](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l13-forum-posts.md) | Customer support agents | All | UC-F16-18 |
| [S-F16-L14 Chat sessions](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l14-chat-sessions.md) | Customer support agents | All | UC-F16-19 |
| [S-F16-L16 Support contracts](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l16-support-contracts.md) | Customer support agents | All | UC-F16-22 |
| [S-F18-L02 Pages](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l02-pages.md) | Hosted websites and domains (hosted edition) | All | UC-F18-04 |
| [S-F18-L04 Contact messages](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l04-contact-messages.md) | Hosted websites and domains (hosted edition) | Open: Sent, Held | UC-F18-04, UC-F18-24 |
| [S-F18-L16 Spam holds](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l16-spam-holds.md) | Hosted websites and domains (hosted edition) | Open: Held, Released | UC-F18-04, UC-F18-24 |
| [S-F18-L23 Page audiences](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l23-page-audiences.md) | Hosted websites and domains (hosted edition) | All | UC-F18-31 |
| [S-F25-L16 Roadmap items](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l16-roadmap-items.md) | DevOps agents (hosted edition) | All | UC-F25-25 |
| [S-T13-L01 Geocoded places](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l01-geocoded-places.md) | Maps and geodata | All | UC-F16-16 |
| [S-T13-L03 Map layers](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l03-map-layers.md) | Maps and geodata | Open: Draft, Published | UC-F16-17 |
| [S-SC01-L02 Quote lots](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l02-quote-lots.md) | Construction | All | UC-SC01-02, UC-SC01-12 |
| [S-SC01-L10 Acceptance records](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l10-acceptance-records.md) | Construction | All | UC-SC01-10, UC-SC01-11 |
| [S-SC01-L11 Warranties](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l11-warranties.md) | Construction | All | UC-SC01-10, UC-SC01-11 |
| [S-SC01-L13 As-built files](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l13-as-built-files.md) | Construction | All | UC-SC01-11 |
| [S-SC01-L16 Off-plan lots](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l16-off-plan-lots.md) | Construction | All | UC-SC01-17 |
| [S-SC01-L18 Grant files](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l18-grant-files.md) | Construction | All | UC-SC01-19 |
| [S-SC02-L01 Stores](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l01-stores.md) | Retail | Open: Planned, Open | UC-SC02-08, UC-SC02-09 |
| [S-SC02-L14 Furniture orders](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l14-furniture-orders.md) | Retail | All | UC-SC02-17 |
| [S-SC03-L01 Engagements](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l01-engagements.md) | Services | Open: PreSales, Running | UC-SC03-01 |
| [S-SC03-L02 Statement of works](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l02-statement-of-works.md) | Services | All | UC-SC03-01 |
| [S-SC03-L06 Rebillable costs](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l06-rebillable-costs.md) | Services | All | UC-SC03-17 |
| [S-SC03-L12 Shared items](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l12-shared-items.md) | Services | All | UC-SC03-11 |
| [S-SC03-L13 Satisfaction surveys](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l13-satisfaction-surveys.md) | Services | Open: Sent | UC-SC03-12 |
| [S-SC03-L18 Creative proofs](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l18-creative-proofs.md) | Services | All | UC-SC03-17 |
| [S-SC04-L01 Care recipients](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l01-care-recipients.md) | Home care | All | UC-SC04-01, UC-SC04-07 |
| [S-SC04-L02 Care fundings](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l02-care-fundings.md) | Home care | All | UC-SC04-01 |
| [S-SC04-L03 Care plans](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l03-care-plans.md) | Home care | All | UC-SC04-02 |
| [S-SC04-L06 Care log entries](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l06-care-log-entries.md) | Home care | All | UC-SC04-05, UC-SC04-07 |
| [S-SC04-L07 Care incidents](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l07-care-incidents.md) | Home care | All | UC-SC04-05 |
| [S-SC04-L08 Care invoices](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l08-care-invoices.md) | Home care | All | UC-SC04-10 |
| [S-SC04-L13 Immediate advance claims](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l13-immediate-advance-claims.md) | Home care | All | UC-SC04-10 |
| [S-SC04-L15 CESU vouchers](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l15-cesu-vouchers.md) | Home care | All | UC-SC04-17 |
| [S-SC04-L16 Mandates](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l16-mandates.md) | Home care | All | UC-SC04-18, UC-SC19-09 |
| [S-SC05-L17 Proofs](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l17-proofs.md) | Manufacturing | All | UC-SC05-18 |
| [S-SC06-L02 Menu dishes](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l02-menu-dishes.md) | Restaurant and hospitality | All | UC-SC06-02 |
| [S-SC06-L08 Room reservations](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l08-room-reservations.md) | Restaurant and hospitality | Open: Booked, Arrived, Departed | UC-SC06-08, UC-SC06-09 |
| [S-SC06-L09 Folios](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l09-folios.md) | Restaurant and hospitality | All | UC-SC06-09 |
| [S-SC06-L11 Tourist tax lines](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l11-tourist-tax-lines.md) | Restaurant and hospitality | All | UC-SC06-16 |
| [S-SC06-L13 Pitches](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l13-pitches.md) | Restaurant and hospitality | All | UC-SC06-16 |
| [S-SC06-L15 Group bookings](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l15-group-bookings.md) | Restaurant and hospitality | All | UC-SC06-18 |
| [S-SC07-L01 Transport orders](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l01-transport-orders.md) | Transport and logistics | All | UC-SC07-01 |
| [S-SC07-L05 Consignment notes](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l05-consignment-notes.md) | Transport and logistics | All | UC-SC07-16 |
| [S-SC07-L06 Stops](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l06-stops.md) | Transport and logistics | Open: New, Open | UC-SC07-16 |
| [S-SC07-L16 Proof of deliveries](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l16-proof-of-deliveries.md) | Transport and logistics | All | UC-SC07-22 |
| [S-SC07-L19 Removals](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l19-removals.md) | Transport and logistics | All | UC-SC07-22 |
| [S-SC08-L01 Members](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l01-members.md) | Non-profit association | Mine: contact | UC-SC08-01, UC-SC08-18 |
| [S-SC08-L02 Dues payments](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l02-dues-payments.md) | Non-profit association | All | UC-SC08-01 |
| [S-SC08-L04 Gifts](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l04-gifts.md) | Non-profit association | All | UC-SC08-04, UC-SC08-07 |
| [S-SC08-L06 Tax receipts](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l06-tax-receipts.md) | Non-profit association | All | UC-SC08-24 |
| [S-SC08-L07 Debit mandates](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l07-debit-mandates.md) | Non-profit association | Open: Signed, Revoked | UC-SC08-07 |
| [S-SC08-L12 Association events](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l12-association-events.md) | Non-profit association | Open: Planned | UC-SC08-12 |
| [S-SC08-L19 Fundraising pages](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l19-fundraising-pages.md) | Non-profit association | All | UC-SC08-24 |
| [S-SC09-L01 Appointments](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l01-appointments.md) | Health practices | Open: Booked, Confirmed, NoShow | UC-SC09-01, UC-SC09-02, UC-SC09-11 |
| [S-SC09-L02 Patients](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l02-patients.md) | Health practices | All | UC-SC09-03, UC-SC09-17 |
| [S-SC09-L03 Clinical record entries](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l03-clinical-record-entries.md) | Health practices | Mine: author | UC-SC09-11, UC-SC09-17 |
| [S-SC09-L07 Patient invoices](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l07-patient-invoices.md) | Health practices | All | UC-SC09-08 |
| [S-SC09-L17 Dental quotes](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l17-dental-quotes.md) | Health practices | All | UC-SC09-24 |
| [S-SC10-L03 Viewings](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l03-viewings.md) | Real estate | All | UC-SC10-03 |
| [S-SC10-L04 Offers](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l04-offers.md) | Real estate | All | UC-SC10-04 |
| [S-SC10-L07 Leases](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l07-leases.md) | Real estate | All | UC-SC10-07 |
| [S-SC10-L08 Deposits](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l08-deposits.md) | Real estate | All | UC-SC10-07, UC-SC10-10 |
| [S-SC10-L09 Rent calls](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l09-rent-calls.md) | Real estate | All | UC-SC10-08, UC-SC10-19 |
| [S-SC10-L10 Charge settlements](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l10-charge-settlements.md) | Real estate | All | UC-SC10-11 |
| [S-SC10-L11 Landlord statements](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l11-landlord-statements.md) | Real estate | All | UC-SC10-19 |
| [S-SC10-L13 Co-owners' assemblies](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l13-co-owners-assemblies.md) | Real estate | Mine: co-ownership | UC-SC10-15 |
| [S-SC10-L14 Call for funds](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l14-call-for-funds.md) | Real estate | Mine: co-ownership | UC-SC10-16 |
| [S-SC10-L16 Co-ownerships](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l16-co-ownerships.md) | Real estate | All | UC-SC10-19 |
| [S-SC10-L17 Stays](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l17-stays.md) | Real estate | All | UC-SC10-21 |
| [S-SC10-L19 Furnished properties](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l19-furnished-properties.md) | Real estate | All | UC-SC10-23 |
| [S-SC10-L20 Memberships](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l20-memberships.md) | Real estate | All | UC-SC10-24 |
| [S-SC11-L04 Engagement letters](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l04-engagement-letters.md) | Professional firms | All | UC-SC11-03 |
| [S-SC11-L05 Matters](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l05-matters.md) | Professional firms | Open: Open | UC-SC11-13 |
| [S-SC11-L07 Fee bills](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l07-fee-bills.md) | Professional firms | All | UC-SC11-13 |
| [S-SC11-L10 Matter documents](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l10-matter-documents.md) | Professional firms | All | UC-SC11-10 |
| [S-SC11-L17 Policies](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l17-policies.md) | Professional firms | All | UC-SC11-22 |
| [S-SC12-L03 Enrolments](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l03-enrolments.md) | Education and training | Open: Enrolled | UC-SC12-03, UC-SC12-05 |
| [S-SC12-L04 Training agreements](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l04-training-agreements.md) | Education and training | All | UC-SC12-03 |
| [S-SC12-L05 Training fundings](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l05-training-fundings.md) | Education and training | All | UC-SC12-23 |
| [S-SC12-L06 Attendance sheets](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l06-attendance-sheets.md) | Education and training | All | UC-SC12-06 |
| [S-SC12-L07 E-learning records](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l07-e-learning-records.md) | Education and training | All | UC-SC12-07 |
| [S-SC12-L08 Completion certificates](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l08-completion-certificates.md) | Education and training | All | UC-SC12-08 |
| [S-SC12-L09 Survey answers](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l09-survey-answers.md) | Education and training | All | UC-SC12-09, UC-SC12-14 |
| [S-SC12-L14 Students](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l14-students.md) | Education and training | All | UC-SC12-15 |
| [S-SC12-L16 Grades](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l16-grades.md) | Education and training | All | UC-SC12-17 |
| [S-SC12-L17 Pupil absences](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l17-pupil-absences.md) | Education and training | All | UC-SC12-18 |
| [S-SC12-L18 School fees](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l18-school-fees.md) | Education and training | All | UC-SC12-19 |
| [S-SC12-L22 Childcare places](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l22-childcare-places.md) | Education and training | All | UC-SC12-23 |
| [S-SC12-L23 Meal bookings](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l23-meal-bookings.md) | Education and training | All | UC-SC12-24 |
| [S-SC13-L09 Direct sales](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l09-direct-sales.md) | Agriculture and food | All | UC-SC13-10 |
| [S-SC13-L20 Basket subscriptions](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l20-basket-subscriptions.md) | Agriculture and food | All | UC-SC13-24 |
| [S-SC14-L01 Software subscriptions](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l01-software-subscriptions.md) | IT and software | Open: Trial, Active | UC-SC14-01, UC-SC14-10, UC-SC14-17 |
| [S-SC14-L02 Customer usage records](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l02-customer-usage-records.md) | IT and software | All | UC-SC14-17 |
| [S-SC14-L05 Service levels](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l05-service-levels.md) | IT and software | All | UC-SC14-05 |
| [S-SC14-L09 Health scores](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l09-health-scores.md) | IT and software | All | UC-SC14-10 |
| [S-SC14-L10 Processor agreements](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l10-processor-agreements.md) | IT and software | All | UC-SC14-11 |
| [S-SC14-L13 Data exports](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l13-data-exports.md) | IT and software | All | UC-SC14-14 |
| [S-SC14-L20 Sponsorships](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l20-sponsorships.md) | IT and software | All | UC-SC14-25 |
| [S-SC15-L01 Price agreements](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l01-price-agreements.md) | Wholesale and distribution | Open: Active | UC-SC15-18 |
| [S-SC15-L04 Sales orders](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l04-sales-orders.md) | Wholesale and distribution | All | UC-SC15-05, UC-SC15-18 |
| [S-SC16-L04 Artist contracts](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l04-artist-contracts.md) | Events and culture | All | UC-SC16-03 |
| [S-SC16-L05 Rider items](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l05-rider-items.md) | Events and culture | Mine: owner | UC-SC16-03 |
| [S-SC16-L07 Ticket orders](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l07-ticket-orders.md) | Events and culture | Open: Refunded, Exchanged | UC-SC16-05, UC-SC16-19 |
| [S-SC16-L08 Admission tickets](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l08-admission-tickets.md) | Events and culture | Open: Sent | UC-SC16-05 |
| [S-SC16-L09 Accreditations](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l09-accreditations.md) | Events and culture | All | UC-SC16-08 |
| [S-SC16-L12 Stands](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l12-stands.md) | Events and culture | All | UC-SC16-11 |
| [S-SC16-L16 Memberships](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l16-memberships.md) | Events and culture | All | UC-SC16-16 |
| [S-SC16-L17 Attendee messages](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l17-attendee-messages.md) | Events and culture | All | UC-SC16-19 |
| [S-SC16-L22 Galleries](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l22-galleries.md) | Events and culture | All | UC-SC16-24 |
| [S-SC17-L02 Salon bookings](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l02-salon-bookings.md) | Beauty and wellness | All | UC-SC17-02, UC-SC17-04 |
| [S-SC17-L03 Booking deposits](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l03-booking-deposits.md) | Beauty and wellness | All | UC-SC17-04 |
| [S-SC17-L04 Session packages](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l04-session-packages.md) | Beauty and wellness | All | UC-SC17-05 |
| [S-SC17-L05 Salon memberships](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l05-salon-memberships.md) | Beauty and wellness | All | UC-SC17-06 |
| [S-SC17-L13 Client files](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l13-client-files.md) | Beauty and wellness | All | UC-SC17-19 |
| [S-SC18-L01 Club memberships](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l01-club-memberships.md) | Sports and fitness | All | UC-SC18-01, UC-SC18-03, UC-SC18-04, UC-SC18-06 and more |
| [S-SC18-L03 Access events](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l03-access-events.md) | Sports and fitness | All | UC-SC18-03 |
| [S-SC18-L04 Classes](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l04-classes.md) | Sports and fitness | All | UC-SC18-06, UC-SC18-07 |
| [S-SC18-L05 Class bookings](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l05-class-bookings.md) | Sports and fitness | All | UC-SC18-03, UC-SC18-06, UC-SC18-07 |
| [S-SC18-L06 Licences](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l06-licences.md) | Sports and fitness | All | UC-SC18-09 |
| [S-SC18-L10 Coaching packages](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l10-coaching-packages.md) | Sports and fitness | All | UC-SC18-13 |
| [S-SC18-L12 Progress records](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l12-progress-records.md) | Sports and fitness | All | UC-SC18-15 |
| [S-SC18-L13 Court bookings](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l13-court-bookings.md) | Sports and fitness | All | UC-SC18-17 |
| [S-SC18-L14 Tournaments](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l14-tournaments.md) | Sports and fitness | All | UC-SC18-18 |
| [S-SC18-L15 Camp registrations](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l15-camp-registrations.md) | Sports and fitness | All | UC-SC18-19 |
| [S-SC18-L16 Rental items](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l16-rental-items.md) | Sports and fitness | All | UC-SC18-20 |
| [S-SC19-L01 Maintenance contracts](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l01-maintenance-contracts.md) | Trades and home services | All | UC-SC19-01 |
| [S-SC19-L04 Interventions](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l04-interventions.md) | Trades and home services | All | UC-SC19-08 |
| [S-SC19-L05 Site reports](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l05-site-reports.md) | Trades and home services | All | UC-SC19-08 |
| [S-SC19-L06 Household contracts](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l06-household-contracts.md) | Trades and home services | All | UC-SC19-09, UC-SC19-12 |
| [S-SC19-L12 Warranty certificates](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l12-warranty-certificates.md) | Trades and home services | All | UC-SC19-18 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Beauty and wellness](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[DevOps agents (hosted edition)](../../../02-functional/f25-devops-agents/screens/00-lists/README.md),
[Education and training](../../../08-sectors/sc12-education-and-training/screens/00-lists/README.md),
[Events and culture](../../../08-sectors/sc16-events-and-culture/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Home care](../../../08-sectors/sc04-home-care/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Non-profit association](../../../08-sectors/sc08-non-profit/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Professional firms](../../../08-sectors/sc11-professional-firms/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Real estate](../../../08-sectors/sc10-real-estate/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md),
[Retail](../../../08-sectors/sc02-retail/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md),
[Sports and fitness](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/README.md),
[Trades and home services](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U09 | desktop | ![Workspace, U09, light](mockups/workspace-desktop-light.png) | ![Workspace, U09, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U09 | phone | ![Workspace, U09, light](mockups/workspace-phone-light.png) | ![Workspace, U09, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
