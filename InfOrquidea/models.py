from django.db import models

# Create your models here.

class Genero(models.Model):
    IdGenero = models.AutoField(primary_key=True)
    NombreGenero = models.CharField(max_length=250)
    EstadoGenero = models.IntegerField()

class Especie(models.Model):
    IdEspecie = models.AutoField(primary_key=True)
    NombreEspecie = models.CharField(max_length=250)
    EstadoEspecie = models.IntegerField()

class FamiliaDeOrquideas(models.Model):
    IdFamiliaDeOrquideas = models.AutoField(primary_key=True)
    NombreFamiliaDeOrquideas = models.CharField(max_length=250)
    EstadoFamiliaDeOrquideas = models.IntegerField()

class Usuario(models.Model):
    IdUsuario = models.AutoField(primary_key=True)
    EmailUsuario = models.CharField(max_length=250)
    PasswordUsuario = models.CharField(max_length=20)
    EstadoUsuario = models.IntegerField()

class Orquidea(models.Model):
    idOrquidea = models.AutoField(primary_key=True)
    tipo_crecimiento = models.CharField(max_length=30)
    nombre_comun = models.CharField(max_length=30, unique=True)
    floracion = models.CharField(max_length=30)
    duracion_flor = models.CharField(max_length=30)
    tamaño_flor = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=60)