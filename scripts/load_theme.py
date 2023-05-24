import json

from django.conf import settings
from django.utils.text import slugify
from loguru import logger

from asso import website as wm
from asso.core.data import load_item


def run():
    with open(settings.BASE_DIR / "scripts" / "default_theme.json", "r") as fp:
        data = json.load(fp)

    if theme := data.get("theme"):
        if theme.pop("logo", None):
            logger.warning("[ThemeConfig] Image loading is not yet supported")
        load_item(theme, wm.ThemeConfig, ("brand",))

    for item in data.get("navbar", []):
        item.setdefault("slug", slugify(item.get("title", "")))
        load_item(item, wm.NavbarItem, ("slug",))

    for social in data.get("socials", []):
        load_item(social, wm.SocialLink)
