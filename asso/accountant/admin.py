from django.contrib import admin

from ..core.admin import (
    CreatedAdmin,
    CreatedTabularInline,
    EditableAdmin,
    EditableTabularInline,
    TrashableAdmin,
)
from . import models


@admin.register(models.Account)
class AccountAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    pass


@admin.register(models.AnalyticTag)
class AnalyticTagAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    pass


class InvoiceRowAdmin(CreatedTabularInline, EditableTabularInline):
    model = models.InvoiceRow


@admin.register(models.Invoice)
class InvoiceAdmin(CreatedAdmin, EditableAdmin, TrashableAdmin):
    inlines = [InvoiceRowAdmin]


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


# NOTE: miss LiberalOffer ModelAdmin
# NOTE: miss Purchase ModelAdmin
