from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"