import pycommence
from pycommence import pycommence_context

from amherst_core.mdls._base import ShipableProtocol
from amherst_core.models.amherst_models import AmherstCustomer


def a_func(thingy: ShipableProtocol):
    print(thingy.customer_name)
    print(thingy.delivery_contact_name)
    print(thingy.delivery_contact_business)
    print(thingy.delivery_contact_phone)
    print(thingy.delivery_contact_email)
    print(thingy.delivery_address_str)
    print(thingy.delivery_address_pc)


class NotIt:
    pass


if __name__ == '__main__':
    # dummy = NotIt()
    # a_func(dummy)
    with pycommence_context('Customer') as pycmc:
        testy = pycmc.read_row(pk='Test')
        test_customer = AmherstCustomer(**testy.data, row_info=testy.row_info)
        a_func(test_customer)
        ...
