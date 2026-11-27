# Supply chain and licences

Dependency policy, SBOM, CVE scanning, AGPL compliance of dependencies and plugins. Nothing of it is built yet.

## Today

Nothing built yet.

## Target design (specified in GH-2, not built yet)

**Dependencies (D415).** Every dependency pinned (`uv.lock`, the front end's lock file); licences checked against
AGPL-3.0 compatibility in CI; vulnerabilities scanned on each push and daily (OSV-Scanner, Trivy); a CycloneDX bill of
materials per image; new dependencies reviewed.

**Integrity.** Images built in CI only, from pinned base images, signed with Sigstore cosign with build provenance (SLSA
level 3 as the target); clusters accept only signed images; plugins and generated features are signed the same way.

**The open-core boundary (D388).** The closed hosted services live in separate private repositories that depend on
SimpleERP only through its published API clients; CI checks that no AGPL source is copied into them and that no closed
code reaches a plugin; a lawyer reviews before launch.

**AI models.** Any model may be used (the owner's choice: no licence gate on models); each model in use is still listed
with its source and checksum, and outside providers work under data-processing terms. The models shipped in the images
by default are checked like dependencies (a licence compatible with AGPL-3.0 that allows redistribution); models a user
or an administrator adds stay free of any gate (D415, clarified after the review of 2026-11-12).

Decided in [D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md).

Last reviewed: 2026-11-12 (GH-2)
