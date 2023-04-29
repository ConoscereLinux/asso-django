from django.contrib.auth.models import User
from django.utils.text import slugify

from admin.data.loaders import JSONLoader

from .models import Member


class MemberLoader(JSONLoader):
    model = Member
    fields = "all"
    defaults = ["cf", "email"]

    def prepare_item(self, item: dict) -> Member:
        return super().prepare_item(item)

    def save(self, path):
        for member in self.load(path):
            user, created = User.objects.get_or_create(
                username=slugify(member.full_name).replace("-", "."),
            )
            member.user = user
            member.full_clean()
            member.save()
