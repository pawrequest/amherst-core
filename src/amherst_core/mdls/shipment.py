from __future__ import annotations

from datetime import date, time

from pydantic import Field, model_validator

from amherst_core.commence_types import (
    CSVLines,
    CSVSpaces,
    CommenceConnection,
    CommenceDate,
    CommencePath,
    CommenceString,
)
from amherst_core.consts_enums import ShipDirection
from amherst_core.mdls._base import AmherstBase
from amherst_core.mdls.contact_address import FullContact
from amherst_core.utils.text_and_date import now_iso_seconds, ordinal_date_name_now


class CommenceShipment(AmherstBase):
    direction: CommenceString
    label: CommencePath | None = Field(None, alias='Label')
    boxes: int = Field(0, alias='Boxes')
    send_date: CommenceDate = Field(..., alias='Send Date')
    collection_id: CommenceString = Field('', alias='Collection ID')

    creation_datetime: CommenceString = Field(default_factory=now_iso_seconds, alias='Creation Datetime')
    name: CommenceString = Field(default_factory=ordinal_date_name_now, alias='Name')
    latest_tracking: CommenceString = Field('', alias='Latest Tracking')
    tracking_links: CSVLines = Field(default_factory=list, alias='Tracking Links')
    shipment_numbers: CSVSpaces = Field(default_factory=list, alias='Shipment Numbers')
    notes: CommenceString = Field('', alias='Notes')

    hires: CommenceConnection = Field(default_factory=list, alias='For Hire')
    sales: CommenceConnection = Field(default_factory=list, alias='For Sale')
    customers: CommenceConnection = Field(default_factory=list, alias='For Customer')


class ShipmentDetails(AmherstBase):
    # mandatory
    recipient: FullContact
    reference: str
    shipping_date: date

    # defaults
    boxes: int = 1
    direction: ShipDirection = ShipDirection.OUTBOUND
    collect_ready: time = time(hour=9, minute=0)
    collect_closed: time = time(hour=17, minute=0)
    package_format: str = 'parcel'
    weight_kg: int = 5

    # optional
    sender: FullContact | None = None

    @model_validator(mode='after')
    def validate_sender(self):
        if self.direction in (ShipDirection.INBOUND, ShipDirection.DROPOFF) and self.sender is None:
            raise ValueError('Sender must be provided for INBOUND or DROPOFF shipments')
        return self

    @property
    def remote_full_contact(self) -> FullContact:
        match self.direction:
            case ShipDirection.OUTBOUND:
                return self.recipient
            case ShipDirection.INBOUND | ShipDirection.DROPOFF:
                return self.sender
            case _:
                raise ValueError('Bad ShipDirection')
