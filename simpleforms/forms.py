from django import forms

from .models import Director, Filial, News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        exclude = ["views"]


    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(DirectorForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"