🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
📣 [Marketing and communication: app shell and home](README.md) › 🧰 U12 Marketing and communication: workspace

# 🧰 U12 Marketing and communication: workspace

**Status:** ✅ specified

## Purpose

The views [U12 Marketing and communication](../../../01-users/personas/u12-marketing.md) works with, embedded on their
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
| [S-F2-L01 Custom fields](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l01-custom-fields.md) | No-code configuration | Open: Draft, Live | UC-F2-01 |
| [S-F2-L06 Document templates](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l06-document-templates.md) | No-code configuration | All | UC-F2-05 |
| [S-F2-L07 Email templates](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l07-email-templates.md) | No-code configuration | All | UC-F2-06 |
| [S-F2-L27 Legal mentions](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l27-legal-mentions.md) | No-code configuration | All | UC-F2-05 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F4-L28 Webinars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l28-webinars.md) | Meetings | Mine: host | UC-F4-29 |
| [S-F5-L01 Posts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l01-posts.md) | Social media and marketing | All | UC-F5-01, UC-F5-04, UC-F5-03, UC-F5-05 and more |
| [S-F5-L02 Social accounts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l02-social-accounts.md) | Social media and marketing | All | UC-F5-07 |
| [S-F5-L03 Automatic post rules](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l03-automatic-post-rules.md) | Social media and marketing | All | UC-F5-03 |
| [S-F5-L04 Social messages](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l04-social-messages.md) | Social media and marketing | All | UC-F5-05, UC-F5-20 |
| [S-F5-L05 Email or SMS campaigns](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l05-email-or-sms-campaigns.md) | Social media and marketing | All | UC-F5-08, UC-F5-09, UC-F5-16, UC-F5-23 |
| [S-F5-L06 Journeys](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l06-journeys.md) | Social media and marketing | All | UC-F5-10 |
| [S-F5-L07 Registration events](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l07-registration-events.md) | Social media and marketing | Open: Draft, Planned, Published | UC-F5-11, UC-F5-17 |
| [S-F5-L08 Surveys](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l08-surveys.md) | Social media and marketing | Open: Draft, Sent | UC-F5-12 |
| [S-F5-L09 Contact segments](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l09-contact-segments.md) | Social media and marketing | Open: Active | UC-F5-14 |
| [S-F5-L10 Consent and suppression records](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l10-consent-and-suppression-records.md) | Social media and marketing | Mine: contact | UC-F5-14, UC-F5-15, UC-F5-16, UC-F5-19 |
| [S-F5-L11 Ticket type and seat maps](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l11-ticket-type-and-seat-maps.md) | Social media and marketing | Open: Draft | UC-F5-17 |
| [S-F5-L13 Landing page and forms](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l13-landing-page-and-forms.md) | Social media and marketing | All | UC-F5-19 |
| [S-F5-L14 WhatsApp templates](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l14-whatsapp-templates.md) | Social media and marketing | All | UC-F5-20 |
| [S-F5-L15 Brand assets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l15-brand-assets.md) | Social media and marketing | Open: Draft | UC-F5-21 |
| [S-F5-L16 A/B tests](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l16-a-b-tests.md) | Social media and marketing | All | UC-F5-22 |
| [S-F5-L17 Campaign budgets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l17-campaign-budgets.md) | Social media and marketing | Open: Open | UC-F5-23 |
| [S-F5-L18 Contacts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l18-contacts.md) | Social media and marketing | All | UC-F5-14, UC-F5-15 |
| [S-F5-L19 Trigger events](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l19-trigger-events.md) | Social media and marketing | All | UC-F5-03 |
| [S-F5-L20 Waiting lists](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l20-waiting-lists.md) | Social media and marketing | All | UC-F5-17 |
| [S-F5-L21 Marketing cards](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l21-marketing-cards.md) | Social media and marketing | All | UC-F5-24 |
| [S-F5-L22 Referrals](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l22-referrals.md) | Social media and marketing | All | UC-F5-25 |
| [S-F5-L23 Push campaigns](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l23-push-campaigns.md) | Social media and marketing | All | UC-F5-26 |
| [S-F5-L24 Brand mentions](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l24-brand-mentions.md) | Social media and marketing | All | UC-F5-27 |
| [S-F5-L25 Postal campaigns](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l25-postal-campaigns.md) | Social media and marketing | All | UC-F5-28 |
| [S-F6-L11 Timeline entries](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l11-timeline-entries.md) | Customers and sales | All | UC-F18-29 |
| [S-F6-L20 Leads](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l20-leads.md) | Customers and sales | All | UC-F5-05, UC-F5-13, UC-F5-19 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F11-L01 Websites](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l01-websites.md) | Online shop (plugin) | All | UC-F11-01, UC-F11-16 |
| [S-F11-L02 Web pages](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l02-web-pages.md) | Online shop (plugin) | All | UC-F11-01, UC-F11-16 |
| [S-F11-L03 Online products](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l03-online-products.md) | Online shop (plugin) | All | UC-F11-02, UC-F11-12, UC-F11-20, UC-F11-23 and more |
| [S-F11-L04 Carts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l04-carts.md) | Online shop (plugin) | Mine: owner | UC-F11-20 |
| [S-F11-L05 Checkouts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l05-checkouts.md) | Online shop (plugin) | All | UC-F11-21, UC-F11-29 |
| [S-F11-L08 Withdrawal requests](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l08-withdrawal-requests.md) | Online shop (plugin) | All | UC-F11-29 |
| [S-F11-L10 Product reviews](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l10-product-reviews.md) | Online shop (plugin) | Open: ToCheck, Published | UC-F11-15 |
| [S-F11-L11 Online promotion codes](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l11-online-promotion-codes.md) | Online shop (plugin) | All | UC-F11-03 |
| [S-F11-L12 Cart reminders](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l12-cart-reminders.md) | Online shop (plugin) | All | UC-F11-14 |
| [S-F11-L13 Channel listings](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l13-channel-listings.md) | Online shop (plugin) | All | UC-F11-18 |
| [S-F11-L14 Legal pages](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l14-legal-pages.md) | Online shop (plugin) | All | UC-F11-19 |
| [S-F11-L15 Tracker consents](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l15-tracker-consents.md) | Online shop (plugin) | All | UC-F11-17 |
| [S-F11-L16 Fraud checks](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l16-fraud-checks.md) | Online shop (plugin) | All | UC-F11-21 |
| [S-F11-L18 Product contents](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l18-product-contents.md) | Online shop (plugin) | All | UC-F11-23 |
| [S-F11-L19 Product feeds](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l19-product-feeds.md) | Online shop (plugin) | All | UC-F11-24 |
| [S-F11-L20 Product safety informations](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l20-product-safety-informations.md) | Online shop (plugin) | All | UC-F11-25 |
| [S-F11-L21 Pre-order and reservations](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l21-pre-order-and-reservations.md) | Online shop (plugin) | Open: Open, Shipped, Released | UC-F11-26 |
| [S-F11-L24 Donations](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l24-donations.md) | Online shop (plugin) | Mine: donor | UC-F11-30 |
| [S-F11-L27 Country price lists](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l27-country-price-lists.md) | Online shop (plugin) | Mine: website | UC-F11-33 |
| [S-F14-L25 Themes](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l25-themes.md) | Plugin store | All | UC-F14-32 |
| [S-F17-L01 Competitors](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l01-competitors.md) | Competitive analysis | All | UC-F17-01, UC-F17-02 |
| [S-F17-L02 Company facts](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l02-company-facts.md) | Competitive analysis | All | UC-F17-02 |
| [S-F17-L03 Price points](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l03-price-points.md) | Competitive analysis | All | UC-F17-03 |
| [S-F17-L04 Job signals](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l04-job-signals.md) | Competitive analysis | All | UC-F17-04 |
| [S-F17-L07 Review digests](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l07-review-digests.md) | Competitive analysis | All | UC-F17-07 |
| [S-F17-L08 Mentions](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l08-mentions.md) | Competitive analysis | All | UC-F17-08, UC-F17-25 |
| [S-F17-L10 Analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l10-analysis.md) | Competitive analysis | All | UC-F17-12 |
| [S-F17-L11 Battle cards](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l11-battle-cards.md) | Competitive analysis | All | UC-F17-24 |
| [S-F17-L13 Alerts](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l13-alerts.md) | Competitive analysis | All | UC-F17-15 |
| [S-F17-L17 Price indexes](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l17-price-indexes.md) | Competitive analysis | All | UC-F17-03, UC-F17-25 |
| [S-F17-L19 Data cost lines](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l19-data-cost-lines.md) | Competitive analysis | All | UC-F17-28 |
| [S-F17-L20 Call topic signals](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l20-call-topic-signals.md) | Competitive analysis | All | UC-F17-24 |
| [S-F17-L21 Ad records](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l21-ad-records.md) | Competitive analysis | All | UC-F17-26 |
| [S-F17-L22 Watched pages](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l22-watched-pages.md) | Competitive analysis | All | UC-F17-27 |
| [S-F17-L23 Keywords](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l23-keywords.md) | Competitive analysis | All | UC-F17-28 |
| [S-F18-L01 Hosted websites](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l01-hosted-websites.md) | Hosted websites and domains (hosted edition) | All | UC-F18-01, UC-F18-13, UC-F18-16 |
| [S-F18-L02 Pages](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l02-pages.md) | Hosted websites and domains (hosted edition) | All | UC-F18-01, UC-F18-03, UC-F18-04, UC-F18-17 and more |
| [S-F18-L03 Identities](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l03-identities.md) | Hosted websites and domains (hosted edition) | All | UC-F18-02 |
| [S-F18-L04 Contact messages](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l04-contact-messages.md) | Hosted websites and domains (hosted edition) | Open: Sent, Held | UC-F18-04, UC-F18-24 |
| [S-F18-L10 Publication check reports](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l10-publication-check-reports.md) | Hosted websites and domains (hosted edition) | All | UC-F18-14 |
| [S-F18-L11 Audience figures](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l11-audience-figures.md) | Hosted websites and domains (hosted edition) | All | UC-F18-18 |
| [S-F18-L13 Blog articles](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l13-blog-articles.md) | Hosted websites and domains (hosted edition) | All | UC-F18-21 |
| [S-F18-L14 Redirects](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l14-redirects.md) | Hosted websites and domains (hosted edition) | All | UC-F18-22 |
| [S-F18-L16 Spam holds](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l16-spam-holds.md) | Hosted websites and domains (hosted edition) | Open: Held, Released | UC-F18-04, UC-F18-24 |
| [S-F18-L17 Sector templates](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l17-sector-templates.md) | Hosted websites and domains (hosted edition) | All | UC-F18-25 |
| [S-F18-L18 Search settings](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l18-search-settings.md) | Hosted websites and domains (hosted edition) | All | UC-F18-26 |
| [S-F18-L20 Page tests](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l20-page-tests.md) | Hosted websites and domains (hosted edition) | All | UC-F18-28 |
| [S-F18-L21 Visits](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l21-visits.md) | Hosted websites and domains (hosted edition) | All | UC-F18-29 |
| [S-F18-L22 Accessibility statements](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l22-accessibility-statements.md) | Hosted websites and domains (hosted edition) | All | UC-F18-30 |
| [S-F18-L23 Page audiences](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l23-page-audiences.md) | Hosted websites and domains (hosted edition) | All | UC-F18-31 |
| [S-SC02-L03 Product grids](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l03-product-grids.md) | Retail | All | UC-SC02-02 |
| [S-SC02-L04 Seasons](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l04-seasons.md) | Retail | Open: Planned, Selling, Clearing | UC-SC02-02 |
| [S-SC02-L08 Markdowns](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l08-markdowns.md) | Retail | All | UC-SC02-06 |
| [S-SC08-L01 Members](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l01-members.md) | Non-profit association | Mine: contact | UC-SC08-17 |
| [S-SC08-L04 Gifts](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l04-gifts.md) | Non-profit association | All | UC-SC08-24 |
| [S-SC08-L05 Fundraising campaigns](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l05-fundraising-campaigns.md) | Non-profit association | All | UC-SC08-05 |
| [S-SC08-L06 Tax receipts](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l06-tax-receipts.md) | Non-profit association | All | UC-SC08-24 |
| [S-SC08-L19 Fundraising pages](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l19-fundraising-pages.md) | Non-profit association | All | UC-SC08-24 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Competitive analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Non-profit association](../../../08-sectors/sc08-non-profit/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Plugin store](../../../02-functional/f14-plugin-store/screens/00-lists/README.md),
[Retail](../../../08-sectors/sc02-retail/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U12 | desktop | ![Workspace, U12, light](mockups/workspace-desktop-light.png) | ![Workspace, U12, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U12 | phone | ![Workspace, U12, light](mockups/workspace-phone-light.png) | ![Workspace, U12, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
