import datetime as dt
from typing import Type

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.utils import IntegrityError
from loguru import logger


def load_item(
    item: dict,
    model: Type[Model],
    fields: (str, ...) = None,
    exclude: (str, ...) = None,
) -> tuple[Model, bool]:
    if exclude:
        item = {k: v for k, v in item.items() if k not in exclude}

    if fields is None:
        filters, defaults = item, {}
    else:
        filters = {k: v for k, v in item.items() if fields and k in fields}
        defaults = {k: v for k, v in item.items() if not fields or k not in fields}

    obj, created = model.objects.update_or_create(**filters, defaults=defaults)
    obj.full_clean()
    obj.save()

    return obj, created


def year_first_day(year: int = None) -> dt.date:
    """Return first date of the year (current if not specified)"""
    if year is None:
        year = dt.date.today().year
    return dt.date(year=year, month=1, day=1)


def yearly_duration(years: int = 1) -> relativedelta:
    """A relative date delta of some years (one by default)"""
    return relativedelta(years=years)
