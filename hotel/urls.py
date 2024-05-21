from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),         # Inclui as urls do app blog
    path('quartos', views.quartos, name="quartos"), # Inclui as urls do app blog
    path('reservas', views.reservas, name='reservas'),
    path('cadastro_usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]