"""Base models for other application."""

# Standard Import

# Site-package Import
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local Import

# Create your models here.


class Base(models.Model):
    """Provides name and description fields."""

    id = models.AutoField(primary_key=True)

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
    """Record some basic information about the edit user and time."""

    creation_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_("Creation Date and Time"),
        help_text=_("The Date and the Time of creation on the object"),
    )

    edit_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name=_("Last edit Date and Time"),
        help_text=_("The Date and the Time of last time the object was edited"),
    )

    creation_user = models.CharField(
        max_length=256,
        default="",
        blank=True,
        verbose_name=_("Creation User"),
        help_text=_("The User that has created the object"),
    )

    edit_user = models.CharField(
        max_length=256,
        default="",
        blank=True,
        verbose_name=_("Last edit User"),
        help_text=_("The User edited the object last time"),
    )

    # TODO: add some management for the user, from the request in the views

    # def save(self, *args, **kwargs):
    #     print()
    #     print(dir(self))
    #     if self.pk is None:
    #         self.creation_user = self.user.username
    #
    #     self.edit_user = self.user.username
    #
    #     super(EditInfo, self).save(*args,**kwargs)

    class Meta:
        abstract = True

        ordering = ["-creation_date"]


class TrashBin(models.Model):
    """Allow object to be trashed rather than deleted."""

    trash_state = models.SmallIntegerField(
        default=0,
        verbose_name=_("Trashed"),
        help_text=_("Indicates if the object is trashed"),
    )

    class Meta:
        abstract = True
