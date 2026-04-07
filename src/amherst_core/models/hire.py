from datetime import date
from typing import ClassVar

from pycommence.core.meta import CommenceTable
from pycommence.core.types import CommenceDateMaybe, CommenceString
from pydantic import Field

from amherst_core.consts_enums import CategoryName, HireStatus
from amherst_core.models._shipable import AmherstOrderBase
from amherst_core.models.shipment_details import ShipmentDetails
from amherst_core.utils.text_and_date import dated_name


class AmherstHire(AmherstOrderBase, CommenceTable):
    category: ClassVar[CategoryName] = CategoryName.Hire
    boxes: int = Field('', alias='Boxes')
    adict: dict = Field(default_factory=dict, alias='Adict')
    delivery_contact_phone: CommenceString = Field(alias='Delivery Tel')
    delivery_method: CommenceString = Field('', alias='Send Method')

    # order overides
    status: HireStatus = Field(alias='Status')

    # hire fields
    send_date: CommenceDateMaybe = Field(default_factory=date.today, alias='Send Out Date')
    missing_kit_str: CommenceString | None = Field(None, alias='Missing Kit')
    due_back_date: CommenceDateMaybe = Field(None, alias='Due Back Date')
    return_notes: CommenceString | None = Field(None, alias='Return Notes')
    number_uhf: int = Field(0, alias='Number UHF')
    radio_type: CommenceString | None = Field(None, alias='Radio Type')
    number_parrot: int = Field(0, alias='Number Parrot')
    arranged_in: bool = Field(False, alias='Pickup Arranged')
    arranged_out: bool = Field(False, alias='DB label printed')
    pickup_date: CommenceDateMaybe = Field(None, alias='Pickup Date')

    def shipment(self) -> ShipmentDetails:
        return ShipmentDetails(
            recipient=self.delivery_full_contact,
            reference=dated_name(self.customers[0], self.send_date),
            shipping_date=self.send_date,
            boxes=self.boxes,
            context=self.model_dump(mode='json'),
        )
