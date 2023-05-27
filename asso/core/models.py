"""Base models for other application."""

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ordered(models.Model):
    """A Model with a field for custom ordering."""

    order = models.SmallIntegerField(
        default=0,
        null=False,
        blank=False,
        verbose_name=_("Order"),
        help_text=_("Object ordering value"),
    )

    class Meta:
        abstract = True
        ordering = ["order"]


class Created(models.Model):
    """A Model with field for creation date and user"""

    creation_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_("Creation Date and Time"),
        help_text=_("Date and Time of object's creation"),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created_by",
        blank=True,
        null=True,
        verbose_name=_("Creation User"),
        help_text=_("The User who has created this object"),
    )

    class Meta:
        abstract = True
        ordering = ["-creation_date"]


class Editable(models.Model):
    """A Model with field for last edit date and user"""

    edit_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name=_("Last edit Date and Time"),
        help_text=_("Date and Time of object's last edit"),
    )

    edit_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updated_by",
        blank=True,
        null=True,
        verbose_name=_("Last edit User"),
        help_text=_("The User who last edited this object"),
    )

    class Meta:
        abstract = True
        ordering = ["-edit_date"]


class Trashable(models.Model):
    """A Model for trashable objects"""

    is_trashed = models.BooleanField(
        default=False,
        verbose_name=_("Trashed"),
        help_text=_("Is the object trashed"),
    )

    class Meta:
        abstract = True


class Activable(models.Model):
    """A Model for activable objects"""

    active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Is the object active"),
    )

    class Meta:
        abstract = True


class Descripted(models.Model):
    title = models.CharField(max_length=256, default="", verbose_name=_("Title"))
    description = models.TextField(
        default="",
        blank=True,
        verbose_name=_("Description"),
        help_text=_("object description"),
    )

    class Meta:
        abstract = True
        ordering = ["title"]


class Common(Descripted, Editable, Created):
    class Meta:
        abstract = True
        ordering = Created.Meta.ordering


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Creates and saves a User with the given email and password."""

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)

    nickname = models.CharField(_("Nickname"), max_length=256, blank=True)

    # first_name = models.CharField(_("first name"), max_length=30, blank=True)
    # last_name = models.CharField(_("last name"), max_length=30, blank=True)
    # avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    creation_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_("Creation Date"),
        help_text=_("Date and Time of user creation"),
    )

    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("Staff member"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["is_staff"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        return self.nickname if self.nickname else self.email

    def get_short_name(self):
        return self.nickname if self.nickname else self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this User"""
        send_mail(subject, message, from_email, [self.email], **kwargs)
