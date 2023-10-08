from django.db import models
from django.utils.translation import gettext_lazy as _

from ..commons.models import OrderedModel, TitleModel


def validate_uppercase(value: str):
    return value.isupper()


class Region(TitleModel, OrderedModel):
    """Represent a state or province in the default country"""

    code = models.CharField(
        _("Region Code"),
        max_length=2,
        help_text=_(
            "A two letter code to identify a state, region, province inside a country"
        ),
        validators=[validate_uppercase],
    )

    class Meta:
        ordering = ["order", "title"]
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
