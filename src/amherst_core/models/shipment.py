from __future__ import annotations

from typing import ClassVar

from pycommence.core.types import (
    CSVLines,
    CSVSpaces,
    CommenceConnection,
    CommenceDateMaybe,
    CommencePath,
    CommenceString,
)
from pydantic import Field

from amherst_core.consts_enums import CategoryName
from amherst_core.models import register_table
from amherst_core.models._base import AmherstTable
from amherst_core.utils.text_and_date import now_iso_seconds, ordinal_date_name_now


@register_table
class CommenceShipment(AmherstTable):
    category: ClassVar[CategoryName] = CategoryName.Shipment
    direction: CommenceString
    label: CommencePath | None = Field(None, alias='Label')
    boxes: int = Field(0, alias='Boxes')
    send_date: CommenceDateMaybe = Field(..., alias='Send Date')
    collection_id: CommenceString = Field('', alias='Collection ID')

    name: CommenceString = Field(default_factory=ordinal_date_name_now, alias='Name')
    creation_datetime: CommenceString = Field(default_factory=now_iso_seconds, alias='Creation Datetime')
    latest_tracking: CommenceString = Field('', alias='Latest Tracking')
    tracking_links: CSVLines = Field(default_factory=list, alias='Tracking Links')
    shipment_numbers: CSVSpaces = Field(default_factory=list, alias='Shipment Numbers')
    notes: CommenceString = Field('', alias='Notes')
    status: CommenceString = Field('', alias='Status')

    # Connections
    hires: CommenceConnection = Field(default_factory=list, alias='For Hire')
    sales: CommenceConnection = Field(default_factory=list, alias='For Sale')
    customers: CommenceConnection = Field(default_factory=list, alias='For Customer')
