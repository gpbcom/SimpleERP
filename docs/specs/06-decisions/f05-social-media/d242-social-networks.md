🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📣 [Decisions: F5 Social media](README.md) ›
📜 D242 Social networks

# 📜 D242 Social networks

**Status:** ✅ decided

## Context

Which networks SimpleERP posts to.

## Options

- LinkedIn, Facebook, Instagram.
- X, YouTube, TikTok.
- Mastodon, Bluesky, Threads.
- Google Business Profile.

## Choice

All of them, through each network's official API.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

One connector per network (T12); tokens in the vault (D240); each network's API rules and costs apply (X's API is paid).

## Related

- [F5 Social media](../../02-functional/f05-social-media/README.md)
- [D29](../foundations/d29-social-media-module.md)

---

⬅️ [D241 Deployable under security frameworks](../security-and-compliance/d241-security-frameworks.md) ·
⬆️ [Up](README.md) · ➡️ [D243 Social formats](d243-social-formats.md)
