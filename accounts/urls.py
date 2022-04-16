
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create-user/', views.Create_user.as_view(), name='create-user'),
]

