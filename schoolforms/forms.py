from django import forms
from django.db import models
from django.forms import fields

from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"