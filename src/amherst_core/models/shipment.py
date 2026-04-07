from __future__ import annotations

from typing import ClassVar

from pycommence.core.meta import CommenceTable
from pycommence.core.types import (
    CSVLines,
    CSVSpaces,
    CommenceDateMaybe,
    CommencePath,
    CommenceString,
)
from pydantic import Field

from amherst_core.consts_enums import CategoryName, ShipDirection
from amherst_core.models._base import AmherstBase
from amherst_core.utils.text_and_date import now_iso_seconds, ordinal_date_name


class CommenceShipmentAdd(AmherstBase):
    category: ClassVar[CategoryName] = CategoryName.Shipment
    direction: ShipDirection = Field(..., alias='Direction')
    label: CommencePath | None = Field(None, alias='Label')
    boxes: int = Field(0, alias='Boxes')
    send_date: CommenceDateMaybe = Field(..., alias='Send Date')
    collection_id: CommenceString = Field('', alias='Collection ID')

    creation_datetime: CommenceString = Field(default_factory=now_iso_seconds, alias='Creation Datetime')
    name: CommenceString = Field(default_factory=ordinal_date_name, alias='Name')
    latest_tracking: CommenceString = Field('', alias='Latest Tracking')
    tracking_links: CSVLines = Field(default_factory=list, alias='Tracking Links')
    shipment_numbers: CSVSpaces = Field(default_factory=list, alias='Shipment Numbers')
    notes: CommenceString = Field('', alias='Notes')

    hires: CSVSpaces = Field(default_factory=list, alias='For Hire')
    sales: CSVSpaces = Field(default_factory=list, alias='For Sale')
    customers: CSVSpaces = Field(default_factory=list, alias='For Customer')


class CommenceShipment(CommenceShipmentAdd, CommenceTable): ...
