from django.contrib import admin

from ..commons.admin import ContentAdmin
from . import models


@admin.register(models.Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("display_name", "user", "biography")


@admin.register(models.EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(models.EventApprovalState)
class EventApprovalStateAdmin(admin.ModelAdmin):
    list_display = ("title", "show", "description")


class EventSessionStackedInline(admin.StackedInline):
    model = models.EventSession
    extra = 0


@admin.register(models.Event)
class EventAdmin(ContentAdmin):
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
        EventSessionStackedInline,
        # EnrollmentAdmin,
    ]


# class EnrollmentAdmin(CreatedTabularInline, EditableTabularInline):
#     model = models.Enrollment
