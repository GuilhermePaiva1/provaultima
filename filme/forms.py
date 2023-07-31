from django.forms import ModelForm
from django import forms
from core.models import Filme

class FilmeForm(ModelForm):

    class Meta:
        model = Filme
        fields = '__all__'
      
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'sinopse' : forms.TextInput(attrs={'class': 'form-control' }),
            'data_lancamento' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria' : forms.Select(attrs={'class': 'form-control' }),
        }
