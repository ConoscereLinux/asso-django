"""
The Accountant realm, here is all the money part.

"""

# Standard Import

# Site-package Import
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

# Project Import
from common import models as cm
from common import util as u


class Account(cm.Base, cm.EditInfo, cm.TrashBin):
    """This represents one of the transaction account of the association or for
    other players.
    """

    pass


class AnalyticTag(cm.Base, cm.EditInfo, cm.TrashBin):
    """Indicate the type of transaction and is used for analysis"""

    parent = models.ForeignKey(
        "AnalyticTag",
        on_delete=models.CASCADE,
        related_name="analytic_tag_children",
        verbose_name=_("Parent"),
        help_text=_("The parent tag of this AnalyticTag"),
    )


class InvoiceDirection(cm.Base, cm.EditInfo, cm.TrashBin):
    """Indicate if the Invoice is for sale or for buy"""

    pass


class Invoice(cm.Base, cm.EditInfo, cm.TrashBin):
    """Represent an invoice"""

    # TODO: Invoice Sender and Recipient are not implemented yet

    direction = models.ForeignKey(
        "InvoiceDirection",
        on_delete=models.CASCADE,
        related_name="invoice_direction_invoices",
        verbose_name=_("Direction"),
        help_text=_("Indicate the direction of the Invoice"),
    )

    invoice_number = models.IntegerField(
        default=0,
        verbose_name=_("Invoice Number"),
        help_text=_("The unique number of the Invoice"),
    )

    year = models.IntegerField(
        default=u.current_year,
        verbose_name=_("Invoice Number"),
        help_text=_("The unique number of the Invoice"),
    )

    printed = models.BooleanField(
        default=False,
        verbose_name=_("Printed"),
        help_text=_("Indicate if the Invoice was printed"),
    )

    sent = models.BooleanField(
        default=False,
        verbose_name=_("Sent"),
        help_text=_("Indicate if the Invoice was sent"),
    )

    def __repr__(self):
        return f"{self.year}/{self.invoice_number}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["invoice_number", "year"], name="unique_invoice_code"
            )
        ]


class InvoiceRow(cm.Base, cm.EditInfo, cm.TrashBin):
    """Represent the single rows in an invoice"""

    invoice = models.ForeignKey(
        "Invoice",
        on_delete=models.CASCADE,
        related_name="invoice_rows",
        verbose_name=_("Invoice"),
        help_text=_("Indicate the Invoice of ownership"),
    )

    row_number = models.IntegerField(
        default=1,
        verbose_name=_("Row Number"),
        help_text=_("The Number of the row in the Invoice"),
    )

    unit_price = MoneyField(
        default=0,
        max_digits=14,
        decimal_places=2,
        default_currency="EUR",
        verbose_name=_("Unit Price"),
        help_text=_("The price of the single unit"),
    )

    quantity = models.DecimalField(
        default=0.0,
        max_digits=14,
        decimal_places=4,
        verbose_name=_("Quantity"),
        help_text=_("How many items in the current row"),
    )

    transaction = models.OneToOneField(
        "Transaction",
        on_delete=models.CASCADE,
        related_name="transaction_invoice_rows",
        verbose_name=_("Transaction"),
        help_text=_("Indicate the Transaction of the row"),
    )


class Purchase(cm.Base, cm.EditInfo, cm.TrashBin):
    """Represents the purchase of something."""

    transaction = models.OneToOneField(
        "Transaction",
        on_delete=models.CASCADE,
        related_name="transaction_purchase",
        verbose_name=_("Transaction"),
        help_text=_("Indicate the Transaction of the Purchase"),
    )


class LiberalOffer(cm.Base, cm.EditInfo, cm.TrashBin):
    """Represents the offer of something."""

    transaction = models.OneToOneField(
        "Transaction",
        on_delete=models.CASCADE,
        related_name="transaction_liberal_offer",
        verbose_name=_("Transaction"),
        help_text=_("Indicate the Transaction of the LiberalOffer"),
    )


class Transaction(cm.EditInfo, cm.TrashBin):
    """Indicate a single transaction between Accounts"""

    value = MoneyField(
        default=0,
        max_digits=14,
        decimal_places=2,
        default_currency="EUR",
        verbose_name=_("Value"),
        help_text=_("The Value of the Transaction"),
    )

    analytic_tag = models.ForeignKey(
        "AnalyticTag",
        on_delete=models.CASCADE,
        related_name="analytic_tag_transactions",
        verbose_name=_("AnalyticTag"),
        help_text=_("The AnalyticTag of this Transaction"),
    )

    account = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
        related_name="account_transactions",
        verbose_name=_("Account"),
        help_text=_("The Account of this Transaction"),
    )

    date = models.DateField(
        default=u.current_date,
        auto_now=False,
        auto_now_add=False,
        verbose_name=_("Transaction Date"),
        help_text=_("It is the day of the Transaction"),
    )
