"""Models to handle Members and Memberships"""

import datetime as dt

from codicefiscale import codicefiscale
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from relativedeltafield import RelativeDeltaField

from asso.address.models import AddressBaseModel, Region
from asso.commons.fields import Gender
from asso.commons.models import (
    OrderedModel,
    SlugModel,
    SoftDeletableModel,
    TimeStampModel,
    TitleModel,
)


def check_member_cf(value: str):
    if not codicefiscale.is_valid(value):
        raise ValidationError(_(f"Fiscal Code {value} formally invalid"))


class MemberQualification(SlugModel, TitleModel, OrderedModel):
    def __str__(self):
        return f"{self.title}"


class MemberPermanentAddress(AddressBaseModel):
    """A Permanent address where the Member lives (ita: Indirizzo di Residenza)"""

    class Meta:
        verbose_name = _("Member Permanent Address")
        verbose_name_plural = _("Member Permanent Addresses")


class Member(TimeStampModel, SoftDeletableModel):
    """It represents an Association Member"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_("User"),
        related_name="member",
    )

    first_name = models.CharField(_("First Name"), max_length=60)
    last_name = models.CharField(_("Last Name"), max_length=60)

    cf = models.CharField(
        _("Social ID"),
        max_length=16,
        validators=[check_member_cf],
    )

    gender = models.CharField(_("Gender"), max_length=1, choices=Gender.choices)

    address = models.OneToOneField(
        MemberPermanentAddress,
        on_delete=models.PROTECT,
        related_name="member",
        verbose_name=_("Permanent Address"),
    )

    birth_date = models.DateField(_("Birth Date"))
    birth_city = models.CharField(
        _("Birth City"),
        max_length=150,
        help_text=_("City/municipality or foreign country where Member is born"),
    )
    birth_province = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        verbose_name=_("Birth Province"),
        help_text=_("Region where Member is born (EE for other countries)"),
    )

    phone = models.CharField(
        _("Phone Number"),
        max_length=50,
        help_text=_("Phone Number, use only digits, +, -, space and parenthesis"),
        validators=[
            RegexValidator(
                r"^(00|\+)?((\d+|\(\d+\))[ \-]?)+\d$",
                _("Use only plus sign (at start), dashes (-), spaces and parenthesis"),
            )
        ],
    )

    class DocumentType(models.TextChoices):
        CARTA_IDENTITA = "carta-identita", _("Carta Identità")
        PASSAPORTO = "passaporto", _("Passaporto")
        PATENTE = "patente", _("Patente")

    document_type = models.CharField(
        _("Document Type"), choices=DocumentType.choices, max_length=16
    )
    document_grant_from = models.CharField(
        _("Who grant the Document"),
        max_length=100,
        help_text=_("Public Authority who grant you the document"),
    )
    document_number = models.CharField(_("Document Number/Code"), max_length=30)
    document_expires = models.DateField(
        _("Document Expiration Date"), default=dt.date.today
    )

    privacy_acknowledgement = models.DateField(
        _("Privacy Page Aknowledgement"),
        null=True,
        blank=True,
        default=None,
        help_text=_("Last date Member has read privacy page"),
    )

    profession = models.CharField(
        _("Profession"), blank=True, max_length=80, default=""
    )
    qualification = models.ForeignKey(
        MemberQualification,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="members",
        verbose_name=_("Qualification"),
    )

    come_from = models.CharField(
        _("How you found us"),
        blank=True,
        max_length=200,
        default="",
    )
    interests = models.CharField(
        _("Interests"),
        blank=True,
        max_length=200,
        default="",
    )

    notes = models.TextField(_("Internal Notes"), default="", blank=True)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def last_membership(self) -> "Membership":
        return self.memberships.order_by("period__end_date").last()

    def get_absolute_url(self):
        return reverse("member", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.full_name} ({self.cf})"

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")


def default_start_date(year: int = None) -> dt.date:
    """Return first date of the year (use current year if not specified)"""
    return dt.date(year=year if year else dt.date.today().year, month=1, day=1)


def default_duration(years: int = 1) -> relativedelta:
    """A relative date delta of some years (one by default)"""
    return relativedelta(years=years)


class MembershipPeriod(TitleModel, TimeStampModel, SoftDeletableModel):
    """Range of validity of memberships"""

    card_prefix = models.SlugField(
        _("Card Prefix"),
        unique=True,
        max_length=50,
        help_text=_("Prefix for the card identifier"),
    )

    start_date = models.DateField(
        default=default_start_date,
        verbose_name=_("Start Date"),
        help_text=_("First day for the Membership period"),
    )

    duration = RelativeDeltaField(
        default=default_duration,
        verbose_name=_("Duration"),
        help_text=_("Duration of this Period (as ISO8601 format with designators)"),
    )

    end_date = models.DateField(
        editable=False,
        verbose_name=_("End Date"),
        help_text=_("Last day for the Membership period"),
    )

    price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        default_currency="EUR",
        verbose_name=_("Price"),
        help_text=_("The default price to pay for this Period Membership"),
    )

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + self.duration
        super().save(*args, **kwargs)


class Membership(TimeStampModel, SoftDeletableModel):
    """The member of a user for a particular period."""

    member = models.ForeignKey(
        "Member",
        on_delete=models.PROTECT,
        related_name="memberships",
        verbose_name=_("Member"),
    )

    period = models.ForeignKey(
        "MembershipPeriod",
        on_delete=models.CASCADE,
        related_name="period_memberships",
        verbose_name=_("Membership Period"),
    )

    card_number = models.SmallIntegerField(
        default=0,
        verbose_name=_("Card Number"),
        help_text=_("The unique number to write on the card"),
    )

    def __str__(self):
        return f"{str(self.period.card_prefix)}/{self.card_number}"


# class MemberRegister(ContentModel):
#     """Member registration referred to a specific Period"""
#
#     period = models.ForeignKey(
#         "MembershipPeriod",
#         on_delete=models.CASCADE,
#         related_name="period_member_registration",
#         verbose_name=_("Period"),
#         help_text=_("The Period the Membership Apply"),
#     )


# class RegisterEntry(TimeStampModel, SoftDeletableModel):
#     """It is the single Entry (corresponding to a Membership) of the Register."""
#
#     register = models.ForeignKey(
#         "MemberRegister",
#         on_delete=models.CASCADE,
#         related_name="register_entries",
#         verbose_name=_("Register"),
#         help_text=_("The owner Register"),
#     )
#
#     membership = models.ForeignKey(
#         "Membership",
#         on_delete=models.CASCADE,
#         related_name="membership_register_entries",
#         verbose_name=_("Membership"),
#         help_text=_("The corresponding Membership"),
#     )
