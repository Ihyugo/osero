from django import forms
from .models import OseroPanel


class OseroPanelForm(forms.ModelForm):
    class Meta:
        model = OseroPanel
        fields = '__all__'
