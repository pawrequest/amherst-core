from __future__ import annotations

from abc import ABC
from typing import ClassVar

from pycommence.core.types import CommenceString
from pydantic import BaseModel, ConfigDict, Field

from amherst_core.consts_enums import CategoryName


AmherstModelConfig = ConfigDict(
    populate_by_name=True,
    use_enum_values=True,
    validate_assignment=True,
)


class AmherstBase(BaseModel, ABC):
    model_config = AmherstModelConfig


class AmherstTable(AmherstBase, ABC):
    name: CommenceString = Field(..., alias='Name')
    category: ClassVar[CategoryName]
