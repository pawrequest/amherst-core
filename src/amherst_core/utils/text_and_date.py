from __future__ import annotations

from datetime import date, datetime
from functools import partial

from amherst_core.consts_enums import NONCOMPLIANT_APOSTROPHES


def replace_noncompliant_apostrophes(value: str) -> str:
    value = str(value)
    if isinstance(value, str):
        for char in NONCOMPLIANT_APOSTROPHES:
            value = value.replace(char, "'")
    if value is None:
        return ''
    return value


def split_addr_str2(address: str) -> tuple[list[str], str]:
    addr_lines = address.splitlines()
    town = addr_lines.pop() if len(addr_lines) > 1 else ''

    if len(addr_lines) < 3:
        addr_lines.extend([''] * (3 - len(addr_lines)))
    elif len(addr_lines) > 3:
        addr_lines[2] = ','.join(addr_lines[2:])
        addr_lines = addr_lines[:3]

    used_lines = [_ for _ in addr_lines if _]
    return used_lines, town


def split_csv(v):
    if isinstance(v, list):
        return v
    if isinstance(v, str):
        v = replace_noncompliant_apostrophes(v)
        return [item.strip() for item in v.split(',') if item.strip()]
    raise ValueError(f'Expected a string, got {type(v)}')


def join_csv(v, separator=', '):
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return separator.join(v)
    raise ValueError(f'Expected a list, got {type(v)}')


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
