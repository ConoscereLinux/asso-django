from django.contrib import admin

from asso.core import admin as ca

from . import models

# Register your models here.


@admin.register(models.Account)
class AccountAdmin(ca.EditInfoAdmin, ca.TrashBinAdmin):
    pass


@admin.register(models.AnalyticTag)
class AnalyticTagAdmin(ca.EditInfoAdmin, ca.TrashBinAdmin):
    pass


class InvoiceRowAdmin(ca.EditInfoTabularInline):
    model = models.InvoiceRow


@admin.register(models.Invoice)
class InvoiceAdmin(ca.EditInfoAdmin, ca.TrashBinAdmin):
    inlines = [InvoiceRowAdmin]


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


# NOTE: miss LiberalOffer ModelAdmin
# NOTE: miss Purchase ModelAdmin
