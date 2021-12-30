
from django.contrib import admin
from django.urls import path, include #o include serve para incluir um arquivo interno da mesma pasta ou um arquivo de outra subpasta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),#tudo o que virá sem diretórios na url será redireciondo para esse arquivo
    path('', include('django.contrib.auth.urls')),

    path('accounts/',include('blog.urls')),

]

