from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Funcionario
from django.core.paginator import Paginator
from . import forms
# Create your views here.


@login_required
def listar(request):
    funcionarios = Funcionario.objetos.all()
    formulario = forms.Formulario()
    usuario_paginator = Paginator(funcionarios,5)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)

    contexto = {
        'page':page,
        'form':formulario
    }
        
    
    return render(request,"funcionarios/index.html",contexto)



##@login_required
def cadastrar(request):
    funcionario = Funcionario()

    if(request.method == 'POST'):

        form = forms.Formulario(request.POST)
        if(form.is_valid):
            funcionario.nome = request.POST.get('nome')
            funcionario.sobrenome = request.POST.get('sobrenome')
            funcionario.cpf = request.POST.get('cpf')
            funcionario.tempo_de_servico = request.POST.get('tempo_de_servico')
            funcionario.remuneracao = request.POST.get('remuneracao')
            funcionario.save()
        
        
    return HttpResponseRedirect(reverse('listar'))

def buscar(request):
    
    if(request.GET.get('nome') == ""):
        funcionarios = Funcionario.objetos.all()
    else:
        funcionarios = Funcionario.objetos.filter(nome__icontains=request.GET.get('nome')).all()

    print(request.GET.get('nome'))
    usuario_paginator = Paginator(funcionarios,5)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)

    contexto = {
        'page':page,
    }
        
    
    return render(request,"funcionarios/buscar.html",contexto)