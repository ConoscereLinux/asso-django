from django.contrib import admin

from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ["cf", "name", "surname", "email"]
    list_filter = ["name", "surname"]


admin.site.register(Member, MemberAdmin)
