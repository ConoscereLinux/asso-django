from django.contrib.auth.models import User
from django.utils.text import slugify

from common.managers import JsonLoadManager


class MemberManager(JsonLoadManager):
    defaults = ("cf", "email")

    def prepare_model(self, item):
        member = super().prepare_model(item)

        user, created = User.objects.get_or_create(
            username=slugify(member.full_name).replace("-", "."),
        )
        member.user = user
        return member
