
from django.contrib import admin
from django.urls import path, include #o include serve para incluir um arquivo interno da mesma pasta ou um arquivo de outra subpasta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),#tudo o que virá sem diretórios na url será redireciondo para esse arquivo
    path('accounts/', include('accounts.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
