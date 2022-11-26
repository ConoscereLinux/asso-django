from django.contrib import admin

from .models import Member, Membership


class MembershipInline(admin.StackedInline):
    model = Membership
    extra = 0


class MemberAdmin(admin.ModelAdmin):
    list_display = ["id", "cf", "name", "surname", "email"]
    list_filter = ["name", "surname"]

    inlines = [MembershipInline]


admin.site.register(Member, MemberAdmin)
admin.site.register(Membership)
