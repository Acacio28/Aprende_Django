from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views
from Kursu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('estudante/', include('estudante.urls')),
    path('docente/', include('docente.urls')),
    path('akademiku/', include('akademiku.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

handler404 = 'Kursu.views.handler404'
handler500 = 'Kursu.views.handler500'
