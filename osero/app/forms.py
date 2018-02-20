from django import forms
from .models import OseroPanel


class OseroPanelForm(forms.ModelForm):
    class Meta:
        model = OseroPanel
        fields = '__all__'

Choices= {
    ('CPU','CPU'),
    ('Human','Human'),

}



class Players(forms.Form):
    style = forms.ChoiceField(
        label='which',
        widget=forms.RadioSelect,
        choices=Choices,
        required=True,)
