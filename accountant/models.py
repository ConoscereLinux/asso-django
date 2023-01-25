"""
The Accountant realm, here is all the money part.

"""

# Standard Import

# Site-package Import
from django.db import models

# Project Import
from common import models as cm



class Account(cm.Base, cm.EditInfo, cm.TrashBin):
    pass


class AnalyticTag(cm.Base, cm.EditInfo, cm.TrashBin):
    pass


class Invoice(cm.Base, cm.EditInfo, cm.TrashBin):
    pass


class InvoiceRow(cm.Base, cm.EditInfo, cm.TrashBin):
    pass 


class Purchase(cm.Base, cm.EditInfo, cm.TrashBin):
    pass


class Transaction(cm.EditInfo, cm.TrashBin):
    pass


