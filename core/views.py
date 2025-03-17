from django.shortcuts import render, get_object_or_404
from .models import Post, Autor, Categoria
from .forms import PostForm, AutorForm, CategoriaForm, BuscarForm

def inicio(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', {'posts': posts})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Crear Post'})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

def buscar_post(request):
    resultados = []
    if request.method == 'GET' and 'termino' in request.GET:
        form = BuscarForm(request.GET)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            resultados = Post.objects.filter(titulo__icontains=termino)
    else:
        form = BuscarForm()
    return render(request, 'core/busqueda.html', {'form': form, 'resultados': resultados})
