from django.contrib import admin

from . import models


@admin.register(models.ThemeConfig)
class ThemeConfigAdmin(admin.ModelAdmin):
    list_display = ("brand", "active", "logo")


@admin.register(models.NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "url", "active", "order")
    ordering = ["-active", "order"]


@admin.register(models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "url", "logo")
