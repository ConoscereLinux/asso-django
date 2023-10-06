from django.contrib import admin

from .models import User, UserMail

admin.site.register(User)
admin.site.register(UserMail)


# class UserMailAdmin()


# @admin.register(User)
# class UserAdmin(django.contrib.auth.admin.UserAdmin):
#     """A Custom UserAdmin using email instead of username
#
#     see: https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#a-full-example
#     see: https://testdriven.io/blog/django-custom-user-model/
#     """
#
#     list_display = [
#         "email",
#         "username",
#         "first_name",
#         "last_name",
#         "is_staff",
#         "is_superuser",
#         "last_login",
#     ]
#
#     list_filter = ["is_staff", "is_superuser"]
#     search_fields = ["email", "first_name", "last_name", "username"]
#     ordering = ["email"]
#
#     form = UserUpdateForm
#     add_form = UserCreateForm
#
#     add_fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": [
#                     "email",
#                     "username",
#                     "first_name",
#                     "last_name",
#                     "password1",
#                     "password2",
#                 ],
#             },
#         ),
#     ]
