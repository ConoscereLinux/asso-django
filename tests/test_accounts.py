import pytest
from django.core.exceptions import ValidationError

from asso.accounts import models
from asso.accounts.models import User


@pytest.mark.django_db
def test_email_insertion(user):
    # Check default user email state
    assert isinstance(user.email, str)
    assert user.emails.count() == 1 and user.emails.first().email == user.email

    # Add a second user
    user2 = models.User.objects.create(
        username="test2", password="test2", email="test2@test.com"
    )
    assert user2.emails.count() == 1 and user2.emails.first().email == user2.email

    # Change second user email and check number of available emails
    user2.email = "test2@test2.com"
    user2.clean()
    user2.save()
    assert user2.emails.count() == 2

    with pytest.raises(ValidationError) as exc_info:
        user.email = "test2@test2.com"
        user.clean()
        user.save()
