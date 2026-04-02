from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import Field

from amherst_core.commence_types import CommenceConnection, CommenceDate, CommencePath, CommenceString
from amherst_core.mdls._base import AmherstTable
from amherst_core.mdls.contact_address import AddressBasic, ContactBasic, FullContact
from amherst_core.mdls.shipment import ShipmentDetails


class AmherstShipableBase(AmherstTable, ABC):
    @property
    def delivery_address(self) -> AddressBasic:
        return AddressBasic.from_str_and_pc(self.delivery_address_str, self.delivery_address_pc)

    @property
    def delivery_contact(self) -> ContactBasic:
        return ContactBasic(
            name=self.delivery_contact_name,
            business=self.delivery_contact_business,
            phone=self.delivery_contact_phone,
            email=self.delivery_contact_email,
        )

    @property
    def delivery_full_contact(self) -> FullContact:
        return FullContact(contact=self.delivery_contact, address=self.delivery_address)

    @property
    @abstractmethod
    def shipment(self) -> ShipmentDetails: ...

    delivery_method: CommenceString = Field('', alias='Delivery Method')
    delivery_contact_business: CommenceString = Field(alias='Delivery Name')
    delivery_contact_name: CommenceString = Field(alias='Delivery Contact')
    delivery_contact_email: CommenceString = Field(alias='Delivery Email')
    delivery_contact_phone: CommenceString = Field(alias='Delivery Telephone')

    delivery_address_str: CommenceString = Field(alias='Delivery Address')
    delivery_address_pc: CommenceString = Field(alias='Delivery Postcode')


class AmherstOrderBase(AmherstShipableBase, ABC):
    customer: CommenceConnection = Field(alias='To Customer')
    status: CommenceString | None = Field(None, alias='Status')
    invoice: CommencePath | None = Field(None, alias='Invoice')
    order_date: CommenceDate | None = Field(None, alias='Order Date')
