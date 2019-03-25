from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='url_home'),
    path('biblioteca/', views.libery_view, name='url_libery'),
    path('cursos/<str:pk>', views.courses_view, name='url_course'),
    path('blog/', views.blog_view, name='url_blog'),
    path('about/', views.about_view, name='url_about'),
    path('matricula/<str:curso>/<str:regime>', views.cad_view, name='url_cad_matricula')

]