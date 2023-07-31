from django.shortcuts import render,get_object_or_404,redirect
from core.models import Categoria
from .forms import CategoriaForm

# Create your views here.

def categoria_criar(request):
    if request.method=='POST':
        form=CategoriaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('oi')
            form=CategoriaForm()

    else:
        form=CategoriaForm()
        print('oi2')
    
    return render(request,'categoria/form.html',{'form':form})

def categoria_editar(request,id):
    categoria=get_object_or_404(Categoria,id=id)
    if request.method=='POST':
        form=CategoriaForm(request.POST,request.FILES,instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_listar')
    
    else:
        form=CategoriaForm(instance=categoria)

    return render(request,'categoria/form.html',{'form':form})

def categoria_remover(request,id):
    categoria=get_object_or_404(Categoria,id=id)
    categoria.delete()
    return redirect('categoria_listar')

def categoria_listar(request):
    categorias=Categoria.objects.all()
    context={
        'categorias':categorias
    }
    return render(request,'categoria/categorias.html',context)