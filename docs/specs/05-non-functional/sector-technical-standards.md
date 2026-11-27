🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 📐 Sector technical standards

# 📐 Sector technical standards

**Status:** ✅ research done (2026-11-10); decided by D207

The owner asked that the legal assistant also cover the technical standards applicable to each activity sector
SimpleERP can be configured for, researched and documented here
([D190](../06-decisions/f15-legal-assistant/d190-legal-assistant-askers.md)), and that law packs, EU regulation and
technical standards be pulled from official sources with no human intervention
([D205](../06-decisions/f15-legal-assistant/d205-law-packs-fed-from-official-apis.md)). This page holds the research of
2026-11-10 by a research agent, with its sources; what could not be checked is marked **unverified**. Check the
unverified items before relying on them.

## Requirement

The legal corpus of [F15](../02-functional/f15-legal-assistant/README.md) holds, for each sector of
[08-sectors](../08-sectors/README.md), its mandatory technical regulations, the voluntary standards made mandatory by
reference or contract, and the usual certifications, each with its source, licence and how it is obtained (T11).

## Finding and decision

Published law (Légifrance, EUR-Lex) and most official guidance are free to reuse and can be pulled unattended in full,
as D205 asks. Copyrighted standards cannot: AFNOR and ISO expressly forbid putting their standards, including their
metadata for AFNOR, into AI systems, and opt out of the text and data mining exception (section 18 below). How
SimpleERP handles them is [Q15](../07-questions/q15-copyrighted-standards.md).

## Research of 2026-11-10

### 0. Legend: access codes used in the tables

| Code | Meaning | Licence and access | Machine-readable |
|---|---|---|---|
| **LF** | French published law on Légifrance (codes, lois, décrets, arrêtés) | Free. Reuse under Licence Ouverte 2.0 (Etalab), DILA no longer requires prior approval. | Yes. Légifrance API on PISTE (free, registration, quotas, JSON). DILA bulk XML dumps LEGI (consolidated codes and texts), JORF (Journal officiel), KALI (collective agreements), CNIL, JADE, CASS, etc. at echanges.dila.gouv.fr/OPENDATA, with **daily** incremental archives (LEGI_20261108, LEGI_20261109 seen on 10 Nov 2026). |
| **EU** | EU regulation or directive on EUR-Lex | Free. Reuse allowed with source acknowledgement (Commission Decision 2011/833/EU). | Yes. Cellar SPARQL endpoint (publications.europa.eu/webapi/rdf/sparql), REST API, ELI URIs, data dumps. Updated daily as the Official Journal is published. |
| **AF** | AFNOR standard (NF, NF EN, NF EN ISO, NF DTU, FD, XP) | Paid copyright document (per standard, or CObaz subscription). Default purchase is for the natural person who bought it; storing it on the company network needs paid "sharing rights"; AFNOR "expressly opposes" integration into AI engines or algorithms and text and data mining, including of metadata, unless it formally agrees. Full text cannot be indexed by SimpleERP. | No public API. Catalogue on boutique.afnor.org (also covered by the AI opposition). |
| **AF-M** | AFNOR standard made mandatory by an arrêté (décret n° 2009-697, art. 17) | Free **online consultation only** on the boutique.afnor.org page of the standard (FileOpen viewer, account login) or in AFNOR offices and CCIs. Not downloadable for free. Still AFNOR copyright, same AI opposition. | No. |
| **ISO** | ISO or ISO/IEC standard | Paid copyright document, sold in France by AFNOR. ISO terms forbid any AI or machine-learning use, explicitly including "embedding, prompting, querying" an AI system with ISO content, unless a separate licence is issued by ISO, a member body or an authorised distributor. ISO opts out of the EU text-and-data-mining exception (Directive 2019/790, art. 4). | Metadata only: ISO Open Data (reference, title in en/fr, ICS, edition, stage, replaces/replacedBy, and the **scope** text) under ODC-By 1.0, updated **daily**, Parquet/JSONL/CSV. |
| **CEN** | European standard (EN), incl. harmonised standards and Eurocodes | Sold in France as NF EN by AFNOR under AF terms. References of harmonised standards are published free in the Official Journal and on the Commission page. | Reference lists only. |
| **GOV** | Official French guidance (ministry, agency) | Free. Licence varies: Licence Ouverte where stated (ANSSI guides; DILA datasets); otherwise "all rights reserved", reuse on request (INRS). | Usually no (PDF/HTML), some datasets on data.gouv.fr. |
| **PRIV** | Private scheme owner (IFS, BRCGS, GlobalG.A.P., Qualibat, GS1) | Usually free download or member access, copyright of the scheme owner, AI and redistribution terms to be checked per scheme (**unverified** for each). | No. |

Notation in tables: "Mandatory?" = **Yes** (published law), **Yes by reference** (voluntary standard made binding by a
legal text), **Contract/insurer** (de facto required by clients, insurers or public procurement), **Voluntary**,
**Required for X** (needed to obtain a benefit, label or market access).


