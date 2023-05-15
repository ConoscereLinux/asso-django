from django.contrib import admin

import common.admin

from . import models

# Register your models here.


@admin.register(models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ["member", "card_number", "period"]


class MembershipInline(admin.StackedInline):
    model = models.Membership
    extra = 0


@admin.register(models.Member)
class MemberAdmin(common.admin.EditInfoAdmin, common.admin.TrashBinAdmin):
    list_display = ["full_name", "cf", "user"]
    list_filter = ["user", "cf"]

    inlines = [MembershipInline]


@admin.register(models.MembershipPeriod)
class MembershipPeriodAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date"]
