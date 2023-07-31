from django.forms import ModelForm
from django import forms
from core.models import Categoria

class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
      
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
        }
