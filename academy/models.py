"""
The Academy section, with teacher event and participation.

"""

# Standard Import

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

import accountant.models

# Project Import
from common import models as cm


class ApprovalState(cm.Base, cm.EditInfo, cm.TrashBin):
    """Represents the state of approval of an Event."""

    show = models.BooleanField(
        default=False,
        verbose_name=_("Show At This State"),
        help_text=_("Indicates if at this state the Event has to be shown"),
    )


class Event(cm.Base, cm.EditInfo, cm.TrashBin):
    """Represents a course, a talk or a conference.

    It can have some attendant teachers and can be carried out in several
    sessions.
    """

    approval_state = models.ForeignKey(
        "ApprovalState",
        on_delete=models.SET_NULL,
        related_name="menu_entries",
        verbose_name=_("Approval State"),
        help_text=_("It represents the state of approval of the event"),
    )

    # TODO: Decide if the Session it is mandatory and so the 'execution_day'
    # could be obsolete, and the first session date could be used instead
    execution_day = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name=_("The Day Of Execution"),
        help_text=_(
            "It is the fist day of execution, is used to order Event"
            " in visualization and to determine when hide the Event"
            " in case of more Sessions"
        ),
    )

    membership_needed = models.BooleanField(
        default=True,
        verbose_name=_("Membership Needed"),
        help_text=_(
            "Indicate if the membership is needed in order to attend" " to this event"
        ),
    )

    price = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        default=0.0,
        verbose_name=_("Price"),
        help_text=_("The price to pay in order to attend the Event"),
    )

    trainers = models.ManyToManyField(
        "Trainer",
        related_name="trainer_events",
        verbose_name=_("Trainers"),
        help_text=_("The Trainers that present the Event"),
    )


class Session(cm.Base, cm.EditInfo, cm.TrashBin):
    """If an Event it is divided in more session, it could be managed here."""

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="event_sessions",
        verbose_name=_("Event"),
        help_text=_("The Event of witch the Session is referred to"),
    )

    execution_day = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name=_("The Day Of Execution"),
        help_text=_(
            "It is the day of execution of that Session"
            " in visualization and determine when hide related Event"
        ),
    )


class Enrollment(cm.EditInfo):
    """Indicate that one User want to attend at an Event."""

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="event_enrollments",
        verbose_name=_("Event"),
        help_text=_("The Event of witch the Enrollment is referred to"),
    )

    attendant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="event_attendants",
        verbose_name=_("Attendant"),
        help_text=_("The Attendant of witch the Enrollment is referred to"),
    )

    transaction = models.OneToOneField(
        accountant.models.Transaction,
        on_delete=models.CASCADE,
        related_name="transaction_enrollment",
        verbose_name=_("Event"),
        help_text=_("The Event of witch the Enrollment is referred to"),
    )


class Presence(cm.EditInfo):
    """Indicate the effective presence of an attendant in a particular session."""

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="event_presences",
        verbose_name=_("Event"),
        help_text=_("The Event of witch the Presence is registered"),
    )

    enrollment = models.ForeignKey(
        "Enrollment",
        on_delete=models.CASCADE,
        related_name="enrollment_presences",
        verbose_name=_("Enrollment"),
        help_text=_("The Enrollment of witch the Presence is registered"),
    )


class Trainer(cm.Base, cm.EditInfo, cm.TrashBin):
    """Represents someone that can present an Event"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="trainer",
        verbose_name=_("User"),
        help_text=_("The User the Trainer use for Login"),
    )
