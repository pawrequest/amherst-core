from __future__ import annotations

from abc import ABC, abstractmethod

from pycommence.core.types import CommenceConnection, CommenceDateMaybe, CommencePath, CommenceString
from pydantic import Field

from amherst_core.models._base import AmherstTable
from amherst_core.models.contact_address import Address, Contact, FullContact
from amherst_core.models.shipment_details import ShipmentDetails


class AmherstShipableBase(AmherstTable, ABC):
    delivery_method: CommenceString = Field('', alias='Delivery Method')
    delivery_contact_business: CommenceString = Field(alias='Delivery Name')
    delivery_contact_name: CommenceString = Field(alias='Delivery Contact')
    delivery_contact_email: CommenceString = Field(alias='Delivery Email')
    delivery_contact_phone: CommenceString = Field(alias='Delivery Telephone')

    delivery_address_str: CommenceString = Field(alias='Delivery Address')
    delivery_address_pc: CommenceString = Field(alias='Delivery Postcode')

    @property
    def delivery_address(self) -> Address:
        return Address.from_str_and_pc(self.delivery_address_str, self.delivery_address_pc)

    @property
    def delivery_contact(self) -> Contact:
        return Contact(
            name=self.delivery_contact_name,
            business=self.delivery_contact_business,
            phone=self.delivery_contact_phone,
            email=self.delivery_contact_email,
        )

    @property
    def delivery_full_contact(self) -> FullContact:
        return FullContact(contact=self.delivery_contact, address=self.delivery_address)

    @abstractmethod
    def shipment(self) -> ShipmentDetails: ...


class AmherstOrderBase(AmherstShipableBase, ABC):
    customers: CommenceConnection = Field(alias='To Customer')
    status: CommenceString | None = Field(None, alias='Status')
    invoice: CommencePath | None = Field(None, alias='Invoice')
    order_date: CommenceDateMaybe = Field(None, alias='Order Date')

    @property
    def customer1(self):
        if not self.customers:
            raise ValueError('No Customer')
        return self.customers[0]
