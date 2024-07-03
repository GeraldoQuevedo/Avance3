# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticia1/', views.noticia1, name='noticia1'),
    path('noticia2/', views.noticia2, name='noticia2'),
    path('noticia3/', views.noticia3, name='noticia3'),
    path('proyecto1/', views.proyecto1, name='proyecto1'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
    path('tiempo/', views.tiempo, name='tiempo'),
    path('periodismo/', views.periodismo, name='periodismo'),
    path('periodista/create/', views.periodista_create, name='periodista_create'),
    path('periodista/update/<str:pk>/', views.periodista_update, name='periodista_update'),
    path('periodista/delete/<str:pk>/', views.periodista_delete, name='periodista_delete'),
]
