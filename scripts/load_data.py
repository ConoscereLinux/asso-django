import json
from pathlib import Path

from website.models import Member

DATA_PATH = Path("data")


def run():
    with open(DATA_PATH / "export.json", "r") as fp:
        data = json.load(fp)

    for member in data.get("members"):
        Member(
            id=member.get("oid"),
            name=member.get("name"),
            surname=member.get("surname"),
            cf=member.get("cf"),
            email=member.get("email")[0]
        ).save()
