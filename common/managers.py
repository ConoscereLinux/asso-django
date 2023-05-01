"""Contains Generic Custom Managers to expand Models functionality"""

import json

from django.db import models
from loguru import logger


class JsonLoadManager(models.Manager):
    """Expand Model with JSON import capability

    Add the method load for loading data from a JSON export file. To customize subclass
    and overwrite methods 'prepare_dict' (who manage data preparation as dict) and
    'prepare_model' (who convert dict to model and by default ensure to update data).

    Example:
        >>> class Sample(models.Model):
        >>>     objects = JsonLoadManager()
        >>>     field = ...
        >>>
        >>> Sample.objects.load("path/to.json")
    """

    defaults: tuple[str]

    def prepare_dict(self, item: dict) -> dict:
        item_ = {k: v for k, v in item.items() if k not in self.defaults}
        item_["defaults"] = {k: v for k, v in item.items() if k in self.defaults}
        return item_

    def prepare_model(self, item: dict):
        model, created = self.get_or_create(**item)

        if not created:
            logger.debug(f"Item {model} already exists")
            for key, value in item["defaults"].items():
                setattr(model, key, value)

        return model

    def load(self, path, field: str = None):
        with open(path, "r") as fp:
            data = json.load(fp)

        items = data[field] if field and isinstance(data, dict) else data
        assert isinstance(items, list)
        assert all(isinstance(v, dict) for v in items)

        for item in items:
            item_ = self.prepare_dict(item)
            model = self.prepare_model(item_)

            model.full_clean()
            model.save()
