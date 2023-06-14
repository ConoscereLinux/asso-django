import datetime as dt
import json
import pathlib

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.utils.text import slugify
from loguru import logger
from tqdm import tqdm

from asso.academy.models import ApprovalState, Event
from asso.core.data import load_item
from asso.core.models.users import User
from asso.membership.models import Member

DEFAULT_PATH = settings.BASE_DIR.parent / ".data" / "export.json"


def fill_none(item: dict, key, default, skip_log: bool = False):
    if item.get(key) is None:
        if not skip_log:
            logger.debug(f"{item.get('title')} | Fill value {key} with {default}")
        item[key] = default


def fill_member(member: dict) -> dict:
    fill_none(member, "cf", "AAAABBBBCCCCDDDD")
    fill_none(member, "sex", "M")
    fill_none(member, "birth_city", "NOT VALID")
    fill_none(member, "birth_date", "1970-01-01")
    fill_none(member, "birth_province", "EE")
    fill_none(member, "phone", "+39 000 0000000")

    fill_none(member, "address_description", "Via")
    fill_none(member, "address_number", "SNC", skip_log=True)
    fill_none(member, "address_city", "NOT VALID")
    fill_none(member, "address_province", "EE")
    fill_none(member, "address_postal_code", "00000")

    fill_none(member, "document_type", "carta-identita")
    fill_none(member, "document_grant_from", "NOT VALID")
    fill_none(member, "document_number", "NOT VALID")
    fill_none(member, "document_expires", dt.date.today(), skip_log=True)

    member.pop("title", None)
    return member


def run(*args):
    path = pathlib.Path(args[0]) if args else DEFAULT_PATH
    if not path.exists():
        print(f"File {path} not found")
        return

    with open(pathlib.Path(path), "r") as fp:
        data = json.load(fp)

    print("Loading members...")
    members, users = {}, {}
    for member in data.get("members", []):
        member_id = member.pop("id")
        users[member_id] = {
            "email": member.pop("email"),
            "username": member.pop("slug"),
            "password": make_password(None),
            "first_name": member.pop("first_name"),
            "last_name": member.pop("last_name"),
        }
        members[member_id] = member

    for membership in tqdm(data.get("memberships", [])):
        if membership["year"] not in {2020, 2021, 2022, 2023}:
            continue

        id_ = membership["member_id"]
        member = fill_member(members[id_])

        user, _ = load_item(users[id_], User, ("email",))
        member.setdefault("user", user)

        load_item(member, Member, ("user",))
        # load_item(membership, Membership, ...)

    print("Loading Courses")
    for event in tqdm(data.get("courses", [])):
        approval_state = {"title": event.pop("approval_state")}
        event["approval_state"], _ = load_item(approval_state, ApprovalState)

        event.setdefault("slug", slugify(event.get("title", "")))
        event["creation_date"] = event.pop("creation_date")
        event["edit_date"] = event.pop("edit_date")
        load_item(event, Event, ("slug",), ("id", "end_sub_date", "teacher_ids"))
