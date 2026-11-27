# erp_config

`erp_config` reads a service's configuration. Every service declares its settings as typed sections, reads them from
`conf/app.yaml`, and can override any value from the environment.

## What it holds

- `ConfigSection`: the base class of a configuration section. Each section of a service subclasses it.
- `AppConfigLoader`: reads the file. The call is
  `AppConfigLoader(Model, Path("conf/app.yaml"), EnvironmentOverrides("ERP", os.environ)).read()`.
  - It refuses a file that does not write out every default.
  - It then applies the overrides named `ERP__SECTION__FIELD`.
- `EnvironmentOverrides`: reads the overrides from the environment under the `ERP` prefix.

The library holds no business rules. It follows [D406](../../../docs/specs/06-decisions/technical/d406-back-end.md) and
sits in the shared libraries of the layout fixed by
[D438](../../../docs/specs/06-decisions/technical/d438-repository-layout.md).

## How a service uses it

1. Subclass `ConfigSection` for each section of the service.
2. Write every default in `conf/app.yaml`.
3. Call `AppConfigLoader(...).read()` at start-up.

Fields ending in `_key` name entries of the credential vault only. They never hold a secret, and they are never
logged. The vault rule is [D240](../../../docs/specs/06-decisions/security-and-compliance/d240-credential-vault.md).

The layers of configuration are in [D413](../../../docs/specs/06-decisions/technical/d413-configuration-layers.md), and
the technical view is in [configuration](../../../docs/technical/architecture/configuration.md).

## Tests

```bash
uv run pytest backend/shared/config/tests -n 2
```
