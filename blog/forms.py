
from django import forms
from .models import Post


class PostForm(forms.ModelForm): #PostForm é o nome do formulario, e o forms.ModelFor é uma função específica do django para tratar de formulários
    
    class Meta:
        model = Post
        fields = ('title', 'text')
        
        
