from django.contrib import admin

from . import models


@admin.register(models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ["__str__", "member", "period", "card_number"]


class MembershipInline(admin.StackedInline):
    model = models.Membership
    extra = 0


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "cf",
        "user",
        "first_name",
        "last_name",
        "birth_date",
        "last_membership",
    ]
    list_filter = ["gender", "document_type"]
    search_fields = ["first_name", "last_name", "cf"]
    inlines = [
        MembershipInline,
    ]


@admin.register(models.MembershipPeriod)
class MembershipPeriodAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "start_date",
        "duration",
        "end_date",
        "price",
        "description",
    ]
