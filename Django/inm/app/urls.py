from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', views.inicio, name='inicio'),
    path('noticia1/', views.noticia1, name='noticia1'),
    path('noticia2/', views.noticia2, name='noticia2'),
    path('noticia3/', views.noticia3, name='noticia3'),
    path('proyecto1/', views.proyecto1, name='proyecto1'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
    path('tiempo/', views.tiempo, name='tiempo'),
    path('periodismo/', views.periodismo, name='periodismo'),
    path('periodista/create/', views.periodista_create, name='periodista_create'),
    path('periodista/<int:pk>/update/', views.periodista_update, name='periodista_update'),
    path('periodista/<int:pk>/delete/', views.periodista_delete, name='periodista_delete'),
    path('login/', views.iniciar_sesion, name='login'),
    path('productos/', views.productos_view, name='productos'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='add_to_cart'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:carrito_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
