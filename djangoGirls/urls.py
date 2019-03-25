from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='url_django'),
    path('post/<int:pk>', views.post, name='url_post'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/',	views.post_edit, name='post_edit'),
]