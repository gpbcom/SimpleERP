# AI operations

Model hosting and GPUs, model choice and evaluation, RAG quality (T7, T8). Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Serving (D417).** One AI gateway (OpenAI-compatible) in front of every model: llama.cpp for quantised models on CPU,
vLLM on GPU nodes in the cloud, outside providers per feature (D82). The gateway also meters (F22), masks, traces and
falls back to local (D84); it is deployed like the MCP and A2A pods (Kubernetes, KEDA), under Docker Compose on the
laptop.

**Speech and embeddings.** By default, faster-whisper or whisper.cpp transcribes in the background on CPU, live on GPU
nodes; outside speech services are supported as well, per feature; speakers are told apart without voice prints; a small
multilingual embedding model and a reranker run locally on every profile.

**Quality.** Each AI feature has an evaluation set (questions, expected answers, forbidden behaviours) run on every
model or prompt change and before each release, with a threshold that blocks the release; paid model runs go through the
cost guard (TEST-5); production ratings feed the sets.

**Prompts and agents.** Prompt templates are versioned in the repository and tested like code; rights, confirmations and
budgets are enforced by the tool policy layer, never only by the prompt; untrusted content (documents, emails, scraped
pages, outside agents) is fenced and never followed as instructions.

Decided in [D417](../../specs/06-decisions/technical/d417-ai-operations-design.md).

Last reviewed: 2026-11-12 (GH-2)
