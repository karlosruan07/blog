from django.shortcuts import render, get_object_or_404 #a biblioteca de 404 serve para retorna uma pagina de erro caso não exista uma determinada página
#from .models import Post
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.


def post_list(request):

    
    #teste = Post.objects.all()  #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('-created_data')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

