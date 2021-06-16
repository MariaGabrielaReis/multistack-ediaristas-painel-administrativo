from django import forms
from ..models import Housekeeper


class HousekeeperForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000.000.000-00'}))
    address_cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00000-000'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))

    class Meta:
        model = Housekeeper
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        return cpf.replace('.', '').replace('-', '')

    def clean_address_cep(self):
        address_cep = self.cleaned_data['address_cep']
        return address_cep.replace('-', '')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        return phone_number.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
