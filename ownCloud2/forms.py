from django import forms

from .models import Cloud


class CloudForm(forms.ModelForm):
    class Meta:
        model = Cloud
        fields = ('title', 'pdf')
