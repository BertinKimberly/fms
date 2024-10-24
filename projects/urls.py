from django.urls import path
from .views import project_list,create_project,update_project,delete_project

urlpatterns = [
    path('', project_list, name='project-list'),
    path('create/', create_project, name='project-create'),
    path('<int:pk>/edit/', update_project, name='project-edit'),
    path('<int:pk>/delete/', delete_project, name='project-delete'),
]
