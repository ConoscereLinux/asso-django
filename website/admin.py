from django.contrib import admin

from . import models


@admin.register(models.ThemeConfig)
class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ("brand", "active")


@admin.register(models.NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "url", "active", "order")
    ordering = ["-active", "order"]
