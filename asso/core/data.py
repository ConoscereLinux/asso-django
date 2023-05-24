from typing import Type

from django.db.models import Model


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
