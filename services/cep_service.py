import requests


def get_city_cep(cep):
    # captura a resposta da requisição à API do ViaCep
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    return response
