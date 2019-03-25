from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='url_home_admin'),
    path('cadastro/funcionario', views.cad_funcionario, name='url_cad_func_admin')
]