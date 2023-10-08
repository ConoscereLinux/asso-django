from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..commons.models import OrderedModel, TitleModel


def validate_uppercase(value: str):
    if not value.isupper():
        raise ValidationError(_("%(value)s is not uppercase"), params={"value": value})


def validate_zip_code(value: str):
    if not (len(value) == 5 and value.isnumeric()):
        raise ValidationError(
            _("%(value)s should be a 5 digit number"), params={"value": value}
        )


class Country(TitleModel, OrderedModel):
    code = models.CharField(
        f"{_('Country Code')} (ISO-3166)",
        unique=True,
        max_length=2,
        help_text=_("A two letter code to identify country (based on ISO-3166)"),
        validators=[validate_uppercase],
    )

    class Meta:
        ordering = ["order", "title"]
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


class Region(TitleModel, OrderedModel):
    """Represent a state or province in the default country"""

    code = models.CharField(
        _("Region Code"),
        max_length=2,
        help_text=(
            _("A two letter code to identify a state, region, province in a country")
        ),
        validators=[validate_uppercase],
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
        help_text=_("The country this Region belongs to"),
    )

    class Meta:
        ordering = ["order", "title"]
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        constraints = [
            models.UniqueConstraint(
                fields=["code", "country"], name="unique_region_code_for_country"
            )
        ]


class AddressBaseModel(models.Model):
    value = models.CharField(
        _("Address info"),
        max_length=200,
        help_text=_("Example: Via Barchetta 77"),
    )
    additional = models.CharField(
        _("Additional Address info"),
        blank=True,
        max_length=200,
        help_text=_("Additional info"),
    )

    city = models.CharField(
        _("City"),
        max_length=100,
        help_text=_("Example: Modena"),
    )

    zip_code = models.CharField(
        _("Postal Code"),
        max_length=5,
        validators=[validate_zip_code],
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        verbose_name=_("Region/Province/State"),
        help_text=_("Region/province/state code (EE for Foreign Country"),
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=_("Country"),
    )

    class Meta:
        abstract = True
