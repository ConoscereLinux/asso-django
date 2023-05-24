import json
import pathlib

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.text import slugify
from tqdm import tqdm

import academy.models as am
import membership.models as mm
from asso.core.data import load_item


def run(*args):
    path = args[0] if args else settings.BASE_DIR / ".data" / "export.json"
    with open(pathlib.Path(path), "r") as fp:
        data = json.load(fp)

    print("Loading members...")
    for member in tqdm(data.get("members", [])):
        if not member["cf"]:
            continue

        user = {
            "username": (email := member.pop("email")),
            "first_name": member.pop("first_name"),
            "last_name": member.pop("last_name"),
            "email": email,
            "password": make_password(None),
        }
        member["user"], _ = load_item(user, User, ("username",))

        load_item(member, mm.Member, ("user",), ("post_id", "phone"))

    print("Loading Courses")
    for event in tqdm(data.get("courses", [])):
        approval_state = {"name": event.pop("approval_state")}
        event["approval_state"], _ = load_item(approval_state, am.ApprovalState)

        event.setdefault("slug", slugify(event.get("title", "")))
        event["creation_date"] = event.pop("published")
        event["edit_date"] = event.pop("modified")
        load_item(event, am.Event, ("slug",), ("post_id", "end_sub_date"))
