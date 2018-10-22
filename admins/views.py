from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Funcionario
from home.models import Estudante, Curso, Matricula


def home(request):
    data = {}
    data['estudantes'] = Matricula.objects.select_related()
    data['user'] = request.user
    data['breadcrown'] = ['Admin']
    return render(request, 'admins/index.html', data)


def cad_funcionario(request):
    return render(request, 'admins/cad_func.html')

