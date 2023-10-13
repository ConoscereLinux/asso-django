import pytest

from asso.accounts.models import User
from asso.address.models import Country, Region


@pytest.fixture
@pytest.mark.django_db
def user():
    return User.objects.create(email="test@example.com")


@pytest.fixture
@pytest.mark.django_db
def country():
    return Country.objects.create(title="Test", order=-10, code="TE")


@pytest.fixture
@pytest.mark.django_db
def region(country):
    return Region.objects.create(title="Test", order=-10, code="TE", country=country)
