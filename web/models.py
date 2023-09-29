from django.db import models

# Create your models here.

class alumnos(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=15)
    apaterno = models.CharField(max_length=15)
    amaterno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=60)
    email = models.CharField(max_length=40)
    fono = models.CharField(max_length=10)


class Usuario(models.Model):
    usuario=models.CharField(max_length=20)
    nombre=models.CharField(max_length=30)
    password=models.CharField(max_length=255)

class ciudad(models.Model):
    nombre = models.CharField(max_length=20)

class tipocurso(models.Model):
    nombre = models.CharField(max_length=20)
    valor = models.IntegerField()

class sucursal(models.Model):
    ciudadId = models.ForeignKey(ciudad,on_delete=models.CASCADE,null = False,blank = False)
    nombre = models.CharField(max_length=20)

class matricula(models.Model):
    tipcurcodigo = models.ForeignKey(tipocurso,on_delete=models.CASCADE,null=True, blank=True)
    alumrut = models.ForeignKey(alumnos,on_delete=models.CASCADE,null=True, blank=True)
    sucursalId = models.ForeignKey(sucursal,on_delete=models.CASCADE,null=True, blank=True)
    matfecha = models.DateField()
