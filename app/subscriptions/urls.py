from django.urls import path
from .views import (get_config, create_customer)

urlpatterns = [
    path('config/', get_config),
    path('create-customer/', create_customer),
]
