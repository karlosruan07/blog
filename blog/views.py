from django.shortcuts import render, get_object_or_404 #a biblioteca de 404 serve para retorna uma pagina de erro caso não exista uma determinada página
#from .models import Post
from blog.models import Post
from django.utils import timezone
from .forms import PostForm  #importa do arquivo form.py a classe PostForm
from django.shortcuts import redirect #importa uma função de redirecionamento de um usuario

from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.order_by('-created_data')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context=context)


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False) #não salva o modelo ainda, pois tem que salvar 1º o autor
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:index')
    else:
        form = PostForm()
        contexto = {
            "titulo": "Novo Post !",
            "form":form,
            "titulo_botao":"Enviar"
        }
    return render(request, 'blog/post_form.html', contexto) 


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context=context)


@login_required        
def post_edit(request, pk): #função para editar um post
     post = get_object_or_404(Post, pk=pk, author=request.user)#filta a linha da tabela pelo ID e pelo usuário que está autenticado
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('blog:index')
     else:
         form = PostForm(instance=post)
         context = {"titulo":"Editando Post !","form":form, "titulo_botao":"Salvar"}
     return render(request, 'blog/post_form.html', context=context)


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.delete()
    return redirect('blog:index')


def sobre(request):
    return render(request, 'blog/sobre.html')
