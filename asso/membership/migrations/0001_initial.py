# Generated by Django 4.2 on 2023-04-21 00:14

import django.db.models.deletion
import relativedeltafield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
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
                    "trash_state",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the object is trashed",
                        verbose_name="Trashed",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Member First Name",
                        max_length=50,
                        verbose_name="First Name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Member Last Name",
                        max_length=50,
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "cf",
                    models.CharField(
                        help_text="Codice Fiscale",
                        max_length=16,
                        unique=True,
                        verbose_name="Codice Fiscale",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
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
                        help_text="The User the Member use for Login",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="member",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "ordering": ["-creation_date"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Membership",
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
                    "trash_state",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the object is trashed",
                        verbose_name="Trashed",
                    ),
                ),
                (
                    "card_number",
                    models.SmallIntegerField(
                        default=0,
                        help_text="The unique number to write on the card",
                        verbose_name="Card Number",
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
                    "member",
                    models.ForeignKey(
                        help_text="The Member for that period",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_memberships",
                        to="membership.member",
                        verbose_name="Member",
                    ),
                ),
            ],
            options={
                "ordering": ["-creation_date"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MembershipPeriod",
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
                    "start_date",
                    models.DateField(
                        auto_now_add=True,
                        help_text="It is the day the Membership starts",
                        verbose_name="Start Date",
                    ),
                ),
                (
                    "duration",
                    relativedeltafield.fields.RelativeDeltaField(
                        default="P1Y",
                        help_text="How long is the Membership Period",
                        verbose_name="Duration",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=4,
                        default=0.0,
                        help_text="The price to pay for this Period Membership",
                        max_digits=14,
                        verbose_name="Price",
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
            name="MembersRegister",
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
                    "period",
                    models.ForeignKey(
                        help_text="The Period the Membership Apply",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="period_member_register",
                        to="membership.membershipperiod",
                        verbose_name="Period",
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
            name="RegisterEntry",
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
                    "membership",
                    models.ForeignKey(
                        help_text="The corresponding Membership",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="membership_register_entries",
                        to="membership.membership",
                        verbose_name="Membership",
                    ),
                ),
                (
                    "rester",
                    models.ForeignKey(
                        help_text="The owner Register",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="register_entries",
                        to="membership.membersregister",
                        verbose_name="Register",
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
            model_name="membership",
            name="period",
            field=models.ForeignKey(
                help_text="The Period the Membership Apply",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="period_memberships",
                to="membership.membershipperiod",
                verbose_name="Period",
            ),
        ),
        migrations.AddField(
            model_name="membership",
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