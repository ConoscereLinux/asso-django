import json
from pathlib import Path

from loguru import logger

from website.models import Member, Membership

DATA_PATH = Path(".data")


def run():
    with open(DATA_PATH / "export.json", "r") as fp:
        data = json.load(fp)

    for member in data.get("members"):
        logger.debug(f"Importing member {member.get('cf')}")
        Member(
            id=member.get("oid"),
            name=member.get("name"),
            surname=member.get("surname"),
            cf=member.get("cf"),
            email=member.get("email")[0],
        ).save()

    for membership in data.get("memberships"):
        logger.debug(f"Importing membership for member {membership.get('member_id')}")
        Membership(
            member=Member.objects.get(id=membership.get("member_id")),
            year=membership.get("year"),
            card=membership.get("card"),
            payment_date=membership.get("payment_date"),
        ).save()
