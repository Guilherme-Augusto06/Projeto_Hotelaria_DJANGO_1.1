from django.db import models
from django.utils import timezone
# Create your models here.
TIPOS_QUARTO = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORT","Confort"),
    ("LUXO","Luxo")
     
)

class Hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1500)
    descricao2 = models.TextField(max_length=1500)
    descricao3 = models.TextField(max_length=1500)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.titulo

class Quarto(models.Model):
    tipo = models.CharField(max_length=50, choices=TIPOS_QUARTO)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=255)
    foto_quarto = models.ImageField(upload_to='foto_quartos/')

    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    data = models.DateField(default=timezone.now)
    quartos = models.CharField(max_length=50)
