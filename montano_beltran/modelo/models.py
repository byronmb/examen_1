from django.db import models

# Create your models here.
class Estudiante(models.Model):
    listaParalelo = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd')
    )
    matricula = models.CharField(max_length=15,unique=True, null=False)
    cedula = models.CharField(max_length=10,unique=True, null=False)
    nombres = models.CharField(max_length=70, null=False)
    apellidos = models.CharField(max_length=70,  null=False)
    ciclo = models.CharField(max_length=70,  null=False)
    paralelo =models.CharField(max_length=15, choices=listaParalelo, null=True)
