from django.http import HttpResponse
from django.shortcuts import render

def saludar (request):
    return HttpResponse('Hola desde Django')
def saludar_con_etiqueta(request):
    return HttpResponse('<h1> Hola con etiquetas</h1>')
def saludar_con_parametros(request,nombre:str,apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(F"HOLA {nombre} {apellido} ")
def index(request):
    from datetime import datetime 
    anio_actual = datetime.now().year
    contexto ={"anio":anio_actual}
    return render(request,"core/index.html",contexto)