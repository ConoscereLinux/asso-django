from django import forms

from . import models


class EnrollForm(forms.ModelForm):
    class Meta:
        model = models.Enrollment
        fields = "__all__"
        initial = {"event": 1}
        widgets = {"event": forms.HiddenInput()}
