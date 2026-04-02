from __future__ import annotations

from datetime import date, datetime
from functools import partial


def ordinal_day(n: int):
    """Convert an integer to its ordinal as a string, e.g. 1 -> 1st, 2 -> 2nd, etc."""
    return str(n) + ('th' if 4 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th'))


def now_iso_seconds() -> str:
    return datetime.now().isoformat(timespec='seconds')


def ordinal_date_name(dt) -> str:
    """sortable and human readable dt eg '2024-June-1st (Saturday @ 14:30:00)'"""
    return dt.strftime(f'%Y-%B-{ordinal_day(dt.day)} (%A @ %H:%M:%S)')


ordinal_date_name_now = partial(ordinal_date_name, datetime.now())


def dated_name(string: str, date_: date | None = None):
    dt = date_ or date.today()
    return f'{string} - {ordinal_date_name(dt)}'
