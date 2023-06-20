from django.contrib import admin

from ..core.admin import (
    CreatedAdmin,
    CreatedTabularInline,
    EditableAdmin,
    EditableTabularInline,
    TrashableAdmin,
)
from . import models


@admin.register(models.ApprovalState)
class ApprovalStateAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    list_display = ("title", "show", "description")


class SessionAdmin(CreatedTabularInline, EditableTabularInline):
    model = models.Session


class EnrollmentAdmin(CreatedTabularInline, EditableTabularInline):
    model = models.Enrollment


@admin.register(models.Event)
class EventAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    list_display = ("title", "slug")
    inlines = [SessionAdmin, EnrollmentAdmin]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Trainer)
class TrainerAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    list_display = ("template_name", "user", "display_name")
