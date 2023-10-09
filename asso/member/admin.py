from django.contrib import admin

from . import models


class MembershipPermanentAddress(admin.StackedInline):
    model = models.MembershipPermanentAddress
    max_num = 1


@admin.register(models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ["__str__", "member", "period", "card_number"]
    inlines = [MembershipPermanentAddress]


class MembershipInline(admin.StackedInline):
    model = models.Membership
    extra = 0


class MemberPermanentAddress(admin.StackedInline):
    model = models.MemberPermanentAddress
    max_num = 1


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "social_card",
        "user",
        "first_name",
        "last_name",
        "birth_date",
        "last_membership",
    ]
    list_filter = ["gender", "document_type"]
    search_fields = ["first_name", "last_name", "social_card"]
    inlines = [
        MembershipInline,
        MemberPermanentAddress,
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
