from django.urls import path
from .views import register_housekeeper, list_housekeepers

# definição das rotas do projeto

urlpatterns = [
    path('register_housekeeper', register_housekeeper, name='register_housekeeper'),
    path('list_housekeepers', list_housekeepers, name='list_housekeepers')
]
