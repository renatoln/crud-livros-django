from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.livro_list, name='livro_list'),
    path('livro/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livro/new', views.livro_new, name='livro_new'),
    path('livro/<int:pk>/edit/', views.livro_edit, name='livro_edit'),
    path('livro/<int:pk>/delete/', views.livro_delete, name='livro_delete'),
]
