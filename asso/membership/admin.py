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
    list_display = ["user", "id", "cf", "birth_date"]
    list_filter = ["sex", "document_type"]

    search_fields = ["user", "cf"]

    inlines = [MembershipInline]


@admin.register(models.MembershipPeriod)
class MembershipPeriodAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date"]
