from email.policy import default
from django.db import models

# Create your models here.

#para criar uma tabela no banco, ela tem que erdar de models.Model
class Professor(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False , default='Nenhum nome foi adicionada até o momento!')
    idade = models.IntegerField(null = False, blank = False, default= 19)
    valor_hora= models.DecimalField(max_digits= 9,decimal_places = 2, null= False, blank = False, default= 50)
    descricao = models.TextField(null = False, blank = False, default='Nenhuma descrição foi adicionada até o momento!')
    foto = models.URLField(max_length= 255, null=False, blank= False, default='Nenhuma foto foi adicionada até o momento!' )



class Aula(models.Model):
    nome = models.CharField(max_length = 100, null = False, blank = False)
    email = models.EmailField(max_length= 255 ,  null = False, blank = False)
    professor = models.ForeignKey(to=Professor, on_delete= models.CASCADE, related_name = 'aulas',
    null = False, blank = False)