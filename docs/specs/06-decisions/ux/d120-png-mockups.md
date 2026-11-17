🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D120 PNG mockups of every flow step

# 📜 D120 PNG mockups of every flow step

**Status:** ✅ decided

## Context

The owner asked: "For each UX views you will generate a comprehensive set of PNG image representing the different steps
of each flow for each user (both light and dark mode). This MUST also handle error cases (the error messages MUST be
nicely displayed and be meaningful for non-technical users)."

## Options

- Not discussed: the owner stated it.

## Choice

Every step of every flow, for each persona taking part, is drawn as a PNG image in light and dark mode, error cases
included. The images are rendered from HTML mockups that use the design tokens, typefaces and icons of the visual
identity, so that they can be regenerated when a specification changes.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Extends D3 (ticket GH-2), which planned Mermaid diagrams and text wireframes only: high-fidelity images are now in
scope. Each flow's step table links its images.

## Related

- [UX](../../04-ux/README.md)
- [Views](../../04-ux/views/README.md)

---

⬅️ [D119 Email templates](../f02-no-code-configuration/d119-email-templates.md) · ⬆️ [Up](README.md) ·
➡️ [D121 Mockup sizes](d121-mockup-sizes.md)
