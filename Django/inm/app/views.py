# app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Periodista
from .forms import PeriodistaForm

# Estructuras básicas de redireccionamiento
def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)

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
    periodistas_listados = Periodista.objects.all()
    return render(request, 'Periodismo.html', {'Periodista': periodistas_listados})

# CRUD Views
def periodista_create(request):
    if request.method == 'POST':
        form = PeriodistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('periodismo')
    else:
        form = PeriodistaForm()
    return render(request, 'periodista_form.html', {'form': form})

def periodista_update(request, pk):
    periodista = get_object_or_404(Periodista, pk=pk)
    if request.method == 'POST':
        form = PeriodistaForm(request.POST, instance=periodista)
        if form.is_valid():
            form.save()
            return redirect('periodismo')
    else:
        form = PeriodistaForm(instance=periodista)
    return render(request, 'periodista_form.html', {'form': form})

def periodista_delete(request, pk):
    periodista = get_object_or_404(Periodista, pk=pk)
    if request.method == 'POST':
        periodista.delete()
        return redirect('periodismo')
    return render(request, 'periodista_confirm_delete.html', {'object': periodista})
