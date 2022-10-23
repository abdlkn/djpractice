#add view name to create url

from django.urls import path
from .views import get_employee_data

urlpatterns = [
 #   path('home/', display),
    path('get_data/',get_employee_data)
    ]