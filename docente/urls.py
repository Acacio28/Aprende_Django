from django.urls import path
from docente import views

urlpatterns = [
    path('docente/', views.Lista_docente, name='lista_docente'),
    path('docente/aumenta', views.add_docente, name='add_docente'),
    path('docente/hadia/<uuid:id>', views.edit_docente, name='edit_docente'),
    path('docente/apaga/<uuid:id>', views.delete_docente, name='delete_docente'),
]