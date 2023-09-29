import django_filters

from .models import alumnos, matricula, ciudad, sucursal, tipocurso, Usuario

from django.contrib.auth.models import User


class AlumnosFilter(django_filters.FilterSet):
    class Meta:
        model = alumnos
        fields = {
            'nombre' : ['icontains'], 'apaterno' : ['icontains'], 'amaterno' : ['icontains']
        }

class MatriculasFilter(django_filters.FilterSet):
    class Meta:
        model = matricula
        fields = {
            'matfecha' : ['gt', 'lt', 'exact'], 'sucursalId' : ['exact']
        }

class CiudadFilter(django_filters.FilterSet):
    class Meta:
        model = ciudad
        fields = {
            'nombre' : ['icontains']
        }

class SucursalFilter(django_filters.FilterSet):
    class Meta:
        model = sucursal
        fields = {
            'nombre' : ['icontains']
        }

class tCursoFilter(django_filters.FilterSet):
    class Meta:
        model = tipocurso
        fields = {
            'nombre' : ['icontains'], 'valor' : ['gt','lt','iexact']
        }

class UserFilter(django_filters.FilterSet):

    model = Usuario
    fields = {
        'usuario' : ['icontains'], 'nombre' : ['icontains']
    }