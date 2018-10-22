from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def my_login(request):
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
            return redirect('url_login')
    else:
        proximo['prox'] = request.GET.get('next')
        return render(request, 'home/login.html', proximo)


def do_logout(request):
    logout(request)
    return redirect('url_login')


def cover(request):
    return render(request, 'home/cover.html')
