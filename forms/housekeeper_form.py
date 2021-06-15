from django import forms
from ..models import Housekeeper


class HousekeeperForm(forms.ModelForm):
    class Meta:
        model = Housekeeper
        fields = '__all__'