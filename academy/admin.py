from django.contrib import admin

import common.admin as ca

from . import models


@admin.register(models.ApprovalState)
class ApprovalStateAdmin(ca.EditInfoAdmin, ca.TrashBinAdmin):
    list_display = ("name", "show", "description")


class SessionAdmin(ca.EditInfoTabularInline):
    model = models.Session


class EnrollmentAdmin(ca.EditInfoTabularInline):
    model = models.Enrollment


@admin.register(models.Event)
class EventAdmin(ca.EditInfoAdmin, ca.TrashBinAdmin):
    list_display = ("title",)
    inlines = [SessionAdmin, EnrollmentAdmin]


@admin.register(models.Trainer)
class TrainerAdmin(ca.EditInfoAdmin, ca.TrashBinAdmin):
    list_display = ("user",)
