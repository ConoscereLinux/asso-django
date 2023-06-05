from django.contrib import admin

from ..core.admin import CreatedAdmin, EditableAdmin, TrashableAdmin
from . import models


@admin.register(models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ["member", "card_number", "period"]


class MembershipInline(admin.StackedInline):
    model = models.Membership
    extra = 0


@admin.register(models.Member)
class MemberAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    list_display = ["user", "id", "first_name", "last_name", "cf", "birth_date"]
    list_filter = ["user", "cf"]

    search_fields = ["first_name", "last_name", "cf"]

    inlines = [MembershipInline]


@admin.register(models.MembershipPeriod)
class MembershipPeriodAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date"]
