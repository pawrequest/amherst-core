from __future__ import annotations

from typing import NamedTuple


class ContactBasic(NamedTuple):
    name: str
    business: str
    phone: str
    email: str


class AmherstAddress(NamedTuple):
    address_str: str
    postcode: str


class AddressBasic(NamedTuple):
    address_lines: list[str]
    postcode: str
    town: str = ''

    def truncated_lines(self, max_lines=3) -> list[str]:
        if len(self.address_lines) <= max_lines:
            return self.address_lines
        else:
            truncated = self.address_lines[: max_lines - 1]
            truncated.append(', '.join(self.address_lines[max_lines - 1 :]))
            return truncated

    @classmethod
    def from_str_and_pc(cls, address_str, postcode) -> AddressBasic:
        addr_lines = address_str.strip().splitlines()
        town = addr_lines.pop() if len(addr_lines) > 1 else ''
        used_lines = [_ for _ in addr_lines if _]
        return cls(address_lines=used_lines, postcode=postcode, town=town)


class FullContact(NamedTuple):
    contact: ContactBasic
    address: AddressBasic
