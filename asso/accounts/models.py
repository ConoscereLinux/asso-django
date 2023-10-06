from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password, **fields):
        """Create and save a user with the given email and password."""
        if not (email := fields.pop("email", None)):
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **fields):
        """Create and save a SuperUser with the given email and password."""
        fields.setdefault("is_staff", True)
        fields.setdefault("is_superuser", True)
        fields.setdefault("is_active", True)

        if fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **fields)


class UserMail(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="emails")
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return f"<{self.user.username}> {self.email}"


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    objects = UserManager()

    def save(self, *args, **kwargs):
        query = UserMail.objects.filter(email=self.email)
        if self.pk:
            query = query.exclude(user__id=self.id)

        if query.exists():
            raise ValueError("email already taken")

        super().save(*args, **kwargs)

        if not UserMail.objects.filter(email=self.email).exists():
            UserMail.objects.create(user=self, email=self.email)
