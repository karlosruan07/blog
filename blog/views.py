from django.shortcuts import render, get_object_or_404 #a biblioteca de 404 serve para retorna uma pagina de erro caso não exista uma determinada página
#from .models import Post
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import PostForm  #importa do arquivo form.py a classe PostForm
from django.shortcuts import redirect #importa uma função de redirecionamento de um usuario

# Create your views here.


def post_list(request):

    
    #teste = Post.objects.all()  #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('-created_data')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False) #não salva o modelo ainda, pois tem que salvar 1º o autor
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
        
def post_edit(request, pk): #função para editar um post
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})
