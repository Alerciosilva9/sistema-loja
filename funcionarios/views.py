from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario
# Create your views here.


def hello(request):

    funcionarios = Funcionario.objetos.all()

    for funcionario in funcionarios:
        print("THS")
        print(funcionario)

    


    contexto = {
        'funcionarios':funcionarios
    }
        
    
    return render(request,"funcionarios/index.html",contexto)
