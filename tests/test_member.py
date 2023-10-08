import datetime as dt

import pytest

from asso.member.models import Member, MemberPermanentAddress


@pytest.mark.django_db
def test_valid_member(user, region):
    address = MemberPermanentAddress.objects.create(
        value="Via NULL 42",
        city="Metropolis",
        region=region,
        zip_code="00000",
    )

    Member.objects.create(
        user=user,
        gender="M",
        first_name="A",
        last_name="B",
        social_card="RSSMRA99D20F205R",
        address=address,
        birth_date=dt.date(1970, 1, 1),
        birth_city="Metropolis",
        birth_province=region,
        phone="000 0000000",
        document_type="carta-identita",
        document_grant_from="Someone",
        document_number="AA0000BB",
    )
