from django.urls import path
from .views import register_housekeeper, list_housekeepers, edit_housekeeper

# definição das rotas do projeto

urlpatterns = [
    path('register_housekeeper', register_housekeeper, name='register_housekeeper'),
    path('list_housekeepers', list_housekeepers, name='list_housekeepers'),
    path('edit_housekeeper/<int:housekeeper_id>', edit_housekeeper, name='edit_housekeeper')
]
