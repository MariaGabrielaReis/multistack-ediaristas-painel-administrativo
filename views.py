from django.shortcuts import render
from .forms import housekeeper_form


def register_housekeeper(request):
    if request.method == 'POST':
        # se a requisição for para envio de dados, ele vê se a resposta do form é valida e depois salva os dados
        form_housekeeper = housekeeper_form.HousekeeperForm(request.POST, request.FILES)
        if form_housekeeper.is_valid():
            form_housekeeper.save()
    else:
        # se não for para cadastrar, só envia o formulário para ser preenchido
        form_housekeeper = housekeeper_form.HousekeeperForm()
    return render(request, 'form_housekeeper.html', {'form_housekeeper': form_housekeeper})
