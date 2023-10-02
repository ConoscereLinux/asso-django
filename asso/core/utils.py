import datetime as dt

from dateutil.relativedelta import relativedelta


def year_first_day(year: int = None) -> dt.date:
    """Return first date of the year (current if not specified)"""
    if year is None:
        year = dt.date.today().year
    return dt.date(year=year, month=1, day=1)


def yearly_duration(years: int = 1) -> relativedelta:
    """A relative date delta of some years (one by default)"""
    return relativedelta(years=years)
