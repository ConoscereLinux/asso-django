from django.contrib import admin

import common.admin

from . import models

# Register your models here.


# @admin.register(models.Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ["year", "card", "member"]
#     list_filter = ["year", "card"]


# class MembershipInline(admin.StackedInline):
#     model = models.Membership
#     extra = 0


# @admin.site.register(models.Member)
# class MemberAdmin(common.admin.EditInfoAdmin, common.admin.TrashBinAdmin):
#     list_display = ["full_name", "id", "cf", "first_name", "last_name", "email"]
#     list_filter = ["first_name", "last_name", "cf", "email"]
#
#     # inlines = [MembershipInline]
