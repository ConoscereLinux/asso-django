from django.contrib import admin

from .models import User, UserMail

admin.site.register(User)
admin.site.register(UserMail)
