from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from Kursu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('estudante/', include('estudante.urls')),
    path('docente/', include('docente.urls')),
    path('akademiku/', include('akademiku.urls')),
]

handler404 = 'Kursu.views.handler404'
handler500 = 'Kursu.views.handler500'
