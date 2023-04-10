from django.shortcuts import render
from helloword.models import Funcionario
from django.views.generic import ListView

class ListaFuncionarios(ListView):
    template_name = "templates/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"


