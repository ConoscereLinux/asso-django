"""The Academy section, with teacher event and participation."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from ..commons.models import ContentModel, SoftDeletableModel, TitleModel


class EventCategory(TitleModel):
    """Represent the kind of event"""

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Event Category")
        verbose_name_plural = _("Event Categories")


# class EventApprovalState(TitleModel):
#     """Represents the state of approval of an Event."""
#
#     show = models.BooleanField(
#         default=False,
#         verbose_name=_("Show"),
#         help_text=_("Indicates if at this state the Event has to be shown"),
#     )


class EventSession(ContentModel):
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

    def __str__(self):
        return f"{self.title}"

    # trainers = models.ManyToManyField(
    #     "Trainer",
    #     related_name="trainer_events",
    #     verbose_name=_("Trainers"),
    #     help_text=_("The Trainers that present the Event"),
    # )

    # approval_state = models.ForeignKey(
    #     EventApprovalState,
    #     on_delete=models.PROTECT,
    #     related_name="events",
    #     verbose_name=_("Approval State"),
    #     help_text=_("Actual approval state for this event"),
    # )


# class Enrollment(Created, Editable):
#     """Indicate that User want to attend the Event."""
#
#     event = models.ForeignKey(
#         "Event",
#         on_delete=models.CASCADE,
#         related_name="event_enrollments",
#         verbose_name=_("Event"),
#         help_text=_("The Event of witch the Enrollment is referred to"),
#     )
#
#     attendant = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="event_attendants",
#         verbose_name=_("Attendant"),
#         help_text=_("The Attendant of witch the Enrollment is referred to"),
#     )
#
#     transaction = models.OneToOneField(
#         Transaction,
#         null=True,
#         on_delete=models.CASCADE,
#         related_name="transaction_enrollment",
#         verbose_name=_("Event"),
#         help_text=_("The Event of witch the Enrollment is referred to"),
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


# class Trainer(Created, Editable, Trashable):
#     """Represents someone that can present an Event"""
#
#     display_name = models.CharField(
#         _("Displayed name"), max_length=200, blank=True, default=""
#     )
#
#     biography = models.TextField(
#         blank=True,
#         verbose_name=_("Biography"),
#         help_text=_("Trainer Biography"),
#     )
#
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         verbose_name=_("User"),
#         help_text=_("The User the Trainer use for Login"),
#     )
#
#     @property
#     def template_name(self):
#         return self.user.full_name if not (dn := self.display_name) else dn
#
#     class Meta:
#         constraints = [
#             models.CheckConstraint(
#                 check=Q(user__isnull=False) | Q(display_name__length__gt=0),
#                 name="not_both_null",
#                 violation_error_message=_(
#                     "displayed name and user cannot be either unset"
#                 ),
#             )
#         ]
