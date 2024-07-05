from django.shortcuts import render, redirect, get_object_or_404  # Importa funciones para renderizar vistas, redireccionar y obtener objetos o retornar 404
from django.contrib.auth import authenticate, login, logout  # Importa funciones para autenticar usuarios, iniciar sesión y cerrar sesión
from django.contrib import messages  # Importa messages para gestionar mensajes de error
from .models import Periodista, Producto, Carrito  # Importa los modelos Periodista, Producto y Carrito desde la aplicación actual
from .forms import PeriodistaForm  # Importa el formulario PeriodistaForm desde forms.py en la aplicación actual
from django.http import JsonResponse  # Importa JsonResponse para devolver respuestas JSON
from django.contrib.auth.decorators import login_required  # Importa el decorador login_required para requerir autenticación

def logout_view(request):
    """
    Vista para cerrar sesión de usuario.
    """
    logout(request)  # Cierra la sesión del usuario actual
    return redirect('inicio')  # Redirige al usuario a la página de inicio

@login_required
def agregar_al_carrito(request, producto_id):
    """
    Vista para agregar un producto al carrito.
    """
    producto = get_object_or_404(Producto, id=producto_id)  # Obtiene el producto con el ID dado, o devuelve 404 si no existe
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user, producto=producto)  # Obtiene o crea un carrito para el usuario actual y el producto dado
    if not creado:
        carrito.cantidad += 1  # Incrementa la cantidad si el carrito ya existía
    carrito.save()  # Guarda el carrito actualizado en la base de datos
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'message': 'Producto agregado al carrito'})  # Devuelve una respuesta JSON si la solicitud fue mediante AJAX
    else:
        messages.success(request, 'Producto agregado correctamente al carrito de compras.')  # Muestra un mensaje de éxito si se agregó el producto al carrito
        return redirect('productos_view')  # Redirige a la vista de productos

@login_required
def ver_carrito(request):
    """
    Vista para mostrar el contenido del carrito de compras.
    """
    carrito_items = Carrito.objects.filter(usuario=request.user)  # Filtra los ítems del carrito por el usuario actual
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)  # Calcula el total de la compra
    return render(request, 'ver_carrito.html', {'carrito_items': carrito_items, 'total': total})  # Renderiza la plantilla ver_carrito.html con los datos del carrito y el total

@login_required
def eliminar_del_carrito(request, carrito_id):
    """
    Vista para eliminar un ítem del carrito de compras.
    """
    carrito = get_object_or_404(Carrito, id=carrito_id)  # Obtiene el ítem del carrito con el ID dado, o devuelve 404 si no existe
    carrito.delete()  # Elimina el ítem del carrito de la base de datos
    return redirect('ver_carrito')  # Redirige de vuelta a la página del carrito después de eliminar el ítem

@login_required
def lista_productos(request):
    """
    Vista para mostrar todos los productos disponibles.
    """
    productos = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'productos.html', {'productos': productos})  # Renderiza la plantilla productos.html con la lista de productos

@login_required
def productos_view(request):
    """
    Vista para mostrar todos los productos disponibles (otra variante).
    """
    productos = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'productos.html', {'productos': productos})  # Renderiza la plantilla productos.html con la lista de productos


# Vistas básicas de redireccionamiento
def inicio(request):
    """
    Vista para la página de inicio.
    """
    context = {}  # Define un contexto vacío
    return render(request, 'inicio.html', context)  # Renderiza la plantilla inicio.html con el contexto

# Otras vistas para diferentes secciones (noticias, proyecto, suscripción, tiempo, etc.) no necesitan comentarios detallados, son vistas simples de renderización de plantillas.

def noticia1(request):
    context = {}
    return render(request, 'noticia1.html', context)

def noticia2(request):
    context = {}
    return render(request, 'noticia2.html', context)

def noticia3(request):
    context = {}
    return render(request, 'noticia3.html', context)

def proyecto1(request):
    context = {}
    return render(request, 'proyecto1.html', context)

def suscribirse(request):
    context = {}
    return render(request, 'suscribirse.html', context)

def tiempo(request):
    context = {}
    return render(request, 'tiempo.html', context)

def periodismo(request):
    """
    Vista para mostrar la lista de periodistas.
    """
    periodistas_listados = Periodista.objects.all()  # Obtiene todos los periodistas de la base de datos
    return render(request, 'Periodismo.html', {'periodistas_listados': periodistas_listados})  # Renderiza la plantilla Periodismo.html con la lista de periodistas

# Vistas CRUD para el modelo Periodista
def periodista_create(request):
    """
    Vista para crear un nuevo periodista.
    """
    if request.method == 'POST':
        form = PeriodistaForm(request.POST)  # Crea un formulario PeriodistaForm con los datos del POST
        if form.is_valid():  # Valida el formulario
            form.save()  # Guarda el nuevo periodista en la base de datos
            return redirect('periodismo')  # Redirige a la vista de periodismo después de guardar
    else:
        form = PeriodistaForm()  # Crea un formulario vacío para mostrar en GET
    return render(request, 'periodista_form.html', {'form': form})  # Renderiza la plantilla periodista_form.html con el formulario

def periodista_update(request, pk):
    """
    Vista para actualizar un periodista existente.
    """
    periodista = get_object_or_404(Periodista, pk=pk)  # Obtiene el periodista con el ID dado, o devuelve 404 si no existe
    if request.method == 'POST':
        form = PeriodistaForm(request.POST, instance=periodista)  # Crea un formulario PeriodistaForm con los datos del POST y la instancia del periodista
        if form.is_valid():  # Valida el formulario
            form.save()  # Guarda los cambios del periodista en la base de datos
            return redirect('periodismo')  # Redirige a la vista de periodismo después de actualizar
    else:
        form = PeriodistaForm(instance=periodista)  # Crea un formulario con la instancia del periodista para mostrar en GET
    return render(request, 'periodista_form.html', {'form': form})  # Renderiza la plantilla periodista_form.html con el formulario

def periodista_delete(request, pk):
    """
    Vista para eliminar un periodista existente.
    """
    periodista = get_object_or_404(Periodista, pk=pk)  # Obtiene el periodista con el ID dado, o devuelve 404 si no existe
    if request.method == 'POST':
        periodista.delete()  # Elimina el periodista de la base de datos
        return redirect('periodismo')  # Redirige a la vista de periodismo después de eliminar
    return render(request, 'periodista_confirm_delete.html', {'object': periodista})  # Renderiza la plantilla periodista_confirm_delete.html con el objeto periodista

def iniciar_sesion(request):
    """
    Vista para iniciar sesión de usuario.
    """
    if request.method == 'POST':
        username = request.POST['username']  # Obtiene el nombre de usuario del formulario POST
        password = request.POST['password']  # Obtiene la contraseña del formulario POST
        user = authenticate(request, username=username, password=password)  # Autentica al usuario con las credenciales proporcionadas
        if user is not None:
            login(request, user)  # Inicia sesión para el usuario autenticado
            return redirect('periodismo')  # Redirige al usuario a la vista de periodismo después del inicio de sesión
        else:
            # Muestra un mensaje de error si las credenciales son incorrectas
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return render(request, 'inicio.html')  # Renderiza la plantilla de inicio con un mensaje de error
    else:
        return render(request, 'inicio.html')  # Renderiza la plantilla de inicio para solicitudes GET
