import json

from django.conf import settings
from django.utils.text import slugify
from loguru import logger

import website.models as wm


def run():
    with open(settings.BASE_DIR / "scripts" / "default_theme.json", "r") as fp:
        data = json.load(fp)

    if theme := data.get("theme"):
        brand = theme.pop("brand", "My Brand")
        theme.setdefault("active", True)
        if image := theme.get("logo"):
            logger.warning("Cannot save theme logo image at the moment")
        obj, _ = wm.ThemeConfig.objects.update_or_create(brand=brand, defaults=theme)
        obj.full_clean()
        obj.save()

    for item in data.get("navbar", []):
        # get slug from obj, if not exists slugify title then check if is valid
        if not (slug := item.pop("slug", slugify(item.get("title", "")))):
            logger.warning("Either slug or title must be set in navbar item, skipping")
            continue

        obj, _ = wm.NavbarItem.objects.update_or_create(slug=slug, defaults=item)
        obj.full_clean()
        obj.save()

    for social in data.get("socials", []):
        obj, _ = wm.SocialLink.objects.update_or_create(**social)
        obj.full_clean()
        obj.save()
