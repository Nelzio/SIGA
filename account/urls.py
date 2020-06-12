from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.account, name='url_account'),
    path('', views.login_view, name='url_account'),
    path('create/', views.create_account, name='url_create_account'),
    path('login/', views.login_view, name='url_login'),
    path('logout/', views.logout_view, name='url_logout'),
    # path('compra/<int:pk>/', views.cad_compra, name='url_cad_cliente'),
]