from django.urls import path
from akademiku import views

urlpatterns = [
    path('turma/', views.Lista_turma, name='lista_turma'),
    path('turma/aumenta', views.add_turma, name='add_turma'),
    path('turma/hadia/<uuid:id>', views.edit_turma, name='edit_turma'),
    path('turma/apaga/<uuid:id>', views.delete_turma, name='delete_turma'),
    path('disciplina/', views.Lista_disciplina, name='lista_disciplina'),
    path('disciplina/aumenta', views.add_disciplina, name='add_disciplina'),
    path('disciplina/hadia/<uuid:id>', views.edit_disciplina, name='edit_disciplina'),
    path('disciplina/apaga/<uuid:id>', views.delete_disciplina, name='delete_disciplina'),
    path('avaliasaun/', views.Lista_avaliasaun, name='lista_avaliasaun'),
    path('avaliasaun/aumenta', views.add_avaliasaun, name='add_avaliasaun'),
    path('avaliasaun/hadia/<uuid:id>', views.edit_avaliasaun, name='edit_avaliasaun'),
    path('avaliasaun/apaga/<uuid:id>', views.delete_avaliasaun, name='delete_avaliasaun'),
]
