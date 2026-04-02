from datetime import date, timedelta

import pytest
from pycommence.core.row_data import RowData
from pycommence.pycommence_client import PyCommenceClient

from amherst_core.models import AmherstCustomer

TEST_DATE = date.today() + timedelta(days=2)
if TEST_DATE.weekday() in (5, 6):
    TEST_DATE += timedelta(days=7 - TEST_DATE.weekday())


@pytest.fixture(scope='session')
def amherst_customer_data() -> RowData:
    with PyCommenceClient('Customer') as cmc:
        return cmc.cursor().read_row(pk='Test')


@pytest.fixture(scope='session')
def amherst_customer(amherst_customer_data) -> AmherstCustomer:
    return AmherstCustomer(row_id=amherst_customer_data.row_id, **amherst_customer_data.data)


def test_it():
    cust = AmherstCustomer
    assert cust.model_fields['name'].alias == 'Name'
    ...


def test_amherst_hire(amherst_customer: AmherstCustomer):
    assert amherst_customer.name == 'Test'
