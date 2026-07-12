from django.contrib import admin
from django.urls import path, include
from Kursu.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('estudante/', include('estudante.urls')),
    path('docente/', include('docente.urls')),
    path('akademiku/', include('akademiku.urls')),
]
