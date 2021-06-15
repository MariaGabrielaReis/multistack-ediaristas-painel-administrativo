from django.shortcuts import render
from .forms import housekeeper_form


def register_housekeeper(request):
    form_housekeeper = housekeeper_form.HousekeeperForm()
    return render(request, 'form_housekeeper.html', {'form_housekeeper': form_housekeeper})
