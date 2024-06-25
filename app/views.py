from django.shortcuts import render

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

