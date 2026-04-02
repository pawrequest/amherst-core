from __future__ import annotations

from datetime import date, time

from pydantic import model_validator

from amherst_core.consts_enums import ShipDirection
from amherst_core.models._base import AmherstBase
from amherst_core.models.contact_address import FullContact


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
