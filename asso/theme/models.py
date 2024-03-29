from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from asso.commons.models import (
    DefaultModel,
    HidableModel,
    OrderedModel,
    SlugModel,
    TitleModel,
)


class ThemeConfig(DefaultModel):
    brand = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos", null=True, blank=True)


class NavbarItem(SlugModel, TitleModel, OrderedModel, HidableModel):
    url = models.CharField(
        max_length=200,
        default="",
        verbose_name=_("A URL or a relative path"),
    )

    def __str__(self):
        return f"({self.order:02}) {self.title}"

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/4.1/ref/models/instances/#get-absolute-url
        if self.url and not self.url.startswith("http") and settings.BASE_URL:
            return str(settings.BASE_URL / self.url.lstrip("/"))
        return self.url


class SocialLink(TitleModel, OrderedModel, HidableModel):
    class SocialIcon(models.TextChoices):
        globe = "globe", _("Web site (default)")
        facebook = "facebook", "Facebook"
        twitter = "twitter", "Twitter"
        x = "x", "x.com"
        linkedin = "linkedin", "LinkedIn"
        youtube = "youtube", "YouTube"
        github = "github", "GitHub"
        instagram = "instagram", "Instagram"

    url = models.URLField()
    logo = models.CharField(
        max_length=24,
        default=SocialIcon.globe,
        verbose_name=_("Logo Icon"),
        choices=SocialIcon.choices,
    )
