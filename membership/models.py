"""
The membership management, from the single one to the MembersRegister.

"""

# Standard Import
import datetime as dt

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from relativedeltafield import RelativeDeltaField

# Project Import
from common import models as cm


class Member(cm.EditInfo, cm.TrashBin):
    """It represents an Association Member"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="member",
        verbose_name=_("User"),
        help_text=_("The User the Member use for Login"),
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name=_("First Name"),
        help_text=_("Member First Name"),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last Name"),
        help_text=_("Member Last Name"),
    )
    cf = models.CharField(
        unique=True,
        max_length=16,
        verbose_name="Codice Fiscale",
        help_text=_("Codice Fiscale"),
    )
    email = models.EmailField()

    # birth_date: types.Date
    # gender: types.Gender | None  # (meta) genere_member
    # address: str  # (meta) indirizzo_member
    # birth_place: str  # (meta) luogo_nascita_member

    @property
    def full_name(self):
        return f"{str(self.first_name)} {str(self.last_name).title()}"

    def __str__(self):
        return self.full_name


class Membership(cm.EditInfo, cm.TrashBin):
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


class MembershipPeriod(cm.Base, cm.EditInfo, cm.TrashBin):
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

    price = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        default=0.0,
        verbose_name=_("Price"),
        help_text=_("The price to pay for this Period Membership"),
    )

    @property
    def end_date(self) -> dt.date:
        return self.start_date + self.duration


class MemberRegister(cm.Base, cm.EditInfo, cm.TrashBin):
    """Member registration referred to a specific Period"""

    period = models.ForeignKey(
        "MembershipPeriod",
        on_delete=models.CASCADE,
        related_name="period_member_registration",
        verbose_name=_("Period"),
        help_text=_("The Period the Membership Apply"),
    )


class RegisterEntry(cm.EditInfo, cm.TrashBin):
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
