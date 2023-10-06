import datetime as dt

import pytest

from asso.member.models import Member


@pytest.mark.django_db
def test_valid_member(user):
    Member.objects.create(
        user=user,
        gender="M",
        first_name="A",
        last_name="B",
        cf="RSSMRA99D20F205R",
        birth_date=dt.date(1970, 1, 1),
        birth_city="Metropolis",
        phone="000 0000000",
        address_description="Via NULL 42",
        address_city="Metropolis",
        address_province="EE",
        address_postal_code="00000",
        document_type="carta-identita",
        document_grant_from="Someone",
        document_number="AA0000BB",
    )
