from django.contrib import admin

import asso.core.admin

from . import models


@admin.register(models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ["member", "card_number", "period"]


class MembershipInline(admin.StackedInline):
    model = models.Membership
    extra = 0


@admin.register(models.Member)
class MemberAdmin(asso.core.admin.EditInfoAdmin, asso.core.admin.TrashBinAdmin):
    list_display = ["cf", "user"]
    list_filter = ["user", "cf"]

    inlines = [MembershipInline]


@admin.register(models.MembershipPeriod)
class MembershipPeriodAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date"]
