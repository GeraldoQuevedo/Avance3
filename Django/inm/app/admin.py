# En tu_app/admin.py
from django.contrib import admin
from .models import Periodista ,Producto, Carrito

admin.site.register(Periodista)
admin.site.register(Producto)
admin.site.register(Carrito)