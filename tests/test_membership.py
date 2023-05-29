import pytest
from django.core.exceptions import ValidationError

from asso.core.models import User
from asso.membership.models import Member


@pytest.fixture
def user(db):
    (user := User(email="a@a.com")).save()
    return user


@pytest.mark.django_db
def test_member(user):
    Member(
        user=user,
        sex="M",
        first_name="A",
        last_name="B",
        cf="RSSMRA99D20F205R",
    ).full_clean()

    with pytest.raises(ValidationError):
        Member().full_clean()
