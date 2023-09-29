
from django import forms
from web.models import *


#form for create user / register :p
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = alumnos
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = matricula
        fields = '__all__'



class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        fields = '__all__'

class TipoCursoForm(forms.ModelForm):
    class Meta:
        model = tipocurso
        fields = '__all__'

class SucursalForm(forms.ModelForm):
    class Meta:
        model = sucursal
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    pass

