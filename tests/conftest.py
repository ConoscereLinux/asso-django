import pytest

from asso.accounts.models import User


@pytest.fixture
@pytest.mark.django_db
def user():
    return User.objects.create(email="test@example.com")
