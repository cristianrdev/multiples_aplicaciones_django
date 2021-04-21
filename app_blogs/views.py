from django.shortcuts import render, HttpResponse, redirect


def indice(request):
    return HttpResponse("marcador de posición para luego mostrar una lista de todos los blogs")

def nuevo(request):
    return HttpResponse("marcador de posición para mostrar un nuevo formulario para crear un nuevo blog")

def crear(request):
    return redirect('/blogs')

def show(request, numero):
    return HttpResponse(f"marcador de posición para mostrar el número de blog: {numero}")

def editar(request, numero):
    return HttpResponse(f"marcador de posición para editar el blog {numero}")

def destruir(request, numero):
    return redirect('/blogs')

# Create your views here.
