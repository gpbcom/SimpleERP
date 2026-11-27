🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔌 [Decisions: F24 Integrations hub](README.md) ›
📜 D428 Office suites: full read and write API

# 📜 D428 Office suites: full read and write API

**Status:** ✅ decided

## Context

What the openDesk and La Suite numérique connectors do.

## Options

- Identity, files, editing, mail, calendar, chat and video.
- Sign-in and files only.

## Choice

The owner: "Full access to their API with read/write permission + all integrations can be used by the AI Assistant."
Every component of each suite that offers an API is connected for reading and writing: for openDesk (product and
operations pages read on 2026-11-12) Nubus and Keycloak for identity, Nextcloud files, Collabora editing, OX App Suite
mail, calendars and contacts, Element and Matrix chat, Jitsi video, OpenProject, XWiki, CryptPad and Notes; for La Suite
numérique (pages read on 2026-11-12) ProConnect sign-in, Docs, Fichiers, Visio, Tchap, Grist, Messagerie and France
Transfert. Their APIs are not documented on the pages read: each connector is specified from the components' own API
documentation when built.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

BR-F24-03, BR-F24-04; every action of every connector is an AI assistant tool within rights (BR-F3-34).

## Related

- [F24 Integrations hub](../../02-functional/f24-integrations-hub/README.md)

---

⬅️ [D427 Integrations hub](d427-integrations-hub-coverage.md) · ⬆️ [Up](README.md) ·
➡️ [D429 Fewest steps for every connector](d429-fewest-steps-for-every-connector.md)
