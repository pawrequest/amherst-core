from __future__ import annotations

from enum import StrEnum

NONCOMPLIANT_APOSTROPHES = ['’', '‘', '′', 'ʼ', '´']


class ShipDirection(StrEnum):
    INBOUND = 'Inbound'
    OUTBOUND = 'Outbound'
    DROPOFF = 'Dropoff'


class RadioType(StrEnum):
    HYTERA = 'Hytera Digital'
    KIRISUN = 'Kirisun UHF'


class CategoryName(StrEnum):
    Shipment = 'Shipment'
    Hire = 'Hire'
    Sale = 'Sale'
    Customer = 'Customer'
    Trial = 'Radio Trial'
    # Repairs = 'Repairs'


class ViewCursorName(StrEnum):
    HiresOut = 'Hires Outbound - Paul'
    HiresIn = 'Hires Inbound - Paul'


class HireStatus(StrEnum):
    BOOKED_IN = 'Booked in'
    PACKED = 'Booked in and packed'
    PARTIALLY_PACKED = 'Partially packed'
    OUT = 'Out'
    RTN_OK = 'Returned all OK'
    RTN_PROBLEMS = 'Returned with problems'
    QUOTE_GIVEN = 'Quote given'
    CANCELLED = 'Cancelled'
    EXTENDED = 'Extended'
    SOLD = 'Sold to customer'


class SaleStatus(StrEnum):
    BOOKED = 'Ordered Ready To Go'
    PACKED = 'Packed'
    SENT = 'Sent'
    WAITING_PAYMENT = 'Waiting For Payment'
    WAITING_OTHER = 'Waiting For Other'
    WAITING_STOCK = 'Waiting For Stock'
    QUOTE = 'Quote Sent'
    LOST_KIT = 'Lost Kit Invoice'
    CANCELLED = 'Cancelled'
    SUPPLIER = 'Sent Direct From Supplier'
