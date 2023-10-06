from django.contrib import admin

from . import models


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["cf", "user", "first_name", "last_name", "birth_date"]
    list_filter = ["gender", "document_type"]
    search_fields = ["first_name", "last_name", "cf"]
    inlines = [
        # MembershipInline,
    ]


# @admin.register(models.Membership)
# class MembershipAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
#     list_display = ["member", "card_number", "period"]

# class MembershipInline(admin.StackedInline):
#     model = models.Membership
#     extra = 0

# @admin.register(models.MembershipPeriod)
# class MembershipPeriodAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
#     list_display = ["title", "start_date", "end_date", "duration", "description"]
