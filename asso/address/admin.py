from django.contrib import admin

from . import models


@admin.register(models.Region)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "order"]
