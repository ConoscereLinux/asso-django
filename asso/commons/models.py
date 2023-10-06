from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class SlugModel(models.Model):
    """A model with a unique required slug field"""

    slug = models.SlugField(
        unique=True,
        max_length=100,
    )

    class Meta:
        abstract = True
        ordering = ["slug"]


class TitleModel(models.Model):
    """A model with a required title field"""

    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_("Title"),
    )
    description = models.TextField(
        default="",
        blank=True,
        verbose_name=_("Description"),
        help_text=_("A short description for this content (not visible in views)"),
    )

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    """A Model who keep track of the user who created it at which time"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Created at"),
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created_by",
        blank=True,
        null=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_("Updated at"),
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updated_by",
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        abstract = True


class SoftDeletableModel(models.Model):
    """A Model which can be soft-deleted"""

    is_removed = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_("Is removed?"),
        help_text=_("Set to True to set as removed or 'soft deleted"),
    )

    @property
    def is_available(self) -> bool:
        return not self.is_removed

    class Meta:
        abstract = True


class ContentModel(SlugModel, TitleModel, SoftDeletableModel, TimeStampModel):
    """Represent a classic CMS content with slug, title, etc.

    Available fields:
        slug: SlugField(unique, required)
        title: CharField(100, required)
        description: TextField(optional)
        is_removed: Boolean(default=False)
    """

    class Meta:
        abstract = True
        ordering = ["slug"]


class OrderedModel(models.Model):
    """A Model with a field for custom ordering."""

    order = models.SmallIntegerField(
        default=0,
        null=False,
        blank=False,
        verbose_name=_("Order"),
        help_text=_("Object ordering value"),
    )

    class Meta:
        abstract = True
        ordering = ["order"]
