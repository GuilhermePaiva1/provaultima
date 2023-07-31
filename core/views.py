from django.shortcuts import render,get_object_or_404,redirect
from .models import Filme

# Create your views here.
def index(request):
    filmes=Filme.objects.all()
    context={
        'filmes':filmes
    }
    return render(request, 'core/index.html',context)

# Create your views here.
# def cadastro(request):
#     return render(request, 'core/form.html')

# def lista(request):
#     return render(request, 'core/lista.html')

#teste
def detalhe_filme(request,id):
    filmes=get_object_or_404(Filme,id=id)
    context={
        'filmes':filmes
    }
    return render(request, 'core/detalhe.html',context)