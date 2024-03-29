from django.db.models import BooleanField, TextChoices
from django.utils.translation import gettext_lazy as _


class UniqueBooleanField(BooleanField):
    """A boolean field which can be True on only one item

    Based upon: https://stackoverflow.com/a/38340608
    """

    def pre_save(self, model_instance, add):
        objects = model_instance.__class__.objects

        if not objects.exclude(id=model_instance.id).filter(**{self.attname: True}):
            # If no true object exists different from saved model, set as True
            return True

        if value := getattr(model_instance, self.attname):
            # If value is True then set all others as False
            objects.update(**{self.attname: False})

        return value


class Gender(TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")
