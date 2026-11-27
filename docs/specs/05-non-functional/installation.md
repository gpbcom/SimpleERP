🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 📦 Installation

# 📦 Installation

**Status:** ✅ specified

## Requirement

- **One company:** one Docker Compose command on a single server.
- **An IT provider:** a Helm chart on Kubernetes, hosting many companies.
- Both use the same images. See [D18](../06-decisions/foundations/d18-installation.md).

**Server:**

- The ERP, with small local AI models, runs on an ordinary server with no graphics card, for example 8 processor
  cores and 32 GB of memory. Its AI is then slower and simpler.
- A graphics card, or an external provider (D5), gives better AI.
- **The ERP works fully with the AI turned off**. See [D22](../06-decisions/foundations/d22-no-graphics-card-needed.md).

**Laptop profile** (D408): the whole stack within 8 GB of RAM on a laptop, to be proved by a measured prototype on the
owner's machine before it is promised (REQ-T09-03); the server example above stays the comfortable size. With the AI
turned off, Milvus is not installed (REQ-T08-01), which frees 2 to 4 GB.

## Measures

⬜ To be specified.

## Open questions

⬜ To be specified.

---

⬅️ [Updates](updates.md) · ⬆️ [Up](README.md) · ➡️ [Data isolation](data-isolation.md)
