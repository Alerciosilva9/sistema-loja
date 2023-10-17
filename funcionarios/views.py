from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Funcionario
# Create your views here.


@login_required
def listar(request):
    funcionarios = Funcionario.objetos.all()

    contexto = {
        'currentuser':request.user,
        'funcionarios':funcionarios
    }
        
    
    return render(request,"funcionarios/index.html",contexto)
