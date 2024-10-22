from django.urls import path
from .views import client_list, create_client, update_client, delete_client

urlpatterns = [
    path('', client_list, name='client-list'),
    path('create/', create_client, name='client-create'),
    path('<int:pk>/edit/', update_client, name='client-edit'),
    path('<int:pk>/delete/', delete_client, name='client-delete'),
]
