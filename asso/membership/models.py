"""The membership management, from the single one to the MembersRegister."""

# Standard Import
import datetime as dt

from codicefiscale import codicefiscale

# Site-package Import
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from relativedeltafield import RelativeDeltaField

from asso.core.models.commons import Common, Created, Editable, Trashable
from asso.core.utils import year_first_day, yearly_duration

from .constants import ITALIAN_PROVINCES


def check_member_cf(value: str):
    if not codicefiscale.is_valid(value):
        raise ValidationError(_(f"Fiscal Code {value} formally invalid"))


class Member(Editable, Created, Trashable):
    """It represents an Association Member"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="member",
    )

    cf = models.CharField(
        _("Codice Fiscale"),
        max_length=16,
        validators=[check_member_cf],
    )

    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    sex = models.CharField(_("Gender"), choices=Gender.choices, max_length=1)

    birth_date = models.DateField(_("Birth Date"))
    # Translators: Comune di nascita (ITA)
    birth_city = models.CharField(
        _("Birth City"),
        max_length=150,
        help_text=_("City/municipality or foreign country where Member is born"),
    )
    birth_province = models.CharField(
        _("Birth Province"),
        help_text=_("Italian Province where Member is born (EE for other countries)"),
        choices=ITALIAN_PROVINCES,
        max_length=2,
        default="MO",
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

    address_description = models.CharField(_("Address description"), max_length=150)
    address_additional = models.CharField(
        _("Address additional info"), max_length=150, blank=True, default=""
    )

    address_city = models.CharField(_("Address City"), max_length=100)
    address_postal_code = models.CharField(
        _("Postal Code"),
        max_length=5,
        validators=[
            RegexValidator(r"[0-9]{5}", _("Italian Postal Code is made of 5 digits"))
        ],
    )
    address_province = models.CharField(
        _("Address Province"),
        help_text=_("Address Province (EE for other countries)"),
        choices=ITALIAN_PROVINCES,
        max_length=2,
        default="MO",
    )

    class DocumentType(models.TextChoices):
        CARTA_IDENTITA = "carta-identita", _("Carta Identità")
        PASSAPORTO = "passaporto", _("Passaporto")
        PATENTE = "patente", _("Patente")

    document_type = models.CharField(
        _("Document Type"), choices=DocumentType.choices, max_length=16
    )
    document_grant_from = models.CharField(
        _("Who has grant the Document"),
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

    class Qualification(models.TextChoices):
        DEFAULT = None
        MASTER = "master", _("Master Universitario")
        PHD = "phd", _("Dottorato di Ricerca")
        MASTER_DEGREE = "master-degree", _("Laurea Magistrale")
        BACHELOR_DEGREE = "bachelor-degree", _("Laurea")
        HIGH_SCHOOL = "high-school", _("Diploma Maturità")
        MID_SCHOOL = "mid-school", _("Licenza Media")
        PRIMARY_SCHOOL = "primary_school", _("Elementari")

    profession = models.CharField(
        _("Profession"), blank=True, max_length=80, default=""
    )
    qualification = models.CharField(
        _("Study Degree"),
        null=True,
        blank=True,
        choices=Qualification.choices,
        max_length=16,
        default=None,
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
        return getattr(self.user, "full_name", None)

    def __str__(self):
        return f"{self.full_name} ({self.cf})"


class Membership(Editable, Created, Trashable):
    """The membership of a user for a particular period."""

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


class MembershipPeriod(Common, Trashable):
    """This represents the applying period of the Membership."""

    start_date = models.DateField(
        default=year_first_day,
        verbose_name=_("Start Date"),
        help_text=_("It is the day the Membership starts"),
    )

    duration = RelativeDeltaField(
        default=yearly_duration,
        verbose_name=_("Duration"),
        help_text=_("How long is the Membership Period"),
    )

    @property
    def end_date(self) -> dt.date:
        return self.start_date + self.duration

    price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        default_currency="EUR",
        verbose_name=_("Price"),
        help_text=_("The default price to pay for this Period Membership"),
    )

    def __str__(self):
        return self.title


class MemberRegister(Common, Trashable):
    """Member registration referred to a specific Period"""

    period = models.ForeignKey(
        "MembershipPeriod",
        on_delete=models.CASCADE,
        related_name="period_member_registration",
        verbose_name=_("Period"),
        help_text=_("The Period the Membership Apply"),
    )


class RegisterEntry(Editable, Created, Trashable):
    """It is the single Entry (corresponding to a Membership) of the Register."""

    register = models.ForeignKey(
        "MemberRegister",
        on_delete=models.CASCADE,
        related_name="register_entries",
        verbose_name=_("Register"),
        help_text=_("The owner Register"),
    )

    membership = models.ForeignKey(
        "Membership",
        on_delete=models.CASCADE,
        related_name="membership_register_entries",
        verbose_name=_("Membership"),
        help_text=_("The corresponding Membership"),
    )
