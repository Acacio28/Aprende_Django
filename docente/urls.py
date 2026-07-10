from django.urls import path
from docente import views

urlpatterns = [
    path('', views.Lista_docente, name='lista_docente'),
    path('aumenta', views.add_docente, name='add_docente'),
    path('hadia/<uuid:id>', views.edit_docente, name='edit_docente'),
    path('apaga/<uuid:id>', views.delete_docente, name='delete_docente'),
]
