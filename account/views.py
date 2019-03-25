from django.shortcuts import render, redirect
from .forms import RegisterForm, UserAdminCreationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout


def account(request):
    pass


def create_account(request):
    data = dict()
    if request.method == "POST":
        form = UserAdminCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("url_home")

    data['form'] = UserAdminCreationForm()
    return render(request, 'account/singup.html', data)


def login_view(request):
    proximo = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if request.POST['url_next'] != 'None':
                caminho = request.POST['url_next']
                return redirect(caminho)
            return redirect('url_home')
        else:
            # Return an 'invalid login' error message.
            print(request.POST['url_next']+"====Aqui")
            return redirect(request.POST['url_next'])
    else:
        proximo['prox'] = request.GET.get('next')
        return render(request, 'account/login.html', proximo)


def logout_view(request):
    logout(request)
    return redirect('url_login')
