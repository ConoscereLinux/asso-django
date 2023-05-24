# Generated by Django 4.1.7 on 2023-03-15 01:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ApprovalState",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="",
                        help_text="Object name",
                        max_length=256,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Object description",
                        verbose_name="Description",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The Date and the Time of creation on the object",
                        verbose_name="Creation Date and Time",
                    ),
                ),
                (
                    "edit_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The Date and the Time of last time the object was edited",
                        verbose_name="Last edit Date and Time",
                    ),
                ),
                (
                    "trash_state",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the object is trashed",
                        verbose_name="Trashed",
                    ),
                ),
                (
                    "show",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if at this state the Event has to be shown",
                        verbose_name="Show At This State",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who has created the object",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creation User",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who edited the object last time",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last edit User",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The Date and the Time of creation on the object",
                        verbose_name="Creation Date and Time",
                    ),
                ),
                (
                    "edit_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The Date and the Time of last time the object was edited",
                        verbose_name="Last edit Date and Time",
                    ),
                ),
                (
                    "attendant",
                    models.ForeignKey(
                        help_text="The Attendant of witch the Enrollment is referred to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_attendants",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Attendant",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who has created the object",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creation User",
                    ),
                ),
            ],
            options={
                "ordering": ["-creation_date"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="",
                        help_text="Object name",
                        max_length=256,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Object description",
                        verbose_name="Description",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The Date and the Time of creation on the object",
                        verbose_name="Creation Date and Time",
                    ),
                ),
                (
                    "edit_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The Date and the Time of last time the object was edited",
                        verbose_name="Last edit Date and Time",
                    ),
                ),
                (
                    "trash_state",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the object is trashed",
                        verbose_name="Trashed",
                    ),
                ),
                (
                    "need_membership",
                    models.BooleanField(
                        default=True,
                        help_text="Indicate if the membership is needed in order to attend to this event",
                        verbose_name="Membership Needed",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=4,
                        default=0.0,
                        help_text="The price to pay in order to attend the Event",
                        max_digits=14,
                        verbose_name="Price",
                    ),
                ),
                (
                    "approval_state",
                    models.ForeignKey(
                        help_text="It represents the state of approval of the event",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="menu_entries",
                        to="academy.approvalstate",
                        verbose_name="Approval State",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who has created the object",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creation User",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Trainer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="",
                        help_text="Object name",
                        max_length=256,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Object description",
                        verbose_name="Description",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The Date and the Time of creation on the object",
                        verbose_name="Creation Date and Time",
                    ),
                ),
                (
                    "edit_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The Date and the Time of last time the object was edited",
                        verbose_name="Last edit Date and Time",
                    ),
                ),
                (
                    "trash_state",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the object is trashed",
                        verbose_name="Trashed",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who has created the object",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creation User",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who edited the object last time",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last edit User",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        help_text="The User the Trainer use for Login",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="",
                        help_text="Object name",
                        max_length=256,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Object description",
                        verbose_name="Description",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The Date and the Time of creation on the object",
                        verbose_name="Creation Date and Time",
                    ),
                ),
                (
                    "edit_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The Date and the Time of last time the object was edited",
                        verbose_name="Last edit Date and Time",
                    ),
                ),
                (
                    "trash_state",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the object is trashed",
                        verbose_name="Trashed",
                    ),
                ),
                (
                    "start",
                    models.DateTimeField(
                        help_text="The start time and date of the session, determine hide state of the event",
                        verbose_name="Start date and time",
                    ),
                ),
                (
                    "end",
                    models.DateTimeField(
                        help_text="The end time and date of the session, determine hide state of the event",
                        verbose_name="End date and time",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who has created the object",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creation User",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        help_text="The Event of witch the Session is referred to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_sessions",
                        to="academy.event",
                        verbose_name="Event",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who edited the object last time",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last edit User",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Presence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The Date and the Time of creation on the object",
                        verbose_name="Creation Date and Time",
                    ),
                ),
                (
                    "edit_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The Date and the Time of last time the object was edited",
                        verbose_name="Last edit Date and Time",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who has created the object",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creation User",
                    ),
                ),
                (
                    "enrollment",
                    models.ForeignKey(
                        help_text="The Enrollment of which the Presence is registered",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enrollment_presences",
                        to="academy.enrollment",
                        verbose_name="Enrollment",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        help_text="The Session for which the Presence is registered",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="session_presences",
                        to="academy.session",
                        verbose_name="Session",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The User who edited the object last time",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last edit User",
                    ),
                ),
            ],
            options={
                "ordering": ["-creation_date"],
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="event",
            name="trainers",
            field=models.ManyToManyField(
                help_text="The Trainers that present the Event",
                related_name="trainer_events",
                to="academy.trainer",
                verbose_name="Trainers",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who edited the object last time",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
        migrations.AddField(
            model_name="enrollment",
            name="event",
            field=models.ForeignKey(
                help_text="The Event of witch the Enrollment is referred to",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event_enrollments",
                to="academy.event",
                verbose_name="Event",
            ),
        ),
        migrations.AddField(
            model_name="enrollment",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User who edited the object last time",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
    ]