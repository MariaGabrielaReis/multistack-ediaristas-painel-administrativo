import json

from django import forms
from ..models import Housekeeper
from ..services import cep_service


class HousekeeperForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000.000.000-00'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00000-000'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))

    class Meta:
        model = Housekeeper
        exclude = ('codigo_ibge', 'logradouro', 'bairro', 'cidade', 'estado', )

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        return cpf.replace('.', '').replace('-', '')

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        format_cep = cep.replace('-', '')
        response = cep_service.get_city_cep(format_cep)
        if response.status_code == 400:
            raise forms.ValidationError('CEP inválido')
        city_api = json.loads(response.content)
        if 'erro' in city_api:
            raise forms.ValidationError('CEP não encontrado')
        return cep.replace('-', '')

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        return telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

    def save(self, commit=True):
        # alterando o comportamento do método save
        instance = super(HousekeeperForm, self).save(commit=False)
        response = cep_service.get_city_cep(self.cleaned_data.get('cep'))
        city_api = json.loads(response.content)
        # capturando o código do IBGE da API e colocando na instância
        instance.codigo_ibge = city_api['ibge']
        instance.logradouro = city_api['logradouro']
        instance.bairro = city_api['bairro']
        instance.cidade = city_api['localidade']
        instance.estado = city_api['uf']
        instance.save()
        return instance
