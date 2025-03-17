from django import forms
from .models import Post, Autor, Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class BuscarForm(forms.Form):
    termino = forms.CharField(label="Buscar", max_length=100)
