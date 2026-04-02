from datetime import date
from typing import ClassVar

from pydantic import Field

from amherst_core.commence_types import CSVSpaces, CommenceDate, CommenceString
from amherst_core.consts_enums import CategoryName
from amherst_core.mdls._shipable import AmherstShipableBase
from amherst_core.mdls.shipment import ShipmentDetails
from amherst_core.utils.text_and_date import dated_name


class AmherstCustomer(AmherstShipableBase):
    category: ClassVar[CategoryName] = CategoryName.Customer

    delivery_contact_name: CommenceString = Field(alias='Deliv Contact')
    delivery_contact_business: CommenceString = Field(alias='Deliv Name')
    delivery_contact_phone: CommenceString = Field(alias='Deliv Telephone')
    delivery_contact_email: CommenceString = Field(alias='Deliv Email')
    delivery_address_str: CommenceString = Field(alias='Deliv Address')
    delivery_address_pc: CommenceString = Field(alias='Deliv Postcode')

    # customer fields
    invoice_email: CommenceString = Field('', alias='Invoice Email')
    accounts_email: CommenceString = Field('', alias='Accounts Email')
    invoice_address_str: CommenceString = Field('', alias='Invoice Address')
    invoice_contact: CommenceString = Field('', alias='Invoice Contact')
    invoice_name: CommenceString = Field('', alias='Invoice Name')
    invoice_postcode: CommenceString = Field('', alias='Invoice Postcode')
    invoice_telephone: CommenceString = Field('', alias='Invoice Telephone')
    primary_email: CommenceString = Field('', alias='Primary Email')
    date_last_contacted: CommenceDate | None = Field(None, alias='Date Last Contact')

    hires: CSVSpaces = Field('', alias='Has Hired Hires')
    sales: CSVSpaces = Field('', alias='Involves Sale')

    @property
    def shipment(self) -> ShipmentDetails:
        return ShipmentDetails(
            recipient=self.delivery_full_contact,
            reference=dated_name(self.name),
            shipping_date=date.today(),
        )
