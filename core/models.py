from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    nome=models.CharField(max_length=100)
    sinopse= models.CharField(max_length=100)
    data_lancamento= models.DateField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)

