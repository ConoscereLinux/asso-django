import datetime as dt

from dateutil.relativedelta import relativedelta
from django.contrib import admin


def year_first_day(year: int = None) -> dt.date:
    """Return first date of the year (current if not specified)"""
    if year is None:
        year = dt.date.today().year
    return dt.date(year=year, month=1, day=1)


def yearly_duration(years: int = 1) -> relativedelta:
    """A relative date delta of some years (one by default)"""
    return relativedelta(years=years)


def _add_fields(
    model: admin.ModelAdmin | admin.TabularInline,
    attribute: str,
    fields: tuple,
) -> tuple:
    """Add fields to an attribute of a ModelAdmin mantaining user defined ones."""
    _fields = getattr(model, attribute, None)
    if _fields is None:
        _fields = tuple()

    for field in fields:
        if field not in _fields:
            _fields += (field,)

    setattr(model, attribute, _fields)

    return _fields
