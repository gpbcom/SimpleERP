from __future__ import annotations

import copy
from typing import Dict, List

from pydantic import JsonValue

HEALTH_PATH = "/v1/health"
HEALTH_POINTER = "#/paths/~1v1~1health"


def a_baseline() -> Dict[str, JsonValue]:
    return {
        "openapi": "3.1.0",
        "info": {"title": "Platform", "version": "1.0.0"},
        "paths": {
            HEALTH_PATH: {
                "get": {
                    "operationId": "get_health",
                    "parameters": [{"in": "query", "name": "verbose", "schema": {"type": "boolean"}}],
                    "responses": {
                        "200": {
                            "description": "Health.",
                            "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Health"}}},
                        }
                    },
                },
                "post": {"operationId": "post_health", "responses": {"204": {"description": "Done."}}},
            },
            "/v1/problems": {"get": {"operationId": "get_problems", "responses": {"200": {"description": "Ok."}}}},
        },
        "components": {
            "schemas": {
                "Health": {
                    "type": "object",
                    "required": ["status"],
                    "properties": {
                        "status": {"type": "string"},
                        "detail": {
                            "type": "object",
                            "properties": {"message": {"type": "string"}, "code": {"type": "integer"}},
                        },
                        "checks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {"name": {"type": "string"}, "ok": {"type": "boolean"}},
                            },
                        },
                        "link": {"$ref": "#/components/schemas/Link"},
                    },
                },
                "Link": {"type": "object", "properties": {"href": {"type": "string"}}},
            }
        },
    }


def health_schema(document: Dict[str, JsonValue]) -> Dict[str, JsonValue]:
    return document["components"]["schemas"]["Health"]  # type: ignore[index, return-value]


def paths_of(document: Dict[str, JsonValue]) -> Dict[str, JsonValue]:
    return document["paths"]  # type: ignore[return-value]


def without_path(path: str) -> Dict[str, JsonValue]:
    document = copy.deepcopy(a_baseline())
    del paths_of(document)[path]
    return document


def without_operation(path: str, method: str) -> Dict[str, JsonValue]:
    document = copy.deepcopy(a_baseline())
    del paths_of(document)[path][method]  # type: ignore[call-overload, attr-defined]
    return document


def without_parameter() -> Dict[str, JsonValue]:
    document = copy.deepcopy(a_baseline())
    paths_of(document)[HEALTH_PATH]["get"]["parameters"] = []  # type: ignore[index, call-overload]
    return document


def without_schema(name: str) -> Dict[str, JsonValue]:
    document = copy.deepcopy(a_baseline())
    del document["components"]["schemas"][name]  # type: ignore[index, call-overload]
    return document


def without_property(trail: List[str]) -> Dict[str, JsonValue]:
    """Remove the property at the end of ``trail``, a list of keys below the ``Health`` schema."""
    document = copy.deepcopy(a_baseline())
    node = health_schema(document)
    for key in trail[:-1]:
        node = node[key]  # type: ignore[assignment, index]
    del node[trail[-1]]  # type: ignore[attr-defined]
    return document


def with_property_type(trail: List[str], value: JsonValue) -> Dict[str, JsonValue]:
    """Set the ``type`` keyword of the node at ``trail`` below ``Health``, or drop it when ``value`` is None."""
    document = copy.deepcopy(a_baseline())
    node = health_schema(document)
    for key in trail:
        node = node[key]  # type: ignore[assignment, index]
    if value is None:
        del node["type"]  # type: ignore[attr-defined]
    else:
        node["type"] = value  # type: ignore[index]
    return document


def with_link_ref(ref: str) -> Dict[str, JsonValue]:
    document = copy.deepcopy(a_baseline())
    health_schema(document)["properties"]["link"]["$ref"] = ref  # type: ignore[index, call-overload]
    return document


def with_additions() -> Dict[str, JsonValue]:
    document = copy.deepcopy(a_baseline())
    paths = paths_of(document)
    paths["/v1/new"] = {"get": {"responses": {"200": {"description": "New."}}}}
    paths[HEALTH_PATH]["put"] = {"responses": {"200": {"description": "Put."}}}  # type: ignore[index]
    paths[HEALTH_PATH]["get"]["parameters"].append(  # type: ignore[index, call-overload]
        {"in": "header", "name": "x-trace", "required": True, "schema": {"type": "string"}}
    )
    paths[HEALTH_PATH]["get"]["responses"]["404"] = {"description": "Missing."}  # type: ignore[index, call-overload]
    schema = health_schema(document)
    schema["required"] = ["status", "extra"]
    schema["properties"]["extra"] = {"type": "string"}  # type: ignore[index]
    schema["properties"]["detail"]["properties"]["more"] = {"type": "string"}  # type: ignore[index, call-overload]
    document["components"]["schemas"]["Extra"] = {"type": "object"}  # type: ignore[index, call-overload]
    return document
