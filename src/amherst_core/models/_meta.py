from typing import TYPE_CHECKING

from loguru import logger

from amherst_core.consts_enums import CategoryName

if TYPE_CHECKING:
    from amherst_core.models._base import AmherstTable

TABLE_REGISTER: dict[str, type['AmherstTable']] = {}


def register_table(cls: type['AmherstTable']) -> type['AmherstTable']:
    TABLE_REGISTER[str(cls.category)] = cls
    logger.debug(f'Registered table model: {cls.category}')
    return cls


def get_table_model(csrname: CategoryName) -> type['AmherstTable'] | None:
    res = TABLE_REGISTER.get(csrname)
    if not res:
        logger.warning(f'No table model found for csrname: {csrname}')
    return res
