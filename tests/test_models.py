import threading
from datetime import datetime

import pytest
from loguru import logger
from pycommence.core.meta import registered_table_models
from pycommence.pycommence_client import PyCommenceClient
from pycommence.threads import com_context

TEST_ITEM_NAME = 'TestItem' + threading.current_thread().name + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


@pytest.fixture(scope='function')
def timed():
    from time import time

    start = time()
    yield
    end = time()
    logger.debug(f'Test took {end - start:.4f} seconds')


@pytest.fixture(scope='function', autouse=True)
def delay_log(caplog):
    with caplog.at_level('DEBUG'):
        yield
    print('\n\nCaptured logs:')
    for record in caplog.records:
        print(f'{record.levelname}: {record.message}')


@pytest.fixture(scope='function')
def pycmc_client():
    with com_context(), PyCommenceClient() as client:
        if not client.conversation().db_name_and_path()[0] == 'Tutorial':
            raise ValueError('Expected Tutorial DB')
        yield client


@pytest.fixture(scope='function')
def pycmc_client_non_tutorial():
    with com_context(), PyCommenceClient() as client:
        yield client


#
@pytest.fixture(scope='function')
def amherst_customer_data(pycmc_client_non_tutorial):
    yield pycmc_client_non_tutorial.cursor('Customer').read_row(pk='Test')


def test_cust(amherst_customer_data):
    print(amherst_customer_data)


def test_register():
    from amherst_core.models.customer import AmherstCustomer

    print(AmherstCustomer.__name__)
    mods = registered_table_models()
    assert mods


#
#
# @pytest.fixture(scope='session')
# def amherst_customer(amherst_customer_data) -> AmherstCustomer:
#     return AmherstCustomer.model_validate(amherst_customer_data.data, from_attributes=True)
#
#
# def test_amherst_customer(amherst_customer): ...
#
#
