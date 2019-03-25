from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    data = {}
    data['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #print(data['posts'].query)
    return render(request, "djangoGirls/index.html", data)

def post(request, pk):
    data = {}
    data['posts'] = Post.objects.filter(id=pk)
    return render(request, "djangoGirls/index.html", data)


def	post_new(request):
    data = {}
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if	form.is_valid():
            post = form.save(commit=False)
            post.author	=	request.user
            post.published_date	=	timezone.now()
            post.save()
            return	redirect('url_post', pk=post.pk)
    form = PostForm()
    data['form'] = form
    return render(request, 'djangoGirls/post_edit.html', data)


def post_edit(request, pk):
    post	=	get_object_or_404(Post,	pk=pk)
    if	request.method	==	"POST":
        form	=	PostForm(request.POST,	instance=post)
        if	form.is_valid():
            post	=	form.save(commit=False)
            post.author	=	request.user
            post.published_date	=	timezone.now()
            post.save()
            return	redirect('url_post',	pk=post.pk)
    form	=	PostForm(instance=post)
    return	render(request,	'djangoGirls/post_edit.html',	{'form':	form})