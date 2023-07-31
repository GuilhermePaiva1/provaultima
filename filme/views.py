from django.shortcuts import render,get_object_or_404,redirect
from core.models import Filme
from .forms import FilmeForm

# Create your views here.

def filme_criar(request):
    if request.method=='POST':
        form=FilmeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=FilmeForm()

    else:
        form=FilmeForm()
    
    return render(request,'filme/form.html',{'form':form})

def filme_editar(request,id):
    filme=get_object_or_404(Filme,id=id)
    if request.method=='POST':
        form=FilmeForm(request.POST,request.FILES,instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filme_listar')
    
    else:
        form=FilmeForm(instance=filme)

    return render(request,'filme/form.html',{'form':form})

def filme_remover(request,id):
    filme=get_object_or_404(Filme,id=id)
    filme.delete()
    return redirect('filme_listar')

def filme_listar(request):
    filmes=Filme.objects.all()
    context={
        'filmes':filmes
    }
    return render(request,'filme/filmes.html',context)