🏠 [Specs](../README.md) › 🌍 Country packs

# 🌍 Country packs

**Status:** ✅ specified

One pack per country, installed as a plugin
([D292](../06-decisions/country-packs/d292-one-country-pack-per-country.md)). A pack holds the country's law corpus,
read by the legal assistant ([F15](../02-functional/f15-legal-assistant/README.md),
[T11](../03-technical/t11-legal-corpora/README.md)), and every legal rule simple-ERP enforces in that country, one page
per rule with its values, articles and effective dates. Capabilities read their legal values from the pack and hard-code
none ([D293](../06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)). When a cited article
changes, the rule is flagged and fixed in a pack update
([D294](../06-decisions/country-packs/d294-flag-then-pack-update.md)).

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🇫🇷 |  | [France](france/README.md) | 🔄 |
