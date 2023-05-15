from django.contrib.auth.models import User

from common.managers import JsonLoadManager


class MemberManager(JsonLoadManager):
    search_on = ("user",)

    def prepare_model(self, item):
        user_email = item.pop("email")
        user_defaults = {
            "first_name": item.pop("first_name"),
            "last_name": item.pop("last_name"),
            "email": user_email,
        }
        user, created = User.objects.get_or_create(
            username=user_email,
            defaults=user_defaults,
        )

        if not created:
            for key, value in user_defaults.items():
                if value and not getattr(user, key):
                    setattr(user, key, value)

        # user.full_clean()  # password cannot be null
        user.save()

        item["user"] = user
        return super().prepare_model(item)
