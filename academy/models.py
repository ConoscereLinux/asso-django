"""
The Academy section, with teacher event and participation.

"""

# Standard Import

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project Import
import accountant.models
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

    It can have some attendant teachers and can be carried out in several sessions.
    """

    approval_state = models.ForeignKey(
        "ApprovalState",
        null=True,
        on_delete=models.SET_NULL,
        related_name="menu_entries",
        verbose_name=_("Approval State"),
        help_text=_("It represents the state of approval of the event"),
    )

    need_membership = models.BooleanField(
        default=True,
        verbose_name=_("Membership Needed"),
        help_text=_(
            "Indicate if the membership is needed in order to attend to this event"
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


class Session(cm.EditInfo):
    """If an Event it is divided in more session, it could be managed here."""

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="event_sessions",
        verbose_name=_("Event"),
        help_text=_("The Event of witch the Session is referred to"),
    )

    start = models.DateTimeField(
        verbose_name=_("Start date and time"),
        help_text=_(
            "The start time and date of the session, determine hide state of the event"
        ),
    )

    end = models.DateTimeField(
        verbose_name=_("End date and time"),
        help_text=_(
            "The end time and date of the session, determine hide state of the event"
        ),
    )


class Enrollment(cm.EditInfo):
    """Indicate that User want to attend the Event."""

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
        null=True,
        on_delete=models.CASCADE,
        related_name="transaction_enrollment",
        verbose_name=_("Event"),
        help_text=_("The Event of witch the Enrollment is referred to"),
    )


class Presence(cm.EditInfo):
    """Indicate the effective presence of an attendant in a particular session."""

    session = models.ForeignKey(
        "Session",
        on_delete=models.CASCADE,
        related_name="session_presences",
        verbose_name=_("Session"),
        help_text=_("The Session for which the Presence is registered"),
    )

    enrollment = models.ForeignKey(
        "Enrollment",
        on_delete=models.CASCADE,
        related_name="enrollment_presences",
        verbose_name=_("Enrollment"),
        help_text=_("The Enrollment of which the Presence is registered"),
    )


class Trainer(cm.EditInfo, cm.TrashBin):
    """Represents someone that can present an Event"""

    biography = models.TextField(
        blank=True,
        verbose_name=_("Biography"),
        help_text=_("Trainer Biography"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("User"),
        help_text=_("The User the Trainer use for Login"),
    )
