from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.createUser, name = 'Create'),      # URL para rota de criação de usuários
    path('users/', views.usersList,name = 'Search'),
    path('users/<str:id>', views.getById, name = 'Find') ,  # URL para rota listar usuário pelo ID
]   

