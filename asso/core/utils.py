from typing import Type

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
    try:
        obj, created = model.objects.update_or_create(**filters, defaults=defaults)
        obj.full_clean()
    except (ValidationError, IntegrityError):
        logger.debug(item)
        raise

    obj.save()

    return obj, created
