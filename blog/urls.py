
from django.urls import path
from . import views #aqui importa todas as views do arquivo blog/views.py 

"""urlpatterns = [
    path('', views.post_list, name='post_list'),

]"""
urlpatterns = [
    path('', views.post_list, name='post_list'), #quando for digitado na url um espaço em branco "sem subpastas" então irá cair nessa view
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #url criada, o post serve para dizer que a url tem que começar com o post, e o <int:pk>/ espera um objeto inteiro para tranferir para a view, esse nº inteiro é relacionado a chave primaria
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
