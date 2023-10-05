from django.contrib import admin

# from ..core.admin import (
#     CreatedAdmin,
#     CreatedTabularInline,
#     EditableAdmin,
#     EditableTabularInline,
#     TrashableAdmin,
# )
from . import models


@admin.register(models.EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


class EventSessionAdmin(admin.StackedInline):
    model = models.EventSession
    extra = 0


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "category",
        "is_removed",
        "need_membership",
        "price",
    )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        EventSessionAdmin,
        # EnrollmentAdmin,
    ]


# @admin.register(models.ApprovalState)
# class ApprovalStateAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
#     list_display = ("title", "show", "description")


# class EnrollmentAdmin(CreatedTabularInline, EditableTabularInline):
#     model = models.Enrollment


# @admin.register(models.Trainer)
# class TrainerAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
#     list_display = ("template_name", "user", "display_name")
