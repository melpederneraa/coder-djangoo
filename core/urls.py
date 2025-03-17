from django.urls import path
from .views import inicio, crear_post, crear_autor, crear_categoria, buscar_post

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-post/', crear_post, name='crear_post'),
    path('crear-autor/', crear_autor, name='crear_autor'),
    path('crear-categoria/', crear_categoria, name='crear_categoria'),
    path('buscar/', buscar_post, name='buscar'),
]
