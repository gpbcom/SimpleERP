from __future__ import annotations

# Standard library imports
from typing import ClassVar, Type

# First-party imports
from erp_models.base.opaque_id import OpaqueId
from erp_models.idempotency.exceptions import SEIdempotencyKeyInvalidValue


class IdempotencyKey(OpaqueId):
    """The key a write carries, so that a write repeated with its key is done once.

    Attributes:
        INVALID_VALUE (Type[Exception]): The exception raised for an invalid ``value``.
        value (str): The key, a non-empty text stripped of surrounding spaces.

    Notes:
        - The model is frozen, so it is hashable and equal by value: a service tells a repeated write by its key.
        - Storing the keys and skipping the repeated write belong to the services that write, not to this model.
        - The key is not a secret. AGENT.md's ``_key`` naming is for fields that name a secret store entry, which is
          why the text lives in ``value``, never in a ``*_key`` field.
    """

    INVALID_VALUE: ClassVar[Type[Exception]] = SEIdempotencyKeyInvalidValue
