from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from asso.core.fields import UniqueBooleanField
from asso.core.models.commons import Described, OrderedModel


class ThemeConfig(models.Model):
    brand = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos", null=True, blank=True)
    active = UniqueBooleanField(default=False, null=False)

    class Meta:
        ordering = ["-active"]


class NavbarItem(OrderedModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=200, default="")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"({self.order:02}) {self.title}"

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/4.1/ref/models/instances/#get-absolute-url
        if self.url and not self.url.startswith("http") and settings.BASE_URL:
            return str(settings.BASE_URL / self.url.lstrip("/"))
        return self.url


class SocialLink(Described, OrderedModel):
    DEFAULT_LOGO = "globe"
    AVAILABLE_LOGOS = [
        (DEFAULT_LOGO, "Web site (default)"),
        ("facebook", "Facebook"),
        ("twitter", "Twitter"),
        ("x", "X"),
        ("linkedin", "LinkedIn"),
        ("youtube", "YouTube"),
        ("github", "GitHub"),
        ("instagram", "Instagram"),
    ]

    url = models.URLField()
    logo = models.CharField(
        max_length=24,
        default=DEFAULT_LOGO,
        verbose_name="Logo Icon",
        choices=AVAILABLE_LOGOS,
    )
