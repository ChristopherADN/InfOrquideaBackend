
from rest_framework import serializers
from rest_framework.utils import field_mapping
from InfOrquidea.models import Genero,Especie,FamiliaDeOrquideas,Usuario,Orquidea

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genero
        fields=('IdGenero','NombreGenero','EstadoGenero')

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Especie
        fields=('IdEspecie','NombreEspecie','EstadoEspecie')

class FamiliaDeOrquideasSerializer(serializers.ModelSerializer):
    class Meta:
        model=FamiliaDeOrquideas
        fields=('IdFamiliaDeOrquideas','NombreFamiliaDeOrquideas','EstadoFamiliaDeOrquideas')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('IdUsuario','EmailUsuario','PasswordUsuario','EstadoUsuario')

class OrquideaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orquidea
        fields=('idOrquidea', 'tipo_crecimiento', 'nombre_comun', 'floracion', 'duracion_flor', 'tamaño_flor', 'ubicacion')