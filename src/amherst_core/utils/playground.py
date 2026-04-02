from pycommence.pycommence_client import PyCommenceClient

from amherst_core.models import AmherstCustomer


class NotIt:
    pass


if __name__ == '__main__':
    # dummy = NotIt()
    # a_func(dummy)
    with PyCommenceClient('Customer') as pycmc:
        testy = pycmc.cursor().read_row(pk='Test')
        test_customer = AmherstCustomer(**testy.data)
        ...
