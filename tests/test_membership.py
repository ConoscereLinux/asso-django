import datetime as dt

import pytest
from django.core.exceptions import ValidationError

from asso.core.models.users import User
from asso.membership.models import Member


@pytest.fixture
def user(db):
    (user := User(email="a@a.com")).save()
    return user


@pytest.mark.django_db
def test_valid_member(user):
    Member(
        user=user,
        sex="M",
        first_name="A",
        last_name="B",
        cf="RSSMRA99D20F205R",
        birth_date=dt.date(1970, 1, 1),
        birth_city="Metropolis",
        phone="000 0000000",
        address_description="Via NULL",
        address_number="42",
        address_city="Metropolis",
        address_province="EE",
        address_postal_code="00000",
        document_type="carta-identita",
        document_grant_from="Someone",
        document_number="AA0000BB",
    ).full_clean()


@pytest.mark.django_db
def test_invalid_member(user):
    with pytest.raises(ValidationError):
        Member().full_clean()