### 1. Horizontal items (apply to most sectors; not repeated in each sector table)

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| RGPD / GDPR, Regulation (EU) 2016/679 | regulation | Yes | Personal data processing | https://eur-lex.europa.eu/eli/reg/2016/679/oj | EU | Cellar SPARQL |
| CNIL référentiels and guidance | regulation guidance | Soft law (referenced by CNIL in controls) | Sector data-processing frameworks (HR, customers, health practices, etc.) | https://www.cnil.fr/fr | GOV (licence **unverified**); CNIL decisions also in DILA "CNIL" dump | DILA CNIL dump for decisions |
| Code du travail, 4th part (health and safety): risk assessment (DUERP), work equipment, electrical work | regulation | Yes | Employer health and safety duties | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/ | LF | LF API + LEGI dump |
| NF C 18-510 (electrical operations and habilitation électrique) | standard | Yes by reference (Code du travail R4544-3 and following). Conseil d'État 30 Dec 2021 n° 436420 annulled the arrêté that made it mandatory without free access | Electrical work and electrical habilitation of staff | Code du travail chapter: https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000022848014/ ; ruling summary: https://www.marche-public.fr/contrats-publics/Normes-techniques-nf-obligatoires-consultables-gratuitement-jp-ce-436420.htm | AF (current mandatory status after 2021 ruling **unverified**) | No |
| ERP fire safety: arrêté du 25 juin 1980 (règlement de sécurité contre les risques d'incendie et de panique dans les ERP) | regulation | Yes, for any premises receiving the public (shops, restaurants, practices, training rooms, venues) | Construction, equipment, staffing and checks per ERP type (M shops, N restaurants, O hotels, U care, R teaching, L venues, W offices, CTS tents, PA open air) | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000290033 ; consolidated id https://www.legifrance.gouv.fr/loda/id/LEGITEXT000020303557 | LF | LF API + LEGI dump |
| Accessibility of new ERP: arrêté du 20 avril 2017 | regulation | Yes (new ERP and installations open to the public, permits filed from 1 July 2017) | Paths, entrances, stairs, lifts, sanitary facilities, etc. | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034485459 | LF | LF API + LEGI dump |
| Accessibility of existing ERP: arrêté du 8 décembre 2014 | regulation | Yes | Existing ERP accessibility rules | **URL unverified** | LF | LF API |
| Tertiary buildings energy reduction ("décret tertiaire"): CCH R174-22 to R174-32 (origin décret n° 2019-771) | regulation | Yes, for owners and tenants of tertiary floor space of 1,000 m² or more | Energy-use reduction targets 2030/2040/2050, yearly declaration on OPERAT | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043819497/ ; https://operat.ademe.fr/ | LF | LF API |
| Code de la consommation | regulation | Yes for B2C | Pre-contract information, price display, legal guarantees | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069565/ | LF | LF API |
| Code de commerce | regulation | Yes | Invoicing mentions, CGV, payment terms, commercial negotiations | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000005634379/ | LF | LF API |
| B2B e-invoicing and e-reporting reform (CGI art. 289 bis, 290 and 290 A; from 2027-01-01 the duties are in CIBS L216-33 to L216-56, and the CGI rules on the invoice format and the transmissions stay in force until the regulatory part of the CIBS takes them over, CR-FR-016 and CR-FR-017; DGFiP external specifications) | regulation + technical specification | Yes: reception by all companies and issuance by large and mid-sized firms from 1 Sep 2026; issuance by SMEs and micro-firms from 1 Sep 2027; via an approved platform (PA) | Invoice formats, flows, statuses, e-reporting | https://aife.economie.gouv.fr/nos-applications/facturation-electronique-b2b/ ; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf | GOV (specifications free; licence **unverified**) | Specifications as documents/XSD (**unverified**) |
| EN 16931-1 and CEN/TS 16931-2 (e-invoice semantic model and syntaxes) | standard | Yes by reference (underlies UBL/CII/Factur-X profiles of the reform) | Core invoice data model | https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/Obtaining+a+copy+of+the+European+standard+on+eInvoicing | Free of charge for parts 1 and 2 under a 2018 Commission-CEN licence agreement, via national bodies; the Commission page reports it also permits derivative use (**exact licence wording unverified**). Parts 3 to 6 are paid. A 2026 edition of part 1 is sold by NSAI; whether free access covers it is **unverified** | No |
| Cash-register software security (CGI art. 286 I 3° bis until 2026-12-31, moved out of the CGI from 2027-01-01 by ordonnance n° 2025-1247, CR-FR-024; BOI-TVA-DECLA-30-10-30) | regulation | Yes for every VAT-registered business recording customer payments in software with a till function | Inalterability, security, retention and archiving of till data; proof by certificate from an accredited body (NF525 by Infocert, or LNE) or, again since the 2026 finance law, an individual publisher's attestation; fine €7,500 | https://bofip.impots.gouv.fr/bofip/10691-PGP.html/identifiant=BOI-TVA-DECLA-30-10-30-20251001 ; https://bofip.impots.gouv.fr/bofip/15035-PGP.html/ACTU-2026-00073 | GOV (BOFiP, free; BOFiP open data on data.gouv.fr **unverified**) | No API verified |
| Product liability, Directive (EU) 2024/2853 | regulation | Yes (transposition due 2026) | Liability for defective products, now incl. software | https://eur-lex.europa.eu/eli/dir/2024/2853/oj | EU | Cellar SPARQL |
| General product safety, Regulation (EU) 2023/988 | regulation | Yes for consumer products | Safety, traceability, online marketplaces, recalls | https://eur-lex.europa.eu/eli/reg/2023/988/oj | EU | Cellar SPARQL |
| European Accessibility Act, Directive (EU) 2019/882 | regulation | Yes for listed products and services (e-commerce, banking, e-books, ticketing terminals) since 28 June 2025 | Accessibility of products and services | https://eur-lex.europa.eu/eli/dir/2019/882/oj | EU | Cellar SPARQL |
| ISO 9001 (quality), ISO 14001 (environment), ISO 45001 (health and safety), ISO 50001 (energy) | standard + certification | Voluntary; often Contract (large clients, public tenders) | Management systems | ISO metadata: https://www.iso.org/open-data.html | ISO (sold in France as NF EN ISO, AF) | ISO Open Data (metadata and scope only) |


### 2. SC01 Construction

Sector folder: [SC01](../08-sectors/sc01-construction/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Code de la construction et de l'habitation (CCH) | regulation | Yes | Building rules (energy, accessibility, safety, tertiary buildings) | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074096/ | LF | LF API + LEGI dump |
| RE2020: décret n° 2021-1004 du 29 juillet 2021 (CCH R172-x) and implementing arrêtés | regulation | Yes for new buildings (housing since 1 Jan 2022, offices and schools since 1 July 2022) | Energy and carbon performance of new buildings | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043877196 ; ministry page https://www.ecologie.gouv.fr/politiques-publiques/reglementation-environnementale-re2020 | LF; ministry page GOV | LF API |
| Fire safety in dwellings: arrêté du 31 janvier 1986 | regulation | Yes | Residential building families, stairs, smoke control, yearly checks | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000474032/ | LF | LF API |
| ERP fire safety and accessibility | regulation | Yes when building or fitting out ERP | See horizontal table | see section 1 | LF | LF API |
| Works near networks (DT-DICT): Code de l'environnement R554-1 and following; arrêté du 15 février 2012 | regulation | Yes | Declarations before works, guichet unique, AIPR operator competence | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000025391351 ; https://www.reseaux-et-canalisations.ineris.fr/ | LF; guichet unique GOV | LF API |
| NF S70-003 (works near networks, technical guide parts) | standard | Yes by reference (**exact mandatory status unverified**) | Locating and working near networks | not located | AF / AF-M (**unverified**) | No |
| Ten-year liability and mandatory insurance: Code civil art. 1792 and following; Code des assurances L241-1 | regulation | Yes | Décennale liability, compulsory insurance | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006070721/ ; https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073984/ | LF | LF API |
| Construction Products Regulation (EU) No 305/2011, being replaced by Regulation (EU) 2024/3110 | regulation | Yes for manufacturers/importers; installers rely on CE marking and declarations of performance | Marketing of construction products | https://eur-lex.europa.eu/eli/reg/2011/305/oj ; https://eur-lex.europa.eu/eli/reg/2024/3110/oj | EU | Cellar SPARQL |
| Site safety: Code du travail (SPS coordination, PPSPS, carte BTP, asbestos sub-sections 3 and 4) | regulation | Yes | Site health and safety | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/ | LF | LF API |
| NF C 15-100 (low-voltage electrical installations) | standard | Yes by reference (shown as "mandatory application standard", free online consultation) | Design, installation and checking of LV installations | https://www.boutique.afnor.org/en-gb/standard/nf-c15100/lowvoltage-electrical-installations-completed-with-update-of-june-2005/fa005536/1556 | AF-M (the free-consultation edition is Dec 2002 with 2005 update; status of newer editions **unverified**) | No |
| NF DTU (Documents techniques unifiés, e.g. DTU 20.1 masonry, 31.2 timber frame, 43.1 roofing) | standard | Contract/insurer: required in public procurement and by décennale insurers in practice; voluntary in private law | Rules of the art for each trade | FFB guidance: https://www.ffbatiment.fr/techniques-batiment/normalisation-regles-de-lart/nf-dtu-normes/dossier/comment-se-procurer-une-norme-du-batiment | AF. Paid from AFNOR or CSTB (Reef subscription: https://boutique.cstb.fr/). **Free for Qualibat holders** for the standards and NF DTU of their speciality via the Qualibat "Espace entreprise" (FFB article of 14 Feb 2025) | No |
| Eurocodes (NF EN 1990 to NF EN 1999) | standard | Contract/insurer; some made mandatory by reference (e.g. seismic rules referencing NF EN 1998, **unverified**) | Structural design | CEN Eurocodes are sold through AFNOR | CEN / AF | No |
| CSTB Avis techniques and Documents techniques d'application | technical assessment | Contract/insurer (non-traditional techniques) | Fitness for use of innovative products | https://boutique.cstb.fr/ (free consultation of individual Avis techniques **unverified**) | CSTB copyright | No |
| RGE (Reconnu garant de l'environnement): décret n° 2014-812; arrêté du 1er décembre 2015 | certification | Required for clients to receive state renovation aids (MaPrimeRénov', CEE, eco-PTZ) | Qualification criteria for energy-renovation works | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029257402 ; https://legifrance.gouv.fr/eli/arrete/2015/12/1/ETLL1524415A/jo/texte | LF (criteria); scheme documents by Qualibat, Qualifelec, Qualit'EnR (PRIV) | LF API for texts |
| Qualibat, Qualifelec, Qualit'EnR (QualiPAC, QualiPV, QualiBois) qualifications | certification | Voluntary; Contract (tenders, insurers); required for RGE | Trade competence | https://www.qualibat.com/ ; https://www.qualifelec.fr/ ; Qualit'EnR site returned a bot challenge (**unverified**) | PRIV | No |
| OPPBTP prevention guidance | guidance | Voluntary | Site safety practice | https://www.oppbtp.com/ | GOV-like (licence **unverified**) | No |


### 3. SC02 Retail

Sector folder: [SC02](../08-sectors/sc02-retail/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Price display: Code de la consommation L112-1 to L112-7; arrêté du 3 décembre 1987 (still cited by the ministry in Jan 2026); arrêté du 16 avril 2024 (shrinkflation) | regulation | Yes | Price and unit-price display | https://www.economie.gouv.fr/entreprises/gerer-son-entreprise-au-quotidien/gerer-un-commerce/professionnels-quelles-sont-vos-obligations-en-matiere-daffichage-des-prix (Légifrance URL of the 1987 arrêté **unverified**) | LF; DGCCRF page GOV | LF API |
| Cash-register software certification (CGI 286 I 3° bis) | regulation | Yes | See section 1 | see section 1 | GOV | No |
| ERP type M fire safety; accessibility | regulation | Yes | See section 1 | see section 1 | LF | LF API |
| Food retail hygiene: Regulation (EC) No 852/2004; arrêté du 21 décembre 2009 (retail, storage, transport temperatures) | regulation | Yes for food retail | Hygiene, HACCP-based procedures, temperatures | https://eur-lex.europa.eu/eli/reg/2004/852/oj ; https://www.legifrance.gouv.fr/loda/id/LEGITEXT000021676844 | EU; LF | Cellar; LF API |
| Food information to consumers (INCO), Regulation (EU) No 1169/2011 | regulation | Yes for food | Labelling, allergens, nutrition declaration | https://eur-lex.europa.eu/eli/reg/2011/1169/oj | EU | Cellar SPARQL |
| General product safety, Regulation (EU) 2023/988 | regulation | Yes | Non-food product safety and recalls | https://eur-lex.europa.eu/eli/reg/2023/988/oj | EU | Cellar SPARQL |
| Non-automatic weighing instruments, Directive 2014/31/EU (and French legal metrology rules, **unverified**) | regulation | Yes for scales used in trade | Conformity and periodic verification of scales | https://eur-lex.europa.eu/eli/dir/2014/31/oj | EU | Cellar SPARQL |
| Packaging and packaging waste, Regulation (EU) 2025/40 (PPWR) | regulation | Yes (staged application) | Packaging design, labelling, reuse targets | https://eur-lex.europa.eu/eli/reg/2025/40/oj | EU | Cellar SPARQL |
| Extended producer responsibility and AGEC rules (Code de l'environnement L541-10 and following; Triman logo; receipts on request) | regulation | Yes | EPR schemes, sorting information, single-use plastics | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074220/ | LF | LF API |
| European Accessibility Act (e-commerce) | regulation | Yes for online shops of non-micro enterprises | Accessibility of e-commerce services | https://eur-lex.europa.eu/eli/dir/2019/882/oj | EU | Cellar |
| NF525 certification (Infocert) | certification | Voluntary route to prove the cash-register obligation | Till software inalterability | https://infocert.org/ | PRIV | No |
| GS1 barcodes (GTIN, GS1 General Specifications) | standard | Contract (required by retailers and marketplaces) | Product identification | GS1 France / gs1.org (specific page **unverified**, tried URL returned 404) | PRIV (member access) | No verified API |


### 4. SC03 Services (generic business services)

Sector folder: [SC03](../08-sectors/sc03-services/README.md).

Services is heterogeneous. The ERP should combine the horizontal items with the sub-sector regulation of each activity.
Examples verified:

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Consumer information and quotes (Code de la consommation) | regulation | Yes for B2C | Pre-contract information, quotes, mediation | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069565/ | LF | LF API |
| Private security activities: Code de la sécurité intérieure, Book VI; CNAPS authorisations | regulation | Yes for security firms | Licensing of firms and agents | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000025503132/ ; https://www.cnaps.interieur.gouv.fr/ | LF; GOV | LF API |
| Regulated crafts (hairdressing qualification, vehicle repair, etc.) | regulation | Yes per activity | Professional qualification | **unverified** (not researched per activity) | LF | LF API |
| NF Service certifications (AFNOR Certification) and ISO 9001 | certification | Voluntary | Service quality | https://certification.afnor.org/en/service/certification-of-services/3 (listing seen in search) | AF / ISO | No |
| Cleaning quality, NF EN 13549 | standard | Voluntary / Contract | Cleaning quality measurement | **unverified** | AF | No |


### 5. SC04 Home care (aide à domicile, SAP / SAAD, now "services autonomie à domicile")

Sector folder: [SC04](../08-sectors/sc04-home-care/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Code de l'action sociale et des familles (CASF), L313-1-3 (services autonomie à domicile) | regulation | Yes (authorised services) | Authorisation and obligations of home-support services | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074069/ | LF | LF API + LEGI dump |
| National specification (cahier des charges) of services autonomie à domicile: décret n° 2023-608 du 13 juillet 2023, CASF annexes 3-0 and 3-0-1 | regulation | Yes | Minimum technical operating conditions (on-call line, free quotes, yearly review, staff, coordination) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047837913 ; annex 3-0 https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037049462/ | LF | LF API |
| Services à la personne: Code du travail L7231-1 and following, D7231-1 (activity list), R7232-6 (agrément) | regulation | Yes (declaration; agrément for children under 3 and vulnerable adults) | Scope, tax-credit eligibility, approval | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000018500042/2022-04-25/ | LF | LF API |
| Agrément specification: arrêté du 24 novembre 2023 fixant le cahier des charges prévu à l'article R. 7232-6 (newer than the arrêté du 1er octobre 2018; whether it fully replaces it **unverified**) | regulation | Yes for approved SAP | Quality and information obligations for approved providers | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465776 | LF | LF API |
| HAS quality evaluation framework for social and medico-social services (ESSMS), since 2022 | regulation guidance | Yes for authorised ESSMS (periodic external evaluation) | Quality evaluation criteria | HAS site timed out (**URL unverified**) | GOV (HAS licence **unverified**) | No |
| Health data: RGPD; HDS hosting (CSP L1111-8) when the service hosts health data with a provider | regulation | Yes | Care-plan and health data protection and hosting | see SC09 | LF / EU | LF API / Cellar |
| NF X50-056 "Services aux personnes à domicile" (Aug 2014) and NF Service certification NF311 | standard + certification | Voluntary; AFNOR presents it as easing agrément renewal | Service quality for home services | https://www.boutique.afnor.org/fr-fr/norme/nf-x50056/services-aux-personnes-a-domicile/fa157675/30985 ; https://certification.afnor.org/services/certification-nf-service-services-aux-personnes-a-domicile | AF | No |
| Qualisap, Cap'Handéo labels | certification | Voluntary | Service quality, disability | **unverified** | PRIV | No |


### 6. SC05 Manufacturing

Sector folder: [SC05](../08-sectors/sc05-manufacturing/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Machinery Directive 2006/42/EC, replaced by Machinery Regulation (EU) 2023/1230 (applies from 20 January 2027) | regulation | Yes | Machinery safety, CE marking | https://eur-lex.europa.eu/eli/dir/2006/42/oj ; https://eur-lex.europa.eu/eli/reg/2023/1230/oj | EU | Cellar SPARQL |
| Low Voltage Directive 2014/35/EU; EMC Directive 2014/30/EU; ATEX Directive 2014/34/EU | regulation | Yes for those products | Electrical safety, EMC, explosive atmospheres | https://eur-lex.europa.eu/eli/dir/2014/35/oj ; https://eur-lex.europa.eu/eli/dir/2014/30/oj ; https://eur-lex.europa.eu/eli/dir/2014/34/oj | EU | Cellar |
| REACH Regulation (EC) No 1907/2006; CLP Regulation (EC) No 1272/2008 | regulation | Yes | Chemicals registration, classification, labelling | https://eur-lex.europa.eu/eli/reg/2006/1907/oj ; https://eur-lex.europa.eu/eli/reg/2008/1272/oj | EU | Cellar |
| Ecodesign for Sustainable Products Regulation (EU) 2024/1781; Batteries Regulation (EU) 2023/1542 | regulation | Yes (delegated acts per product group) | Ecodesign, digital product passport, batteries | https://eur-lex.europa.eu/eli/reg/2024/1781/oj ; https://eur-lex.europa.eu/eli/reg/2023/1542/oj | EU | Cellar |
| F-gas Regulation (EU) 2024/573 | regulation | Yes if refrigerants are used | Fluorinated gases | https://eur-lex.europa.eu/eli/reg/2024/573/oj | EU | Cellar |
| Energy Efficiency Directive (EU) 2023/1791 and Code de l'énergie (energy audits / energy management systems above consumption thresholds) | regulation | Yes above thresholds (French transposition details **unverified**) | Energy audits, ISO 50001 alternative | https://eur-lex.europa.eu/eli/dir/2023/1791/oj ; https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000023983208/ | EU; LF | Cellar; LF API |
| Installations classées (ICPE): Code de l'environnement Book V; sector arrêtés of general prescriptions | regulation | Yes above nomenclature thresholds | Environmental permits and technical prescriptions | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074220/ ; consolidated ICPE texts: https://aida.ineris.fr/ | LF; AIDA (INERIS) free (licence **unverified**) | LF API |
| Work equipment rules (Code du travail R4321-1 and following; periodic checks) and NF C 18-510 | regulation | Yes | Machine use, inspections, electrical habilitation | see section 1 | LF / AF | LF API |
| Harmonised standards (EN) giving presumption of conformity | standard | Voluntary but practically required for CE conformity | Technical means to meet EU essential requirements | References list: https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards_en | CEN / AF for text; reference list free | Reference list only |
| ISO 9001, 14001, 45001, 50001; IATF 16949 (automotive), EN 9100 (aerospace), ISO 13485 (medical devices) | standard + certification | Contract (customer requirements) | Management systems | https://www.iso.org/open-data.html (metadata) | ISO / AF; IATF and EN 9100 sold by sector bodies (**unverified**) | ISO Open Data metadata |
| NF mark and notified-body certification | certification | Required for some CE routes; voluntary NF | Product conformity | https://www.cofrac.fr/ (accreditation) | PRIV | No |


### 7. SC06 Restaurant and hospitality

Sector folder: [SC06](../08-sectors/sc06-hospitality/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Hygiene package: Regulation (EC) No 178/2002 (general food law), No 852/2004 (hygiene, HACCP principles), No 853/2004 (food of animal origin, if applicable); official controls Regulation (EU) 2017/625 | regulation | Yes | Food safety, HACCP-based procedures, traceability | https://eur-lex.europa.eu/eli/reg/2002/178/oj ; https://eur-lex.europa.eu/eli/reg/2004/852/oj ; https://eur-lex.europa.eu/eli/reg/2004/853/oj ; https://eur-lex.europa.eu/eli/reg/2017/625/oj | EU | Cellar SPARQL |
| Arrêté du 21 décembre 2009 (temperatures, culinary preparations, reference dishes kept 5 days, thawing) | regulation | Yes | Retail and catering hygiene rules | https://www.legifrance.gouv.fr/loda/id/LEGITEXT000021676844 | LF | LF API |
| Mandatory food-hygiene training: décret n° 2011-731 du 24 juin 2011 (at least one trained person per commercial restaurant); a newer décret n° 2025-922 is reported to set the training framework (**unverified**) | regulation | Yes | Hygiene training of staff | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024266465 | LF | LF API |
| INCO Regulation (EU) No 1169/2011 (allergen information incl. non-prepacked food; French implementing decree **unverified**) | regulation | Yes | Allergen display | https://eur-lex.europa.eu/eli/reg/2011/1169/oj | EU | Cellar |
| Guides de bonnes pratiques d'hygiène (GBPH), e.g. "Restaurateur" | guidance (validated by the administration, notice in JO) | Voluntary, but the reference used by inspectors | Practical HACCP application per trade | https://agriculture.gouv.fr/guides-de-bonnes-pratiques-dhygiene-gbph | GOV, free digital download (no longer printed); reuse licence **unverified** | No |
| ERP fire safety types N (restaurants) and O (hotels); accessibility | regulation | Yes | Fire and accessibility | see section 1 | LF | LF API |
| Alcohol licences (Code de la santé publique L3331-1 and following) | regulation | Yes for alcohol sales | Licence categories, permis d'exploitation | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072665/ | LF | LF API |
| Amplified sound: décret n° 2017-1244 (CSP R1336-1 and following) | regulation | Yes if amplified music | Sound levels, limiters, information | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000035388481 | LF | LF API |
| Hotel classification: arrêté du 29 décembre 2021 (Atout France référentiel, more than 240 criteria) | regulation + label | Voluntary classification (but the only way to use "étoiles") | Star-rating criteria | https://www.entreprises.gouv.fr/espace-entreprises/s-informer-sur-la-reglementation/hotels-et-hotels-de-tourisme ; https://www.classement.atout-france.fr/ (Légifrance URL of the arrêté **unverified**) | LF; Atout France guides GOV | LF API for the arrêté |
| Cash-register software; price display | regulation | Yes | See sections 1 and 3 | see above | GOV / LF | - |
| ISO 22000 | standard + certification | Voluntary | Food safety management | ISO Open Data | ISO | metadata only |


### 8. SC07 Transport and logistics

Sector folder: [SC07](../08-sectors/sc07-transport/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Code des transports | regulation | Yes | Registration, licences, capacity, sanctions | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000023086525/ | LF | LF API |
| Access to the occupation of road transport operator, Regulation (EC) No 1071/2009; international haulage market, Regulation (EC) No 1072/2009 | regulation | Yes | Establishment, good repute, financial standing, professional competence; cabotage | https://eur-lex.europa.eu/eli/reg/2009/1071/oj ; https://eur-lex.europa.eu/eli/reg/2009/1072/oj | EU | Cellar |
| Driving and rest times, Regulation (EC) No 561/2006 | regulation | Yes | Driving time, breaks, rest | https://eur-lex.europa.eu/eli/reg/2006/561/oj | EU | Cellar |
| Tachographs, Regulation (EU) No 165/2014 | regulation | Yes | Chronotachygraph equipment, data download | https://eur-lex.europa.eu/eli/reg/2014/165/oj | EU | Cellar |
| Driver CPC (FIMO/FCO), Directive 2003/59/EC | regulation | Yes | Initial and periodic driver training | https://eur-lex.europa.eu/eli/dir/2003/59/oj | EU | Cellar |
| ADR 2025 (UNECE Agreement on dangerous goods by road; next edition 2027) | regulation (international treaty, annexes A and B) | Yes when carrying dangerous goods | Classification, packaging, documents, vehicles, safety adviser | https://unece.org/adr-2025-files (reached through search; direct fetch blocked by Cloudflare) | Free PDF download from UNECE (UN copyright, reproduction via Copyright Clearance Center); updated every two years | No API (PDF) |
| Arrêté TMD du 29 mai 2009 | regulation | Yes | French application of ADR/RID/ADN, safety adviser, derogations | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000020796240 | LF | LF API |
| ATP Agreement (perishable foodstuffs, refrigerated transport) | regulation (treaty) | Yes for perishable food transport | Insulated and refrigerated equipment | UNECE page blocked by Cloudflare (**URL unverified**) | Free UNECE text (**unverified**) | No |
| Electronic freight transport information (eFTI), Regulation (EU) 2020/1056 | regulation | Authorities must accept eFTI (staged application) | Electronic transport documents | https://eur-lex.europa.eu/eli/reg/2020/1056/oj | EU | Cellar |
| Covered warehouses (ICPE rubrique 1510): arrêté du 11 avril 2017 | regulation | Yes above thresholds | Fire safety and design of warehouses | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000034429274/ | LF | LF API |
| Lift-truck competence (CACES R489 recommendations) | guidance | Practically required (employer authorisation to drive) | Forklift driver training | **unverified** | GOV/INRS copyright | No |
| ISO 9001, ISO 28000 (supply-chain security), TAPA FSR/TSR | standard + certification | Contract | Quality and security | ISO Open Data; TAPA **unverified** | ISO; PRIV | metadata only |
| CMR Convention (1956) and its e-CMR Additional Protocol (2008) | regulation (international treaty) | Yes for international road freight between contracting states | Consignment note, carrier liability, electronic note | UNECE (**URL unverified**) | Free UNECE text (**unverified**) | No |
| TIR Convention (1975) | regulation (treaty) | Yes when moving goods under TIR customs transit | Customs transit carnet, sealed vehicles | UNECE (**URL unverified**) | Free UNECE text (**unverified**) | No; eTIR exists (**unverified**) |
| RID (rail), IMDG Code (sea), IATA DGR (air) | regulation and industry rules | Yes for dangerous goods on those modes | Dangerous goods outside the road | OTIF, IMO, IATA (**URLs unverified**) | RID free; IMDG and IATA DGR sold (**unverified**) | No |
| ISO 14083 (greenhouse-gas emissions of transport chains) and the GLEC Framework | standard + industry method | Contract; the method behind CO2 information to clients | Emission calculation per shipment | ISO; Smart Freight Centre (**URLs unverified**) | ISO sold; GLEC free (**unverified**) | metadata only |
| GS1 standards: SSCC, GTIN, GS1 logistic label, GS1 EDI | standard | Contract (retail and industry clients) | Pallet and parcel identification, logistics messages | https://www.gs1.org/ (**unverified**) | Membership (**unverified**) | Yes (EDI, XML) |
| UN/EDIFACT transport messages (IFTMIN, IFTSTA) | standard | Contract | Transport orders and status messages | UNECE (**URL unverified**) | Free (**unverified**) | Yes |
| Incoterms 2020 (ICC) | standard (trade terms) | Contract | Cost and risk transfer between seller and buyer | ICC (**URL unverified**) | Sold by ICC (**unverified**) | No |
| ISO 39001 (road traffic safety management) | standard + certification | Contract | Road safety management system | ISO Open Data (**unverified**) | ISO | metadata only |


### 9. SC08 Non-profit association

Sector folder: [SC08](../08-sectors/sc08-non-profit/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Loi du 1er juillet 1901 relative au contrat d'association | regulation | Yes | Formation, declaration, capacity, dissolution | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000497458 | LF | LF API; DILA also publishes ASSOCIATIONS and COMPTES_DES_ASSOCIATIONS datasets |
| Association accounting: ANC regulations (association chart of accounts) | regulation (accounting standard published by a public body) | Yes for associations keeping accounts (thresholds) | Accounts, use of resources | https://www.anc.gouv.fr/ (specific regulation URL **unverified**) | GOV (free; licence **unverified**) | No |
| Tax receipts for gifts (CGI art. 200 and 238 bis) | regulation | Yes when issuing receipts | Eligibility and receipts | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/ | LF | LF API |
| Temporary drinks stalls (buvettes), CSP | regulation | Yes for events | Temporary alcohol licences | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072665/ | LF | LF API |
| ERP fire and accessibility when the association runs premises; event rules (see SC16) | regulation | Yes | Premises and events | see section 1 | LF | LF API |
| "Don en confiance" and similar labels | certification | Voluntary | Fund-raising transparency | **unverified** | PRIV | No |

Technical standards are marginal for SC08: the corpus is mostly law (association, tax, employment, RGPD) and the sector
of activity of the association (often SC04, SC12 or SC16).


### 10. SC09 Health practices (cabinets médicaux, paramédicaux)

Sector folder: [SC09](../08-sectors/sc09-health-practices/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Code de la santé publique (CSP), incl. professional ethics codes of regulated professions (e.g. doctors R4127-x) | regulation | Yes | Exercise of health professions, records, secrecy | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072665/ | LF | LF API |
| Health data hosting (HDS): CSP L1111-8; certification framework v2 approved by arrêté du 26 avril 2024 (JO 16 May 2024; existing hosts had until 16 May 2026 to move to v2) | regulation + certification | Yes: any provider hosting personal health data for a practice must be HDS-certified | Hosting security, data location (EU), contracts | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049577902 ; framework (FR) https://esante.gouv.fr/sites/default/files/media_entity/documents/referentiel_certification_hds---fr--v2.pdf ; (EN) https://esante.gouv.fr/sites/default/files/media_entity/documents/referentiel_certification_hds---en--v2.pdf ; arrêté article https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000049537698 | LF; ANS framework free (licence **unverified**). HDS v2 builds on NF ISO/IEC 27001:2023 (ISO) | LF API; PDF |
| Infectious healthcare waste (DASRI): CSP R1335-1 and following; arrêté du 7 septembre 1999 (storage) | regulation | Yes | Sorting, storage time limits, disposal chain | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000213467 ; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006190977/ | LF | LF API |
| Medical Devices Regulation (EU) 2017/745 | regulation | Yes (practices as users: vigilance, maintenance obligations) | Device conformity and vigilance | https://eur-lex.europa.eu/eli/reg/2017/745/oj | EU | Cellar |
| ERP type U fire safety, accessibility of practices | regulation | Yes | Premises | see section 1 | LF | LF API |
| ANS frameworks (PGSSI-S security policy, INS identity, Pro Santé Connect) | regulation guidance (some made opposable by arrêté) | Partly mandatory (**which ones unverified**) | Health IT security and identity | https://esante.gouv.fr/ (specific pages **unverified**) | GOV | No |
| Radiation protection for practices with X-ray equipment (CSP, Code du travail, ASN decisions) | regulation | Yes where applicable | Room design, dosimetry, checks | **specific decisions unverified** | LF | LF API |
| HAS recommendations | guidance | Soft law | Clinical and organisational good practice | HAS site timed out (**unverified**) | GOV | No |
| ISO/IEC 27001 | standard + certification | Contract (IT suppliers); prerequisite inside HDS | Information security | ISO Open Data | ISO | metadata only |


### 11. SC10 Real estate

Sector folder: [SC10](../08-sectors/sc10-real-estate/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Loi Hoguet n° 70-9 du 2 janvier 1970 (and implementing decree) | regulation | Yes | Professional card (CCI), financial guarantee, insurance, mandates, fees | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000512228/ | LF | LF API |
| Technical diagnostics file (DDT) and DPE: CCH (L271-4 and following; DPE articles and implementing arrêtés) | regulation | Yes for sales and lettings | Asbestos, lead, gas, electricity, termites, energy performance, natural risks | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074096/ (individual arrêtés **unverified**) | LF | LF API |
| Certification of diagnosticians by COFRAC-accredited bodies | certification | Yes for diagnosticians | Competence of diagnosticians | https://www.cofrac.fr/ | LF (rules); PRIV (certifiers) | No |
| Decency of dwellings, condominium law (loi du 10 juillet 1965), ALUR | regulation | Yes | Rental quality, co-ownership management | **specific URLs unverified** | LF | LF API |
| Anti-money laundering (Code monétaire et financier L561-2 and following) | regulation | Yes for estate agents | Customer due diligence | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072026/ | LF | LF API |
| NF Habitat / NF HQE certifications (for developers) | certification | Voluntary | Housing quality | **unverified** | PRIV | No |


### 12. SC11 Professional firms (avocats, experts-comptables, architectes)

Sector folder: [SC11](../08-sectors/sc11-professional-firms/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Lawyers: décret n° 2023-552 du 30 juin 2023 portant code de déontologie des avocats | regulation | Yes | Professional ethics | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047774060 | LF | LF API |
| Lawyers: Règlement intérieur national (RIN) of the CNB | professional regulation | Yes for avocats | Detailed professional rules | https://cnb.avocat.fr/ (RIN page URL **unverified**) | Free on CNB site (licence **unverified**); RIN decisions are also published in the JO (**unverified**) | No |
| Chartered accountants: ordonnance n° 45-2138, décret n° 2012-432 (exercise and ethics), professional standards of the Ordre | regulation + professional standards | Yes | Exercise, ethics, engagement standards | Ordre site timed out (**URLs unverified**) | LF; Ordre standards free (**unverified**) | LF API |
| Statutory auditors: normes d'exercice professionnel (NEP), homologated by arrêté | professional standards | Yes for auditors | Audit engagement standards | **unverified** | LF (homologation arrêtés) | LF API |
| Architects: loi n° 77-2, décret n° 80-217 (code des devoirs professionnels); Ordre des architectes | regulation | Yes | Exercise and ethics | https://www.architectes.org/ (Légifrance URLs **unverified**) | LF | LF API |
| Professional insurance (décennale for architects: Code des assurances L241-1) | regulation | Yes | Compulsory insurance | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073984/ | LF | LF API |
| Anti-money laundering (CMF L561-2) | regulation | Yes for lawyers (some activities), accountants | Due diligence | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072026/ | LF | LF API |
| Architects' technical references: CCH, RE2020, accessibility, fire, Eurocodes, NF DTU | regulation + standard | See SC01 | Design | see SC01 | LF / AF | see SC01 |
| ISO 9001 | standard + certification | Voluntary | Quality | ISO Open Data | ISO | metadata |


### 13. SC12 Education and training (organismes de formation)

Sector folder: [SC12](../08-sectors/sc12-education-and-training/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Qualiopi: Code du travail L6316-1 and following; décret n° 2019-565 (référentiel national qualité, 7 criteria, indicators); arrêté du 6 juin 2019 (audit methods) | regulation + certification | Yes to receive public or mutualised funds (since 1 January 2022) | Quality of training, skills assessment, VAE and apprenticeship actions | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038565259 ; https://www.legifrance.gouv.fr/loda/id/JORFTEXT000038565293 | LF | LF API |
| Qualiopi reading guide (guide de lecture, V.7 of 29 March 2021 found; a newer version **unverified**) | guidance | Used by certifiers in audits | Interpretation of each indicator | https://travail-emploi.gouv.fr/sites/travail-emploi/files/files-spip/pdf/guide-lecture-referentiel-qualite.pdf ; https://travail-emploi.gouv.fr/qualiopi-marque-de-certification-qualite-des-prestataires-de-formation | GOV (free; licence **unverified**) | No |
| Declaration of activity, BPF (annual pedagogical and financial report), Code du travail L6351-1 and following | regulation | Yes | Registration and reporting | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/ | LF | LF API |
| RNCP / Répertoire spécifique (France compétences) | regulation | Yes for certifying programmes (CPF eligibility) | Registration of certifications | https://www.francecompetences.fr/ | GOV (RNCP open data on data.gouv.fr **unverified**) | **unverified** |
| ERP type R fire safety; accessibility | regulation | Yes | Premises | see section 1 | LF | LF API |
| ISO 21001 (educational organisations) | standard + certification | Voluntary | Management system for education | ISO Open Data | ISO | metadata |


### 14. SC13 Agriculture and food

Sector folder: [SC13](../08-sectors/sc13-agriculture-and-food/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| General food law (EC) No 178/2002; hygiene (EC) No 852/2004 and No 853/2004; official controls (EU) 2017/625 | regulation | Yes | Food and feed safety, traceability, HACCP | https://eur-lex.europa.eu/eli/reg/2002/178/oj ; https://eur-lex.europa.eu/eli/reg/2004/852/oj ; https://eur-lex.europa.eu/eli/reg/2004/853/oj ; https://eur-lex.europa.eu/eli/reg/2017/625/oj | EU | Cellar |
| INCO Regulation (EU) No 1169/2011 | regulation | Yes | Food labelling | https://eur-lex.europa.eu/eli/reg/2011/1169/oj | EU | Cellar |
| Organic production, Regulation (EU) 2018/848 ("Agriculture Biologique" logo) | regulation + certification | Yes to use organic claims (certification by an approved body) | Organic rules and labelling | https://eur-lex.europa.eu/eli/reg/2018/848/oj | EU | Cellar |
| Geographical indications, Regulation (EU) 2024/1143; INAO product specifications (AOP, IGP, Label Rouge) | regulation + label | Yes for producers using the sign | Product specifications | https://eur-lex.europa.eu/eli/reg/2024/1143/oj ; https://www.inao.gouv.fr/ | EU; INAO specifications free (licence **unverified**) | Cellar |
| Deforestation Regulation (EU) 2023/1115 | regulation | Yes for listed commodities (application date postponed, current date **unverified**) | Due diligence on deforestation-free supply | https://eur-lex.europa.eu/eli/reg/2023/1115/oj | EU | Cellar |
| Code rural et de la pêche maritime | regulation | Yes | Farming, plant protection, animal health, HVE certification | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006071367/ | LF | LF API |
| Certiphyto (individual certificate for plant protection products, 5 categories, valid 5 years) | certification (mandatory) | Yes for any professional handling, selling or advising on PPP | Pesticide competence | https://mesdemarches.agriculture.gouv.fr/demarches/exploitation-agricole/obtenir-un-droit-une-autorisation/article/obtenir-le-certificat-produits-322 | GOV | No |
| Haute Valeur Environnementale (HVE) | certification | Voluntary | Farm environmental performance | Code rural (specific articles **unverified**) | LF | LF API |
| ICPE for livestock and agri-food plants | regulation | Yes above thresholds | Environmental prescriptions | https://aida.ineris.fr/ | LF / AIDA | LF API |
| GBPH (hygiene guides per food trade) | guidance | Voluntary (inspection reference) | Trade-specific hygiene | https://agriculture.gouv.fr/guides-de-bonnes-pratiques-dhygiene-gbph | GOV | No |
| Codex Alimentarius (General Principles of Food Hygiene, HACCP) | international standard | Voluntary (basis of EU HACCP) | HACCP method | https://codex.fao.org/ (redirect from fao.org Codex page) | FAO/WHO, free download (licence **unverified**) | No |
| IFS Food version 8 (mandatory for IFS audits since 1 January 2024) | standard + certification | Contract (French and German retailers for private labels) | Food-safety audit requirements | https://www.ifs-certification.com/en/ | PRIV: documents downloadable from IFS site (free download of the standard text itself **unverified**) | No |
| BRCGS Global Standard Food Safety Issue 9 | standard + certification | Contract (UK and export retailers) | Food-safety audit requirements | https://www.brcgs.com/ | PRIV: reported free download from the BRCGS store (secondary sources), copyright BRCGS | No |
| GlobalG.A.P. | standard + certification | Contract (fresh produce buyers) | Farm assurance | https://globalgap.org/ | PRIV (download terms **unverified**) | No |
| ISO 22000 / FSSC 22000 | standard + certification | Contract | Food safety management | ISO Open Data | ISO (FSSC scheme documents PRIV) | metadata |


### 15. SC14 IT and software

Sector folder: [SC14](../08-sectors/sc14-it-and-software/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| RGPD | regulation | Yes | Data protection, processor contracts | see section 1 | EU | Cellar |
| Cyber Resilience Act, Regulation (EU) 2024/2847 | regulation | Yes for products with digital elements placed on the EU market (reporting obligations from 11 Sep 2026, main obligations from 11 Dec 2027) | Secure development, vulnerability handling, CE marking of software | https://eur-lex.europa.eu/eli/reg/2024/2847/oj | EU | Cellar |
| NIS2 Directive (EU) 2022/2555 | regulation | Yes for essential and important entities once transposed. **France had not promulgated its transposition law ("loi Résilience") as of early November 2026, nor on 2026-11-27 (CR-FR-169)**; Commission referral to the CJEU reported on 9 July 2026 (secondary sources) | Cyber risk management, incident reporting | https://eur-lex.europa.eu/eli/dir/2022/2555/oj ; https://cyber.gouv.fr/ | EU; ANSSI guidance under Licence Ouverte 2.0 (stated in ANSSI guide notices) | Cellar |
| AI Act, Regulation (EU) 2024/1689 | regulation | Yes (staged application) | AI systems, GPAI, transparency | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | EU | Cellar |
| eIDAS, Regulation (EU) No 910/2014 as amended by (EU) 2024/1183 | regulation | Yes for trust services | E-signatures, seals, timestamps, EU digital identity wallet | https://eur-lex.europa.eu/eli/reg/2014/910/oj ; https://eur-lex.europa.eu/eli/reg/2024/1183/oj | EU | Cellar |
| E-invoicing reform and EN 16931 | regulation + standard | Yes for invoicing software and platforms | Formats and flows | see section 1 | GOV; EN 16931-1/-2 free | - |
| Cash-register software certification (if the product has a till function) | regulation | Yes for publishers' customers; certificate route via accredited body | Till data security | see section 1 | GOV | - |
| RGAA 4 (French web accessibility framework) and EN 301 549 | regulation + standard | Yes for public bodies and large companies; EAA for listed services | Digital accessibility | https://accessibilite.numerique.gouv.fr/ ; EN 301 549 on https://www.etsi.org/standards/ | RGAA free (Licence Ouverte **unverified**); ETSI EN free PDF download, reproduction needs ETSI permission | No |
| HDS (if hosting health data) and SecNumCloud (ANSSI cloud qualification) | certification | Required by clients in health and public sector | Hosting security | see SC09 ; https://cyber.gouv.fr/ | GOV (frameworks free) | No |
| ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001 | standard + certification | Contract | Information security, privacy, AI management | ISO Open Data | ISO | metadata |

Note for SimpleERP itself: the ERP is a product of SC14. If it ships a point-of-sale feature it falls under CGI 286 I
3° bis; it must produce EN 16931-based invoices for the French reform; and the CRA applies to it when placed on the EU
market commercially.


### 16. SC15 Wholesale and distribution

Sector folder: [SC15](../08-sectors/sc15-wholesale-and-distribution/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| Code de commerce: CGV, invoicing, payment terms, EGalim negotiation rules for food | regulation | Yes | B2B trade rules | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000005634379/ | LF | LF API |
| General product safety (EU) 2023/988; REACH; CLP; Batteries (EU) 2023/1542 | regulation | Yes for importers and distributors | Product compliance duties of distributors | see SC05 links | EU | Cellar |
| Packaging (EU) 2025/40 and French EPR (AGEC) | regulation | Yes | Packaging, EPR fees, labelling | see SC02 links | EU / LF | Cellar / LF API |
| Food wholesale: hygiene package, arrêté du 21 décembre 2009 (storage and transport temperatures), approval of establishments where required | regulation | Yes | Cold chain, traceability | see SC06 / SC13 links | EU / LF | Cellar / LF API |
| Deforestation Regulation (EU) 2023/1115 | regulation | Yes for listed commodities | Due diligence | https://eur-lex.europa.eu/eli/reg/2023/1115/oj | EU | Cellar |
| ADR and arrêté TMD (if dangerous goods shipped) | regulation | Yes | Dangerous goods | see SC07 | UNECE / LF | LF API |
| Covered warehouses ICPE 1510 | regulation | Yes above thresholds | Warehouse fire safety | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000034429274/ | LF | LF API |
| GS1 standards (GTIN, GLN, SSCC, EDI EANCOM) | standard | Contract | Identification and EDI | GS1 (URL **unverified**) | PRIV | No |
| IFS Logistics / IFS Broker; BRCGS Storage and Distribution | standard + certification | Contract | Logistics and trading food safety | https://www.ifs-certification.com/en/ ; https://www.brcgs.com/ | PRIV | No |
| ISO 9001 | standard + certification | Contract | Quality | ISO Open Data | ISO | metadata |


### 17. SC16 Events and culture

Sector folder: [SC16](../08-sectors/sc16-events-and-culture/README.md).

| Item | Kind | Mandatory? | Governs | Source URL | Licence and access | Machine-readable? |
|---|---|---|---|---|---|---|
| ERP fire safety, special establishments (Book IV): CTS chapiteaux, tentes et structures (arrêté du 23 janvier 1985, integrated in the 1980 regulation), PA open-air establishments, type L venues | regulation | Yes | Temporary structures, venues, open-air events | CTS chapter: https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000290033/LEGISCTA000020370853/ ; Book IV: https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000290033/LEGISCTA000020342842/ | LF | LF API |
| Amplified sound: décret n° 2017-1244 (CSP R1336-1 and following; Code de l'environnement R571-25 and following) | regulation | Yes (incl. open-air festivals) | 102 dB(A) / 118 dB(C) limits over 15 minutes, recording, free ear protection, rest areas | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000035388481 | LF | LF API |
| Live-performance entrepreneur licence (Code du travail, articles L7122-x) | regulation | Yes for organisers above thresholds | Licence of spectacle entrepreneurs | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/ (exact articles **unverified**) | LF | LF API |
| Public safety of large gatherings and private security (Code de la sécurité intérieure) | regulation | Yes | Declarations, security staff | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000025503132/ | LF | LF API |
| Temporary drinks licences (CSP) | regulation | Yes | Buvettes | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072665/ | LF | LF API |
| Music rights (Sacem) and CNM tax on shows | regulation / collective management | Yes | Royalties, levy | https://www.sacem.fr/ ; https://cnm.fr/ | PRIV / GOV | No |
| Ticketing rules (CGI, ticketing software) | regulation | Yes | Ticket mentions and records | **articles unverified** | LF | LF API |
| NF EN 13782 (tents), NF EN 13814 (fairground and amusement park machinery) | standard | Contract / referenced by inspection bodies (**unverified**) | Structural safety of temporary structures | **URLs unverified** | AF / CEN | No |
| ISO 20121 (sustainable events) | standard + certification | Voluntary | Event sustainability management | ISO Open Data | ISO | metadata |


### 18. Cross-sector: how AFNOR and ISO licensing affects a RAG

#### 18.1 What the rights holders actually say (verified on their sites)

1. **AFNOR, boutique legal notice** (https://www.boutique.afnor.org/en-gb/legal-notices): "AFNOR expressly opposes the
   integration, transmission, absorption in any way in artificial intelligence engines or algorithms, data, whatever
   their form (content, pages, books, standards, metadata, etc.)" for which it holds rights or distribution rights, and
   "opposes any operation of scraping, mining of texts and data (within the meaning of Article L. 122-5-3 of the Code of
   Intellectual Property), enrichment, derivative creation ... including by automated data collection devices or
   artificial intelligence, which would therefore constitute acts of infringement, unless specifically agreed to by
   AFNOR." This is an express opt-out from the French TDM exception (CPI L122-5-3, transposing Directive 2019/790 art.
   4).
2. **AFNOR, boutique FAQ "Copyright issues"** (https://www.boutique.afnor.org/en-gb/faq), about standards a customer has
   bought:
   - Reproduction is authorised "only for the natural person who purchased it, for its own use and for a non-commercial
     purpose"; e-mailing it to colleagues or clients is infringement.
   - Storing and networking a standard on the company's internal network is possible only "if you have paid the sharing
     rights associated with the standard"; otherwise it stays personal use.
   - "Do I have the right to feed/transmit to an artificial intelligence the content, in part or in whole, of the
     standard that I purchased? No, AFNOR does not authorize the absorption of its intellectual property by so-called
     'public' artificial intelligence", followed by the same general opposition "unless specific agreement formally
     expressed" by AFNOR.
   - Mandatory standards: consultable free on the standard's page (FileOpen plug-in, login) and in AFNOR offices and
     CCIs, but "Mandatory standards are subject, like all standards, to copyright" and are not downloadable for free.
   - Penalties cited: up to €300,000 fine and 3 years' imprisonment for counterfeiting.
3. **AFNOR's own AI product**: CObaz (AFNOR Editions' modular subscription for very small, SME and large companies)
   includes a "Compagnon IA" that answers "uniquement à partir du contenu des normes", presented as respecting copyright
   (AFNOR press release:
   [afnor.org](https://www.afnor.org/api/file/uploads/Communique_de_presse_Cobaz_Compagnon_IA_9bfb9ed19c.pdf)). So AFNOR
   monetises AI over standards itself; a licence for a third-party self-hosted RAG would be a negotiated, case-by-case
   agreement (contact innovation.cobaz@afnor.org or AFNOR Editions). No public price or template licence was found
   (**unverified**).
4. **ISO, Online Browsing Platform terms** (published 18 Sep 2026,
   [iso.org](https://www.iso.org/home/store/iso-obp-terms.html)): the licensee "is not permitted to access, use, or
   process the ISO Content ... for or related to any machine learning, artificial intelligence (AI), or analogous
   computational purposes, unless such use is expressly authorized under a separate licence agreement issued by ISO, an
   ISO Member Body, or an authorized distributor". The restriction explicitly covers "embedding, prompting, querying ...
   or otherwise enabling an AI or ML models or system to ingest, reproduce, restate, summarize ... or generate outputs
   derived from the ISO Content", and "ISO expressly opts out of the text-and-data-mining exception under Article 4 of
   Directive (EU) 2019/790". The site-wide notice adds: with the exception of ISO Open Data, "no ISO content may be used
   for any machine learning and/or artificial intelligence ... including ... (ii) prompt or otherwise enable artificial
   intelligence or similar tools to generate responses". A RAG over ISO text is therefore squarely prohibited without a
   specific licence, and AFNOR (the ISO member body) is the French route to such a licence.
5. **ISO Open Data** (https://www.iso.org/open-data.html): ISO deliverables metadata, technical committees and ICS,
   ODC-By 1.0, deliverables updated daily, Parquet/JSONL/CSV, explicitly offered to "enhance your AI models ... and
   compliance tracking systems". The dataset includes the **scope** (former abstract) of each standard in English and
   French. This is the only large, clean, reusable source of standard summaries found.
6. **Other national bodies** (same model): NEN Connect EULA (amended 16 Jan 2026,
   [connect.nen.nl](https://connect.nen.nl/Legal/EULA)) art. 5: AI use "including ... text and data mining and machine
   learning ... is strictly prohibited. The content may not be used in an AI application, database or training model".
   DIN reserves TDM rights in its reproduction conditions and DIN Media sells a separate AI licence that requires DIN
   membership, a network licence with internal reproduction rights and an **isolated AI environment**, price on request,
   standards bought separately (PBP article of 15 June 2026:
   [iww.de](https://www.iww.de/pbp/planungsleistungen/din-normen-wer-normen-mit-kuenstlicher-intelligenz-nutzen-will-zahlt-dreimal-f174541);
   DIN Media's own page did not render, **unverified first-hand**).

#### 18.2 Public-law limits on that copyright

- **Décret n° 2009-697, art. 17**: standards made mandatory by arrêté must be consultable free of charge on AFNOR's
  website. The Conseil d'État annulled provisions making standards mandatory without free access (CE 28 July 2017, n°
  402752, refrigerants; CE 30 December 2021, n° 436420, NF C 18-510). Free **consultation** is not a reuse licence:
  AFNOR keeps copyright and its AI opposition.
- **CJEU, Grand Chamber, 5 March 2024, C-588/21 P (Public.Resource.Org and Right to Know v Commission)**: harmonised
  standards are part of EU law and there is an overriding public interest in access to them under the
  access-to-documents rules; the Commission had to grant access to the four requested CEN standards. Commentators
  disagree on how far this extends to all harmonised standards and to reuse rights; it gives a right of access on
  request, not a licence to index (**scope of reuse unverified**).
- **EN 16931-1 and CEN/TS 16931-2** (e-invoicing) are a documented exception: free of charge under a 2018 Commission-CEN
  licence agreement that reportedly also permits derivative use.

#### 18.3 Conclusion for the RAG

- **Can SimpleERP index the full text of AFNOR or ISO standards (NF, NF EN, NF DTU, Eurocodes, ISO 9001, 22000,
  27001...)?** No. Not in a shared corpus shipped with the product, and not by scraping: AFNOR and ISO have both made an
  express opt-out from the TDM exception and specifically forbid AI integration, prompting and querying. Mandatory
  standards (NF C 15-100) are no exception: free viewing only.
- **Metadata and summaries?** ISO metadata and scope texts: yes, from ISO Open Data with ODC-By attribution. AFNOR
  catalogue metadata: AFNOR's notice covers "metadata" too, so do not scrape boutique.afnor.org. Bare references
  (number, title, date) cited from regulatory texts that reference them (Légifrance, OJ lists of harmonised standards)
  are facts taken from public law and are safe. Summaries written by the SimpleERP team in their own words from public
  information (what a standard covers, which law references it, who certifies it) are low risk; summaries derived from
  reading the standard's text are a derivative-work risk and should be avoided.
- **Customer-supplied copies under their own licence?** Legally fragile by default. A plain AFNOR purchase is a single
  natural-person licence; network storage needs sharing rights; AI ingestion is refused unless AFNOR agrees in writing;
  ISO content needs a separate AI licence from ISO or AFNOR. A self-hosted, tenant-isolated RAG is the most defensible
  set-up (it resembles DIN's "isolated AI environment" licence model, and AFNOR's FAQ targets "public" AI), but it still
  needs the customer to hold an AI-use authorisation. The feature can exist only as an opt-in that the customer
  activates under its own responsibility, with a licence attestation and per-document provenance.


### 19. Recommended approach options for SimpleERP

**Option A (baseline, ship by default): free law in full, standards as references.**
- Index fully: Légifrance (LEGI, JORF, KALI dumps daily, or the PISTE API) for all French texts above; EUR-Lex via
  Cellar SPARQL/REST for EU acts; free official guidance (GBPH, Qualiopi reading guide, HDS framework, BOFiP, DGFiP
  e-invoicing specifications, ADR PDF, ANSSI guides under Licence Ouverte, DILA "ENTREPRENDRE_SERVICE-PUBLIC" dataset of
  business guidance sheets).
- For copyrighted standards, hold a **standards register**, not text: reference, title, edition, status (from ISO Open
  Data for ISO and EN ISO; manually curated for NF-only documents such as NF DTU and NF C 15-100), the legal texts that
  make it mandatory or reference it, the sector IDs it applies to, how to obtain it (AFNOR boutique, CObaz, CSTB Reef,
  free via Qualibat for holders, free online view for mandatory standards), and an in-house plain-language note written
  without copying the standard.
- The AI assistant answers "what applies to me and where do I get it", cites the law verbatim, and for standard content
  says "see clause X of NF DTU 20.1, available from ..." without quoting it.
- Cost: zero licence cost; Légifrance and EUR-Lex reuse is free; ISO Open Data requires attribution.

**Option B (opt-in, per tenant): customer's own licensed documents.**
- A private, tenant-isolated corpus (never shared, never used for training, stored and embedded on the customer's own
  self-hosted instance) where the company uploads documents it is entitled to use: its own procedures, insurer
  requirements, client specifications, and standards **only if** it declares holding an AI-use authorisation from the
  rights holder (AFNOR, ISO via AFNOR, DIN Media, etc.).
- Controls: licence attestation checkbox per document, licensor and licence reference fields, user-count limit mirroring
  the licence, no export of chunks, answers that cite the clause instead of reproducing long passages, audit log, easy
  purge.
- Default for standards marked AFNOR or ISO: "reference-only" mode (title and clause pointers indexed, body text not
  embedded) unless the authorisation is recorded.

**Option C (commercial partnership, later): negotiated licence or integration.**
- Approach AFNOR Editions about a licence for a self-hosted RAG (or an integration with CObaz and its Compagnon IA,
  letting the customer's CObaz subscription answer standard questions while SimpleERP handles law). Similar talks would
  be needed per country (DIN Media has a priced AI licence model; NEN currently prohibits AI use outright).
- Re-evaluate if EU case law after C-588/21 P or the free-access policy for harmonised standards evolves (watch
  CEN-CENELEC and Commission announcements).

**Recommended**: ship A for all 16 sectors, design B with the safeguards above as an opt-in, and keep C as a
business-development track. Refresh cadence: Légifrance and EUR-Lex daily; ISO Open Data daily; curated standards
register monthly; scheme documents (IFS, BRCGS, GlobalG.A.P., Qualiopi guide, ADR biennial) checked at each new version.


### 20. Other EU countries

EU-wide technical regulations (hygiene package, INCO, tachographs and driving times, CPR, machinery, GPSR, REACH/CLP,
MDR, CRA, NIS2, AI Act, EAA, packaging, organic and GI rules, eFTI) are identical across Member States and come from
EUR-Lex, reusable free with acknowledgement and queryable through the Cellar SPARQL endpoint and REST API, in all EU
languages; directives need each country's transposition text from its national gazette (for example BOE in Spain,
Gazzetta Ufficiale/Normattiva in Italy, gesetze-im-internet.de and the Bundesgesetzblatt in Germany, wetten.overheid.nl
in the Netherlands; open-data licences of each portal **unverified**). ADR and ATP are UNECE treaties, the same text
everywhere. National technical standards follow the AFNOR model with similar or stricter terms: DIN (sold by DIN Media,
TDM reserved, separate AI licence requiring an isolated environment), NEN (EULA of 16 Jan 2026 strictly prohibits AI use
and TDM), UNE (Spain, distributed by UNE; AI terms **unverified**, site behind a bot challenge), UNI (Italy,
store.uni.com; AI terms **unverified**), and the ISO terms apply to every ISO adoption. Construction rules of the art
also have national equivalents with the same copyright issue (German DIN norms and VOB/C ATV, Italian UNI and NTC 2018,
Spanish CTE which is free law plus UNE norms; specifics **unverified**). The same three-tier approach (free law in full,
standards as references with ISO Open Data metadata, customer-licensed documents in an isolated opt-in corpus) transfers
directly; each new country needs its own legislation connector and a check of its national standards body's AI terms.


### 21. Items marked unverified (to check before relying on them)

- Légifrance URLs of: arrêté du 8 décembre 2014 (existing ERP accessibility); arrêté du 3 décembre 1987 (price display);
  arrêté du 29 décembre 2021 (hotel classification); décret n° 2012-432 and décret n° 80-217; loi n° 77-2; DPE and
  diagnostics arrêtés; live-performance licence articles; ticketing articles; HVE articles.
- Current mandatory status of NF C 18-510 after CE 2021 n° 436420; mandatory status of NF S70-003; mandatory status of
  newer NF C 15-100 editions; Eurocode 8 made mandatory by the seismic arrêté.
- Décret n° 2025-922 on food-hygiene training (reported by a DRAAF page only).
- Whether the arrêté du 24 novembre 2023 fully replaces the arrêté du 1er octobre 2018 (SAP agrément).
- Licences of GBPH, HAS, ANS, CNIL, RGAA, AIDA (INERIS), INAO, ANC and DGFiP specification documents (free to read;
  reuse licence not confirmed except ANSSI guides: Licence Ouverte 2.0; INRS: copyright, reproduction on request).
- Exact download and reuse terms of IFS Food 8, BRCGS Issue 9, GlobalG.A.P., GS1 specifications, TAPA.
- ATP agreement URL (UNECE blocked automated access); UNE and Qualit'EnR sites (bot challenges); HAS, Ordre des
  experts-comptables and France Rénov' sites (timed out).
- DIN Media AI licence page (did not render; details from a June 2026 trade article).
- EUDR application date; NIS2 French transposition status after the 9 November 2026 Assemblée session; whether free
  access to EN 16931 covers the 2026 edition.
- Whether AFNOR offers a licence for third-party self-hosted RAG and at what price.


### 22. URLs checked

Rights holders, licensing and access:
- [boutique.afnor.org](https://www.boutique.afnor.org/en-gb/legal-notices) (fetched, AI and TDM opposition quoted)
- [boutique.afnor.org](https://www.boutique.afnor.org/en-gb/faq) (fetched, copyright, sharing rights, AI and
  mandatory-standard answers quoted)
- [boutique.afnor.org](https://www.boutique.afnor.org/en-gb/abonnement-Cobaz) (fetched)
-
  [boutique.afnor.org](https://www.boutique.afnor.org/en-gb/standard/nf-c15100/lowvoltage-electrical-installations-completed-with-update-of-june-2005/fa005536/1556)
  (fetched, "mandatory application standard", "Consult online for free")
- [afnor.org](https://www.afnor.org/api/file/uploads/Communique_de_presse_Cobaz_Compagnon_IA_9bfb9ed19c.pdf) (search
  result)
- [afnor.org](https://afnor.org/wp-content/uploads/2024/08/cobaz-cge-2024.pdf) (fetched; content was a marketing page,
  no licence clauses)
- [afnor.org](https://www.afnor.org/wp-content/uploads/2022/02/conditions_generales_vente_adhesion.pdf) (404 on fetch;
  quoted only through search snippet, not relied on)
- [afnor.org](https://www.afnor.org/) ; [norminfo.afnor.org](https://norminfo.afnor.org/) (reachable)
-
  [certification.afnor.org](https://certification.afnor.org/services/certification-nf-service-services-aux-personnes-a-domicile)
  ;
  [boutique.afnor.org](https://www.boutique.afnor.org/fr-fr/norme/nf-x50056/services-aux-personnes-a-domicile/fa157675/30985)
  (search results)
- [iso.org](https://www.iso.org/home/store/iso-obp-terms.html) (fetched, AI clauses quoted)
- [iso.org](https://www.iso.org/open-data.html) (fetched, ODC-By, daily, scope field)
- [iso.org](https://www.iso.org/copyright.html) (403)
- [connect.nen.nl](https://connect.nen.nl/Legal/EULA) (fetched, art. 5 quoted)
-
  [iww.de](https://www.iww.de/pbp/planungsleistungen/din-normen-wer-normen-mit-kuenstlicher-intelligenz-nutzen-will-zahlt-dreimal-f174541)
  (fetched)
- [dinmedia.de](https://www.dinmedia.de/de/normen-produkte/ki-lizenzen-fuer-normen) (empty render) ;
  [dinmedia.de](https://www.dinmedia.de/de) (reachable) ;
  [din.de](https://www.din.de/resource/blob/1223804/4d0cf0540513ad3c3b7345405d62f43a/vervbedinternetpublikationen-data.pdf)
  (search result)
- [une.org](https://www.une.org/) (bot challenge) ; [store.uni.com](https://store.uni.com/) ;
  [nen.nl](https://www.nen.nl/) ; [bsigroup.com](https://www.bsigroup.com/) ;
  [cencenelec.eu](https://www.cencenelec.eu/) ; [etsi.org](https://www.etsi.org/standards/) (reachable)
-
  [ec.europa.eu](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/Obtaining+a+copy+of+the+European+standard+on+eInvoicing)
  (search result)
-
  [marche-public.fr](https://www.marche-public.fr/contrats-publics/Normes-techniques-nf-obligatoires-consultables-gratuitement-jp-ce-402752.htm)
  ;
  [marche-public.fr](https://www.marche-public.fr/contrats-publics/Normes-techniques-nf-obligatoires-consultables-gratuitement-jp-ce-436420.htm)
  (search results)
- [mofo.com](https://www.mofo.com/resources/news/240305-morrison-foerster-and-fp-logue-achieve-full-reset) ;
  [ipkitten.blogspot.com](https://ipkitten.blogspot.com/2024/07/harmonized-technical-standards-under-eu.html) ;
  [ds.dk](https://ds.dk/en/news/2024/public-access-portal-related-to-case-c-588-21-p-is-now-accessible) (search results
  on C-588/21 P)
-
  [ffbatiment.fr](https://www.ffbatiment.fr/techniques-batiment/normalisation-regles-de-lart/nf-dtu-normes/dossier-bam/corpus-qualibat-normes-et-nf-dtu-en-libre-acces-pour-les-metiers)
  (fetched, 14 Feb 2025)
-
  [ffbatiment.fr](https://www.ffbatiment.fr/techniques-batiment/normalisation-regles-de-lart/nf-dtu-normes/dossier/comment-se-procurer-une-norme-du-batiment)
  (search result)
- [inrs.fr](https://www.inrs.fr/accueil/footer/mentions-legales.html) (search result) ; [inrs.fr](https://www.inrs.fr/)
  (reachable)
- [cyber.gouv.fr](https://www.cyber.gouv.fr/sites/default/files/document/anssi-guide-openstack_v1-0.pdf) (search result,
  Licence Ouverte notice)

Open data and APIs:
- [piste.gouv.fr](https://piste.gouv.fr/) ;
  [data.gouv.fr](https://www.data.gouv.fr/datasets/legi-codes-lois-et-reglements-consolides) ;
  [echanges.dila.gouv.fr](https://echanges.dila.gouv.fr/OPENDATA/) (listing read; LEGI and KALI daily archives seen) ;
  [echanges.dila.gouv.fr](https://echanges.dila.gouv.fr/OPENDATA/LEGI/) ;
  [echanges.dila.gouv.fr](https://echanges.dila.gouv.fr/OPENDATA/KALI/)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/contenu/pied-de-page/open-data-et-api) (bot challenge)
- [op.europa.eu](https://op.europa.eu/en/web/cellar) ;
  [publications.europa.eu](https://publications.europa.eu/webapi/rdf/sparql) (queried: 41 CELEX numbers confirmed) ;
  [eur-lex.europa.eu](https://eur-lex.europa.eu/content/help/data-reuse/reuse-contents-eurlex-details.html) ;
  [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/dec/2011/833/oj/eng) (search results; eur-lex.europa.eu returns HTTP
  202 bot challenges to automated clients)

Légifrance (fetched or returned by searches restricted to legifrance.gouv.fr):
- Codes (all fetched, titles confirmed):
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/) (travail) ;
  LEGITEXT000006074096 (construction et habitation) ; LEGITEXT000006069565 (consommation) ; LEGITEXT000005634379
  (commerce) ; LEGITEXT000006074220 (environnement) ; LEGITEXT000006072665 (santé publique) ; LEGITEXT000006071367
  (rural) ; LEGITEXT000023086525 (transports) ; LEGITEXT000006074069 (action sociale et familles) ; LEGITEXT000006069577
  (CGI) ; LEGITEXT000006070721 (civil) ; LEGITEXT000006073984 (assurances) ; LEGITEXT000025503132 (sécurité intérieure)
  ; LEGITEXT000023983208 (énergie) ; LEGITEXT000006069414 (propriété intellectuelle) ; LEGITEXT000006072026 (monétaire
  et financier), all under [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/texte_lc/)<id>/
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000290033) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000020303557) (ERP fire safety)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000290033/LEGISCTA000020370853/) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000290033/LEGISCTA000020342842/) (CTS,
  Book IV)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043877196) (RE2020)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034485459) (accessibility new ERP)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000474032/) (fire safety dwellings)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000021676844) (arrêté 21 Dec 2009)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000020796240) (arrêté TMD)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038565259) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000038565293) (Qualiopi; second fetched)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047837913) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037049462/) (SAD cahier des charges)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465776) (fetched) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037466369) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000018500042/2022-04-25/)
  (SAP)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049577902) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000049537698) (HDS; the JORFTEXT form of
  the latter id showed no content)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000512228/) (loi Hoguet)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024266465) (hygiene training)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000213467) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006190977/)
  (DASRI)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029257402) ;
  [legifrance.gouv.fr](https://legifrance.gouv.fr/eli/arrete/2015/12/1/ETLL1524415A/jo/texte) (RGE)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000035388481) (amplified sound)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000034429274/) (ICPE 1510)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000025391351) (DT-DICT)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038812251) ;
  [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043819497/)
  (tertiary buildings)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047774060) (lawyers' ethics code)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000497458) (loi 1901; an earlier guessed id
  JORFTEXT000000497166 was checked and rejected)
- [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000022848014/)
  (electrical operations)

EUR-Lex ELI URLs (existence and titles confirmed through Cellar SPARQL by CELEX): reg/2016/679, reg/2004/852,
reg/2004/853, reg/2002/178, reg/2017/625, reg/2011/1169, reg/2006/561, reg/2014/165, reg/2009/1071, reg/2009/1072,
dir/2003/59, reg/2020/1056, reg/2018/848, reg/2024/1143, reg/2023/1115, reg/2023/988, dir/2024/2853, dir/2019/882,
reg/2011/305, reg/2024/3110, dir/2006/42, reg/2023/1230, dir/2014/35, dir/2014/30, dir/2014/34, dir/2014/31,
reg/2006/1907, reg/2008/1272, reg/2024/1781, reg/2023/1542, reg/2024/573, dir/2023/1791, reg/2017/745, reg/2024/2847,
dir/2022/2555, reg/2024/1689, reg/2014/910, reg/2024/1183, reg/2025/40, dir/2019/790, dec/2011/833; each as
[eur-lex.europa.eu](https://eur-lex.europa.eu/eli/)<type>/<year>/<number>/oj

Government and agency pages (reachable unless noted):
- [single-market-economy.ec.europa.eu](https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards_en)
- [accessibilite.numerique.gouv.fr](https://accessibilite.numerique.gouv.fr/)
- [agriculture.gouv.fr](https://agriculture.gouv.fr/guides-de-bonnes-pratiques-dhygiene-gbph)
- [ecologie.gouv.fr](https://www.ecologie.gouv.fr/politiques-publiques/reglementation-environnementale-re2020) ;
  [ecologie.gouv.fr](https://www.ecologie.gouv.fr/)
- [esante.gouv.fr](https://esante.gouv.fr/produits-services/hds) ;
  [esante.gouv.fr](https://esante.gouv.fr/sites/default/files/media_entity/documents/referentiel_certification_hds---fr--v2.pdf)
  ;
  [esante.gouv.fr](https://esante.gouv.fr/sites/default/files/media_entity/documents/referentiel_certification_hds---en--v2.pdf)
  (search results)
-
  [travail-emploi.gouv.fr](https://travail-emploi.gouv.fr/qualiopi-marque-de-certification-qualite-des-prestataires-de-formation)
  ;
  [travail-emploi.gouv.fr](https://travail-emploi.gouv.fr/sites/travail-emploi/files/files-spip/pdf/guide-lecture-referentiel-qualite.pdf)
- [bofip.impots.gouv.fr](https://bofip.impots.gouv.fr/bofip/10691-PGP.html/identifiant=BOI-TVA-DECLA-30-10-30-20251001)
  ; [bofip.impots.gouv.fr](https://bofip.impots.gouv.fr/bofip/15035-PGP.html/ACTU-2026-00073)
- [aife.economie.gouv.fr](https://aife.economie.gouv.fr/nos-applications/facturation-electronique-b2b/) ;
  [impots.gouv.fr](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf)
  (search results) ; [impots.gouv.fr](https://www.impots.gouv.fr/professionnel/facturation-electronique) (404) ;
  [economie.gouv.fr](https://www.economie.gouv.fr/tout-savoir-sur-la-facturation-electronique-pour-les-entreprises) (bot
  challenge)
-
  [economie.gouv.fr](https://www.economie.gouv.fr/entreprises/gerer-son-entreprise-au-quotidien/gerer-un-commerce/professionnels-quelles-sont-vos-obligations-en-matiere-daffichage-des-prix)
  (search result)
-
  [entreprises.gouv.fr](https://www.entreprises.gouv.fr/espace-entreprises/s-informer-sur-la-reglementation/hotels-et-hotels-de-tourisme)
  ; [classement.atout-france.fr](https://www.classement.atout-france.fr/)
-
  [mesdemarches.agriculture.gouv.fr](https://mesdemarches.agriculture.gouv.fr/demarches/exploitation-agricole/obtenir-un-droit-une-autorisation/article/obtenir-le-certificat-produits-322)
  (search result)
- [inao.gouv.fr](https://www.inao.gouv.fr/) ; [anc.gouv.fr](https://www.anc.gouv.fr/) ;
  [cnil.fr](https://www.cnil.fr/fr) ; [cyber.gouv.fr](https://cyber.gouv.fr/) ;
  [francecompetences.fr](https://www.francecompetences.fr/) ; [aida.ineris.fr](https://aida.ineris.fr/) ;
  [reseaux-et-canalisations.ineris.fr](https://www.reseaux-et-canalisations.ineris.fr/) ;
  [cnaps.interieur.gouv.fr](https://www.cnaps.interieur.gouv.fr/) ; [operat.ademe.fr](https://operat.ademe.fr/) ;
  [cofrac.fr](https://www.cofrac.fr/) ;
  [entreprendre.service-public.gouv.fr](https://entreprendre.service-public.gouv.fr/) ;
  [codex.fao.org](https://codex.fao.org/)
- [has-sante.fr](https://www.has-sante.fr/) ; [france-renov.gouv.fr](https://france-renov.gouv.fr/) ;
  [experts-comptables.fr](https://www.experts-comptables.fr/) (timed out)
- [unece.org](https://unece.org/adr-2025-files) ; [unece.org](https://unece.org/transport/dangerous-goods/atp-agreement)
  (Cloudflare 403; ADR page confirmed through search results)

Professional and scheme bodies (reachable unless noted):
- [qualibat.com](https://www.qualibat.com/) ; [qualifelec.fr](https://www.qualifelec.fr/) ;
  [qualit-enr.org](https://www.qualit-enr.org/) (bot challenge) ; [boutique.cstb.fr](https://boutique.cstb.fr/) ;
  [oppbtp.com](https://www.oppbtp.com/) ; [cnb.avocat.fr](https://cnb.avocat.fr/) ;
  [architectes.org](https://www.architectes.org/) ; [infocert.org](https://infocert.org/) ;
  [atee.fr](https://www.atee.fr/) ; [sacem.fr](https://www.sacem.fr/) ; [cnm.fr](https://cnm.fr/)
- [globalgap.org](https://globalgap.org/) ; [ifs-certification.com](https://www.ifs-certification.com/en/) ;
  [brcgs.com](https://www.brcgs.com/) ; [agencebio.org](https://www.agencebio.org/) (bot challenge) ;
  [gs1.org](https://www.gs1.org/standards/barcodes-epcglobal/gs1-general-specifications) (404)
- [ffbatiment.fr](https://www.ffbatiment.fr/) (pages above)

## Country pack

The legal values this page relies on, from the France country pack (D293):

- [CR-FR-055 Health data hosting](../10-country-packs/france/data-protection/cr-fr-055-health-data-hosting.md)

## Open questions

None.

---

⬆️ [Up](README.md)
