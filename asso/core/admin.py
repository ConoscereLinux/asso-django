from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    """A Custom USerAdmin

    see: https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#a-full-example
    """

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", "nickname", "is_staff", "is_active", "creation_date"]
    list_filter = ["is_staff", "is_active"]

    fieldsets = [
        (None, {"fields": ["email", "nickname", "password"]}),
        ("Permissions", {"fields": ["is_staff", "is_active", "groups"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "creation_date", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)  # uncomment to disable groups


def _add_fields(
    model: admin.ModelAdmin | admin.TabularInline,
    attribute: str,
    fields: tuple,
) -> tuple:
    """Add fields to an attribute of a ModelAdmin mantaining user defined ones."""
    _fields = getattr(model, attribute, None)
    if _fields is None:
        _fields = tuple()

    for field in fields:
        if field not in _fields:
            _fields += (field,)

    setattr(model, attribute, _fields)

    return _fields


class CreatedAdmin(admin.ModelAdmin):
    """An abstract Admin model to mamage Model which subclass Created.

    Based upon:
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    """

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("created_by",))
        super().__init__(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class CreatedTabularInline(admin.TabularInline):
    """An abstract Admin model to mamage Model with Created enabled.

    Based upon:
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    """

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("created_by",))
        super().__init__(*args, **kwargs)


class EditableAdmin(admin.ModelAdmin):
    """An abstract Admin model to mamage Model which subclass Editable.

    Based upon:
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    """

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("edit_by",))
        super().__init__(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.edit_by = request.user
        super().save_model(request, obj, form, change)


class EditableTabularInline(admin.TabularInline):
    """An abstract Admin model to mamage Model with Editable enabled.

    Based upon:
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    """

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("edit_by",))
        super().__init__(*args, **kwargs)


class TrashableAdmin(admin.ModelAdmin):
    """An abstract Admin model to mamage Model with EditInfo enabled."""

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("is_trashed",))
        _add_fields(self, "list_filter", ("is_trashed",))
        super().__init__(*args, **kwargs)
