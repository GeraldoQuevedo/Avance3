from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # URL simple
    path('noticia1/', views.noticia1, name='noticia1'),
    path('noticia2/', views.noticia2, name='noticia2'),
    path('noticia3', views.noticia3, name='noticia3'),
    path('proyecto1/', views.proyecto1, name='proyecto1'),
    path('suscribirse', views.suscribirse, name='suscribirse'),
    path('tiempo', views.tiempo, name='tiempo'),    
]
