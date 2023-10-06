from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
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

    @staticmethod
    def is_available(email: str):
        """Check if email is available"""
        return not UserMail.objects.filter(email=email).exists()

    @staticmethod
    def is_registered(email, exclude: "User"):
        """Check if email is already registered (excluded given user)"""
        return UserMail.objects.filter(email=email).exclude(user=exclude).exists()

    def __str__(self):
        return f"<{self.user.username}> {self.email}"

    class Meta:
        verbose_name = _("User Email")
        verbose_name_plural = _("User Emails")


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    objects = UserManager()

    def clean(self):
        if UserMail.is_registered(self.email, exclude=self):
            raise ValidationError(
                _("Email %(email)s is already used by another user"),
                params={"email": self.email},
            )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if UserMail.is_available(self.email):
            UserMail.objects.create(user=self, email=self.email)
