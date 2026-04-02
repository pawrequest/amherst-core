from datetime import date
from pathlib import Path

from pycommence.pycommence_client import PyCommenceClient

from amherst_core.consts_enums import ShipDirection
from amherst_core.models import CommenceShipment


def test_create():
    ship = CommenceShipment(
        direction=ShipDirection.OUTBOUND,
        customers=['Test'],
        label=Path(r'C:\prdev\data\sandbox\labels\Outbound\Shipping_Label_TO_Test_Company_ON_2026-04-03.pdf'),
        send_date=date.today(),
    )
    shpdict = ship.model_dump(by_alias=True)
    with PyCommenceClient('Shipment') as cmc:
        res = cmc.cursor().create_row(shpdict)

    print(res)


def test_1():
    with PyCommenceClient('Shipment') as cmc:
        res = cmc.cursor().read_row(pk='2026-April-1st (Wednesday @ 20:42:02)')
        obj = CommenceShipment(**res.data)
    print(obj)
