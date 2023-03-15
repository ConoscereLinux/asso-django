"""Base models for other application."""

# Standard Import

from django.conf import settings

# Site-package Import
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local Import

# Create your models here.


class Base(models.Model):
    """Provides name and description fields."""

    name = models.CharField(
        max_length=256, default="", verbose_name=_("Name"), help_text=_("Object name")
    )

    description = models.TextField(
        default="",
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Object description"),
    )

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ordered(models.Model):
    """When inheriting this model an order field is gained."""

    order_index = models.SmallIntegerField(
        default=10, verbose_name=_("Order"), help_text=_("Used for object ordering")
    )

    class Meta:
        abstract = True
        ordering = ["order_index"]


class EditInfo(models.Model):
    """Record some basic information about the edit user and time.

    created_by and updated_by fields inspired by:
    https://dev.to/forhadakhan/automatically-add-logged-in-user-under-createdby-and-updatedby-to-model-in-django-rest-framework-4c9c  # noqa
    """

    # TODO: ensure it's best practice
    creation_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_("Creation Date and Time"),
        help_text=_("The Date and the Time of creation on the object"),
    )

    # TODO: ensure it's best practice
    edit_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name=_("Last edit Date and Time"),
        help_text=_("The Date and the Time of last time the object was edited"),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created_by",
        blank=True,
        null=True,
        verbose_name=_("Creation User"),
        help_text=_("The User who has created the object"),
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updated_by",
        blank=True,
        null=True,
        verbose_name=_("Last edit User"),
        help_text=_("The User who edited the object last time"),
    )

    class Meta:
        abstract = True

        ordering = ["-creation_date"]


class TrashBin(models.Model):
    """Allow object to be trashed rather than deleted."""

    trash_state = models.BooleanField(
        default=False,
        verbose_name=_("Trashed"),
        help_text=_("Indicates if the object is trashed"),
    )

    class Meta:
        abstract = True
