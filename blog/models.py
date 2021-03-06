
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):#o nome da classe é Post (ela tem que iniciar com maiúsculas) models.Model é um modelo em django.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #é método com um limite de caracteres no banco de dados
    text = models.TextField() #Método que serve para não definir um limite no banco de dados
    created_data = models.DateTimeField(default=timezone.now)#método que serve para pegar uma data e hora da publicação
    published_date = models.DateTimeField(blank=True, null=True) #linkando para outro modelo
    
    def publish(self): #função publish
        self.published_date = timezone.now()
        self.save()
        

    def __str__(self): #quando se usa o __str__ é porque irá retorna um string
        return self.title

#app teste para enviar arquivos;
    

