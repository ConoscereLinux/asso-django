from django.db import models
from django.utils.translation import gettext_lazy as _

from ..commons.models import OrderedModel, TitleModel


def validate_uppercase(value: str):
    return value.isupper()


class Region(OrderedModel):
    """Represent a state or province in the default country"""

    name = models.CharField(
        _("Displayed name"),
        max_length=100,
        help_text="The name to display in selector",
    )
    code = models.CharField(
        _("Region Code"),
        max_length=2,
        help_text=(
            "A two letter code to identify a state, region, province inside a country"
        ),
        validators=[validate_uppercase],
    )

    class Meta:
        ordering = ["order", "name"]
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
