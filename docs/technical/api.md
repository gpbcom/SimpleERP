# API

The entry points of simple-erp: what calls it, and how.

## Command line

| Command | Defined in | Does |
|---|---|---|
| `simple-erp` | `src/api/cli/main.py` (`[project.scripts]` in `pyproject.toml`) | Prints a greeting. It is the place where commands will be added, through `api/factories/` |

Only `api/cli/` prints to the terminal; every other layer logs.

## HTTP

None yet. When the first endpoint is added, this chapter lists each one (method, path, request, response, errors), its
OpenAPI definition, and its requests in the Bruno collection `bruno/` (rule TEST-1).

Last reviewed: 2026-11-10 (GH-1)
