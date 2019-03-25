from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Funcionario
from home.models import Estudante, Curso, Matricula


@login_required
def home(request):
    data = {}
    data['estudantes'] = Matricula.objects.select_related()
    data['user'] = request.user
    data['breadcrown'] = ['Admin']
    return render(request, 'admins/index.html', data)


@login_required
def cad_funcionario(request):
    return render(request, 'admins/cad_func.html')

