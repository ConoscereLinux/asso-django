from django.contrib import admin

import common.admin as ca

from . import models


@admin.register(models.Trainer)
class TrainerAdmin(ca.EditInfoAdmin, ca.TrashBinAdmin):
    list_display = ("user",)
