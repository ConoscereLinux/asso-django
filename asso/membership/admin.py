from django.contrib import admin

from ..core.admin import CreatedAdmin, EditableAdmin, TrashableAdmin
from . import models


@admin.register(models.Membership)
class MembershipAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    list_display = ["member", "card_number", "period"]


class MembershipInline(admin.StackedInline):
    model = models.Membership
    extra = 0


@admin.register(models.Member)
class MemberAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    list_display = ["user", "id", "cf", "birth_date"]
    list_filter = ["sex", "document_type"]

    search_fields = ["user__first_name", "user__last_name", "user__email", "cf"]

    inlines = [MembershipInline]


@admin.register(models.MembershipPeriod)
class MembershipPeriodAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    list_display = ["title", "start_date", "end_date", "duration", "description"]
