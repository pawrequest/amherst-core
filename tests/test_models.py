import pytest
from pycommence import pycommence_context
from pycommence.pycmc_types import RowData

from amherst_core.mdls.customer import AmherstCustomer


@pytest.fixture(scope='session')
def amherst_customer_data() -> RowData:
    with pycommence_context(csrname='Customer') as cmc:
        return cmc.read_row(pk='Test')


@pytest.fixture(scope='session')
def amherst_customer(amherst_customer_data) -> AmherstCustomer:
    return AmherstCustomer.model_validate(amherst_customer_data.data, from_attributes=True)


def test_amherst_customer(amherst_customer): ...
