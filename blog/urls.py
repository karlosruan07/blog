
from django.urls import path
from . import views #aqui importa todas as views do arquivo blog/views.py 
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    
    path('', views.index, name='index'), #quando for digitado na url um espaço em branco "sem subpastas" então irá cair nessa view
    path('post/new/', views.post_new, name='post-new'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'), #url criada, o post serve para dizer que a url tem que começar com o post, e o <int:pk>/ espera um objeto inteiro para tranferir para a view, esse nº inteiro é relacionado a chave primaria
    path('post/<int:pk>/edit/', views.post_edit, name='post-edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
    path('sobre/', views.sobre, name='sobre'),

    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='blog/change_password.html')),

]
