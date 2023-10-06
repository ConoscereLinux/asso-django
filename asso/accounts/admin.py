from django.contrib import admin

from .models import User, UserEmail

admin.site.register(User)
admin.site.register(UserEmail)
