from django.shortcuts import render, HttpResponse, redirect
def ir_index(request):
    return HttpResponse('Usuarios')

def registrar(request):
    return HttpResponse("marcador de posición para que los usuarios creen un nuevo registro de usuario")

def acceso(request):
    return HttpResponse("marcador de posición para que los usuarios inicien sesión")
def mostrar_usuarios(request):
    return HttpResponse("marcador de posición para luego mostrar toda la lista de usuarios")