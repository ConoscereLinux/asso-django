from django.conf import settings
from django.db import models


class NavbarItem(models.Model):
    class Meta:
        ordering = ["order"]

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    order = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"({self.order:02}) {self.title}"

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/4.1/ref/models/instances/#get-absolute-url
        if self.url and settings.BASE_URL:
            return str(settings.BASE_URL / self.url.lstrip("/"))
        return self.url
