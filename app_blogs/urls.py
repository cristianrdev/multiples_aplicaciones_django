from django.urls import path     
from . import views
urlpatterns = [
    path('', views.indice),
    path('/new', views.nuevo),
    path('/create', views.crear),
    path('/<numero>', views.show),
    path('/<numero>/edit', views.editar),
    path('/<numero>/delete', views.destruir)  
]



