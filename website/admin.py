from django.contrib import admin

from . import models


@admin.register(models.NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("order", "title", "url")
