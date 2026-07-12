from django.contrib import admin
from django.urls import path, include
from Kursu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('estudante/', include('estudante.urls')),
    path('docente/', include('docente.urls')),
    path('akademiku/', include('akademiku.urls')),
]
