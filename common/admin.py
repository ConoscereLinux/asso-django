from django.contrib import admin


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


class EditInfoAdmin(admin.ModelAdmin):
    """An abstract Admin model to mamage Model with EditInfo enabled.

    Based upon:
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    """

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("created_by", "updated_by"))
        super().__init__(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class EditInfoTabularInline(admin.TabularInline):
    """An abstract Admin model to mamage Model with EditInfo enabled.

    Based upon:
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    """

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("created_by", "updated_by"))
        super().__init__(*args, **kwargs)


class TrashBinAdmin(admin.ModelAdmin):
    """An abstract Admin model to mamage Model with EditInfo enabled."""

    def __init__(self, *args, **kwargs):
        _add_fields(self, "exclude", ("trash_state",))
        _add_fields(self, "list_filter", ("trash_state",))
        super().__init__(*args, **kwargs)
