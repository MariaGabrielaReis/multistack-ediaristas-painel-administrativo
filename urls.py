from django.urls import path
from .views import register_housekeeper

urlpatterns = [
    path('register_housekeeper', register_housekeeper, name='register_housekeeper')
]
