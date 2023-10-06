"""The member management, from the single one to the MembersRegister."""

import datetime as dt

from codicefiscale import codicefiscale
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from relativedeltafield import RelativeDeltaField

from asso.commons.models import (
    ContentModel,
    OrderedModel,
    SlugModel,
    SoftDeletableModel,
    TimeStampModel,
    TitleModel,
)
from asso.commons.utils import year_first_day, yearly_duration

from .constants import ITALIAN_PROVINCES


def check_member_cf(value: str):
    if not codicefiscale.is_valid(value):
        raise ValidationError(_(f"Fiscal Code {value} formally invalid"))


class MemberQualification(SlugModel, TitleModel, OrderedModel):
    def __str__(self):
        return f"{self.title}"


class Member(TimeStampModel, SoftDeletableModel):
    """It represents an Association Member"""

    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.PROTECT,
    #     verbose_name=_("User"),
    #     related_name="member",
    # )

    # cf = models.CharField(
    #     _("Codice Fiscale"),
    #     max_length=16,
    #     validators=[check_member_cf],
    # )

    # class Gender(models.TextChoices):
    #     MALE = "M", _("Male")
    #     FEMALE = "F", _("Female")
    #
    # sex = models.CharField(_("Gender"), choices=Gender.choices, max_length=1)

    # birth_date = models.DateField(_("Birth Date"))
    # Translators: Comune di nascita (ITA)
    # birth_city = models.CharField(
    #     _("Birth City"),
    #     max_length=150,
    #     help_text=_("City/municipality or foreign country where Member is born"),
    # )
    # birth_province = models.CharField(
    #     _("Birth Province"),
    #     help_text=_("Italian Province where Member is born (EE for other countries)"),
    #     choices=ITALIAN_PROVINCES,
    #     max_length=2,
    #     default="MO",
    # )

    # phone = models.CharField(
    #     _("Phone Number"),
    #     max_length=50,
    #     help_text=_("Phone Number, use only digits, +, -, space and parenthesis"),
    #     validators=[
    #         RegexValidator(
    #             r"^(00|\+)?((\d+|\(\d+\))[ \-]?)+\d$",
    #             _("Use only plus sign (at start), dashes (-), spaces and parenthesis"),
    #         )
    #     ],
    # )

    # address_description = models.CharField(
    #     _("Address"), max_length=200, help_text=_("Example: Via Roma 42/a")
    # )
    # address_city = models.CharField(_("Address City"), max_length=100)
    # address_postal_code = models.CharField(
    #     _("Postal Code"),
    #     max_length=5,
    #     validators=[
    #         RegexValidator(r"[0-9]{5}", _("Italian Postal Code is made of 5 digits"))
    #     ],
    # )
    # address_province = models.CharField(
    #     _("Address Province"),
    #     help_text=_("Address Province (EE for other countries)"),
    #     choices=ITALIAN_PROVINCES,
    #     max_length=2,
    #     default="MO",
    # )

    # class DocumentType(models.TextChoices):
    #     CARTA_IDENTITA = "carta-identita", _("Carta Identità")
    #     PASSAPORTO = "passaporto", _("Passaporto")
    #     PATENTE = "patente", _("Patente")
    #
    # document_type = models.CharField(
    #     _("Document Type"), choices=DocumentType.choices, max_length=16
    # )
    # document_grant_from = models.CharField(
    #     _("Who has grant the Document"),
    #     max_length=100,
    #     help_text=_("Public Authority who grant you the document"),
    # )
    # document_number = models.CharField(_("Document Number/Code"), max_length=30)
    # document_expires = models.DateField(
    #     _("Document Expiration Date"), default=dt.date.today
    # )

    # privacy_acknowledgement = models.DateField(
    #     _("Privacy Page Aknowledgement"),
    #     null=True,
    #     blank=True,
    #     default=None,
    #     help_text=_("Last date Member has read privacy page"),
    # )

    # profession = models.CharField(
    #     _("Profession"), blank=True, max_length=80, default=""
    # )
    # qualification = models.ForeignKey(
    #     to=MemberQualification,
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT,
    #     related_name="members",
    #     verbose_name=_("Study Degree"),
    # )

    # come_from = models.CharField(
    #     _("How you found us"),
    #     blank=True,
    #     max_length=200,
    #     default="",
    # )
    # interests = models.CharField(
    #     _("Interests"),
    #     blank=True,
    #     max_length=200,
    #     default="",
    # )

    # notes = models.TextField(_("Internal Notes"), default="", blank=True)

    # @property
    # def full_name(self) -> str:
    #     return getattr(self.user, "full_name", None)

    # def get_absolute_url(self):
    #     return reverse("member", kwargs={"pk": self.pk})

    # def __str__(self):
    #     return f"{self.full_name} ({self.cf})"

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")


# class Membership(TimeStampModel, SoftDeletableModel):
#     """The member of a user for a particular period."""
#
#     member = models.ForeignKey(
#         "Member",
#         on_delete=models.PROTECT,
#         related_name="memberships",
#         verbose_name=_("Member"),
#     )
#
#     period = models.ForeignKey(
#         "MembershipPeriod",
#         on_delete=models.CASCADE,
#         related_name="period_memberships",
#         verbose_name=_("Membership Period"),
#     )
#
#     card_number = models.SmallIntegerField(
#         default=0,
#         verbose_name=_("Card Number"),
#         help_text=_("The unique number to write on the card"),
#     )
#
#     def __str__(self):
#         return f"{str(self.period)}/{self.card_number}"


# class MembershipPeriod(ContentModel):
#     """This represents the applying period of the Membership."""
#
#     start_date = models.DateField(
#         default=year_first_day,
#         verbose_name=_("Start Date"),
#         help_text=_("Initial day of the Membership period"),
#     )
#
#     duration = RelativeDeltaField(
#         default=yearly_duration,
#         verbose_name=_("Duration"),
#         help_text=_("Duration of this Period (as ISO8601 format with designators)"),
#     )
#
#     @property
#     def end_date(self) -> dt.date:
#         return self.start_date + self.duration
#
#     price = MoneyField(
#         max_digits=10,
#         decimal_places=2,
#         default=0.0,
#         default_currency="EUR",
#         verbose_name=_("Price"),
#         help_text=_("The default price to pay for this Period Membership"),
#     )
#
#     def __str__(self):
#         return self.title


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
