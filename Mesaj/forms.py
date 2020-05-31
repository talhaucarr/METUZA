from django import forms

from .models import Msg


class MsgForm(forms.ModelForm):
    class Meta:
        model = Msg
        fields = ["username", "msg_content", "files"]
