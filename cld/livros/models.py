from django.db import models

# Create your models here.

class Livro(models.Model):
    codigo = models.IntegerField()
    ISBN = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=60)
    ano = models.IntegerField()
    editora = models.CharField(max_length=60)
    
    def __str__(self):
        return self.titulo




