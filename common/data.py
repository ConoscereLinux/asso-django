from django.db.models import Model
from typing import Type


def load_item(
    item: dict, model: Type[Model], fields: tuple[str] = None
) -> tuple[Model, bool]:
    if fields is None:
        filters, defaults = item, {}
    else:
        filters = {k: v for k, v in item.items() if fields and k in fields}
        defaults = {k: v for k, v in item.items() if not fields or k not in fields}

    obj, created = model.objects.update_or_create(**filters, defaults=defaults)
    obj.full_clean()
    obj.save()

    return obj, created
