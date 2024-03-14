from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_administrador/', views.login_administrador, name='login_administrador'),
    path('equipos/', views.equipos, name='equipos'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('base_paises/', views.base_pais, name='base_paises'),
    path("equipos/<str:nombre_equipo>", views.detalle_equipo, name="equipo"),
]
