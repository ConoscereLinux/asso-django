from django.contrib import admin

from . import models


@admin.register(models.ThemeConfig)
class ThemeConfigAdmin(admin.ModelAdmin):
    list_display = ("brand", "logo", "active")


@admin.register(models.NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "url", "show", "order")
    ordering = ["-show", "order"]


@admin.register(models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "logo", "url", "show", "order")
    ordering = ["-show", "order"]
