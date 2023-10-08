from django.contrib import admin

from . import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["title", "code", "country", "order"]


class RegionTabularInline(admin.TabularInline):
    model = models.Region
    exclude = ["description"]
    extra = 0


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["title", "code", "order"]
    inlines = [RegionTabularInline]
