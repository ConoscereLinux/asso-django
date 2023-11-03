"""The Academy section, with teacher event and participation."""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ..commons.models import (
    ContentModel,
    HidableModel,
    OrderedModel,
    SoftDeletableModel,
    TimeStampModel,
    TitleModel,
)


class Trainer(TimeStampModel, SoftDeletableModel):
    """A person who present an event as speaker, teacher, guest, ..."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="trainers",
        verbose_name=_("User"),
        help_text=_("Login credentials for Trainer"),
    )

    display_name = models.CharField(
        _("Displayed name"),
        max_length=200,
        help_text=_("The name to display in teacher card"),
    )

    biography = models.TextField(
        _("Biography"),
        default="",
        blank=True,
        help_text=_("Trainer Biography"),
    )

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = _("Trainer")
        verbose_name_plural = _("Trainers")


class EventCategory(TitleModel):
    """Represent the kind of event"""

    class Meta:
        verbose_name = _("Event Category")
        verbose_name_plural = _("Event Categories")


class EventApprovalState(TitleModel, HidableModel, OrderedModel):
    """Represents the state of approval of an Event."""

    class Meta:
        ordering = ["order", "-show"]
        verbose_name = _("Event Approval State")
        verbose_name_plural = _("Event Approval States")


class EventSession(TitleModel, SoftDeletableModel, TimeStampModel):
    """Single session of an Event."""

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="sessions",
        null=False,
        blank=False,
        help_text=_("The event who generate this session"),
    )

    start = models.DateTimeField(
        verbose_name=_("Start datetime"),
        help_text=_("The start time and date of the session"),
    )

    end = models.DateTimeField(
        verbose_name=_("End datetime"),
        help_text=_("The end time and date of the session"),
    )

    def clean(self):
        if self.start > self.end:
            raise ValidationError(
                _("End timestamp should be greater than start timestamp")
            )

    def save(self, *args, **kwargs):
        super().save()

        query = EventSession.objects.filter(event=self.event)
        self.event.start_date = query.order_by("start").first().start
        self.event.end_date = query.order_by("end").last().end
        self.event.save()


class Event(ContentModel):
    """Represents a course, a talk or a conference."""

    subtitle = models.CharField(
        max_length=250,
        default="",
        blank=True,
        verbose_name=_("Subtitle"),
    )

    category = models.ForeignKey(
        EventCategory,
        on_delete=models.PROTECT,
        related_name="events",
        verbose_name=_("Category"),
        help_text=_("The event category (course, talk, ...)"),
    )

    approval_state = models.ForeignKey(
        EventApprovalState,
        on_delete=models.PROTECT,
        related_name="events",
        verbose_name=_("Approval State"),
        help_text=_("Actual approval state for this event"),
    )

    need_membership = models.BooleanField(
        default=True,
        verbose_name=_("Membership Needed"),
        help_text=_(
            "Indicate if the membership is needed in order to attend to this event"
        ),
    )

    price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default=0.0,
        verbose_name=_("Price"),
        help_text=_("The price to pay for this event (leave blank for free events)"),
    )

    start_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_(
            "The starting date of the first session of this event "
            "(generated from sessions)"
        ),
    )

    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_(
            "The ending date of the last session of this event "
            "(generated from sessions)"
        ),
    )

    trainers = models.ManyToManyField(
        Trainer,
        blank=True,
        related_name="events",
        verbose_name=_("Trainers"),
        help_text=_("The Trainers that present the Event"),
    )

    def get_absolute_url(self):
        return reverse("event", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


class Enrollment(TimeStampModel):
    """Person enrollment to an event"""

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name=_("Event"),
        help_text=_("Event related to this enrollment"),
    )

    email = models.EmailField(
        _("Email"), help_text=_("Email used for comunication regarding this event")
    )
    phone = models.CharField(
        _("Phone Number"),
        max_length=24,
        blank=True,
        default="",
        help_text=_("Phone number used for comunication regarding this event"),
    )

    def __str__(self):
        return f"{self.event} | {self.email}"


# class MemberEnrollment(Enrollment):
#     """An enrollment for a registered member"""
#
#     member = models.ForeignKey(
#         Member,
#         on_delete=models.CASCADE,
#         related_name="enrollments",
#         verbose_name=_("Member"),
#         help_text=_("The member enrolled to this event"),
#     )


# class Presence(Created, Editable):
#     """Indicate the effective presence of an attendant in a particular session."""
#
#     session = models.ForeignKey(
#         "Session",
#         on_delete=models.CASCADE,
#         related_name="session_presences",
#         verbose_name=_("Session"),
#         help_text=_("The Session for which the Presence is registered"),
#     )
#
#     enrollment = models.ForeignKey(
#         "Enrollment",
#         on_delete=models.CASCADE,
#         related_name="enrollment_presences",
#         verbose_name=_("Enrollment"),
#         help_text=_("The Enrollment of which the Presence is registered"),
#     )
