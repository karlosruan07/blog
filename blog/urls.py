
from django.urls import path
from . import views #aqui importa todas as views do arquivo blog/views.py 

"""urlpatterns = [
    path('', views.post_list, name='post_list'),

]"""
urlpatterns = [
    path('', views.post_list, name='post_list'), #quando for digitado na url um espaço em branco "sem subpastas" então irá cair nessa view
]
