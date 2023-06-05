"""The membership management, from the single one to the MembersRegister."""

# Standard Import
import datetime as dt

# Site-package Import
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from relativedeltafield import RelativeDeltaField

from ..core.models import Common, Created, Editable, Trashable
from .constants import ITALIAN_PROVINCES


class Member(Editable, Created, Trashable):
    """It represents an Association Member"""

    class Genders(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        unique=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="member",
        help_text=_("The User used for Login"),
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    cf = models.CharField(
        _("Codice Fiscale"),
        max_length=16,
        help_text=_("Codice Fiscale"),
        validators=[RegexValidator(r"[A-Z0-9]{16}", _("Invalid Fiscal Code"))],
    )

    sex = models.CharField(_("Gender"), choices=Genders.choices, max_length=1)
    birth_date = models.DateField(_("Birth Date"), help_text=_("Birth Date"))
    birth_city = models.CharField(
        _("Birth City"),
        max_length=150,
        help_text=_("City/municipality or foreign country where Member is born"),
    )  # ITA: Comune di nascita
    birth_province = models.CharField(
        _("Birth Province"),
        help_text=_("Italian Province where Member is born (EE for other countries)"),
        choices=ITALIAN_PROVINCES,
        max_length=2,
        default="EE",
    )

    phone = models.CharField(
        _("Phone Number"),
        max_length=50,
        help_text="Phone Number",
        validators=[
            RegexValidator(
                r"^(00|\+)?((\d+|\(\d+\))[ \-]?)+\d$",
                _("Use only plus sign (at start), dashes (-), spaces and parenthesis"),
            )
        ],
    )

    # address: str  # (meta) indirizzo_member
    # ...

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Membership(Editable, Created, Trashable):
    """The membership of a user for a particular period."""

    member = models.ForeignKey(
        "Member",
        on_delete=models.CASCADE,
        related_name="member_memberships",
        verbose_name=_("Member"),
        help_text=_("The Member for that period"),
    )

    period = models.ForeignKey(
        "MembershipPeriod",
        on_delete=models.CASCADE,
        related_name="period_memberships",
        verbose_name=_("Period"),
        help_text=_("The Period the Membership Apply"),
    )

    card_number = models.SmallIntegerField(
        default=0,
        verbose_name=_("Card Number"),
        help_text=_("The unique number to write on the card"),
    )


class MembershipPeriod(Common, Trashable):
    """This represents the applying period of the Membership."""

    start_date = models.DateField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_("Start Date"),
        help_text=_("It is the day the Membership starts"),
    )

    duration = RelativeDeltaField(
        default="P1Y",
        verbose_name=_("Duration"),
        help_text=_("How long is the Membership Period"),
    )

    price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        default_currency="EUR",
        verbose_name=_("Price"),
        help_text=_("The price to pay for this Period Membership"),
    )

    @property
    def end_date(self) -> dt.date:
        return self.start_date + self.duration


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

    rester = models.ForeignKey(
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
