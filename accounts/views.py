
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import FormUser


class Create_user(generic.CreateView):
    template_name = 'accounts/create-user.html'
    form_class = FormUser
    success_url = reverse_lazy('login')

