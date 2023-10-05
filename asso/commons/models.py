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
    )

    class Meta:
        abstract = True


class Content(SlugModel, TitleModel):
    """Represent a classic CMS content with slug, title and description."""

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
