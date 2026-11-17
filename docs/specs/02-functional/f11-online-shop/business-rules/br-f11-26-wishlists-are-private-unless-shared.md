🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F11-26 Wishlists are private unless shared

# 📏 BR-F11-26 Wishlists are private unless shared

**Status:** ✅ specified

## Statement

A wishlist can be read only by its owner until they share it by a link they chose to create; a shared list is read-only,
shows the products and the first name the owner chose and nothing else, and stops being readable the moment the owner
stops sharing it.

## Why

A wishlist tells what a person wants, and sometimes who they are. The shopper decides who sees it. The owner's answer:
"Wishlists and compare" ([D530](../../../06-decisions/f11-online-shop/d530-benchmark-gaps-f11-online-shop.md)).

## Examples

| Case | Result |
|---|---|
| A new wishlist | private, no link exists |
| The shopper shares it | a link is created that shows the products and a first name |
| The shopper stops sharing | the link no longer shows the list |
| Marketing asks for the most wished products | counts only, no names |
| The account is erased | its wishlists are erased and the links stop |

## Applies to

- [UC-F11-31 Keep wishlists and compare products](../use-cases/11-donations-gift-cards-and-cross-border/uc-f11-31-keep-wishlists-and-compare-products.md)
- [E-F11-25 Wishlist](../data/e-f11-25-wishlist.md)
- [UC-F11-10 Use the customer account](../use-cases/03-after-the-order/uc-f11-10-use-the-customer-account.md)

## Exceptions

None: the owner is always the only one who changes the list.

## Configurable

No: wishlists are always private by default.

## Open questions

None.

---

⬅️ [BR-F11-25](br-f11-25-donations-reach-the-stated-beneficiary-with-a-receipt.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F11-27 One gift-card balance across shop and tills](br-f11-27-one-gift-card-balance-across-shop-and-tills.md)
