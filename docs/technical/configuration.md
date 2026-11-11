# Configuration

Where simple-erp reads its settings.

| File | Holds |
|---|---|
| `conf/logger.yaml` | The logging: a coloured console handler and a coloured rotating file in `logs/`, root level `DEBUG` |
| `conf/app.yaml` | Planned: the application settings, with every default written out |
| `conf/catalogs/` | Planned: data that would otherwise be hard-coded, loaded by `YamlCatalog` models |

- Secrets live in a secret store, never in configuration or logs. A field ending in `_key` names a secret store entry.
- The log file holds colour codes: read it with `tail -f` or `less -R`.

Last reviewed: 2026-11-10 (GH-1)
