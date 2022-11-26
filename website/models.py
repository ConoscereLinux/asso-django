from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    cf = models.CharField(unique=True, max_length=16)
    email = models.EmailField()

    # birth_date: types.Date
    # gender: types.Gender | None  # (meta) genere_member
    # address: str  # (meta) indirizzo_member
    # birth_place: str  # (meta) luogo_nascita_member

    @property
    def full_name(self):
        return f"{str(self.name)} {str(self.surname).title()}"

    def __str__(self):
        return self.full_name


class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    card = models.SmallIntegerField(unique_for_year="payment_date")
    payment_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.year} n° {self.card}"
