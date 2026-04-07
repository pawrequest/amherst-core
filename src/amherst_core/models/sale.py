from datetime import date
from typing import ClassVar

from pycommence.core.types import CommenceDateMaybe, CommenceString
from pydantic import Field

from amherst_core.consts_enums import CategoryName, SaleStatus
from amherst_core.models._shipable import AmherstOrderBase
from amherst_core.models.shipment_details import ShipmentDetails
from amherst_core.utils.text_and_date import dated_name


class AmherstSale(AmherstOrderBase):
    category: ClassVar[CategoryName] = CategoryName.Sale
    delivery_method: CommenceString | None = None

    # optional overrides order
    status: SaleStatus = Field(None, alias='Status')
    booking_date: CommenceDateMaybe | None = Field(None, alias='Date Ordered')

    # sale fields
    lost_equipment: CommenceString | None = Field(None, alias='Lost Equipment')
    purchase_order: CommenceString | None = Field(None, alias='Purchase Order')

    def shipment(self) -> ShipmentDetails:
        return ShipmentDetails(
            recipient=self.delivery_full_contact,
            reference=dated_name(self.customers[0]),
            shipping_date=date.today(),
        )
