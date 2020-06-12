from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Curso, Estudante, Contacto, Disciplina, Endereco, Matricula
from .forms import ContactoModelForm, EnderecoModelForm, EstudanteModelForm


def caps_no_space(value):
    list_value = value.split(" ")
    val = ""
    for v in list_value:
        if v != v.lower():
            val = val + v[0]
    return val

# @login_required
def home(request):
    data = {}
    data['boxes'] = ['1', '2', '3']
    data['listes'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    data['cursos'] = Curso.objects.all()
    return render(request, 'home/index.html', data)


# @login_required
def libery_view(request):
    return render(request, 'home/libery.html')


# @login_required
def courses_view(request, pk):
    data = dict()
    data['cursos'] = Curso.objects.all()
    for c in data['cursos']:
        if pk == caps_no_space(c.nome):
            data['curso'] = Curso.objects.get(nome=c.nome)
    return render(request, 'home/courses.html', data)


# @login_required
def blog_view(request):
    return render(request, 'home/blog.html')


# @login_required
def about_view(request):
    return render(request, 'home/about.html')


# @login_required
def cad_view(request, curso, regime):
    data = dict()
    data['cursos'] = Curso.objects.all()
    for c in data['cursos']:
        if curso == caps_no_space(c.nome):
            data['curso'] = Curso.objects.get(nome=c.nome)
    if request.method == "POST":
        formContacto = ContactoModelForm(request.POST)
        formEndereco = EnderecoModelForm(request.POST)
        formEstudante = EstudanteModelForm(request.POST)
        if formContacto.is_valid and formEndereco.is_valid:
            formContacto.save()
            formEndereco.save()
            contacto = Contacto.objects.get(email=request.POST['email'])
            endereco = Endereco.objects.all()
            estudante = Estudante(
                endereco=endereco[len(endereco) - 1],
                contacto=contacto,
                nome=request.POST['nome'],
                dataNasc=request.POST['dataNasc'],
                doc_type=request.POST['doc_type'],
                num_doc=request.POST['num_doc']
            )
            estudante.save()
            # estudante=Estudante.objects.select_related('contacto').filter(contacto__email=request.POST['email'])[0],
            matricula = Matricula(
                estudante=Estudante.objects.get(contacto=contacto),
                curso=data['curso'],
                regime=regime
            )
            matricula.save()
            # print(endereco[len(endereco) - 1])

    # return redirect("url_home")
    return render(request, 'home/cad.html', data)


