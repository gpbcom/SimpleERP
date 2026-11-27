🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 📴 TC-06 Offline devices and synchronisation

# 📴 TC-06 Offline devices and synchronisation

**Status:** ✅ listed for the technical interviews

## Challenge

Keep tills, waiters' tablets, field workers, carers and drivers working without a network, then merge their work without
losing or duplicating a sale, a visit or a delivery.

## Raised by

- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md)
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md)
- [SC04 Home care](../../08-sectors/sc04-home-care/README.md)
- [SC07 Transport and logistics](../../08-sectors/sc07-transport/README.md)
- [SC01 Construction](../../08-sectors/sc01-construction/README.md)

## Why it is hard

- An offline till still issues numbered, inalterable receipts.
- Two devices can change the same record offline.
- Phones and tablets have little storage and must not keep more personal data than needed.

## Already decided

- [D293](../../06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md) Capabilities take legal
  rules from the country pack

## Options to weigh

- An offline-first local store with a sync protocol, against a server-first app with a short offline queue.
- Conflict rules per record type: last write, merge, or ask.
- Number ranges reserved per device.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19d API design and contracts ([chapter](../../../technical/interfaces/api.md))
- 19c Storage ([chapter](../../../technical/data/storage.md))
- Then the technical capabilities: [T5 API and webhooks](../t05-api-and-webhooks/README.md) (REQ-T05-07).

## Questions for the interview

- How long must a device work offline: hours or days?
- Which screens must work offline on day one?

---

⬅️ [TC-05 Records that must never change, and those that must be erased](tc-05-inalterable-and-certified-records.md) ·
⬆️ [Up](README.md) ·
➡️ [TC-07 The AI assistant can do everything, within the user's rights](tc-07-ai-everywhere-within-rights.md)
