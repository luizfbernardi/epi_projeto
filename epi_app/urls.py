from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),

    path('inserir_colaborador/', views.inserir_colaborador, name='inserir_colaborador'),
    path('listar_colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    path('atualizar_colaborador/<int:id>', views.atualizar_colaborador, name='atualizar_colaborador'),
    path('excluir_colaborador/<int:id>', views.excluir_colaborador, name='excluir_colaborador'),

    path('inserir_epi/', views.inserir_epi, name='inserir_epi'),
    path('listar_epis/', views.listar_epis, name='listar_epis'),
    path('atualizar_epi/<int:id>', views.atualizar_epi, name='atualizar_epi'),
    path('excluir_epi/<int:id>', views.excluir_epi, name='excluir_epi'),
    path('inserir_emprestimo/', views.inserir_emprestimo, name='inserir_emprestimo'),
]
