from unicodedata import name
from django.contrib.auth import login,logout
from django import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', Index,name='index'),

    #path('login/',Iniciar ,name="login" ),

    #path('validar/',Login ,name="validar" ),

    path('registro/', Registro, name="registro"), # USER 

    path('logout/', CerrarSesion, name='logout'), # USER

    path('alumnos/',IndexAlumnos, name='IndexAlumnos'),# ALUMNOS

    path('alumno/<id>/', Alumno, name="alumno"),# ALUMNOS

    path('modificar-alumno/<id>', EditAlumno, name='modificar-alumno'),# ALUMNOS

    path('agregar-alumno/', AddAlumno, name="agregar-alumno"),# ALUMNOS

    path('eliminar-alumno/<id>', DeleteAlumno, name='eliminar-alumno'),# ALUMNOS

    path('matriculas/', IndexMatriculas, name='IndexMatriculas'),# MATRICULAS

    path('matricula/<id>', Matricula, name='matricula'),# MATRICULAS

    path('agregar-matricula/', AddMatricula, name='agregar-matricula'),# MATRICULAS

    path('eliminar-matricula/<id>', DeleteMatricula, name="eliminar-matricula" ),# MATRICULAS

    path('modificar-matricula/<id>', EditMatricula, name='modificar-matricula'),# MATRICULAS

    path('ciudades/', IndexCiudades, name='IndexCiudades'),# CIUDADES

    path('ciudad/<id>', Ciudad, name='ciudad'),# CIUDADES

    path('agregar-ciudad/', AddCiudad, name='agregar-ciudad'),# CIUDADES

    path('modificar-ciudad/<id>', EditCiudad, name='modificar-ciudad'),# CIUDADES

    path('eliminar-ciudad/<id>', DeleteCiudad, name="eliminar-ciudad" ),# CIUDADES

    path('usuarios/', IndexUser, name='IndexUsuarios'),# USER TOO

    path('usuario/<id>', Usuario, name='usuario'),# USER TOO



    path('sucursales/', IndexSucursal, name='IndexSucursales'), # SUCURSALES 

    path('sucursal/<id>',Sucursal,name='sucursal'),

    path('agregar-sucursal/', AddSucursal, name='agregar-sucursal'),

    path('modificar-sucursal/<id>',EditSucursal, name='modificar-sucursal'),

    path('eliminar-sucursal/<id>', DeleteSucursal, name='eliminar-sucursal'),
 

    path('tipos-curso/', IndexTipoCurso, name='IndexTipoCurso'),# TIPOS DE CURSOS

    path('tipo-curso/<id>',TipoCurso, name="tipoCurso"),

    path('modificar-curso/<id>',EditTipoCurso, name='modificar-curso'),

    path('agregar-curso/', AddTipoCurso, name='agregar-curso'),

    path('eliminar-curso/<id>', DeleteTipoCurso, name='eliminar-curso')

]
