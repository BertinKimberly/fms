from django.urls import path
from .views import freelancer_list, create_freelancer, update_freelancer, delete_freelancer

urlpatterns = [
    path('', freelancer_list, name='freelancer-list'),
    path('create/', create_freelancer, name='freelancer-create'),
    path('<int:pk>/edit/', update_freelancer, name='freelancer-edit'),
    path('<int:pk>/delete/', delete_freelancer, name='freelancer-delete'),
]
