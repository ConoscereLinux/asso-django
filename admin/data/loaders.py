import json
from abc import ABC
from typing import Iterable, Literal

import django.db.models
from loguru import logger


class Loader(ABC):
    model: django.db.models.Model

    # fields used to create obj and search if exists (except if exluded by defaults)
    fields: Literal["all"] | list[str] | dict[str, str] = "all"

    # Fields to be skipped when searching if model already exists
    defaults: Literal["none"] | list[str] | dict[str, str] = "none"


class JSONLoader(Loader, ABC):
    def _prepare_item(self, item: dict):
        defaults_ = self.defaults if isinstance(self.defaults, (list, dict)) else []

        match self.fields:
            case [*fields]:
                item_ = {k: item[k] for k in fields if k not in defaults_}
            case {**fields}:
                item_ = {
                    mk: item[ik] for ik, mk in fields.items() if ik not in defaults_
                }
            case "all" | _:
                item_ = {k: v for k, v in item.items() if k not in defaults_}

        match defaults_:
            case {}:
                item_["defaults"] = {mk: item[ik] for ik, mk in defaults_.items()}
            case [] | _:
                item_["defaults"] = {k: item[k] for k in defaults_}

        return self.prepare_item(item_)

    def load(self, path) -> Iterable[django.db.models.Model]:
        with open(path, "r") as fp:
            data = json.load(fp)

        if isinstance(data, dict):
            data = data[self.model.__name__.lower()]

        return map(self._prepare_item, data)

    def prepare_item(self, item: dict) -> django.db.models.Model:
        model, created = self.model.objects.get_or_create(**item)
        if not created:
            logger.debug(f"Item {model} already exists")
            for key, value in item.get("defaults", {}).items():
                setattr(model, key, value)
        return model

    def save(self, path):
        """Save all models found inside json file."""
        for item in self.load(path):
            logger.debug(f"Creating object {item}")
            item.full_clean()
            item.save()
