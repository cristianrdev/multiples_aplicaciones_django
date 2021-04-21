from django.urls import path     
from . import views
urlpatterns = [
    path('', views.ir_index),
    path('register', views.registrar),
    path('login', views.acceso),
    path('users/new', views.registrar),
    path('users', views.mostrar_usuarios),
    # path('/new', views.nuevo),	

]