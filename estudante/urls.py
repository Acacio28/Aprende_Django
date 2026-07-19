from django.urls import path
from estudante import views

urlpatterns =[
    path('',views.Lista_estudante,name='lista'),
    path('aumenta',views.add_estudante,name='add'),
    path('hadia/<uuid:id>',views.edit_estudante,name='edit'),
    path('apaga/<uuid:id>',views.delete_estudante,name='delete')
]
path('detail/<uuid:id>', views.detail_estudante, name='detail_estudante'),
