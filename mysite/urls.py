"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #o include serve para incluir um arquivo interno da mesma pasta ou um arquivo de outra subpasta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),#tudo o que virá sem diretórios na url será redireciondo para esse arquivo

    path('',include('django.contrib.auth.urls')),

]

