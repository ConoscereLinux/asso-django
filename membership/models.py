"""
The membership management, from the single one to the MembersRegister.

"""

# Standard Import

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project Import
from common import models as cm


class Member(cm.EditInfo, cm.TrashBin):
    """It represents an Association Member"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="member",
        verbose_name=_("User"),
        help_text=_("The User the Member use for Login"),
    )


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

    card_number = models.IntegerField(
        default=0,
        verbose_name=_("Card Number"),
        help_text=_("The unique number to write on the card"),
    )


class MembershipPeriod(cm.Base, cm.EditInfo, cm.TrashBin):
    """This represents the applying period of the Membership."""

    start_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name=_("Start Date"),
        help_text=_("It is the day the Membership starts"),
    )

    # TODO: that library is not working
    # duration = rdf.RelativeDeltaField(
    #     default=dateutil.relativedelta(year=1),
    #     verbose_name=_("Duration"),
    #     help_text=_("How long is the Membership Period"),
    # )

    price = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        default=0.0,
        verbose_name=_("Price"),
        help_text=_("The price to pay for this Period Membership"),
    )


class MembersRegister(cm.Base, cm.EditInfo, cm.TrashBin):
    """It represents the Registry of the Members in the specified Period."""

    period = models.ForeignKey(
        "MembershipPeriod",
        on_delete=models.CASCADE,
        related_name="period_memberships",
        verbose_name=_("Period"),
        help_text=_("The Period the Membership Apply"),
    )


class RegisterEntry(cm.EditInfo, cm.TrashBin):
    """It is the single Entry (corresponding to a Membership) of the Register."""

    # TODO: evaluate to eliminate this model, and use a ManyToMany relation
    # instead
    rester = models.ForeignKey(
        "MembersRegister",
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
