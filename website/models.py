from django.db import models

import common.models as cm


# TODO: move to Membership module
class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    card = models.SmallIntegerField(unique_for_year="payment_date")
    payment_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.year} n° {self.card}"
