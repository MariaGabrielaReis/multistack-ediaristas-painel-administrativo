from django.shortcuts import render, redirect
from .forms import housekeeper_form
from .models import Housekeeper

def register_housekeeper(request):
    if request.method == 'POST':
        # se a requisição for para envio de dados, ele vê se a resposta do form é valida e depois salva os dados
        form_housekeeper = housekeeper_form.HousekeeperForm(request.POST, request.FILES)
        if form_housekeeper.is_valid():
            form_housekeeper.save()
            return redirect('list_housekeepers')
    else:
        # se não for para cadastrar, só envia o formulário para ser preenchido
        form_housekeeper = housekeeper_form.HousekeeperForm()
    return render(request, 'form_housekeeper.html', {'form_housekeeper': form_housekeeper})


def list_housekeepers(request):
    housekeepers = Housekeeper.objects.all()
    return render(request, 'housekeepers_list.html', {'housekeepers': housekeepers})


def edit_housekeeper(request, housekeeper_id):
    housekeeper = Housekeeper.objects.get(id = housekeeper_id)
    form_housekeeper = housekeeper_form.HousekeeperForm(request.POST or None, instance=housekeeper)
    if form_housekeeper.is_valid():
        form_housekeeper.save()
        return redirect('list_housekeepers')
    return render(request, 'form_housekeeper.html', {'form_housekeeper': form_housekeeper})
