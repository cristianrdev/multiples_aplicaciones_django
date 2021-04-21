from django.urls import path     
from . import views
urlpatterns = [
    path('', views.mostrar),
    path('/new', views.nuevo),	

]