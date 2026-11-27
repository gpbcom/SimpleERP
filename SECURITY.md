# Security policy

## Supported versions

SimpleERP has no released version yet: the specifications v1 are complete and the implementation is in progress.
Until the first release, security fixes go to `develop` only.

| Version | Supported |
|---|---|
| None released yet | Fixes on `develop` |

Once versions are released, this table lists the ones that receive security fixes, following the release and support
policy of [Release and versioning](docs/technical/delivery/release-and-versioning.md).

## Reporting a vulnerability

**Never report a vulnerability in a public issue, pull request or discussion.** A public report shows the hole to
attackers before it is fixed ([BR-F25-12](docs/specs/02-functional/f25-devops-agents/business-rules/br-f25-12-security-reports-stay-private.md)).

Report it privately through GitHub's private vulnerability reporting:

1. Open the [Security tab](https://github.com/gpbcom/SimpleERP/security) of the repository.
2. Choose **Report a vulnerability** ([direct link](https://github.com/gpbcom/SimpleERP/security/advisories/new)).
3. Describe the problem: the part concerned (service, front end, plugin, workflow), the version or commit, the steps
   to reproduce it, and its impact. Do not include real personal data or secrets.

The report opens a private security advisory that only the maintainers and you can see. There is no security email
address: GitHub's private reporting is the only channel.

## What happens next

- The maintainers acknowledge the report in the advisory and assess its severity.
- A confirmed vulnerability is fixed by severity, starting with a test that fails without the fix
  ([BR-F25-15](docs/specs/02-functional/f25-devops-agents/business-rules/br-f25-15-vulnerabilities-handled-under-the-cra.md)).
- The advisory stays private until the fix is released, then it is published with its CVE, crediting the reporter.
- An actively exploited vulnerability is also reported under the EU Cyber Resilience Act, as the specifications
  describe ([UC-F25-22](docs/specs/02-functional/f25-devops-agents/use-cases/06-vulnerability-handling/uc-f25-22-handle-a-reported-vulnerability-under-the-cra.md)).

## Scope

This policy covers the code of this repository: the back-end services, the front ends, the plugins, the SDK, the
infrastructure files, the workflows and the Claude Code harness. A vulnerability in a dependency is reported to its
own project; tell us too if SimpleERP is affected.
