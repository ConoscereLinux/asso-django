from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from common import fields
from common import models as cm


class ThemeConfig(models.Model):
    brand = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos", null=True, blank=True)
    active = fields.UniqueBooleanField(default=False, null=False)

    class Meta:
        ordering = ["-active"]


class NavbarItem(cm.OrderedModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"({self.order:02}) {self.title}"

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/4.1/ref/models/instances/#get-absolute-url
        if self.url and settings.BASE_URL:
            return str(settings.BASE_URL / self.url.lstrip("/"))
        return self.url


class SocialLink(cm.OrderedModel):
    title = models.CharField(max_length=100, blank=True)
    url = models.URLField()
    logo = models.SlugField(
        verbose_name="Logo Icon",
        help_text=_(
            "One of the logo-* icons on https://ionic.io/ionicons (facebook, twitter, "
            "linkedin, youtube, ...)"
        ),
    )
